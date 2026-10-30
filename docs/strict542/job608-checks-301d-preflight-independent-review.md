# Independent preflight review: job608 checks 301d

Reviewed: docs/strict542/job608-checks-301d-preflight.json (0edf2b6c) against P/stage-checks-301d
(P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private). C = 301d7456bf5b0c4179b27d0db97eac7b07143f4a.
Precedent: job608-checks-b246-preflight.json + its approval 03dd497a.

VERDICT: APPROVE

## Evidence (live, read-only, 2026-10-30)
- sha256: export-manifest.json 1a5d47a7...a9ee, run608.sh b04abd4d...7816, stage608.py 1d2bf411...bffd,
  successor598.tar e2ed663e...e53b; all equal the json. run608.sh/stage608.py byte-identical (cmp) to `git show C:docs/strict542/{run-stage608.sh,stage608.py}`.
- Manifest: run_id stage608-checks-301d, stage checks, execution_state UNUSED, launch_history "none (fresh finite export)",
  source_commit = runner_commit = C, source_export_sha256 99add7e1...291d, successor_archive_sha256 = json, stage_inputs {},
  required_checks 14, no lineage fields (checks does not use lineage, as the scope says).
- `sh -n run608.sh` rc 0; `python3 -I -B stage608.py verify-inputs` rc 0; __pycache__/*.pyc under E: 0.
- `storage608.py check --root P --stage checks` rc 0 (free_bytes 4301152256 = gates_at_prepare; reserve 2147483648).
- Absent: P/checks-301d-offload.log, P/checks-301d-offload.rc, E/result608-checks.
- Launch argv identical to b246 precedent: `offload run --timeout 1200 --mem 14g --cpus 4 --artifacts result608-checks
  -- timeout -k 15s 1140s sh run608.sh`; minimum_worker_seconds 1575, required_checks 14, acceptance_extra unchanged.
- Source: 7beaf342 (job608-input-lineage-301d7456-independent-review.md) is the independent review of C with Verdict APPROVE; C..0edf2b6c adds only docs files.

## Conditions
Conditional on fresh live gates at launch (health up, no competing run, verify-inputs 0, storage608 check 0,
no result/log/rc, remaining >= 1575s). ONE run only; no unchanged replay after admission. Not acceptance:
acceptance needs the run's own result (14 checks, zero group/other-writable result entries).
