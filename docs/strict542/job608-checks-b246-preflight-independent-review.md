# Independent preflight review: job608 checks b246

Reviewed: docs/strict542/job608-checks-b246-preflight.json (069eebd3) against P/stage-checks-b246
(P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private). C = b246ebebab7d99f189a1d9cc327b7da1f0fc3f69.
Precedent: job608-checks-m674-preflight.json + job608-checks-m674-preflight-independent-review.md.

VERDICT: APPROVE

## Evidence (live, read-only, 2026-10-30)
- sha256: export-manifest.json 16552908c856bff99fde8ae0096b79f1a13d5a511dff9ae45809c21649f658ac,
  run608.sh b04abd4d6d08f2352bd04e5ecc4e3e56d9f6c67223c175a03e98fa44cc0b7816,
  stage608.py a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4,
  successor598.tar 82dc2314b55092e43da87234a32a4996261523a110cff9d7117eff3186dba9b3; all equal the json.
- runner/helper equal `git show b246ebeb:docs/strict542/{run-stage608.sh,stage608.py}` and the m674 checks pins.
- Manifest: run_id stage608-checks-b246, stage checks, execution_state UNUSED, launch_history "none (fresh finite export)",
  source_commit = runner_commit = C, source_export_sha256 264d042c...3007 and successor_archive_sha256 82dc2314...b9b3 (= json),
  stage_inputs {}, required_checks 14.
- `python3 -I -B stage608.py verify-inputs` rc 0; `sh -n run608.sh` rc 0; __pycache__ count under E: 0.
- `storage608.py check --root P --stage checks` rc 0 (free_bytes 4321648640, reserve 2147483648; matches gates_at_prepare).
- Absent: P/checks-b246-offload.log, P/checks-b246-offload.rc, E/result608-checks.
- Launch argv identical to m674 checks precedent: `offload run --timeout 1200 --mem 14g --cpus 4 --artifacts result608-checks
  -- timeout -k 15s 1140s sh run608.sh`; minimum_worker_seconds 1575; required_checks 14; acceptance_extra unchanged.
- Source: 6db9fa81 is the independent review of b246ebeb with VERDICT: APPROVE. `git diff 674840b6 b246ebeb --name-only | grep -v job608-`
  = build598.sh, frozen-package608.py, test_frozen_package608.py. Each was changed only by b246ebeb itself, and those are exactly the files that review covered.

## Conditions
Conditional on fresh live gates at launch (health up, no competing run, verify-inputs 0, storage608 check 0,
no result/log/rc, remaining >= 1575s). ONE run only; no unchanged replay after admission. Not acceptance:
acceptance needs the run's own result (14 checks, zero group/other-writable result entries).
