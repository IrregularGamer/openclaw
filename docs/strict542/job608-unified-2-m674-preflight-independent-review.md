# job608 independent review: unified-2 preflight m674 at 674840b6

Reviewer: independent (read-only; no offload/build/service run). Date 2026-10-30.
Reviewed: docs/strict542/job608-unified-2-m674-preflight.json (c8aef54b) against P/stage-unified-2-m674
(P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private). C = 674840b669c43af54a62e30b4028f219f4a428c9.
Model: job608-unified-1-m674-preflight-independent-review.md.

## 1. Hashes (all match preflight)
- export-manifest.json b9ae8e5a94fdf6d1c12abff1e8b134dc395d66e8d62206f3a05601bf737c247d (= manifest_sha256)
- run608.sh b04abd4d...0b7816 (= runner_sha256); stage608.py a558db9a...0c0de4 (= stage_helper_sha256);
  both cmp-equal to `git show C:docs/strict542/run-stage608.sh` / `stage608.py`.
- Manifest: run_id stage608-unified-2-m674, stage unified-2, execution_state UNUSED, launch_history "none (fresh finite export)".

## 2. Stage inputs (STAGES['unified-2']=['native','runtime'], per stage608.py and continuation NEXT line)
- native/{libtests-receipt.json, receipt.json, rolldown-binding.linux-x64-gnu.node, stage-receipt.json}: each cmp-equal
  to P/stage-native-m674/result608-native/native (native m674 accepted 5a412599).
- runtime/{build.log, checkpoint.tar.gz, stage-receipt.json}: each cmp-equal to P/stage-runtime-m674/result608-runtime/runtime
  (runtime m674 accepted 388d36b8). No other stage inputs. Base/commit/stage/flags match the continuation NEXT line.

## 3. Gates
- `python3 -I -B stage608.py verify-inputs` exit 0; `sh -n run608.sh` exit 0.
- Export top-level: export-manifest.json, native598.tar, native608-stages, rolldown608-source.tar.gz, run608.sh,
  source598.tar, stage608-inputs, stage608.py, successor598.tar. No __pycache__ present; the removed unmanifested
  __pycache__ note is acceptable (no manifest entry altered).
- storage608.py check not rerun here; remains a fresh live gate.

## 4. Launch caps
- `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-2 -- timeout -k 15s 2400s sh run608.sh`,
  identical to job608-unified-2-tsccwdf6a4-launch.md; no cap raised; minimum_worker_seconds 2655.
- Absent: P/unified-2-m674-offload.log, P/unified-2-m674-offload.rc, P/stage-unified-2-m674/result608-unified-2.

## Notes (non-blocking)
- Manifest `purpose` still reads "...stage native..." (inherited carry-over, as in prior m674 reviews).

Conditional on fresh live gates at launch (health up, no competing run, verify-inputs 0, storage608.py check
--stage unified-2 0, no result/log/rc, remaining >= 2655s). ONE run only; no unchanged replay after admission.

Verdict: APPROVE
