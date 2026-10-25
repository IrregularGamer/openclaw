"""Secretless supervisor proof; never writes host cgroups or starts services."""
import hashlib
import importlib.util
import os
import json
import signal
import subprocess
import sys
from pathlib import Path
import socket
import stat
import tempfile
import threading
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

supervisor = load('supervisor542', HERE/'root_owner_supervisor.py')
server = load('server542', HERE/'native_owner_server.py')


class RootSupervisor(unittest.TestCase):
    def test_reviewed_server_bytes_and_isolated_external_pin(self):
        self.assertEqual(hashlib.sha256((HERE/'native_owner_server.py').read_bytes()).hexdigest(),
                         supervisor.SERVER_SHA256)
        self.assertEqual(str(server.NATIVE_PATH), '/opt/openclaw-strict542/598/native/maintenance.py')
        self.assertEqual(server.NATIVE_SHA256, 'bca40971a35d160ad87b5d18fd1cc7f7730a7f90d2bb5b8480f3d7d79d11c182')

    def test_worker_and_nonroot_and_argument_contexts_refuse_before_source(self):
        for uid, cgroup, argv in [(0, '0::/system.slice/agentq-work.slice/worker', ['fixed']),
                                  (1000, supervisor.UNIT_CGROUP, ['fixed']),
                                  (0, supervisor.UNIT_CGROUP, ['fixed', '/caller/command'])]:
            with self.subTest(uid=uid, cgroup=cgroup, argv=argv), \
                 patch.object(supervisor.os, 'geteuid', return_value=uid), \
                 patch.object(supervisor.Path, 'read_text', return_value=cgroup), \
                 patch.object(supervisor.sys, 'argv', argv), \
                 patch.object(supervisor, 'load_server') as source:
                with self.assertRaises(supervisor.Refused): supervisor.main()
                source.assert_not_called()

    def test_source_path_writable_or_symlink_refuses(self):
        for mode in (stat.S_IFREG | 0o666, stat.S_IFLNK | 0o777):
            with patch.object(supervisor.Path, 'lstat', return_value=SimpleNamespace(st_uid=0, st_mode=mode)):
                with self.assertRaises(supervisor.Refused): supervisor.protected(Path('/fixture/source'))

    def test_server_pin_drift_refuses_before_execution(self):
        with patch.object(supervisor, 'protected', return_value=b'raise AssertionError("unverified")'):
            with self.assertRaises(supervisor.Refused): supervisor.load_server()

    def test_socket_parent_writable_refuses_before_bind(self):
        with patch.object(supervisor.Path, 'lstat', return_value=SimpleNamespace(st_uid=0, st_mode=stat.S_IFDIR|0o777)), \
             patch.object(supervisor.socket, 'socket') as create:
            with self.assertRaises(supervisor.Refused): supervisor.bind_socket()
            create.assert_not_called()

    def test_self_only_exact_cgroup_placement_and_limits(self):
        writes = []
        with patch.object(supervisor.Path, 'write_text', autospec=True, side_effect=lambda path, value: writes.append((path, value))), \
             patch.object(supervisor.Path, 'read_text', return_value=supervisor.HQ_CGROUP), \
             patch.object(supervisor.resource, 'setrlimit') as limits:
            supervisor.place_endpoint()
        self.assertEqual(writes, [(supervisor.CGROUP/'cgroup.procs', str(os.getpid())+'\n')])
        self.assertEqual(limits.call_count, 3)
        limits.assert_any_call(supervisor.resource.RLIMIT_AS, (96*1024*1024,)*2)
        limits.assert_any_call(supervisor.resource.RLIMIT_CPU, (30,30))
        limits.assert_any_call(supervisor.resource.RLIMIT_CORE, (0,0))

    def test_placement_mismatch_refuses_without_limits_or_serving(self):
        with patch.object(supervisor.Path, 'write_text'), \
             patch.object(supervisor.Path, 'read_text', return_value='0::/wrong'), \
             patch.object(supervisor.resource, 'setrlimit') as limits:
            with self.assertRaises(supervisor.Refused): supervisor.place_endpoint()
            limits.assert_not_called()

    def test_gateway_mainpid_change_ends_before_cpu_or_next_request(self):
        child = SimpleNamespace(pid=42)
        with patch.object(supervisor.select, 'select', return_value=([],[],[])), \
             patch.object(server, 'leader_status', return_value=None), \
             patch.object(supervisor, 'identity', return_value=('start', supervisor.HQ_CGROUP)), \
             patch.object(supervisor, 'gateway_pid', return_value=999), \
             patch.object(supervisor, 'tree_cpu_seconds') as cpu:
            supervisor.supervise(server, child, 42, 3, ('start', supervisor.HQ_CGROUP), [False])
            cpu.assert_not_called()

    def test_gateway_pidfd_exit_and_cpu_budget_end_monitor(self):
        for exited, cpu in [(True, 0), (False, 30)]:
            with self.subTest(exited=exited), \
                 patch.object(supervisor.select, 'select', return_value=([3] if exited else [],[],[])), \
                 patch.object(server, 'leader_status', return_value=None), \
                 patch.object(supervisor, 'identity', return_value=('start', supervisor.HQ_CGROUP)), \
                 patch.object(supervisor, 'gateway_pid', return_value=42), \
                 patch.object(supervisor, 'tree_cpu_seconds', return_value=cpu):
                supervisor.supervise(server, SimpleNamespace(pid=43), 42, 3,
                                     ('start', supervisor.HQ_CGROUP), [False])

    def test_partial_framing_has_absolute_deadline_and_checks_lifecycle(self):
        client, accepted = socket.socketpair()
        stopped = threading.Event()
        def dribble():
            while not stopped.wait(0.04):
                try: client.sendall(b'{')
                except OSError: return
        thread = threading.Thread(target=dribble)
        thread.start()
        start = time.monotonic()
        try:
            with self.assertRaises((socket.timeout,server.Refused)): server.read_request(accepted)
            self.assertLess(time.monotonic()-start,0.3)
            with patch.object(server,'endpoint_alive',return_value=False):
                with self.assertRaises(server.Refused): server.read_request(accepted)
        finally:
            stopped.set()
            thread.join(1)
            client.close()
            accepted.close()

    def test_endpoint_idle_lifetime_and_parent_death_refuse(self):
        for parent_dead, deadline in [(True,time.monotonic()+5),(False,time.monotonic()-1)]:
            with patch.object(server,'PARENT_FD',4), \
                 patch.object(server,'ENDPOINT_DEADLINE',deadline), \
                 patch.object(server.select,'select',return_value=([4] if parent_dead else [],[],[])):
                self.assertFalse(server.endpoint_alive())

    def test_parent_sigkill_cancels_real_native_tree_before_receipt(self):
        server.child_subreaper()
        client, accepted = socket.socketpair()
        client.settimeout(4)
        with tempfile.TemporaryDirectory() as temp:
            marker = Path(temp)/'descendant'
            guardian = os.fork()
            if guardian == 0:
                try:
                    client.close()
                    fd = os.pidfd_open(os.getpid())
                    endpoint = os.fork()
                    if endpoint != 0:
                        accepted.close()
                        while True: signal.pause()
                    server.PARENT_FD = fd
                    server.ENDPOINT_DEADLINE = time.monotonic()+5
                    original = subprocess.Popen
                    def popen(argv, **kwargs):
                        self.assertEqual(argv, server.SYSTEMCTL)
                        code = ('import os,signal,time; pid=os.fork(); '
                                'os.setsid() if pid==0 else None; '
                                'open(%r,"w").write(str(os.getpid())) if pid==0 else None; '
                                'signal.signal(signal.SIGTERM,signal.SIG_IGN); time.sleep(60)') % str(marker)
                        return original([sys.executable,'-c',code], **kwargs)
                    def adapter(controller):
                        return SimpleNamespace(owner_check=lambda *a,**k: controller.runner(
                            server.SYSTEMCTL,capture_output=True,text=True,timeout=3))
                    native = SimpleNamespace(HQ='synthetic',ROOT=Path(temp),Native510=adapter)
                    with patch.object(server,'load_native',return_value=native), \
                         patch.object(server.os,'geteuid',return_value=0), \
                         patch.object(server.subprocess,'Popen',side_effect=popen):
                        server.serve_connected(accepted)
                    os._exit(0)
                except BaseException: os._exit(2)
            accepted.close()
            request = dict(schemaVersion=1,operation='operator-read',requestId='parent-kill-proof',
                           deadlineNs=str(time.monotonic_ns()+3_000_000_000))
            client.sendall(json.dumps(request).encode()+b'\n')
            try:
                end = time.monotonic()+2
                while (not marker.exists() or marker.stat().st_size == 0) and time.monotonic()<end: time.sleep(0.01)
                self.assertTrue(marker.exists(),'native descendant never started')
                descendant = int(marker.read_text())
                os.kill(guardian,signal.SIGKILL)
                os.waitpid(guardian,0)
                guardian = None
                raw = b''
                while not raw.endswith(b'\n'):
                    chunk = client.recv(4096)
                    if not chunk: break
                    raw += chunk
                receipt = json.loads(raw)
                self.assertTrue(receipt['cancelled'])
                self.assertTrue(receipt['settled'])
                self.assertIsNone(receipt['owner'])
                with self.assertRaises(ProcessLookupError): os.kill(descendant,0)
                # The endpoint is adopted after its genuine parent was killed.
                self.assertTrue(server.reap_adopted(time.monotonic_ns()+1_000_000_000))
            finally:
                client.close()
                if guardian is not None:
                    os.kill(guardian,signal.SIGKILL)
                    os.waitpid(guardian,0)
                    server.reap_adopted(time.monotonic_ns()+1_000_000_000)

    def test_real_fd3_endpoint_and_escaped_descendant_settle_on_shutdown(self):
        # The process/IPC lifecycle is real. Only placement and authoritative
        # owner facts are synthetic; neither kernel cgroups nor root paths move.
        code = b'''import os,signal,socket,time
listener=socket.socket(fileno=3)
connection,_=listener.accept()
pid=os.fork()
if pid==0:
 os.setsid()
 signal.signal(signal.SIGTERM,signal.SIG_IGN)
 time.sleep(60)
 os._exit(0)
connection.sendall(str(pid).encode()+b"\\n")
time.sleep(60)
'''
        descendants = []
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)/'fixture.sock'
            listener = socket.socket(socket.AF_UNIX)
            listener.bind(str(path))
            listener.listen(1)
            inode = path.lstat().st_ino
            def monitor(*args):
                with socket.socket(socket.AF_UNIX) as client:
                    client.settimeout(2)
                    client.connect(str(path))
                    descendants.append(int(client.recv(64)))
                # This return models signal/expiry/restart: main must settle.
            with patch.object(supervisor, 'SOCKET', path), \
                 patch.object(supervisor.os, 'geteuid', return_value=0), \
                 patch.object(supervisor.Path, 'read_text', return_value=supervisor.UNIT_CGROUP), \
                 patch.object(supervisor.sys, 'argv', ['fixed']), \
                 patch.object(supervisor, 'load_server', return_value=(server, code)), \
                 patch.object(supervisor, 'gateway_pid', return_value=os.getpid()), \
                 patch.object(supervisor, 'identity', return_value=('start',supervisor.HQ_CGROUP)), \
                 patch.object(supervisor, 'bind_socket', return_value=(listener,inode)), \
                 patch.object(supervisor, 'place_endpoint'), \
                 patch.object(supervisor, 'supervise', side_effect=monitor):
                supervisor.main()
            self.assertFalse(path.exists())
        self.assertEqual(len(descendants),1)
        with self.assertRaises(ProcessLookupError): os.kill(descendants[0],0)
        with self.assertRaises(ChildProcessError): os.waitpid(-1,os.WNOHANG)


if __name__ == '__main__': unittest.main()
