# job608 independent review: native preflight at substep-budget freeze a39ad5ee

**VERDICT: APPROVE**

SOURCE ONLY; 595 MUST NOT APPLY; not install authority. No application, package or
reseal authority.

Reviewed `job608-native-substep-a39a-preflight.md` (commit bce656a3) against
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-native-substep-a39a`.
Read-only: nothing launched (no offload, run608.sh, build, preparer, install or service
change). Commands: sha256sum, stat, cmp, find, git show/log/diff, read-only JSON parsing,
`python3 -I -B stage608.py verify-inputs` (from inside the export; no `__pycache__` left).

## Findings

1. On-disk sha256 matches the doc: export-manifest.json 9ede9116...9a16a476, run608.sh
   e2ed7e13...82780605, stage608.py a558db9a...27c0de4, native598.tar d73e4e35...2b8701de,
   rolldown608-source.tar.gz 203aa483...5d258ac, source598.tar e79a0e45...ba743de3,
   successor598.tar e44987e3...df1ed474. Manifest runner_sha256, stage_helper_sha256,
   native_export_sha256, compiler_upstream_archive_sha256, base_source_archive_sha256 and
   successor_archive_sha256 agree.
2. run608.sh equals `git show a39ad5ee...:docs/strict542/run-stage608.sh`; stage608.py equals
   the committed helper (a39ad5ee and HEAD). a39ad5ee is an ancestor of HEAD; no commits touch
   run-stage608.sh, stage608.py or prepare-stage608-export.py (1e701de0..., as doc) since.
3. Manifest: stage native, execution_state UNUSED, run_id stage608-native-a39a, source_commit
   and runner_commit a39ad5ee, stage_inputs {}, required_checks 14, source_export_sha256
   d2875624...0ef3f62 = the a39a checks stage-receipt.json value. Recomputed from the
   preparer's canonical identity: matches.
4. Versus the approved stage-checks-substep-a39a manifest (322e58a9..., = checks receipt
   manifest_sha256) the only differing fields are run_id and stage; run608.sh and
   successor598.tar are byte-identical to that export.
5. native598.tar, source598.tar, rolldown608-source.tar.gz are the same inodes
   (395541/395540/395542) as ../base (= the a46c/1bed native pins). Both
   native608-stages receipt.json files are cmp-identical to ../base and match manifest
   native_stage_outputs (4a651254..., 2f81179f...).
6. `python3 -I -B stage608.py verify-inputs` exit 0. No .env, .db, key, pem or id_* files.
7. Launch block is identical to the approved a46c native block after substituting the
   export/log/rc names: timeout 2460, --mem 4g, --cpus 1, inner `timeout -k 15s 2400s`,
   artifacts result608-native, `../native-substep-a39a-offload.{log,rc}`, deadline
   >= 2655 s. No gate weakened; doc additionally requires this review before launch.
8. Note (non-blocking): manifest field source_correction_review still reads "5ec111ba ...
   independent review pending"; it is inherited unchanged from the approved checks a39a
   manifest and is descriptive only.

No discrepancies against the doc.
