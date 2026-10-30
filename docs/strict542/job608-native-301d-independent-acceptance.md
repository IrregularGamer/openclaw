# Job 608 native 301d: independent acceptance

This covers the native stage only: P/stage-native-301d at source 301d7456 (evidence 7e81d22c, preflight APPROVE a86f43a3).
It uses the criteria of job608-native-m674-independent-acceptance.md.

## Verified
- `P/native-301d-offload.rc` = 0. The committed `native-offload.rc` = 0. `result608-native/exit-code.txt` = 0.
- `zcat native-offload.log.gz` contains `STEP608 native-rebuild-pass`.
- `cd P/stage-native-301d && sha256sum -c docs/strict542/job608-native-301d/result-files.sha256` gives 10 of 10 OK. The tree holds exactly 10 files.
- `export-manifest.json` sha256 is b61f89b5...815b0, which equals preflight manifest_sha256 (stage unchanged).
- `native/stage-receipt.json` has kind JOB608_STAGE_RECEIPT, exit_code 0, run_id `stage608-native-301d`,
  source_commit `301d7456bf5b0c4179b27d0db97eac7b07143f4a`, manifest_sha256 b61f89b5...815b0,
  source_export_sha256 99add7e1...291d (= preflight) and stage_inputs `{}`. Same structure as the m674 receipt;
  its output hashes equal the m674 receipt outputs and the files on disk.
- `native/receipt.json` has complete=true, compaction_tests_exit 0, lifetime_tests_exit 0,
  retention_negative_detected true, addon_sha256 0b6607e7...e042. Both addon copies hash to that value,
  identical to m674. `result598-native/receipt.json` is byte-identical to `native/receipt.json`.
  `libtests-receipt.json` has native_lib_tests_exit 0.
- Compaction tests report `2 passed; 0 failed`; release builds finished (20m 27s, 9m 35s).
- The result size is 48652047 bytes, under 64 MiB (67108864).
- `find result608-native -perm /022` returns 0 entries; all 10 files have nlink 1.

## Scope and limits
- This accepts the native run only. It does not approve install, seal, package or application. 595 MUST NOT APPLY.
- The review was read-only. No offload, builds, tests or services were run.

Verdict: ACCEPT native 301d at 301d7456 (rc 0, 10/10 hashes OK, identity/manifest/addon verified, 0 group/other-writable, nlink 1; 595 MUST NOT APPLY)
