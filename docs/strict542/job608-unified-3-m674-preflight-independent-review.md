# job608 independent review: unified-3 preflight m674 at 674840b6

Reviewer: independent (read-only; no offload/build/service run). Date 2026-10-30.
Reviewed: docs/strict542/job608-unified-3-m674-preflight.json (e1d27a31) against P/stage-unified-3-m674
(P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private). C = 674840b669c43af54a62e30b4028f219f4a428c9.
Model: job608-unified-2-m674-preflight-independent-review.md.

## 1. Hashes (all match preflight)
- export-manifest.json de4ec8896e749ea0361a4f623c3867db8239c417f5a3334c80f35a46c973f1f6 (= manifest_sha256)
- run608.sh b04abd4d...0b7816 (= runner_sha256); stage608.py a558db9a...0c0de4 (= stage_helper_sha256);
  both cmp-equal to `git show C:docs/strict542/run-stage608.sh` / `stage608.py` (same runner/helper as unified-2).
- Manifest: run_id stage608-unified-3-m674, stage unified-3, source_commit = runner_commit = C,
  execution_state UNUSED, launch_history "none (fresh finite export)".

## 2. Stage inputs (STAGES['unified-3']=['native','runtime'], per stage608.py)
- native/{libtests-receipt.json, receipt.json, rolldown-binding.linux-x64-gnu.node, stage-receipt.json}: each cmp-equal
  to P/stage-native-m674/result608-native/native (native m674 accepted 5a412599).
- runtime/{build.log, checkpoint.tar.gz, stage-receipt.json}: each cmp-equal to P/stage-runtime-m674/result608-runtime/runtime
  (runtime m674 accepted 388d36b8). No other stage inputs.

## 3. Gates
- `python3 -I -B stage608.py verify-inputs` exit 0 (no __pycache__ created); `sh -n run608.sh` exit 0.
- Export top-level (`ls -a`): export-manifest.json, native598.tar, native608-stages, rolldown608-source.tar.gz, run608.sh,
  source598.tar, stage608-inputs, stage608.py, successor598.tar. No __pycache__, .env, secrets or keys (also none at depth 2).
- Gate note: prepare's unmanifested __pycache__ was moved with `mv -n` to P/trash-608/unified-3-m674-pycache
  (present) because `trash` is not on PATH; acceptable, recoverable, no manifest entry altered.
- storage608.py check not rerun here; remains a fresh live gate.

## 4. Launch caps
- `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-3 -- timeout -k 15s 2400s sh run608.sh`,
  identical to job608-unified-3-tsccwdf6a4-launch.md; no cap raised; minimum_worker_seconds 2655.
- Absent: P/unified-3-m674-offload.log, P/unified-3-m674-offload.rc, P/stage-unified-3-m674/result608-unified-3.

## Notes (non-blocking)
- Manifest `purpose` still reads "...stage native..." (inherited carry-over, as in prior m674 reviews).

Conditional on fresh live gates at launch (health up, no competing run, verify-inputs 0, storage608.py check
--stage unified-3 0, no result/log/rc, remaining >= 2655s). ONE run only; no unchanged replay after admission.

Verdict: independent APPROVE
