# Independent preflight review: job608 tail m674 (preflight b7d710e3)

Precedent: job608-sdk-1-m674-preflight.json and its independent review (APPROVE); job608-tail-tsccwdf6a4/README.md line 12 (caps).

Findings (all checked live against P/stage-tail-m674, read-only):
1. Prepare: `--base P/stage-unified-0-tsccwdf6a4 --commit 674840b6 --stage tail --input P/stage-native-m674/result608-native --input P/stage-middle-m674/result608-middle --input P/stage-sdk-0-m674/result608-sdk-0 --input P/stage-sdk-1-m674/result608-sdk-1` -- matches STAGES['tail'] = native, middle, sdk-0, sdk-1 in the export's stage608.py. Export manifest: stage tail, run_id stage608-tail-m674, source_commit/runner_commit 674840b6..., execution_state UNUSED, launch_history "none (fresh finite export)". (purpose string "...build stage native..." is the same template text as the sdk-0/sdk-1 m674 manifests; not a deviation.)
2. Hashes: export-manifest.json 4a3b2833... = manifest_sha256; run608.sh b04abd4d... = runner_sha256; stage608.py a558db9a... = stage_helper_sha256 (identical to sdk-1 m674).
3. Inputs: all 13 stage_inputs entries (stage608-inputs/{native,middle,sdk-0,sdk-1}; on-disk file set equals manifest key set, no extras) match the manifest and are hash-equal to P/stage-native-m674/result608-native/native/* (4 files), P/stage-middle-m674/result608-middle/middle/* (build.log, checkpoint.tar.gz b80f8116..., stage-receipt.json), P/stage-sdk-0-m674/result608-sdk-0/sdk-0/* (build.log, checkpoint.tar.gz 307e76bf..., stage-receipt.json) and P/stage-sdk-1-m674/result608-sdk-1/sdk-1/* (build.log, checkpoint.tar.gz 8a0f1f2e..., stage-receipt.json). Each source dir's file set equals its manifest subset. Tarballs hashed only, not extracted.
4. Gates: `python3 -I -B stage608.py verify-inputs` rc 0; `sh -n run608.sh` rc 0; `storage608.py check --root P --stage tail` rc 0 (free_bytes 4453801984 live, equal to prepare; above 2 GiB reserve; return_cap_bytes 201326592 = the 192MiB tail cap from 8f4fb3b3, which the tsccwdf6a4 tail result 161610911 fit under); no __pycache__ under stage dir; P/tail-m674-offload.log/.rc absent (only the tsccwdf6a4 log/rc exist).
5. Launch caps identical to tail tsccwdf6a4 README line 12 and sdk-1 m674: --timeout 2460 --mem 14g --cpus 4, artifacts result608-tail, timeout -k 15s 2400s sh run608.sh; nothing raised. minimum_worker_seconds 2655 and acceptance_extra unchanged. 595 MUST NOT APPLY retained in scope.

No deviations from precedent other than the stage name, inputs (sdk-0, sdk-1 added per STAGES), artifacts name, manifest hash and free bytes.

Verdict: APPROVE
