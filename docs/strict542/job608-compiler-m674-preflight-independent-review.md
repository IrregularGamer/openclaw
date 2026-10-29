# job608 independent review: compiler preflight m674 at 674840b6

Reviewer: independent (read-only; no offload/build/service run). Date 2026-10-29.
Reviewed: docs/strict542/job608-compiler-m674-preflight.json (a130cb2b) against P/stage-compiler-m674
(P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private). C = 674840b669c43af54a62e30b4028f219f4a428c9
(fix APPROVED 017cd166). Models: job608-checks-m674-preflight-independent-review.md, job608-compiler-tsccwdf6a4-launch.md.

## 1. Hashes (all match preflight and manifest)
- export-manifest.json 0807dbe2a6ebf2e45ab9d421bc9cbe12a1e7b896e53a2c84715d7a5a442354ba (= manifest_sha256)
- run608.sh b04abd4d...0b7816 (= runner_sha256); stage608.py a558db9a...0c0de4 (= stage_helper_sha256);
  both cmp-equal to `git show C:docs/strict542/run-stage608.sh` / `C:docs/strict542/stage608.py`.
- successor598.tar 9374675e...190296 (= successor_archive_sha256); source598.tar e79a0e45..., native598.tar d73e4e35...,
  rolldown608-source.tar.gz 203aa483... (same pins as checks m674).
- Manifest: run_id stage608-compiler-m674, stage compiler, execution_state UNUSED, launch_history none,
  source_commit = runner_commit = C, source_export_sha256 e1a6de35...4461b (= preflight).

## 2. Stage inputs (STAGES['compiler']=['native'])
- stage_inputs native/{libtests-receipt.json 2f81179f, receipt.json 4a651254, rolldown-binding.linux-x64-gnu.node
  0b6607e7, stage-receipt.json 0bb266db}: each equals sha256 of the same path in P/stage-native-m674/result608-native
  (native m674 accepted 5a412599). Staged copies in stage608-inputs/native are 0644.

## 3. Gates
- `python3 -I -B stage608.py verify-inputs` exit 0; `sh -n run608.sh` exit 0.
- run608.sh has `umask 022` and `tar --no-same-permissions` on source/successor/native extraction (fix 674840b6).
- storage608.py check not rerun here; remains a fresh live gate at launch.

## 4. Launch caps
- `offload run --timeout 600 --mem 14g --cpus 4 --artifacts result608-compiler -- timeout -k 15s 540s sh run608.sh`,
  identical to job608-compiler-tsccwdf6a4-launch.md; minimum_worker_seconds 975 unchanged.
- Absent: P/compiler-m674-offload.log, P/compiler-m674-offload.rc, P/stage-compiler-m674/result608-compiler.
- Export top-level names: export-manifest.json, native598.tar, native608-stages/, rolldown608-source.tar.gz, run608.sh,
  source598.tar, stage608-inputs/, stage608.py, successor598.tar. No secret/key/env/credential names.

## Notes (non-blocking)
- Manifest `purpose` still reads "...stage native..." (inherited carry-over, as noted in the checks m674 review);
  not read by run608.sh or stage608.py.

## VERDICT
Conditional on fresh live gates at launch (health up, no competing run, verify-inputs 0, storage608.py check
--stage compiler 0, no result/log/rc, remaining >= 975s). ONE run only; no unchanged replay after admission.
Not acceptance; acceptance needs the run's own result plus zero group/other-writable checkpoint entries.

VERDICT: APPROVE
