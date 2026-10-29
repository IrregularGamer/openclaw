# Job 608 native m674: independent acceptance

This covers the native stage only: P/stage-native-m674 at source 674840b6 (evidence 53bda0a0, preflight 6049ed36).
It uses the criteria of job608-native-tsccwdf6a4-independent-acceptance.md plus the mode rule in
job608-after-package-moderefusal-continuation.md.

## Verified
- `P/native-m674-offload.rc` = 0. The committed `native-offload.rc` = 0. `exit-code.txt` = 0.
- `P/native-m674-offload.log` has 3 lines: BEFORE/AFTER_ARCHIVE_RELEASE608, then `STEP608 native-rebuild-pass`.
  It contains no error or refusal. `zcat native-offload.log.gz` is byte-identical to it.
- `cd P/stage-native-m674 && sha256sum -c result-files.sha256` gives 10 of 10 OK. The tree holds exactly 10 files.
- Committed copies equal the originals (cmp, and zcat for .gz) for all 8 non-binary result files.
- `export-manifest.json` sha256 is 738684f3...2dbf5, which is the prepared manifest.
- `native/stage-receipt.json` has kind JOB608_STAGE_RECEIPT, exit_code 0, run_id `stage608-native-m674`,
  source_commit `674840b669c43af54a62e30b4028f219f4a428c9`, manifest_sha256 738684f3...2dbf5 and stage_inputs `{}`.
  Its output hashes match the files on disk.
- `native/receipt.json` has complete=true, compaction_tests_exit 0, lifetime_tests_exit 0 and
  retention_negative_detected true. Its addon_sha256 is 0b6607e7...e042. The actual sha256 of both copies
  (`native/` and `result598-native/`, 24303312 bytes each) matches that value. `result598-native/receipt.json` is
  byte-identical to `native/receipt.json`. `libtests-receipt.json` has native_lib_tests_exit 0.
- Test logs: compaction reports `2 passed; 0 failed`. In native-rebuild.log, lifetime reports `7 passed; 0 failed` and
  compaction reports `2 passed; 0 failed`. The release build finished in 20m 35s.
- `lifetime-retention-negative.log` reports `3 failed`. This is the intended negative control, not a failure.
- The result size is 48651969 bytes, under 64 MiB (67108864).
- Mode rule: `find result608-native -perm /022` returns 0 entries. Every file is 0644 and every directory is 0755.
  The result contains no tar or tgz, so no listing was needed.
- The README claims are accurate.

## Scope and limits
- This accepts the native run only. It does not approve install, seal, package or application. 595 MUST NOT APPLY.
- The review was read-only. No offload, builds, tests or services were run.

VERDICT: ACCEPT native m674 at 674840b6 (rc 0, 10/10 hashes OK, identity/manifest/addon verified, 0 group/other-writable; 595 MUST NOT APPLY)
