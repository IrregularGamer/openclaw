# Independent preflight review: job608 middle m674 (preflight d5cd807b)

Precedent: job608-unified-5-m674-preflight.json (APPROVE 1c9da566 chain); job608-middle-tsccwdf6a4-preflight.md line 17 (caps); continuation NEXT (m674, C=674840b6).

Findings (all checked live against P/stage-middle-m674):
1. Prepare: `--base P/stage-unified-0-tsccwdf6a4 --commit 674840b6 --stage middle --input P/stage-{native,runtime,unified-0..5}-m674/result608-*` -- matches STAGES['middle'] = native, runtime, unified-0..5. Export manifest: stage middle, run_id stage608-middle-m674, source_commit/runner_commit 674840b6..., execution_state UNUSED, launch_history none.
2. Hashes: export-manifest.json 365d4ea6... = manifest_sha256; run608.sh b04abd4d... = runner_sha256; stage608.py a558db9a... = stage_helper_sha256 (identical to unified-5 m674).
3. Inputs: all 25 stage_inputs entries (stage608-inputs/{native,runtime,unified-0..5} only, no extra files) hash-equal to P/stage-*-m674/result608-*/ files. 19 differ from the tsccwdf6a4 counterparts; the 3 native receipt/binding files are byte-identical to tsccwdf6a4 by content (deterministic pinned native outputs), but native/stage-receipt.json is m674-specific. tsccwdf6a4 appears in the manifest only in successor_paths (doc names) and predecessor_package_attempt, never in stage_inputs.
4. Gates: `python3 -I -B stage608.py verify-inputs` rc 0; `sh -n run608.sh` rc 0; `storage608.py check --root P --stage middle` rc 0 (free_bytes 4629483520 = JSON); no __pycache__ under stage dir; no middle-m674 offload log/rc present (unused).
5. Launch caps identical to middle tsccwdf6a4 line 17 and unified-5 m674: --timeout 2460 --mem 14g --cpus 4, artifacts result608-middle, timeout -k 15s 2400s sh run608.sh; nothing raised. minimum_worker_seconds 2655 and acceptance_extra unchanged. 595 MUST NOT APPLY retained.

No deviations from precedent other than the stage name, input set, manifest hash and free bytes.

Verdict: APPROVE
