"""Fixed, finite root lifecycle for the reviewed fd3 endpoint. SOURCE ONLY.

The unit MainPID stays in its bounded system cgroup. Only its newly forked
endpoint writes its own PID to the existing gateway cgroup; no worker, gateway
or unrelated process is moved. This never grants an HQ session or accepted run.
"""
import hashlib
import os
from pathlib import Path
import resource
import select
import signal
import socket
import stat
import subprocess
import sys
import time
from types import ModuleType

SERVER = Path('/usr/local/libexec/agentq-safety/native_owner_server542.py')
SERVER_SHA256 = 'a145387432fbf8e17fffbf1e552328e651054e9d603b1d9bdad2d8494dc6a373'
SOCKET = Path('/run/agentq-safety/owner542.sock')
UNIT_CGROUP = '0::/system.slice/strict542-owner.service'
HQ_CGROUP = '0::/user.slice/user-1000.slice/user@1000.service/app.slice/openclaw-gateway.service'
CGROUP = Path('/sys/fs/cgroup') / HQ_CGROUP.removeprefix('0::/')
LIFETIME = 900
ADDRESS_LIMIT = 96 * 1024 * 1024
CPU_LIMIT = 30


class Refused(Exception): pass


def protected(path):
    for item in (path, *path.parents):
        info = item.lstat()
        if info.st_uid != 0 or info.st_mode & 0o022 or stat.S_ISLNK(info.st_mode):
            raise Refused('unsafe_root_path')
    with path.open('rb') as stream:
        if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode): raise Refused('not_regular')
        raw = stream.read(262145)
    if len(raw) > 262144: raise Refused('source_size')
    return raw


def load_server():
    raw = protected(SERVER)
    if hashlib.sha256(raw).hexdigest() != SERVER_SHA256: raise Refused('server_pin')
    module = ModuleType('reviewed_owner542')
    exec(compile(raw, str(SERVER), 'exec'), module.__dict__)
    # Verify actual native generation before creating an accessible endpoint.
    native = module.load_native()
    if native.HQ_CGROUP != HQ_CGROUP: raise Refused('native_cgroup_drift')
    return module, raw


def identity(pid):
    base = Path('/proc') / str(pid)
    return (base.joinpath('stat').read_text().rsplit(')', 1)[1].split()[19],
            base.joinpath('cgroup').read_text().strip())


def gateway_pid():
    result = subprocess.run(['/usr/bin/systemctl', *['--user', '--machine=deploy@.host',
        'show', 'openclaw-gateway.service', '-p', 'MainPID', '--value']],
        capture_output=True, timeout=1, check=True,
        env={'PATH': '/usr/bin:/bin', 'LANG': 'C'})
    if len(result.stdout) > 32 or not result.stdout.strip().isdigit(): raise Refused('mainpid')
    pid = int(result.stdout)
    if pid <= 1: raise Refused('mainpid')
    return pid


def bind_socket():
    parent = SOCKET.parent
    for item in (parent, *parent.parents):
        info = item.lstat()
        if (info.st_uid != 0 or info.st_mode & 0o022 or not stat.S_ISDIR(info.st_mode)
                or stat.S_ISLNK(info.st_mode)): raise Refused('socket_parent')
    listener = socket.socket(socket.AF_UNIX)
    try:
        # Existing nodes (including stale sockets/symlinks) refuse; never unlink
        # an endpoint owned by another invocation.
        old_umask = os.umask(0o177)
        try: listener.bind(str(SOCKET))
        finally: os.umask(old_umask)
        os.chown(SOCKET, 0, 1000)
        os.chmod(SOCKET, 0o660)
        info = SOCKET.lstat()
        if (not stat.S_ISSOCK(info.st_mode) or info.st_uid != 0 or info.st_gid != 1000
                or stat.S_IMODE(info.st_mode) != 0o660): raise Refused('socket_policy')
        listener.listen(8)
        return listener, info.st_ino
    except BaseException:
        listener.close()
        raise


def place_endpoint():
    # Kernel cgroup-v2 process migration API, fixed target, self only. The
    # supervisor unit cannot use ProtectControlGroups=yes. No delegation or
    # writable control files are granted to the unprivileged gateway.
    CGROUP.joinpath('cgroup.procs').write_text(str(os.getpid()) + '\n')
    if Path('/proc/self/cgroup').read_text().strip() != HQ_CGROUP: raise Refused('placement')
    resource.setrlimit(resource.RLIMIT_AS, (ADDRESS_LIMIT, ADDRESS_LIMIT))
    resource.setrlimit(resource.RLIMIT_CPU, (CPU_LIMIT, CPU_LIMIT))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


class Child:
    def __init__(self, pid): self.pid = pid
    def wait(self, timeout):
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            if os.waitpid(self.pid, os.WNOHANG)[0]: return
            time.sleep(0.002)
        raise subprocess.TimeoutExpired('fixed-endpoint', timeout)


def tree_cpu_seconds():
    """All descendants remain kernel-owned until settled by the subreaper.

    Include live descendants' own CPU and their already-reaped descendants
    (utime/stime/cutime/cstime), plus the parent's RUSAGE_CHILDREN for already
    reaped direct trees. Unreaped children are not included in parents' cutime.
    """
    total = resource.getrusage(resource.RUSAGE_CHILDREN)
    seconds = total.ru_utime + total.ru_stime
    pending = [os.getpid()]
    seen = set()
    while pending:
        parent = pending.pop()
        try: children = Path('/proc/%s/task/%s/children' % (parent, parent)).read_text().split()
        except FileNotFoundError: continue
        for value in children:
            if value in seen: continue
            seen.add(value)
            try:
                fields = Path('/proc/%s/stat' % value).read_text().rsplit(')', 1)[1].split()
                seconds += (int(fields[11]) + int(fields[12]) + int(fields[13]) + int(fields[14])) / os.sysconf('SC_CLK_TCK')
            except FileNotFoundError: continue
            pending.append(int(value))
    return seconds


def supervise(server, child, gateway, gateway_fd, expected, stopped):
    end = time.monotonic() + LIFETIME
    while time.monotonic() < end and not stopped[0]:
        if select.select([gateway_fd], [], [], 0.1)[0]: break
        if server.leader_status(child) is not None: break
        if (identity(gateway) != expected or gateway_pid() != gateway
                or tree_cpu_seconds() >= CPU_LIMIT): break
    # Stop accepting before settling the endpoint and its adopted descendants.
    # No successful ACK is synthesized by this lifecycle owner.


def main():
    if (os.geteuid() != 0 or len(sys.argv) != 1
            or Path('/proc/self/cgroup').read_text().strip() != UNIT_CGROUP):
        raise Refused('dedicated_system_unit_required')
    server, raw = load_server()
    server.child_subreaper()
    gateway = gateway_pid()
    expected = identity(gateway)
    if expected[1] != HQ_CGROUP: raise Refused('gateway_placement')
    gateway_fd = os.pidfd_open(gateway)
    if identity(gateway) != expected or gateway_pid() != gateway:
        os.close(gateway_fd)
        raise Refused('gateway_replaced')
    listener = None
    inode = None
    child = None
    parent_fd = None
    stopped = [False]
    def stop(signum, frame): stopped[0] = True
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    try:
        listener, inode = bind_socket()
        parent_fd = os.pidfd_open(os.getpid())
        pid = os.fork()
        if pid == 0:
            try:
                signal.signal(signal.SIGTERM, signal.SIG_DFL)
                signal.signal(signal.SIGINT, signal.SIG_DFL)
                # Capture parent before any migration; pidfd remains readable
                # after abrupt parent death, letting endpoint settle itself.
                os.close(gateway_fd)
                os.setsid()
                place_endpoint()
                if listener.fileno() != 3: os.dup2(listener.fileno(), 3)
                os.dup2(parent_fd, 4)
                if parent_fd not in (3, 4): os.close(parent_fd)
                exec(compile(raw, str(SERVER), 'exec'), {'__name__': '__main__'})
            finally: os._exit(1)
        child = Child(pid)
        listener.close()
        supervise(server, child, gateway, gateway_fd, expected, stopped)
    finally:
        if listener is not None: listener.close()
        # PID stays unreaped until all group signals complete. The parent
        # adopts escaped descendants and kills them using kernel child+pidfd.
        if child is not None:
            # Close the fork-before-setsid race using a pidfd for our unreaped
            # direct child. Group cleanup alone cannot cover that brief window.
            endpoint_fd = os.pidfd_open(child.pid)
            try:
                try: signal.pidfd_send_signal(endpoint_fd, signal.SIGKILL)
                except ProcessLookupError: pass
            finally: os.close(endpoint_fd)
        settled = child is None or server.settle_group(child, time.monotonic_ns()+2_000_000_000)
        os.close(gateway_fd)
        if parent_fd is not None: os.close(parent_fd)
        if inode is not None:
            try:
                info = SOCKET.lstat()
                if info.st_ino == inode and stat.S_ISSOCK(info.st_mode): SOCKET.unlink()
            except FileNotFoundError: pass
        if not settled: raise Refused('unsettled_tree')


if __name__ == '__main__':
    main()
