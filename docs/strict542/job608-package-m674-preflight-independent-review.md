# Independent preflight review: job608 package m674 (preflight 43959f7c)

Precedent: job608-tail-m674-preflight.json and its independent review (APPROVE); job608-package-tsccwdf6a4/README.md line 10 and job608-package-tsccwdf6a4-preflight.md line 32 (caps).

Findings (all checked live against P/stage-package-m674, read-only):
1. Prepare: `--base P/stage-unified-0-tsccwdf6a4 --commit 674840b6 --stage package --input P/stage-native-m674/result608-native --input P/stage-checks-m674/result608-checks --input P/stage-compiler-m674/result608-compiler --input P/stage-tail-m674/result608-tail` -- matches STAGES['package'] = native, checks, compiler, tail in the export's stage608.py. Export manifest: stage package, run_id stage608-package-m674, source_commit/runner_commit 674840b6..., execution_state UNUSED, launch_history "none (fresh finite export)".
2. Hashes: export-manifest.json 352ae639... = manifest_sha256; run608.sh b04abd4d... = runner_sha256; stage608.py a558db9a... = stage_helper_sha256 (identical to tail m674).
3. Inputs: all 12 stage_inputs entries (stage608-inputs/{native,checks,compiler,tail}; on-disk file set equals manifest key set, no extras, none missing) match the manifest and are hash-equal to P/stage-native-m674/result608-native/native/* (4 files), P/stage-checks-m674/result608-checks/checks/* (installed.json, stage-receipt.json, tests.log), P/stage-compiler-m674/result608-compiler/compiler/* (stage-receipt.json, tests.log) and P/stage-tail-m674/result608-tail/tail/* (build.log, checkpoint.tar.gz 54b49d68..., stage-receipt.json). Each source dir's file set equals its manifest subset. Tarballs hashed only, not extracted.
4. Gates: `python3 -I -B stage608.py verify-inputs` rc 0; `sh -n run608.sh` rc 0; `storage608.py check --root P --stage package` rc 0 (free_bytes 4362960896 live, equal to prepare; above 2 GiB reserve; return_cap_bytes 2147483648); no __pycache__ under stage dir; P/package-m674-offload.log/.rc absent.
5. Launch argv identical to package tsccwdf6a4 (README line 10) and tail m674: --timeout 2460 --mem 14g --cpus 4, artifacts result608-package, timeout -k 15s 2400s sh run608.sh; nothing raised. minimum_worker_seconds 2655 and acceptance_extra unchanged. 595 MUST NOT APPLY retained in scope.

Deviations (copy-paste from tail m674 preflight, not updated):
- D1 (blocking): `"log"` and `"rc"` point at P/tail-m674-offload.log and P/tail-m674-offload.rc. Both files exist and are the accepted tail m674 run evidence (f9ab7977). A launch that follows this preflight would overwrite them and would not produce P/package-m674-offload.log/.rc, which acceptance expects. They must be P/package-m674-offload.log and P/package-m674-offload.rc.
- D2 (minor): `"scope"` still reads "tail rerun at reviewed mode fix 674840b6"; should say package rerun.

Everything else (export, hashes, inputs, gates, caps) is correct. Fix D1 and D2 in the preflight json only. The export does not need to be re-prepared, and the manifest hash 352ae639 stays valid. Then re-review.

Verdict: REJECT

## Re-review (3f2790f8)

- `git diff e12d8ed1..3f2790f8`: only docs/strict542/job608-package-m674-preflight.json changed, 3 lines. `scope` now reads "SOURCE ONLY; package rerun at reviewed mode fix 674840b6; 595 MUST NOT APPLY" (D2 fixed). `log`/`rc` now point at P/package-m674-offload.log and P/package-m674-offload.rc (D1 fixed). Launch argv, hashes, inputs, minimum_worker_seconds and acceptance_extra are unchanged.
- Export unchanged: export-manifest.json 352ae639..., run608.sh b04abd4d..., stage608.py a558db9a... (re-hashed live).
- Gates still hold: `storage608.py check --root P --stage package` rc 0 (free_bytes 4362960896, unchanged); P/package-m674-offload.log/.rc absent; no __pycache__ under the export. The tail m674 log/rc are no longer referenced.

Verdict: APPROVE
