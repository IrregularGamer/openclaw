# Independent preflight review: job608 sdk-1 m674 (preflight 6eb72338)

Precedent: job608-sdk-0-m674-preflight.json and its independent review (APPROVE); job608-sdk-1-tsccwdf6a4/README.md line 15 (caps).

Findings (all checked live against P/stage-sdk-1-m674, read-only):
1. Prepare: `--base P/stage-unified-0-tsccwdf6a4 --commit 674840b6 --stage sdk-1 --input P/stage-native-m674/result608-native --input P/stage-middle-m674/result608-middle` -- matches STAGES['sdk-1'] = native, middle in the export's stage608.py. Export manifest: stage sdk-1, run_id stage608-sdk-1-m674, source_commit/runner_commit 674840b6..., execution_state UNUSED, launch_history "none (fresh finite export)". (purpose string "...build stage native..." is the same template text as the sdk-0 m674 manifest; not a deviation.)
2. Hashes: export-manifest.json 23f06cb0... = manifest_sha256; run608.sh b04abd4d... = runner_sha256; stage608.py a558db9a... = stage_helper_sha256 (identical to sdk-0 m674).
3. Inputs: all 7 stage_inputs entries (stage608-inputs/{native,middle} only; on-disk file set equals manifest key set, no extras) match the manifest and are hash-equal to P/stage-native-m674/result608-native/native/* (4 files) and P/stage-middle-m674/result608-middle/middle/* (build.log, checkpoint.tar.gz b80f8116..., stage-receipt.json). Tarballs hashed only, not extracted.
4. Gates: `python3 -I -B stage608.py verify-inputs` rc 0; `sh -n run608.sh` rc 0; `storage608.py check --root P --stage sdk-1` rc 0 (free_bytes 4473159680 live vs 4492427264 at prepare; above 2 GiB reserve); no __pycache__ under stage dir; P/sdk-1-m674-offload.log/.rc absent (unused; only the tsccwdf6a4 log/rc exist).
5. Launch caps identical to sdk-1 tsccwdf6a4 README line 15 and sdk-0 m674: --timeout 2460 --mem 14g --cpus 4, artifacts result608-sdk-1, timeout -k 15s 2400s sh run608.sh; nothing raised. minimum_worker_seconds 2655 and acceptance_extra unchanged. 595 MUST NOT APPLY retained in scope.

No deviations from precedent other than the stage name, artifacts name, manifest hash and free bytes.

Verdict: APPROVE
