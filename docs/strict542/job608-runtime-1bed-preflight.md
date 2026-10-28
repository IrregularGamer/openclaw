# job608 runtime stage preflight (UNUSED export, frozen 1bed)

Source-only preparation. No install, build-package or application authority. **595 MUST NOT APPLY.**

- Export: `/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-runtime-1bed` (private staging, review 1e4c30d0, init receipt db1969ac).
- Prepared 2026-10-28T20:11Z with the committed preparer `git show 1bed4d1b:docs/strict542/prepare-stage608-export.py` (sha256 1e701de0…, identical to HEAD): `--base <root>/base --commit 1bed4d1b --stage runtime --input <root>/stage-native-1bed/result608-native`, under ulimit -v 512MiB, rc 0. The preparer's import left a `__pycache__/stage608.cpython-314.pyc`; it was removed so the export matches the native export layout (not a pinned file).
- `storage608.py check --stage runtime` (ec3b1b4d) before prep: unique 772158871 B, free 6552563712 B, reserve 2 GiB, return cap 128 MiB.
- Manifest sha256 7deb2f4d5603208df276c9590ae587c875447f74563c2add88d49aeed5f3e7b5: stage runtime, execution_state UNUSED, run_id stage608-runtime-1bed, source/runner 1bed4d1b, source_export 5d7e9d57… (same as checks r2 and native), runner eac266cf…, helper a558db9a…, successor ea5b2c39…, predecessor manifest 20111ce5….
- stage_inputs (STAGES['runtime']=['native']), all hard links (link count 2, same inodes as `stage-native-1bed/result608-native/native/*`): stage-receipt e8198c1d…, receipt 4a651254…, libtests-receipt 2f81179f…, addon 0b6607e7…. They equal the accepted native receipt 8866a036.
- `python3 -I -B stage608.py verify-inputs` in the export: rc 0. run608.sh and stage608.py are byte-identical to 1bed4d1b. source598.tar has the same inode (395540) as base.
- Planned single launch (same bound as runtime-owned launch cf8907d3): `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-runtime -- timeout -k 15s 2400s sh run608.sh`, only with >=2655 s worker life left. Afterwards `storage608.py result --stage runtime` on the return. On failure or timeout, do not rerun unchanged.
- Not launched in this worker: the compiler stage (launched 20:10:43Z) holds this worker's offload and life budget. Launch runtime FIRST in a fresh worker, after recording the compiler result.
