**VERDICT: APPROVE**

# Independent review: job608 unified-0 UNUSED export preflight at frozen 1bed

Reviewed claim: `docs/strict542/job608-unified-0-1bed-preflight.md` (commit 2d38d7ed).
Export: `/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-unified-0-1bed`.
Read-only review. Nothing was run in the export, no offload or build was started, and nothing in the export was changed.

This review grants no install, build-package, application or reseal authority. **595 MUST NOT APPLY.** It only finds that the export matches the preflight and is fit for the one planned bounded launch.

## Findings

1. Manifest hash matches. `export-manifest.json` sha256 is 3353363af6809be69c2089c30a79baabe8a05af9f1f2af68e4c28e029d59d948, as the preflight says.
2. Manifest fields match. stage `unified-0`, execution_state `UNUSED`, run_id `stage608-unified-0-1bed`, source_commit and runner_commit both 1bed4d1bb53eff145f724cc6a448dc73b3609015, source_export_sha256 5d7e9d57fb660e2b54f5595e81ddf332027e21b303937c2cd6bc7f718f311263.
3. Only the expected fields changed. Compared with `../stage-runtime-1bed/export-manifest.json`, only `stage`, `run_id` and `stage_inputs` differ. All other keys are equal.
4. Stage inputs match. All 7 files under `stage608-inputs/` hash to the values in `stage_inputs`: native stage-receipt e8198c1d, receipt 4a651254, libtests-receipt 2f81179f, addon 0b6607e7, and runtime stage-receipt 726b81a2, checkpoint.tar.gz e8ae538c, build.log f30637b6.
5. Stage inputs are the accepted outputs themselves, not copies. Their inodes (395570-395573, 395621-395623) are the same as `../stage-native-1bed/result608-native/native/*` and `../stage-runtime-1bed/result608-runtime/runtime/*`.
6. Stage receipts match the committed ones. The native and runtime `stage-receipt.json` files are byte-identical to `docs/strict542/job608-native-1bed/stage-receipt.json` and `docs/strict542/job608-runtime-1bed/stage-receipt.json`.
7. Runner and helper match the frozen commit. `run608.sh` is byte-identical to `git show 1bed4d1b:docs/strict542/run-stage608.sh` (sha256 eac266cf, the same as manifest runner_sha256). `stage608.py` is byte-identical to `git show 1bed4d1b:docs/strict542/stage608.py` (sha256 a558db9a, the same as stage_helper_sha256).
8. Stage dependencies are correct. Evaluating STAGES from the export's `stage608.py` gives `STAGES['unified-0'] == ['native', 'runtime']`.
9. Base archives were checked. `source598.tar` was not hashed, as instructed. Its inode 395540 is the same as `../base/source598.tar`. `native598.tar` has the same inode as base (395541). `successor598.tar` has a different inode from base, but it is byte-identical to `../base/successor598.tar` and its sha256 ea5b2c39 matches the manifest. `run608.sh` also has its own inode and is byte-identical to the base copy. Nothing is wrong here.
10. The export is clean. There is no `result608-unified-0` directory, no `__pycache__`, and no `.env`, `.db`, key or pem files.
11. The planned command is bounded. `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-unified-0 -- timeout -k 15s 2400s sh run608.sh`, run once, first in a fresh worker with at least 2655 s of life left. This is the same bound as the historical unified0 launch (job608-after-unified0-continuation.md). That earlier unified0 at 2b543da3 hit this timeout (rc 124). The preflight correctly says a timeout or failure here must not be rerun unchanged.

## Limits

I did not re-run `verify-inputs`, the preparer or `storage608.py check`, so those claims were not independently re-executed. The hash, inode and byte comparisons above cover what those steps produce.
