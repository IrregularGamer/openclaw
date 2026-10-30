# job608 runtime 301d preflight: independent review

Preflight: job608-runtime-301d-preflight.json (commit 4dd6fc6a). Read-only review; nothing launched, export untouched.

1. Manifest/runner/helper sha256 (7677269f..., b04abd4d..., 1d2bf411...) match the preflight. Manifest source_commit=301d7456bf5b0c4179b27d0db97eac7b07143f4a, stage=runtime, no input_lineage key, source_export_sha256 (99add7e1...) and successor_archive_sha256 (e2ed663e...) equal the preflight.
2. All 4 stage_inputs (libtests-receipt.json, receipt.json, rolldown-binding.linux-x64-gnu.node, stage-receipt.json) equal sha256 of P/stage-native-301d/result608-native/native/* and the accepted job608-native-301d/result-files.sha256.
3. `stage608.py verify-inputs` (python3 -I -B) rc=0; `sh -n run608.sh` rc=0; no __pycache__ under E afterwards.
4. Launch argv is identical to runtime-m674 (2460s / 14g / 4CPU / timeout -k 15s 2400s / artifacts result608-runtime); nothing raised. No .env, *.pem, id_*, *.key found in E.
5. `diff -r E/native608-stages P/stage-native-301d/native608-stages`: identical.
6. Dependencies: m674 runtime preflight takes stage inputs from native only; unified-*, middle, sdk-*, tail and package all list runtime (and/or later stages) as upstream, so runtime is the correct next stage after native/compiler at 301d.

Preflight differs from m674 only by added input_lineage(null), launch_rule, native608_stages, source_export_sha256, successor_archive_sha256 fields.

VERDICT: APPROVE
