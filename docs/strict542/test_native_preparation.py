"""Synthetic source preparation tests, never a native availability receipt.

Run only in the approved remote source-only export. NATIVE_SOURCE points to an
ABH HEAD archive, not to a runtime installation or credential/config directory.
"""
import ast
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
BASE = Path(os.environ['NATIVE_SOURCE'])


class NativePreparation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temporary.cleanup)
        cls.source = Path(cls.temporary.name)
        for relative, digest in json.loads((HERE/'native-targets.json').read_text())['targets'].items():
            raw = (BASE/relative).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest, relative
        shutil.copytree(BASE/'tools', cls.source/'tools')
        subprocess.run(['patch','--batch','--fuzz=0','-p1','-i',str(HERE/'native-owner-read.patch')],
                       cwd=cls.source, check=True, capture_output=True)
        subprocess.run(['python3',str(cls.source/'tools/scheduler_handoff/build_candidate.py')],
                       check=True, capture_output=True)
        cls.maintenance = ast.parse((cls.source/'tools/scheduler_handoff/candidate/maintenance.py').read_text())
        cls.control = ast.parse((cls.source/'tools/scheduler_handoff/candidate/control.py').read_text())

    def setUp(self):
        self.clock = 1_000_000_000
        self.calls = []
        self.stat = '1 (gateway) ' + ' '.join(['S'] + ['0']*18 + ['123'])
        self.owner_cgroup = '0::/user.slice/user-1000.slice/user@1000.service/app.slice/openclaw-gateway.service'
        def read(path):
            key = str(path)
            if key == '/proc/7/stat': return self.stat
            if key in ('/proc/7/cgroup','/proc/self/cgroup'): return self.owner_cgroup
            raise AssertionError('unexpected read: '+key)
        self.read = read
        def run(argv, **options):
            self.calls.append((argv, options))
            return SimpleNamespace(returncode=0, stdout='7\n')
        self.run = run
        self.namespace = dict(Path=Path, ROOT=Path('/var/lib/agentq-safety'),
                              HQ510='agent:claw:telegram:group:-5217857869',
                              HQ='agent:claw:telegram:group:-5217857869',
                              HQ_CGROUP=self.owner_cgroup, os=os, time=time, subprocess=subprocess)
        # Keep the actual existing predicates, not an always-success replacement.
        nodes = []
        for name, methods in [('Preservation', {'__init__','owner'}), ('Native510', {'__init__','owner_check'})]:
            node = next(n for n in self.maintenance.body if isinstance(n,ast.ClassDef) and n.name == name)
            node.body = [n for n in node.body if isinstance(n,ast.FunctionDef) and n.name in methods]
            nodes.append(node)
        nodes.append(next(n for n in self.maintenance.body if isinstance(n,ast.FunctionDef) and n.name == 'owner542_read'))
        exec(compile(ast.Module(body=nodes, type_ignores=[]), '<exact-native-source>', 'exec'), self.namespace)

    def call(self, deadline=11_000_000_000):
        with patch('os.geteuid',return_value=0), patch('time.monotonic_ns',side_effect=lambda:self.clock), \
             patch('pathlib.Path.read_text',autospec=True,side_effect=self.read), \
             patch('subprocess.run',side_effect=lambda *a,**kw:self.run(*a,**kw)):
            return self.namespace['owner542_read'](deadline)

    def test_derived_identity_and_existing_predicate_before_after(self):
        value=self.call()
        self.assertEqual(value, {'schemaVersion':1,'owner':{'name':'Pinch','session':self.namespace['HQ'],'pid':7,'start':'123'}})
        self.assertEqual(len(self.calls),3)
        self.assertTrue(all(0 < options['timeout'] <= 5 for _,options in self.calls))

    def test_deadline_invalid_expired_and_overlong(self):
        for deadline in (None, True, self.clock, self.clock-1, self.clock+10_000_000_001):
            with self.subTest(deadline=deadline), self.assertRaisesRegex(PermissionError,'owner542_deadline'):
                self.call(deadline)
        self.assertEqual(self.calls,[])

    def test_deadline_covers_all_native_checks(self):
        def run(argv,**options):
            self.calls.append((argv,options))
            self.clock += 4_000_000_000
            return SimpleNamespace(returncode=0, stdout='7')
        self.run=run
        with self.assertRaisesRegex(PermissionError,'owner542_deadline'): self.call()
        self.assertLessEqual(len(self.calls),3)

    def test_nonroot_refuses(self):
        with patch('os.geteuid',return_value=1000), self.assertRaisesRegex(PermissionError,'owner542_root'):
            self.namespace['owner542_read'](time.monotonic_ns()+1_000_000_000)

    def test_bad_mainpid_refuses(self):
        for value in ('0','-1','7 8','', '７'):
            self.run=lambda *a,**kw:SimpleNamespace(returncode=0,stdout=value)
            with self.subTest(value=value), self.assertRaises(PermissionError): self.call()

    def test_exact_existing_cgroup_predicate_refuses_queue(self):
        self.owner_cgroup='0::/system.slice/agentq-work.slice/worker'
        with self.assertRaisesRegex(PermissionError,'owner_loss'): self.call()

    def test_root_with_valid_gateway_but_queue_caller_refuses(self):
        original=self.read
        def read(path):
            if str(path)=='/proc/self/cgroup':
                return '0::/system.slice/agentq-work.slice/worker'
            return original(path)
        self.read=read
        with self.assertRaisesRegex(PermissionError,'owner_loss'): self.call()
        # Gateway discovery succeeds, but caller=True rejects before MainPID recheck.
        self.assertEqual(len(self.calls),1)

    def test_second_owner_check_caller_cgroup_change_refuses(self):
        original=self.read
        count=0
        def read(path):
            nonlocal count
            if str(path)=='/proc/self/cgroup':
                count+=1
                if count==2:
                    return '0::/system.slice/agentq-work.slice/worker'
            return original(path)
        self.read=read
        with self.assertRaisesRegex(PermissionError,'owner_loss'): self.call()
        self.assertEqual(count,2)
        self.assertEqual(len(self.calls),2)

    def test_second_owner_check_root_loss_refuses(self):
        original=self.run
        def run(*args,**options):
            result=original(*args,**options)
            if len(self.calls)==2:
                self.uid_patch.return_value=1000
            return result
        self.run=run
        # The outer call's mock owns the uid. Capture it through a narrow patched
        # call rather than asserting an invented transport or a caller identity.
        with patch('os.geteuid',return_value=0) as self.uid_patch, \
             patch('time.monotonic_ns',side_effect=lambda:self.clock), \
             patch('pathlib.Path.read_text',autospec=True,side_effect=self.read), \
             patch('subprocess.run',side_effect=lambda *a,**kw:self.run(*a,**kw)):
            with self.assertRaisesRegex(PermissionError,'owner_loss'):
                self.namespace['owner542_read'](11_000_000_000)
        self.assertEqual(len(self.calls),2)

    def test_start_change_refuses(self):
        count=0
        original=self.read
        def read(path):
            nonlocal count
            value=original(path)
            if str(path)=='/proc/7/stat':
                count+=1
                if count>1: return value[:-3]+'456'
            return value
        self.read=read
        with self.assertRaisesRegex(PermissionError,'owner_loss'): self.call()

    def test_gateway_mainpid_change_refuses(self):
        count=0
        def run(*a,**kw):
            nonlocal count
            count+=1
            return SimpleNamespace(returncode=0, stdout='7' if count<3 else '8')
        self.run=run
        with self.assertRaisesRegex(PermissionError,'gateway_loss'): self.call()

    def test_cancel_refuses_and_restores_handlers(self):
        import signal
        previous=signal.getsignal(signal.SIGTERM)
        def run(*a,**kw): signal.getsignal(signal.SIGTERM)(signal.SIGTERM,None)
        self.run=run
        with self.assertRaisesRegex(PermissionError,'owner542_cancelled'): self.call()
        self.assertIs(signal.getsignal(signal.SIGTERM),previous)

    def test_second_owner_check_start_change_refuses(self):
        count=0
        original=self.read
        def read(path):
            nonlocal count
            value=original(path)
            if str(path)=='/proc/7/stat':
                count+=1
                if count==3: return value[:-3]+'456'
            return value
        self.read=read
        with self.assertRaisesRegex(PermissionError,'owner_loss'): self.call()

    def test_missing_or_malformed_proc_refuses(self):
        original=self.read
        for error in (FileNotFoundError(), PermissionError()):
            def read(path): raise error
            self.read=read
            with self.subTest(error=type(error).__name__), self.assertRaises(OSError): self.call()
        self.read=original
        self.stat='malformed'
        with self.assertRaises((IndexError,ValueError)): self.call()

    def test_nonzero_systemctl_refuses(self):
        self.run=lambda *a,**kw:SimpleNamespace(returncode=1,stdout='7')
        with self.assertRaisesRegex(PermissionError,'owner542_gateway'): self.call()

    def synthetic_child(self, cancel):
        # Exercise Python's actual subprocess cleanup, without invoking systemctl,
        # any native endpoint, auth resolver or provider. Timer is always joined.
        import signal
        import sys
        import threading
        actual_run=subprocess.run
        actual_popen=subprocess.Popen
        children=[]
        def popen(*a,**kw):
            child=actual_popen(*a,**kw)
            children.append(child)
            if timer: timer.start()
            return child
        def run(argv,**options):
            return actual_run([sys.executable,'-c','import time; time.sleep(60)'],**options)
        self.run=run
        timer=threading.Timer(.05,lambda:os.kill(os.getpid(),signal.SIGTERM)) if cancel else None
        try:
            with patch('subprocess.Popen',side_effect=popen):
                if cancel:
                    with self.assertRaisesRegex(PermissionError,'owner542_cancelled'): self.call()
                else:
                    with self.assertRaises(subprocess.TimeoutExpired): self.call(self.clock+100_000_000)
        finally:
            if timer:
                timer.cancel()
                timer.join()
        self.assertEqual(len(children),1)
        self.assertIsNotNone(children[0].returncode)
        with self.assertRaises(ProcessLookupError): os.kill(children[0].pid,0)

    def test_actual_synthetic_child_is_killed_and_reaped_on_cancel(self):
        self.synthetic_child(True)

    def test_actual_synthetic_child_is_killed_and_reaped_on_timeout(self):
        self.synthetic_child(False)

    def test_cli_read_precedes_controller_and_mutating_error_handler(self):
        main=next(n for n in self.control.body if isinstance(n,ast.FunctionDef) and n.name=='main')
        statements=[ast.unparse(n) for n in main.body]
        read=next(i for i,s in enumerate(statements) if s.startswith("if args.action == 'owner542-read':"))
        controller=next(i for i,s in enumerate(statements) if s=='controller = Controller()')
        self.assertLess(read,controller)
        self.assertNotIn('controller.',statements[read])
        self.assertIn('owner542_read(args.deadline_ns)',statements[read])

if __name__=='__main__': unittest.main()
