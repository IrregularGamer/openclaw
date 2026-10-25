"""Fork-owned operator-read transport, never a replacement native owner.

Source only. A supervised installation must supply a root-owned listening Unix
socket and place this root endpoint in the existing gateway cgroup. This module
does not create sockets, change privilege/cgroups, install policy, or construct
Controller. A missing or different external native generation refuses.
"""
import hashlib
import ctypes
import json
import os
from pathlib import Path
import select
import signal
import socket
import struct
import subprocess
import time
from types import ModuleType, SimpleNamespace

NATIVE_PATH = Path('/usr/local/libexec/agentq-safety/maintenance.py')
# Exact ABH handoff candidate, derived from the unchanged external owner inputs.
NATIVE_SHA256 = 'bca40971a35d160ad87b5d18fd1cc7f7730a7f90d2bb5b8480f3d7d79d11c182'
SYSTEMCTL = ['systemctl', '--user', '--machine=deploy@.host', 'show',
             'openclaw-gateway.service', '-p', 'MainPID', '--value']
RESERVE_NS = 200_000_000


class Refused(Exception): pass
class Cancelled(Refused): pass
class Deadline(Refused): pass
class Unsettled(Refused): pass


def child_subreaper():
    # This dedicated endpoint owns no other subprocess work. Adopt grandchildren
    # so a leader exit cannot turn outstanding native work into a settled ACK.
    if ctypes.CDLL(None, use_errno=True).prctl(36, 1, 0, 0, 0) != 0:
        raise Refused()
    # Refuse unsupported kernels before any native child exists.
    if (not hasattr(os, 'P_PIDFD') or not hasattr(os, 'pidfd_open')
            or not hasattr(signal, 'pidfd_send_signal')):
        raise Refused()
    fd = os.pidfd_open(os.getpid())
    try:
        signal.pidfd_send_signal(fd, 0)
        try: os.waitid(os.P_PIDFD, fd, os.WEXITED | os.WNOHANG | os.WNOWAIT)
        except ChildProcessError: pass  # Self is not our child, kernel recognized PIDFD.
    finally: os.close(fd)


def leader_status(child):
    # Observe exit without reaping. The zombie retains PID/PGID ownership until
    # every group signal is complete, preventing a recycled-group signal.
    return os.waitid(os.P_PID, child.pid, os.WEXITED | os.WNOHANG | os.WNOWAIT)


def reap_adopted(deadline):
    # The endpoint is a dedicated, serial supervisor, with no unrelated children.
    # A descendant that escaped the original session is still adopted here.
    while time.monotonic_ns() < deadline - 10_000_000:
        try:
            while True:
                pid, _ = os.waitpid(-1, os.WNOHANG)
                if pid == 0: break
        except ChildProcessError: return True
        for task in Path('/proc/self/task').iterdir():
            try:
                with open(task/'children', encoding='ascii') as stream:
                    children = stream.read(65536).split()
            except FileNotFoundError: continue
            for value in children:
                try: fd = os.pidfd_open(int(value))
                except ProcessLookupError: continue
                try:
                    # Kernel child ownership plus pidfd, never a PID-only kill.
                    os.waitid(os.P_PIDFD, fd, os.WEXITED | os.WNOHANG | os.WNOWAIT)
                    signal.pidfd_send_signal(fd, signal.SIGKILL)
                except (ChildProcessError, ProcessLookupError): pass
                finally: os.close(fd)
        time.sleep(0.002)
    return False


def settle_group(child, deadline):
    # Keep the direct child unreaped while signaling its owned group.
    try: os.killpg(child.pid, signal.SIGTERM)
    except ProcessLookupError: pass
    grace = min(deadline - 100_000_000, time.monotonic_ns()+50_000_000)
    while time.monotonic_ns() < grace: time.sleep(0.002)
    try: os.killpg(child.pid, signal.SIGKILL)
    except ProcessLookupError: pass
    # All group signals are now complete. Reaping cannot enable a later signal
    # to a reused group. Adopted descendants use kernel child checks and pidfds.
    try: child.wait(timeout=max(0.001, (deadline-time.monotonic_ns())/1e9-0.02))
    except subprocess.TimeoutExpired: return False
    return reap_adopted(deadline)


def compile_native(raw):
    if hashlib.sha256(raw).hexdigest() != NATIVE_SHA256:
        raise PermissionError('native_source_pin')
    native = ModuleType('strict542_external_native')
    native.__file__ = str(NATIVE_PATH)
    # Compile the actual hashed bytes. No path reopen or unverified pyc import.
    exec(compile(raw, '<pinned-external-native>', 'exec'), native.__dict__)
    return native


def load_native():
    for path in (NATIVE_PATH, *NATIVE_PATH.parents):
        info = path.lstat()
        if info.st_uid != 0 or info.st_mode & 0o022 or path.is_symlink():
            raise PermissionError('native_source_path')
    return compile_native(NATIVE_PATH.read_bytes())


class ReadScope:
    def __init__(self, connection, request):
        self.connection = connection
        self.request = request
        self.deadline = int(request['deadlineNs'])
        self.pending = b''
        self.cancelled = False
        self.settled = True

    def check(self):
        if select.select([self.connection], [], [], 0)[0]:
            raw = self.connection.recv(1024)
            if not raw: self.cancelled = True
            self.pending += raw
            if len(self.pending) > 512: self.cancelled = True
            if b'\n' in self.pending:
                try:
                    value = json.loads(self.pending)
                    if value != dict(operation='cancel', requestId=self.request['requestId']):
                        raise ValueError('invalid_cancel')
                except (ValueError, TypeError): pass
                # Any unexpected control input also cancels, never grants authority.
                self.cancelled = True
        if self.cancelled: raise Cancelled()
        if time.monotonic_ns() >= self.deadline - RESERVE_NS: raise Deadline()

    def runner(self, argv, *, capture_output, text, timeout):
        if argv != SYSTEMCTL or capture_output is not True or text is not True:
            raise Refused()
        self.check()
        child = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                 env={'PATH':'/usr/bin:/bin', 'LANG':'C'}, start_new_session=True)
        self.settled = False
        end = min(self.deadline - RESERVE_NS, time.monotonic_ns()+int(timeout*1e9))
        output = b''
        os.set_blocking(child.stdout.fileno(), False)
        try:
            while True:
                self.check()
                chunk = child.stdout.read(129) or b''
                output += chunk
                if len(output) > 128: raise Refused()
                status = leader_status(child)
                if status is not None:
                    # Retain the exited leader while draining bounded output.
                    output += child.stdout.read(129) or b''
                    if len(output) > 128: raise Refused()
                    self.settled = True
                    return SimpleNamespace(returncode=status.si_status if status.si_code == os.CLD_EXITED else -status.si_status, stdout=output.decode('ascii'))
                if time.monotonic_ns() >= end: raise Deadline()
                select.select([self.connection, child.stdout], [], [], 0.005)
        finally:
            self.settled = settle_group(child, self.deadline)
            child.stdout.close()
            if not self.settled: raise Unsettled()


def read_request(connection):
    # Before a request exists there is no native work and no authority to retain.
    connection.settimeout(0.15)
    raw = b''
    while not raw.endswith(b'\n'):
        part = connection.recv(513)
        if not part: raise Refused()
        raw += part
        if len(raw) > 512: raise Refused()
    value = json.loads(raw)
    if (type(value) is not dict or set(value) != {'schemaVersion','operation','requestId','deadlineNs'}
            or type(value['schemaVersion']) is not int or value['schemaVersion'] != 1
            or value['operation'] != 'operator-read'
            or type(value['requestId']) is not str or not 8 <= len(value['requestId']) <= 128
            or type(value['deadlineNs']) is not str or not value['deadlineNs'].isascii()
            or not value['deadlineNs'].isdecimal()): raise Refused()
    left = int(value['deadlineNs']) - time.monotonic_ns()
    if not RESERVE_NS < left <= 10_000_000_000: raise Refused()
    return value


def serve_connected(connection):
    """Serve one kernel-authenticated gateway peer; no callback grants ownership."""
    scope = None
    try:
        if os.geteuid() != 0: raise Refused()
        child_subreaper()
        pid, uid, gid = struct.unpack('3i', connection.getsockopt(socket.SOL_SOCKET, socket.SO_PEERCRED, 12))
        if pid <= 1: raise Refused()
        request = read_request(connection)
        scope = ReadScope(connection, request)
        native = load_native()
        scope.check()
        # Derive identity from the kernel peer, never a caller's owner assertion.
        start = (Path('/proc')/str(pid)/'stat').read_text().rsplit(')', 1)[1].split()[19]
        owner = dict(name='Pinch', session=native.HQ, pid=pid, start=start)
        adapter = native.Native510(SimpleNamespace(root=native.ROOT, runner=scope.runner))
        adapter.owner_check(owner, caller=True)
        scope.check()
        adapter.owner_check(owner, caller=True)
        scope.check()
        reason = None
    except Cancelled:
        owner, reason = None, 'cancelled'
    except Deadline:
        owner, reason = None, 'deadline'
    except (OSError, ValueError, KeyError, TypeError, PermissionError, Refused):
        owner, reason = None, 'native_refused'
    if scope is None or not scope.settled or time.monotonic_ns() >= scope.deadline:
        return  # Never manufacture a settled receipt.
    receipt = dict(schemaVersion=1, requestId=scope.request['requestId'], settled=True,
                   cancelled=scope.cancelled, reason=reason, owner=owner)
    connection.settimeout(max(0.001, (scope.deadline-time.monotonic_ns())/1e9))
    try: connection.sendall(json.dumps(receipt, separators=(',', ':')).encode()+b'\n')
    except OSError: pass


def serve(listener):
    """Existing supervisor supplies the endpoint and lifecycle, not this read."""
    if os.geteuid() != 0 or listener.family != socket.AF_UNIX: raise Refused()
    while True:
        connection, _ = listener.accept()
        with connection: serve_connected(connection)


if __name__ == '__main__':
    # Fixed inherited endpoint, supplied by a separately authorized supervisor.
    # No bind, installation, command arguments or privilege transition occurs.
    with socket.socket(fileno=3) as listener:
        if (listener.getsockname() != '/run/agentq-safety/owner542.sock'
                or not listener.getsockopt(socket.SOL_SOCKET, socket.SO_ACCEPTCONN)):
            raise Refused()
        serve(listener)
