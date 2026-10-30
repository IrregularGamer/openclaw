# Independent preflight review: job608 unified-5 m674 (preflight 68ea86a5)

Precedent: job608-unified-4-m674-preflight.json (APPROVE f48fb963); continuation Progress/NEXT (m674, C=674840b6).

Findings (all checked live against P/stage-unified-5-m674):
1. Prepare: `--base P/stage-unified-0-tsccwdf6a4 --commit 674840b6 --stage unified-5 --input P/stage-native-m674/result608-native --input P/stage-runtime-m674/result608-runtime --dest P/stage-unified-5-m674` -- matches NEXT exactly (STAGES unified-N = native, runtime). Export manifest: stage unified-5, run_id stage608-unified-5-m674, source_commit 674840b6..., execution_state UNUSED, stage608-inputs/{native,runtime} only.
2. Hashes: run608.sh b04abd4d... = runner_sha256; stage608.py a558db9a... = stage_helper_sha256 (identical to unified-4); export-manifest.json 0a57d40c... = manifest_sha256. Definition consistent with unified-4 (P/stage-unified-4-m674/export-manifest.json = e829ea95..., its manifest_sha256).
3. Gates: `python3 -I -B stage608.py verify-inputs` rc 0; `sh -n run608.sh` rc 0; no __pycache__ under stage dir (import pycache moved to P/trash-608/unified-5-m674-pycache per continuation procedure). Free bytes 4650037248 match the JSON. No unified-5-m674 offload log/rc present (unused).
4. Launch caps identical to unified-4: --timeout 2460 --mem 14g --cpus 4, timeout -k 15s 2400s, sh run608.sh, artifacts result608-unified-5; nothing raised. minimum_worker_seconds 2655 and acceptance_extra unchanged. 595 MUST NOT APPLY retained.

No deviations from precedent other than the stage name, manifest hash and free bytes.

Verdict: APPROVE
