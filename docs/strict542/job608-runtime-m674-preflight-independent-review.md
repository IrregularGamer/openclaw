# job608 independent review: runtime preflight m674 at 674840b6

Reviewer: independent (read-only; no offload/build/service run). Date 2026-10-29.
Reviewed: docs/strict542/job608-runtime-m674-preflight.json (651d63be) against P/stage-runtime-m674
(P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private). C = 674840b669c43af54a62e30b4028f219f4a428c9
(fix APPROVED 017cd166). Models: job608-compiler-m674-preflight-independent-review.md, job608-runtime-tsccwdf6a4-launch.md.

## 1. Hashes (all match preflight)
- export-manifest.json 7b4724f9b7dc55ff983c66ec096aa1e8c86fd69e6c211c462c8596300e91de70 (= manifest_sha256)
- run608.sh b04abd4d...0b7816 (= runner_sha256); stage608.py a558db9a...0c0de4 (= stage_helper_sha256);
  both cmp-equal to `git show C:docs/strict542/run-stage608.sh` / `C:docs/strict542/stage608.py`.
- Manifest: run_id stage608-runtime-m674, stage runtime, execution_state UNUSED, launch_history
  "none (fresh finite export)", source_commit = runner_commit = C.

## 2. Stage inputs (STAGES['runtime']=['native'])
- stage_inputs native/{libtests-receipt.json 2f81179f, receipt.json 4a651254, rolldown-binding.linux-x64-gnu.node
  0b6607e7, stage-receipt.json 0bb266db}: staged files hash to the manifest values and each equals the sha256 of the
  same-named file in P/stage-native-m674/result608-native (native m674 accepted 5a412599; addon 0b6607e7).
  Staged copies in stage608-inputs/native are 0644. No inputs from any other stage.

## 3. Gates
- `python3 -I -B stage608.py verify-inputs` exit 0; `sh -n run608.sh` exit 0 (run inside the export dir).
- run608.sh has `umask 022` and `tar --no-same-permissions` on source/successor/native extraction (fix 674840b6).
- storage608.py check not rerun here; remains a fresh live gate at launch.

## 4. Launch caps
- `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-runtime -- timeout -k 15s 2400s sh run608.sh`,
  identical to job608-runtime-tsccwdf6a4-launch.md; minimum_worker_seconds 2655.
- Absent: P/runtime-m674-offload.log, P/runtime-m674-offload.rc, P/stage-runtime-m674/result608-runtime.
- Export top-level names: export-manifest.json, native598.tar, native608-stages/, rolldown608-source.tar.gz, run608.sh,
  source598.tar, stage608-inputs/, stage608.py, successor598.tar. No secret/key/env/credential names.

## Notes (non-blocking)
- Manifest `purpose` still reads "...stage native..." (inherited carry-over, as in prior m674 reviews);
  not read by run608.sh or stage608.py.

## VERDICT
VERDICT: APPROVE

Conditional on fresh live gates at launch (health up, no competing run, verify-inputs 0, storage608.py check
--stage runtime 0, no result/log/rc, remaining >= 2655s). ONE run only; no unchanged replay after admission.
