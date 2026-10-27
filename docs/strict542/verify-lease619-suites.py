"""Read-only completeness gate for619's post-application offloaded suite logs.

This validates evidence, never supplies HQ ownership, application or review.
The original approved619 script is intentionally unchanged. Its exit status
does not prove success: it ends with comm even when either unittest timed out.
"""
import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
PINS = HERE / 'lease619-suite-inputs.json'
MODULES = ('test_control', 'test_launch', 'test_integration', 'test_pressure',
           'test_lease_cap_619', 'test_install_619')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(root):
    pins = json.loads(PINS.read_text())
    for name, expected in pins.items():
        path = root / name
        if not path.is_file() or path.is_symlink() or digest(path) != expected:
            raise ValueError(f'619 source drift: {name}')
    tests = set()
    for module in MODULES:
        directory = 'lease-cap-619' if module.endswith('_619') else 'inc-261023-03'
        tree = ast.parse((root / directory / f'{module}.py').read_text())
        for cls in tree.body:
            if isinstance(cls, ast.ClassDef):
                tests.update(f'{module}.{cls.name}.{fn.name}' for fn in cls.body
                             if isinstance(fn, ast.FunctionDef) and fn.name.startswith('test_'))
    baseline = {name for name in tests if not name.startswith('test_install_619.')}
    if (len(baseline), len(tests)) != (78, 90):
        raise ValueError('619 test inventory changed; new review required')
    return baseline, tests


def baseline_regressions():
    return [tuple(item) for item in json.loads(
        (HERE / 'lease619-baseline-regressions.json').read_text())]


def shared_diagnostics():
    return [tuple(item) for item in json.loads(
        (HERE / 'lease619-shared-diagnostics.json').read_text())]


def test_id(method, owner):
    # Python versions print either module.Class or module.Class.test_method.
    return owner if owner.endswith('.' + method) else owner + '.' + method


def parse_log(raw, expected):
    starts = re.findall(r'^(test_\w+) \(([^\n)]+)\) \.\.\. ?([^\n]*)$', raw, re.M)
    seen = [test_id(method, owner) for method, owner, _ in starts]
    if Counter(seen) != Counter(expected):
        raise ValueError('incomplete, duplicate or unexpected test inventory')
    allowed = {'ok', 'FAIL', 'ERROR', ''}  # empty parent status accompanies failing subtests
    if any(status.strip() not in allowed for _, _, status in starts):
        raise ValueError('skipped, expected-failure or unknown test status')
    summaries = re.findall(r'^Ran (\d+) tests? in [^\n]+$', raw, re.M)
    if summaries != [str(len(expected))]:
        raise ValueError('missing or inconsistent unittest completion summary')
    codes = re.findall(r'^rc=(\d+)$', raw, re.M)
    if len(codes) != 1 or codes[0] not in ('0', '1') or not raw.rstrip().endswith('rc=' + codes[0]):
        raise ValueError('missing completion, timeout, signal or runner failure')

    records = []
    pattern = r'^(FAIL|ERROR): (test_\w+) \(([^\n)]+)\)([^\n]*)\n-{10,}\n(.*?)(?=^={10,}$|^-{10,}$|\Z)'
    for kind, method, owner, subtest, trace in re.findall(pattern, raw, re.M | re.S):
        name = test_id(method, owner)
        if name not in expected:
            raise ValueError('failure outside expected inventory')
        lines = [line for line in trace.splitlines() if line.strip()]
        if not lines:
            raise ValueError('failure without traceback')
        records.append((name, kind, subtest, lines[-1]))
    failures = sum(record[1] == 'FAIL' for record in records)
    errors = len(records) - failures
    if records:
        fields = ', '.join(f'{key}={count}' for key, count in
                           (('failures', failures), ('errors', errors)) if count)
        finals = re.findall(r'^(OK|FAILED[^\n]*)$', raw, re.M)
        if finals != [f'FAILED ({fields})'] or codes != ['1']:
            raise ValueError('failure diagnostics, summary and exit disagree')
    elif re.findall(r'^(OK|FAILED[^\n]*)$', raw, re.M) != ['OK'] or codes != ['0']:
        raise ValueError('success summary and exit disagree')
    failed = {record[0] for record in records}
    for method, owner, status in starts:
        if (status.strip() == 'ok') == (test_id(method, owner) in failed):
            raise ValueError('per-test result and diagnostics disagree')
    return records


def validate(root, logs):
    base_ids, new_ids = inventory(root)
    base_path, new_path = logs / 'baseline.log', logs / 'candidate.log'
    base = parse_log(base_path.read_text(), base_ids)
    candidate = parse_log(new_path.read_text(), new_ids)
    # Reconcile the exact returned619 fixture diagnostics, including test ID and
    # subtest. The historical generic23 fixed-root assumption was inaccurate:
    #19 fixed-root +4 stale dispatcher fixture errors. No arbitrary shared error
    # or changed diagnostic location can satisfy this reviewed evidence gate.
    if Counter(candidate) != Counter(shared_diagnostics()):
        raise ValueError('candidate has unexpected failures or changed known-error count')
    shared = Counter(candidate)
    if any(count > Counter(base)[record] for record, count in shared.items()):
        raise ValueError('candidate-only regression')
    extra = Counter(base) - shared
    if extra != Counter(baseline_regressions()):
        raise ValueError('baseline differences outside exact619 focused regressions')
    return {
        'kind': 'lease619-suite-completeness',
        'baseline_tests': len(base_ids), 'candidate_tests': len(new_ids),
        'shared_known_fixed_root_errors': sum(record[3] ==
            'PermissionError: preservation_fixed_root_required' for record in candidate),
        'shared_known_dispatcher_fixture_errors': sum(record[3] ==
            "AttributeError: module 'isolated_reasoning_q' has no attribute 'requeue_history'"
            for record in candidate),
        'shared_diagnostics_sha256': digest(HERE / 'lease619-shared-diagnostics.json'),
        'baseline_additional_diagnostics': sum(extra.values()),
        'candidate_only_regressions': 0,
        'baseline_log_sha256': digest(base_path), 'candidate_log_sha256': digest(new_path),
        'input_pins_sha256': digest(PINS),
        'scope': 'evidence completeness only; requires independent outcome review and actual HQ receipt',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ops-source', required=True, type=Path)
    parser.add_argument('--logs', required=True, type=Path)
    args = parser.parse_args()
    try:
        result = validate(args.ops_source, args.logs)
    except (ValueError, OSError, KeyError, SyntaxError) as exc:
        parser.exit(1, f'REFUSED: {exc}\n')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
