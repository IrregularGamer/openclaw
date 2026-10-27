"""Small synthetic evidence refusal checks; never runs619's control suites."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('suite_gate', Path(__file__).with_name('verify-lease619-suites.py'))
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


def log(ids, errors, *, modern=True):
    diagnostics = {item[0]: item for item in errors}
    lines = []
    for name in sorted(ids):
        owner, method = name.rsplit('.', 1)
        label = name if modern else owner
        status = diagnostics[name][1] if name in diagnostics else 'ok'
        lines.append(f'{method} ({label}) ... {status}')
    for name, kind, subtest, reason in errors:
        owner, method = name.rsplit('.', 1)
        label = name if modern else owner
        lines.extend(['=' * 70, f'{kind}: {method} ({label}){subtest}', '-' * 70,
                      'Traceback (most recent call last):', '  synthetic pinned fixture', reason, ''])
    lines.extend(['-' * 70, f'Ran {len(ids)} tests in 1.000s', ''])
    if errors:
        counts = ', '.join(f'{key}={sum(item[1] == kind for item in errors)}'
                           for key, kind in [('failures', 'FAIL'), ('errors', 'ERROR')]
                           if any(item[1] == kind for item in errors))
        lines.extend([f'FAILED ({counts})', 'rc=1'])
    else:
        lines.extend(['OK', 'rc=0'])
    return '\n'.join(lines) + '\n'


class EvidenceGate(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir='/var/tmp')
        self.addCleanup(self.temp.cleanup)
        self.logs = Path(self.temp.name)
        self.old = {f'test_control.ControllerTests.test_case{i:02}' for i in range(61)}
        self.old |= {f'test_lease_cap_619.Capability.test_case{i:02}' for i in range(17)}
        self.new = self.old | {f'test_install_619.Installer.test_case{i:02}' for i in range(12)}
        self.shared = [(name, 'ERROR', '', 'PermissionError: preservation_fixed_root_required')
                       for name in sorted(self.old)[:23]]
        self.regression = ('test_lease_cap_619.Capability.test_case00', 'FAIL', '',
                           'AssertionError: expected reviewed red baseline')
        self.base = log(self.old, self.shared + [self.regression])
        self.candidate = log(self.new, self.shared)
        self.addCleanup(patch.stopall)
        patch.object(gate, 'inventory', return_value=(self.old, self.new)).start()
        patch.object(gate, 'baseline_regressions', return_value=[self.regression]).start()
        patch.object(gate, 'shared_diagnostics', return_value=self.shared, create=True).start()

    def check(self):
        (self.logs / 'baseline.log').write_text(self.base)
        (self.logs / 'candidate.log').write_text(self.candidate)
        return gate.validate(Path('/unused'), self.logs)

    def test_complete_reviewed_difference_has_exact_counts_and_hashes(self):
        receipt = self.check()
        self.assertEqual((receipt['baseline_tests'], receipt['candidate_tests']), (78, 90))
        self.assertEqual(receipt['candidate_only_regressions'], 0)
        self.assertEqual(receipt['candidate_log_sha256'], gate.digest(self.logs / 'candidate.log'))

    def test_exact_reviewed_shared_diagnostics_can_include_stale_dispatcher_fixture(self):
        self.shared[-1] = (*self.shared[-1][:3],
            "AttributeError: module 'isolated_reasoning_q' has no attribute 'requeue_history'")
        self.base = log(self.old, self.shared + [self.regression])
        self.candidate = log(self.new, self.shared)
        self.assertEqual(self.check()['candidate_only_regressions'], 0)

    def test_timeout_cannot_pass_even_if_shell_would_exit_zero(self):
        self.candidate = self.candidate.replace('rc=1', 'rc=124')
        with self.assertRaisesRegex(ValueError, 'timeout'): self.check()

    def test_partial_log_without_any_failing_names_refuses(self):
        self.candidate = '\n'.join(self.candidate.splitlines()[:40]) + '\nrc=0\n'
        with self.assertRaisesRegex(ValueError, 'inventory'): self.check()

    def test_omitted_or_duplicated_test_refuses(self):
        original = self.candidate
        for content in (original.split('\n', 1)[1], original.splitlines()[0] + '\n' + original):
            self.candidate = content
            with self.assertRaisesRegex(ValueError, 'inventory'): self.check()

    def test_wrong_completion_count_refuses(self):
        self.candidate = self.candidate.replace('Ran 90 tests', 'Ran 89 tests')
        with self.assertRaisesRegex(ValueError, 'summary'): self.check()

    def test_shared_arbitrary_error_is_not_a_known_fixture_exception(self):
        self.candidate = self.candidate.replace('PermissionError: preservation_fixed_root_required',
                                                'PermissionError: new real regression')
        self.base = self.base.replace('PermissionError: preservation_fixed_root_required',
                                      'PermissionError: new real regression')
        with self.assertRaisesRegex(ValueError, 'unexpected failures'): self.check()

    def test_candidate_new_failure_refuses(self):
        changed = self.shared.copy()
        changed[0] = (sorted(self.old)[24], *changed[0][1:])
        self.candidate = log(self.new, changed)
        with self.assertRaisesRegex(ValueError, 'unexpected failures'): self.check()

    def test_missing_failure_trace_refuses(self):
        self.candidate = self.candidate.replace('ERROR: test_case00', 'BROKEN: test_case00', 1)
        with self.assertRaisesRegex(ValueError, 'diagnostics'): self.check()

    def test_skipped_case_refuses(self):
        self.candidate = self.candidate.replace('... ok', "... skipped 'unavailable'", 1)
        with self.assertRaisesRegex(ValueError, 'skipped'): self.check()

    def test_python_older_class_labels_and_subtests(self):
        regression = (self.regression[0], 'FAIL', ' (max_memory_MiB=4096)', self.regression[3])
        raw = log(self.old, self.shared + [regression], modern=False)
        self.assertEqual(gate.parse_log(raw, self.old)[-1], regression)

    def test_baseline_unrelated_failure_refuses(self):
        extra = (sorted(self.old)[25], 'ERROR', '', 'RuntimeError: unrelated')
        self.base = log(self.old, self.shared + [self.regression, extra])
        with self.assertRaisesRegex(ValueError, 'outside exact'): self.check()

    def test_missing_baseline_regression_is_not_accepted_as_equivalence(self):
        self.base = log(self.old, self.shared)
        with self.assertRaisesRegex(ValueError, 'outside exact'): self.check()

    def test_success_label_cannot_hide_error(self):
        self.candidate = self.candidate.replace('... ERROR', '... ok', 1)
        with self.assertRaisesRegex(ValueError, 'per-test'): self.check()


if __name__ == '__main__':
    unittest.main()
