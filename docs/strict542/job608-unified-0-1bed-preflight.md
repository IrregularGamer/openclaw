# job608 unified-0 stage preflight (UNUSED export, frozen 1bed)

Source-only preparation. No install, build-package or application authority. **595 MUST NOT APPLY.**

- Export: `/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-unified-0-1bed` (private staging, review 1e4c30d0, init receipt db1969ac).
- Prepared 2026-10-28T20:44Z with the committed preparer `git show 1bed4d1b:docs/strict542/prepare-stage608-export.py` (sha256 1e701de0…): `--base <root>/base --commit 1bed4d1b --stage unified-0 --input <root>/stage-native-1bed/result608-native --input <root>/stage-runtime-1bed/result608-runtime`, run with `python3 -I -B` under ulimit -v 512MiB, rc 0. No `__pycache__` was written.
- `storage608.py check --stage unified-0` before prep: unique 887731964 B, free 6436847616 B, reserve 2 GiB, return cap 32 MiB.
- Manifest sha256 3353363af6809be69c2089c30a79baabe8a05af9f1f2af68e4c28e029d59d948: stage unified-0, execution_state UNUSED, run_id stage608-unified-0-1bed, source/runner 1bed4d1b, source_export 5d7e9d57….
- stage_inputs (STAGES['unified-0']=['native','runtime']): native stage-receipt e8198c1d…, receipt 4a651254…, libtests-receipt 2f81179f…, addon 0b6607e7… (accepted 8866a036); runtime stage-receipt 726b81a2…, checkpoint.tar.gz e8ae538c…, build.log f30637b6… (accepted 7d3d1bd6).
- `python3 -I -B stage608.py verify-inputs` in the export: rc 0.
- Planned single launch (same bound as the historical unified0 launch): `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-unified-0 -- timeout -k 15s 2400s sh run608.sh`, FIRST in a fresh worker with >=2655 s life left, only after independent review. Note: the earlier unified0 at frozen 2b543da3 hit its finite timeout (rc 124, job608-after-unified0-continuation.md). The 1bed runtime build-all finished tsdown-unified in 6m33s, but a timeout or failure here is not rerun unchanged. Afterwards run `storage608.py result --stage unified-0` with an absolute `--result` path.
