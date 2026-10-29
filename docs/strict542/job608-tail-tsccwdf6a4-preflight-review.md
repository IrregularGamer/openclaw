# Independent preflight review: job608 tail tsccwdf6a4

Reviewed `docs/strict542/job608-tail-tsccwdf6a4-preflight.md` at commit 40043eb9. Review date 2026-10-29.
The review was read-only: nothing was launched, built or installed, and no stage dir was changed.
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private, T=P/stage-tail-tsccwdf6a4.

## Check 1: manifest pin, committed copy and identity
- PASS. sha256 of T/export-manifest.json is add772f5f0e861bf1a28f8ecdf1d616aea4a505af745579e192bc9e17fe3bbdb, equal to the doc pin. `cmp` against job608-tail-tsccwdf6a4-export-manifest.json returns 0.
- PASS. Fields: stage=tail, execution_state=UNUSED, launch_history=none, source_commit=runner_commit=f6a4de2ebc6924d16fe559f9858bf8c50dce1eba, source_export_sha256=e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145, run_id=stage608-tail-tsccwdf6a4.

## Check 2: stage inputs equal accepted results
STAGES in f6a4de2e stage608.py: `'tail': ['native','middle','sdk-0','sdk-1']`. T/stage608-inputs holds exactly middle, native, sdk-0, sdk-1.
- PASS. Manifest stage_inputs lists 13 files; every on-disk sha256 equals its manifest value.
- PASS native: libtests-receipt 2f81179f…, receipt 4a651254…, rolldown-binding 0b6607e7…, stage-receipt 1047485796fe… equal P/stage-native-tsccwdf6a4/result608-native/native/*.
- PASS middle: build.log 9d1fdaf9…, checkpoint 32ea0475…, stage-receipt 9eb3083c… equal docs/strict542/job608-middle-tsccwdf6a4/result-files.sha256 and the live result608-middle.
- PASS sdk-0: build.log 766e2130…, checkpoint 09f9d2b8…, stage-receipt 08530815… equal job608-sdk-0-tsccwdf6a4/result-files.sha256 and live result608-sdk-0.
- PASS sdk-1: build.log ab5dfafc…, checkpoint f31068ea…, stage-receipt e57265f3… equal job608-sdk-1-tsccwdf6a4/result-files.sha256 and live result608-sdk-1.

## Check 3: runner and helper identity
- PASS. T/stage608.py sha256 a558db9a… == P/stage-sdk-1-tsccwdf6a4/stage608.py == `git show f6a4de2e:docs/strict542/stage608.py` == manifest stage_helper_sha256.
- PASS. T/run608.sh sha256 715e53bd… == P/stage-sdk-1-tsccwdf6a4/run608.sh == `git show f6a4de2e:docs/strict542/run-stage608.sh` == manifest runner_sha256.

## Check 4: live gates and absent outputs
- PASS. `cd T && python3 -I -B stage608.py verify-inputs` rc=0. `sh -n run608.sh` rc=0.
- PASS. `python3 -I -B docs/strict542/storage608.py check --root P --stage tail` rc=0 (free 5166112768, reserve 2147483648, return cap 134217728).
- PASS. T/result608-tail, P/tail-tsccwdf6a4-offload.log and P/tail-tsccwdf6a4-offload.rc are all absent (ENOENT).

## Check 5: launch command
- PASS. `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-tail -- timeout -k 15s 2400s sh run608.sh`, foreground, log redirected, rc captured. It is the same finite shape as the accepted sdk-0/sdk-1 stages. The runner takes no caller argv. Its build budget is `2280 - elapsed`, which is inside the 2400s limit. The doc requires >=2655s left after preflight, one launch per stage, and never detached.

## Check 6 (open point): empty sdk-2 partition in the tail join
The sdk-1 checkpoint holds sdk/openclaw-dts-plugin-sdk-2/{artifact-record.json, receipt.json, data/dist/ (empty), data/compiler-inputs/openclaw-dts-plugin-sdk-2.json = `{"roots":[],"inputs":[]}`} plus the .build608.json binding. The receipt status is COMPILED_GROUP_NOT_PUBLISHED, record version 6, signature present, inputs 0, outputs 1 (the compiler-inputs receipt).
How tail consumes it at f6a4de2e:
- `bounded-build-checkpoint608.mjs:29`: tail = labels from write-plugin-sdk-entry-dts, predecessor middle, join 'sdk'.
- `build-checkpoint608.mts`: each sdk group binding is validated against its receipt and data inventory, then `writeBoundedDeclarationCheckpoint608('sdk', {mode:'join'})` runs.
- `tsdown-declaration-writer.mts:258-279` (join): this checks the exact entry set, private regular receipts, and record==receipt.record. It then runs `validateCheckpoint608`, which requires `Object.keys(record.outputs).length>0`. That passes because the compiler-inputs receipt is an output. The signature is checked over `record.inputs` (empty), then data is copied and rechecked with `readDeclarationInputs`, which must equal [] and does. Join mode compiles nothing (`misses=[]`).
- `tsdown-declaration-writer.mts:188-191` documents the design: "An empty canonical partition still owns its successful compiler receipt". requiredOutputs = `dist/<required entries>` + receipt. With no emit roots, only the receipt is required.
- PASS (by source inspection). The tail join explicitly tolerates an empty sdk-2 partition. No private-QA flag is set: the writer forces OPENCLAW_BUILD_PRIVATE_QA to "0" unless it is already "1", and bounded-package608.mjs strips OPENCLAW_BUILD_PRIVATE_QA from the env. Nothing in this package sets the flag or waives a check.
- Recorded residual risk: I did not trace every post-join tail phase (for example plugin-sdk export/entry checks) to confirm that none of them expects private-QA declarations. With the flag unset those entries should be outside the public set. If any phase did require them, the fixed build would fail loudly (build-fail status, then build.log tail on stdout, rc != 0). It would not pass silently. That outcome would require a source-only fix, never the flag.

VERDICT: APPROVE
