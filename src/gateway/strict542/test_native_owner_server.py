"""Secretless source-only transport tests. Never execute host owner commands."""
import importlib.util
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import threading
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('transport542', HERE/'native_owner_server.py')
server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server)
SOURCE = Path(os.environ['NATIVE_SOURCE'])/'tools/scheduler_handoff/candidate/maintenance.py'


class NativeTransport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Actual external pinned source, not an injectable availability callback.
        # The generated external module hashes __file__ at import. Keep that
        # reference inside this source archive, never the host native directory.
        with patch.object(server, 'NATIVE_PATH', SOURCE):
            cls.native = server.compile_native(SOURCE.read_bytes())

    def setUp(self):
        self.children = []
        self.pid = os.getpid()
        self.start = '123456'
        self.cgroup = self.native.HQ_CGROUP
        self.caller_cgroup = self.native.HQ_CGROUP
        self.uid = 0
        self.mainpid = self.pid
        self.child_code = 'print(%r)' % str(self.pid)
        self.actual_popen = subprocess.Popen

    def read_proc(self, path, *args, **kwargs):
        key = str(path)
        if key == '/proc/%s/stat' % self.pid:
            return '%s (gateway) ' % self.pid + ' '.join(['S'] + ['0']*18 + [self.start])
        if key == '/proc/self/cgroup': return self.caller_cgroup
        if key == '/proc/%s/cgroup' % self.pid:
            return self.cgroup
        raise AssertionError('unexpected native read: ' + key)

    def popen(self, argv, **kwargs):
        self.assertEqual(argv, server.SYSTEMCTL)
        child = self.actual_popen([sys.executable, '-c', self.child_code], **kwargs)
        self.children.append(child)
        return child

    def exchange(self, cancel=False, ms=800, **changes):
        client, accepted = socket.socketpair()
        client.settimeout(2)
        errors = []
        def run():
            try: server.serve_connected(accepted)
            except Exception as exc: errors.append(exc)
            finally: accepted.close()
        request = dict(schemaVersion=1, operation='operator-read', requestId='synthetic-probe',
                       deadlineNs=str(time.monotonic_ns()+ms*1_000_000))
        request.update(changes)
        with patch.object(server, 'load_native', return_value=self.native), \
             patch('pathlib.Path.read_text', autospec=True, side_effect=self.read_proc), \
             patch('os.geteuid', side_effect=lambda: self.uid), \
             patch('subprocess.Popen', side_effect=self.popen):
            thread = threading.Thread(target=run)
            thread.start()
            try: client.sendall(json.dumps(request).encode()+b'\n')
            except BrokenPipeError: pass  # Endpoint can refuse before request receipt.
            if cancel:
                time.sleep(0.08)
                client.sendall(json.dumps(dict(operation='cancel',requestId=request['requestId'])).encode()+b'\n')
            raw = b''
            while not raw.endswith(b'\n'):
                try: chunk = client.recv(4096)
                except ConnectionResetError: break
                if not chunk: break
                raw += chunk
            thread.join(2)
            self.assertFalse(thread.is_alive(), 'native connection did not settle')
        client.close()
        self.assertFalse(errors, errors)
        self.assertTrue(all(child.poll() is not None for child in self.children))
        return json.loads(raw) if raw else None

    def test_actual_existing_predicates_accept_root_gateway_peer(self):
        receipt = self.exchange()
        self.assertEqual(receipt['owner'], dict(name='Pinch', session=self.native.HQ,
                                               pid=self.pid, start=self.start))
        self.assertTrue(receipt['settled'])
        self.assertEqual(len(self.children), 2)

    def test_native_caller_cgroup_refuses_queue(self):
        self.cgroup = '0::/system.slice/agentq-work.slice/worker'
        self.assertEqual(self.exchange()['reason'], 'native_refused')
        self.assertEqual(self.children, [])

    def test_native_mainpid_refuses_other_gateway(self):
        self.child_code = 'print(999999)'
        self.assertEqual(self.exchange()['reason'], 'native_refused')

    def test_root_endpoint_outside_gateway_cgroup_refuses(self):
        self.caller_cgroup = '0::/system.slice/agentq-work.slice/worker'
        self.assertEqual(self.exchange()['reason'], 'native_refused')
        self.assertEqual(self.children, [])

    def test_nonroot_endpoint_refuses_without_work(self):
        self.uid = 1000
        self.assertIsNone(self.exchange())
        self.assertEqual(self.children, [])

    def test_peer_start_change_between_actual_owner_checks_refuses(self):
        original = self.popen
        def replace_start(argv, **kwargs):
            child = original(argv, **kwargs)
            self.start = 'replaced'
            return child
        self.popen = replace_start
        self.assertEqual(self.exchange()['reason'], 'native_refused')
        self.assertEqual(len(self.children), 1)

    def test_cancel_ack_means_actual_child_reaped(self):
        self.child_code = 'import time; time.sleep(60)'
        start = time.monotonic()
        receipt = self.exchange(cancel=True)
        self.assertTrue(receipt['cancelled'])
        self.assertTrue(receipt['settled'])
        self.assertEqual(receipt['reason'], 'cancelled')
        self.assertLess(time.monotonic()-start, 1)

    def test_ignored_sigterm_is_killed_and_reaped_before_ack(self):
        self.child_code = 'import signal,time; signal.signal(signal.SIGTERM,signal.SIG_IGN); time.sleep(60)'
        receipt = self.exchange(cancel=True)
        self.assertTrue(receipt['cancelled'])
        self.assertEqual(self.children[0].returncode, -9)

    def test_grandchild_holding_stdout_is_killed_and_reaped_before_ack(self):
        self.child_code = ('import os,signal,time; pid=os.fork(); '
                           'signal.signal(signal.SIGTERM,signal.SIG_IGN); time.sleep(60)')
        receipt = self.exchange(cancel=True)
        self.assertTrue(receipt['cancelled'])
        self.assertTrue(receipt['settled'])
        with self.assertRaises(ProcessLookupError): os.killpg(self.children[0].pid, 0)

    def test_escaped_descendant_is_adopted_and_settled_with_pidfd(self):
        self.child_code = ('import os,signal,time; pid=os.fork(); '
                           'os.setsid() if pid==0 else None; '
                           'signal.signal(signal.SIGTERM,signal.SIG_IGN); time.sleep(60)')
        receipt = self.exchange(cancel=True)
        self.assertTrue(receipt['cancelled'])
        self.assertTrue(receipt['settled'])

    def test_exited_leader_does_not_publish_before_descendant_settlement(self):
        self.child_code = ('import os,signal,time; pid=os.fork(); '
                           'print(%s,flush=True) if pid else None; '
                           'os._exit(0) if pid else None; '
                           'signal.signal(signal.SIGTERM,signal.SIG_IGN); time.sleep(60)') % self.pid
        receipt = self.exchange()
        self.assertIsNone(receipt['reason'])
        with self.assertRaises(ChildProcessError): os.waitpid(-1, os.WNOHANG)

    def test_subreaper_setup_failure_refuses_without_work(self):
        with patch.object(server, 'child_subreaper', side_effect=server.Refused()):
            self.assertIsNone(self.exchange())
        self.assertEqual(self.children, [])

    def test_shared_deadline_terminates_and_reaps(self):
        self.child_code = 'import time; time.sleep(60)'
        receipt = self.exchange(ms=400)
        self.assertEqual(receipt['reason'], 'deadline')
        self.assertTrue(receipt['settled'])

    def test_extra_keys_and_overlong_deadline_refuse_without_work(self):
        self.assertIsNone(self.exchange(extra=True))
        self.assertIsNone(self.exchange(schemaVersion=True))
        self.assertIsNone(self.exchange(ms=11000))
        self.assertEqual(self.children, [])

    def test_external_pin_drift_refuses_before_execution(self):
        with self.assertRaises(PermissionError): server.compile_native(b'raise Exception("must not execute")')


def socket_fixture(endpoint, mode):
    """Real cross-language socket transport, actual predicates, synthetic proc."""
    with patch.object(server, 'NATIVE_PATH', SOURCE):
        native = server.compile_native(SOURCE.read_bytes())
    listener = socket.socket(socket.AF_UNIX)
    listener.bind(endpoint)
    os.chmod(endpoint, 0o600)
    listener.listen(1)
    print('ready', flush=True)
    with listener, listener.accept()[0] as connection:
        pid, _, _ = server.struct.unpack('3i', connection.getsockopt(socket.SOL_SOCKET, socket.SO_PEERCRED, 12))
        def read(path, *args, **kwargs):
            if str(path) == '/proc/%s/stat' % pid:
                return '%s (gateway) ' % pid + ' '.join(['S']+['0']*18+['123456'])
            if str(path) in ('/proc/%s/cgroup' % pid, '/proc/self/cgroup'):
                return native.HQ_CGROUP if mode != 'wrong-cgroup' else '0::/queue'
            raise AssertionError('unexpected fixture read')
        actual_popen = subprocess.Popen
        children = []
        def popen(argv, **kwargs):
            if argv != server.SYSTEMCTL: raise AssertionError('unexpected command')
            code = 'print(%s)' % pid if mode != 'cancel' else 'import time; time.sleep(60)'
            child = actual_popen([sys.executable, '-c', code], **kwargs)
            children.append(child)
            return child
        with patch.object(server, 'load_native', return_value=native), \
             patch('pathlib.Path.read_text', autospec=True, side_effect=read), \
             patch('os.geteuid', return_value=0), patch('subprocess.Popen', side_effect=popen):
            server.serve_connected(connection)
        if not all(child.poll() is not None for child in children):
            raise AssertionError('fixture work not settled')


if __name__ == '__main__':
    if len(sys.argv) == 4 and sys.argv[1] == '--socket-fixture': socket_fixture(*sys.argv[2:])
    else: unittest.main()
