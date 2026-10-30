# Independent review: job608 compiler-301d preflight (04230866)

Checks and results:
1. sha256 of export-manifest.json, run608.sh, stage608.py match manifest_sha256 / runner_sha256 / stage_helper_sha256 in the preflight. Manifest: source_commit 301d7456bf5b..., stage compiler, source_export_sha256 99add7e1... and successor_archive_sha256 e2ed663e... match. No input_lineage key in the manifest (no lineage; consistent with null).
2. The four stage_inputs digests (libtests-receipt 2f81179f, receipt 4a651254, rolldown-binding .node 0b6607e7, stage-receipt 6e4f20df) equal sha256sum of P/stage-native-301d/result608-native/native/* and the entries in job608-native-301d/result-files.sha256.
3. `python3 -I -B stage608.py verify-inputs` exit 0; `sh -n run608.sh` exit 0; no __pycache__ under E afterwards.
4. Launch argv identical to compiler-m674 (600s / 14g / 4CPU / timeout -k 15s 540s, artifacts result608-compiler); nothing raised. find for .env*, *.pem, id_*, *.key in E: none.
5. diff -r E/native608-stages vs P/stage-native-301d/native608-stages: identical (exit 0).

Note: runner_sha256 equals the m674 runner; stage helper and manifest differ as expected for the new commit.

VERDICT: APPROVE
