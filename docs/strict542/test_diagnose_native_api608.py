import importlib.util
import contextlib
import io
import json
import os
from pathlib import Path
import signal
import hashlib
import subprocess
import tempfile
import threading
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('diagnose_native_api608', HERE/'diagnose-native-api608.py')
launcher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(launcher)


class NativeApiLauncherTests(unittest.TestCase):
    def test_real_preload_smoke_parent_and_spawned_query_share_one_lazy_store(self):
        with tempfile.TemporaryDirectory(dir='/var/tmp') as directory:
            root = Path(directory)
            source = root/'source'
            package = source/'node_modules/typescript'
            package.mkdir(parents=True)
            (root/'native-api608').mkdir()
            (source/'package.json').write_text('{"type":"module"}')
            (package/'package.json').write_text('{"name":"typescript","type":"module","exports":{"./unstable/async":"./async.mjs"}}')
            for name in ('install-native-api-phases608.mjs', 'native-api-phases608.mjs', 'native-api-cpu-profile608.mjs'):
                (root/name).write_bytes((HERE/name).read_bytes())
            methods = ('getConfigFileParsingDiagnostics', 'getProgramDiagnostics', 'getGlobalDiagnostics',
                       'getSyntacticDiagnostics', 'getBindDiagnostics', 'getSemanticDiagnostics',
                       'emitToString', 'getSourceFileNames')
            (package/'async.mjs').write_text('''import fs from 'node:fs';import path from 'node:path';
export class API {
 constructor(){this.internal={async startCPUProfile(dir){this.file=path.join(dir,'123-456-cpuprofile.pb.gz');fs.writeFileSync(this.file,'synthetic finalized profile');},async stopCPUProfile(){return this.file;}};}
 parseConfigFile(){return {};} createSnapshot(){return {};} close(){}
}
export class Program {''' + ''.join(name+'(){return [];}' for name in methods) + '}')
            preload = str(root/'install-native-api-phases608.mjs')
            for _ in range(2):
                smoke = subprocess.run(['node', '--import', preload, '--input-type=module', '-e', ''],
                                       cwd=source, capture_output=True, text=True, timeout=15)
                self.assertEqual(smoke.returncode, 0, smoke.stderr)
                self.assertFalse((root/'native-api608/cpu-profile').exists())
            child = "import {API,Program} from 'typescript/unstable/async';const api=new API();await api.createSnapshot();await new Program().getGlobalDiagnostics();await api.close();"
            parent = "import {spawn} from 'node:child_process';const child=spawn(process.execPath,['--input-type=module','-e',"+json.dumps(child)+"],{stdio:'inherit'});child.on('exit',code=>{process.exitCode=code??1;});"
            run = subprocess.run(['node', '--import', preload, '--input-type=module', '-e', parent],
                                 cwd=source, capture_output=True, text=True, timeout=20)
            self.assertEqual(run.returncode, 0, run.stderr)
            log = root/'native-api608/unified-0/unified-0/build.log'
            log.parent.mkdir(parents=True)
            log.write_text(run.stderr)
            receipt = launcher.verify_cpu_profile(root/'native-api608')
            self.assertEqual(receipt['bytes'], len(b'synthetic finalized profile'))
            self.assertIn('"phase":"finalized"', run.stderr)

    def profile_fixture(self, directory):
        result = Path(directory)/'native-api608'
        profile = result/'cpu-profile'
        profile.mkdir(parents=True, mode=0o700)
        payload = b'fixed synthetic finalized profile'
        name = '123-456-cpuprofile.pb.gz'
        (profile/name).write_bytes(payload)
        receipt = dict(kind='NATIVE_CPU_PROFILE_RECEIPT608', complete=True,
                       profile=name, sha256=hashlib.sha256(payload).hexdigest(),
                       bytes=len(payload), limit_ms=120000, max_profile_bytes=8388608)
        (profile/'receipt.json').write_text(json.dumps(receipt))
        (profile/'receipt.json').chmod(0o600)
        log = result/'unified-0/unified-0/build.log'
        log.parent.mkdir(parents=True)
        log.write_text(json.dumps(dict(kind='NATIVE_API_PHASE608', method='Program.getGlobalDiagnostics', phase='start'))+'\n')
        return result, profile, receipt, log

    def test_finalized_cpu_profile_requires_exact_bytes_inventory_and_global_entry(self):
        with tempfile.TemporaryDirectory(dir='/var/tmp') as directory:
            result, profile, receipt, log = self.profile_fixture(directory)
            self.assertEqual(launcher.verify_cpu_profile(result), receipt)
            (profile/receipt['profile']).write_bytes(b'changed')
            with self.assertRaises(ValueError):
                launcher.verify_cpu_profile(result)

    def test_cpu_profile_refuses_late_failure_even_after_published_receipt(self):
        for failure in ('NATIVE_CPU_PROFILE_REFUSED608', json.dumps(dict(kind='NATIVE_CPU_PROFILE608', phase='refused', reason='ambiguous-api'))):
            with tempfile.TemporaryDirectory(dir='/var/tmp') as directory:
                result, profile, receipt, log = self.profile_fixture(directory)
                with log.open('a') as stream:
                    stream.write(failure+'\n')
                with self.assertRaises(ValueError):
                    launcher.verify_cpu_profile(result)

    def test_cpu_profile_missing_extra_oversize_and_redirected_evidence_refuse(self):
        for fault in ('missing', 'extra', 'oversize', 'symlink', 'no-global'):
            with tempfile.TemporaryDirectory(dir='/var/tmp') as directory:
                result, profile, receipt, log = self.profile_fixture(directory)
                target = profile/receipt['profile']
                if fault == 'missing':
                    (profile/'receipt.json').unlink()
                elif fault == 'extra':
                    (profile/'unexpected').write_text('extra')
                elif fault == 'oversize':
                    with target.open('wb') as stream:
                        stream.truncate(8388609)
                elif fault == 'symlink':
                    outside = Path(directory)/'outside'
                    target.rename(outside)
                    target.symlink_to(outside)
                else:
                    log.write_text('no global entry\n')
                with self.assertRaises(ValueError):
                    launcher.verify_cpu_profile(result)

    def test_runner_only_fixed_entry_and_acceptance_are_changed(self):
        original = (HERE/'run-stage608.sh').read_text()
        changed = launcher.external_runner(original)
        self.assertIn('python3 stage608.py verify-inputs', changed)
        self.assertIn('python3 stage608.py stage-native && python3 stage608.py restore-build', changed)
        self.assertNotIn('python3 stage608.py archive-build "$RESULT"', changed)
        self.assertNotIn('python3 stage608.py receipt "$RESULT"', changed)
        restored = changed.replace('sh ../native-api-build608.sh "$STAGE"', 'sh docs/strict542/run-build-stage608.sh "$STAGE"')
        restored = restored.replace('echo DIAGNOSTIC_ONLY_NO_CHECKPOINT608', 'python3 stage608.py archive-build "$RESULT"')
        restored = restored.replace('echo DIAGNOSTIC_ONLY_NO_STAGE_RECEIPT608', 'python3 stage608.py receipt "$RESULT"')
        self.assertEqual(restored, original)

    def test_install_and_preflights_precede_actual_preload_smoke(self):
        original = (HERE/'run-build-stage608.sh').read_text()
        self.assertEqual(launcher.digest(HERE/'run-build-stage608.sh'), launcher.BUILD)
        changed = launcher.external_build(original)
        prefix = original.rsplit('node --import ./scripts/tsx.mjs scripts/build-checkpoint608-owned.mjs "$STAGE"', 1)[0]
        self.assertTrue(changed.startswith(prefix))
        self.assertLess(changed.index('pnpm install --frozen-lockfile'), changed.index('NATIVE_API_PRELOAD_SMOKE608'))
        self.assertLess(changed.index('NATIVE_API_PRELOAD_SMOKE608'), changed.index('timeout -k 15s 900s'))
        self.assertEqual(changed.count('scripts/build-checkpoint608-owned.mjs "$STAGE"'), 1)
        self.assertEqual(changed.count('frozen-package608.py preflight'), 2)

    def test_boundary_change_and_duplicate_refuse(self):
        for text in ('different', 'fixed fixed'):
            with self.assertRaises(ValueError):
                launcher.once(text, 'fixed', 'new')

    def test_real_reviewed_observers_match_pins(self):
        for name, expected in launcher.OBSERVERS.items():
            self.assertEqual(launcher.digest(HERE/name), expected)

    def test_manifest_identity_and_runner_refuse_before_launch(self):
        old = Path.cwd()
        with tempfile.TemporaryDirectory(dir='/var/tmp') as directory:
            os.chdir(directory)
            try:
                manifest = dict(source_commit='wrong', source_export_sha256=launcher.COMMON, stage='unified-0')
                Path('export-manifest.json').write_text(json.dumps(manifest))
                with self.assertRaisesRegex(ValueError, 'unchanged'):
                    launcher.validate()
                manifest.update(source_commit=launcher.FREEZE, runner_sha256='wrong')
                Path('export-manifest.json').write_text(json.dumps(manifest))
                with self.assertRaisesRegex(ValueError, 'runner pin'):
                    launcher.validate()
            finally:
                os.chdir(old)

    def test_current_a39a_export_is_accepted_and_historical_profile_refused(self):
        current = dict(source_commit='a39ad5ee95609193502850d0dbb87b5dcbb5e3e3',
                       source_export_sha256='d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62',
                       stage='unified-0',
                       runner_sha256='e2ed7e1337f5d0564b56e61174d0837440655cd38f75416608bff3de82780605')
        pins = {'run608.sh': current['runner_sha256'],
                'stage608.py': 'a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4',
                **launcher.OBSERVERS}
        old = Path.cwd()
        with tempfile.TemporaryDirectory(dir='/var/tmp') as directory:
            os.chdir(directory)
            try:
                for name in pins:
                    Path(name).write_text('synthetic pinned-file fixture')
                Path('export-manifest.json').write_text(json.dumps(current))
                with patch.object(launcher, 'digest', side_effect=lambda name: pins[str(name)]):
                    self.assertEqual(launcher.validate(), current)
                    historical = dict(current,
                        source_commit='1bed4d1bb53eff145f724cc6a448dc73b3609015',
                        source_export_sha256='5d7e9d57fb660e2b54f5595e81ddf332027e21b303937c2cd6bc7f718f311263',
                        runner_sha256='eac266cfaab7efef7c92ed94c53a0a55e75303b8ee4810bc15f21f243a76b8ee')
                    Path('export-manifest.json').write_text(json.dumps(historical))
                    with self.assertRaisesRegex(ValueError, 'unchanged'):
                        launcher.validate()
                    wrong_common = dict(current, source_export_sha256=historical['source_export_sha256'])
                    Path('export-manifest.json').write_text(json.dumps(wrong_common))
                    with self.assertRaisesRegex(ValueError, 'unchanged'):
                        launcher.validate()
            finally:
                os.chdir(old)

    def test_resource_samples_reuse_fixed_sampler_and_preserve_actual_status(self):
        with tempfile.TemporaryDirectory(dir='/var/tmp') as directory:
            log = Path(directory)/'runner.log'
            sample = {'at':1, 'processes':[], 'cgroup':{'cpu.stat':'usage_usec 1'}}
            self.assertEqual(launcher.collect(['sh', '-c', 'exit 7'], log, 2,
                                             sample_fn=lambda: sample), (7, None))
            records = [json.loads(line) for line in log.with_name('samples.jsonl').read_text().splitlines()]
            self.assertTrue(records)
            self.assertTrue(all(record == sample for record in records))

    def test_resource_sampling_failure_is_explicit_and_does_not_leak_message(self):
        def refused():
            raise OSError('private exception detail')
        with tempfile.TemporaryDirectory(dir='/var/tmp') as directory:
            log = Path(directory)/'runner.log'
            self.assertEqual(launcher.collect(['sh', '-c', 'exit 7'], log, 2,
                                             sample_fn=refused), (7, None))
            raw = log.with_name('samples.jsonl').read_text()
            self.assertNotIn('private', raw)
            self.assertEqual({json.loads(line)['sampling_error'] for line in raw.splitlines()}, {'OSError'})

    def test_collect_keeps_actual_failure_distinct(self):
        with tempfile.TemporaryDirectory(dir='/var/tmp') as directory:
            log = Path(directory)/'runner.log'
            self.assertEqual(launcher.collect(['sh', '-c', 'echo refused; exit 7'], log, 2), (7, None))
            self.assertEqual(log.read_text(), 'refused\n')

    def test_collect_timeout_retains_output_and_actual124(self):
        with tempfile.TemporaryDirectory(dir='/var/tmp') as directory:
            log = Path(directory)/'runner.log'
            self.assertEqual(launcher.collect(['sh', '-c', 'echo started; exec sleep 10'], log, 1), (124, None))
            self.assertEqual(log.read_text(), 'started\n')

    def test_cancellation_is_forwarded_and_collected(self):
        with tempfile.TemporaryDirectory(dir='/var/tmp') as directory:
            log = Path(directory)/'runner.log'
            timer = threading.Timer(0.3, lambda: os.kill(os.getpid(), signal.SIGTERM))
            timer.start()
            try:
                rc, cancelled = launcher.collect(['sh', '-c', 'trap "echo settled; exit 143" TERM; echo started; sleep 10'], log, 20)
            finally:
                timer.cancel()
            self.assertEqual(cancelled, 143)
            # GNU timeout reports 124 after an externally forwarded TERM too;
            # the separate cancellation field must prevent success collection.
            self.assertIn(rc, (124, 143, -15))
            self.assertIn('started', log.read_text())
            self.assertIn('settled', log.read_text())

    def test_main_refuses_missing_or_failed_resource_evidence_without_masking_timeout(self):
        old = Path.cwd()
        for raw in ('', '{"sampling_error":"OSError"}\n'):
            with tempfile.TemporaryDirectory(dir='/var/tmp') as directory:
                os.chdir(directory)
                try:
                    Path('run608.sh').write_text('synthetic fixture')
                    def collect_fixture(*args, **kwargs):
                        Path('native-api608/samples.jsonl').write_text(raw)
                        return (124, None)
                    with patch.object(launcher, 'validate', return_value={'run_id':'fixture'}), \
                         patch.object(launcher, 'external_runner', return_value='fixture'), \
                         patch.object(launcher, 'resource_sampler', return_value=lambda: None), \
                         patch.object(launcher, 'collect', side_effect=collect_fixture), \
                         patch('sys.argv', ['diagnose-native-api608.py']), \
                         contextlib.redirect_stdout(io.StringIO()):
                        with self.assertRaises(SystemExit) as raised:
                            launcher.main()
                    self.assertEqual(raised.exception.code, 7)
                    receipt = json.loads(Path('native-api608/diagnostic.json').read_text())
                    self.assertEqual(receipt['command_exit'], 124)
                    self.assertEqual(receipt['resource_sampling_errors'], 1)
                    self.assertFalse(receipt['accepted_checkpoint'])
                finally:
                    os.chdir(old)

    def test_main_profile_failure_retains_timeout_and_suppresses_failure_message(self):
        old = Path.cwd()
        for valid_profile in (False, True):
            with tempfile.TemporaryDirectory(dir='/var/tmp') as directory:
                os.chdir(directory)
                try:
                    Path('run608.sh').write_text('synthetic fixture')
                    def collect_fixture(*args, **kwargs):
                        Path('native-api608/samples.jsonl').write_text('{"at":1,"processes":[],"cgroup":{}}\n')
                        return (124, None)
                    profile = {'complete':True} if valid_profile else None
                    with patch.object(launcher, 'validate', return_value={'run_id':'fixture'}), \
                         patch.object(launcher, 'external_runner', return_value='fixture'), \
                         patch.object(launcher, 'resource_sampler', return_value=lambda: None), \
                         patch.object(launcher, 'collect', side_effect=collect_fixture), \
                         patch.object(launcher, 'verify_cpu_profile', return_value=profile,
                                      side_effect=None if valid_profile else ValueError('private failure detail')), \
                         patch('sys.argv', ['diagnose-native-api608.py']), \
                         contextlib.redirect_stdout(io.StringIO()):
                        with self.assertRaises(SystemExit) as raised:
                            launcher.main()
                    self.assertEqual(raised.exception.code, 0 if valid_profile else 7)
                    raw = Path('native-api608/diagnostic.json').read_text()
                    receipt = json.loads(raw)
                    self.assertEqual(receipt['command_exit'], 124)
                    self.assertEqual(receipt['resource_sampling_errors'], 0)
                    self.assertEqual(receipt['cpu_profile_error'], None if valid_profile else 'ValueError')
                    self.assertNotIn('private failure detail', raw)
                    self.assertFalse(receipt['accepted_checkpoint'])
                finally:
                    os.chdir(old)

    def test_no_caller_selected_command(self):
        with patch('sys.argv', ['diagnose-native-api608.py', 'arbitrary']):
            with self.assertRaisesRegex(ValueError, 'caller-selected'):
                launcher.main()

    def test_progress_forwards_only_fixed_observer_fields(self):
        events = ['secret arbitrary args', 'NATIVE_API_PRELOAD_SMOKE608',
                  '{"kind":"NATIVE_API_PHASE608","pid":1,"method":"API.close","phase":"start","monotonic_ms":1}',
                  '{"kind":"NATIVE_API_PHASE608","method":"API.close","phase":"start","args":"secret"}']
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            launcher.forward_events(io.StringIO('\n'.join(events)+'\n'))
        self.assertNotIn('secret', output.getvalue())
        self.assertEqual(len(output.getvalue().splitlines()), 2)

    def test_term_ignoring_grandchild_is_killed_after_leader_exit(self):
        with tempfile.TemporaryDirectory(dir='/var/tmp') as directory:
            pid_file = Path(directory)/'child.pid'
            command = 'trap "exit 0" TERM; sh -c \'trap "" TERM; echo $$ >"$1"; exec sleep 60\' fixture "$1" & wait'
            rc, cancelled = launcher.collect(['sh', '-c', command, 'fixture', str(pid_file)], Path(directory)/'log', 1)
            self.assertEqual(rc, 124)
            self.assertIsNone(cancelled)
            pid = int(pid_file.read_text())
            stat = Path('/proc')/str(pid)/'stat'
            if stat.exists():
                self.assertIn(stat.read_text().rsplit(')', 1)[1].split()[0], ('Z', 'X'))


if __name__ == '__main__':
    unittest.main()
