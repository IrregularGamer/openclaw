import importlib.util
import contextlib
import io
import json
import os
from pathlib import Path
import signal
import tempfile
import threading
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('diagnose_native_api608', HERE/'diagnose-native-api608.py')
launcher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(launcher)


class NativeApiLauncherTests(unittest.TestCase):
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
