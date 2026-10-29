# Job 608 native tsccwdf6a4: independent acceptance

This covers the native stage only, at source f6a4de2e (evidence f830137b, preflight review 54587210).

## Verified
- `$P/../native-tsccwdf6a4-offload.rc` = 0. The committed `native-offload.rc` is also 0. `R/exit-code.txt` = 0.
- The offload log (3 lines: BEFORE/AFTER_ARCHIVE_RELEASE608 memory stats, then `STEP608 native-rebuild-pass`) has no
  error or refusal. `zcat native-offload.log.gz` is byte-identical to the original.
- `cd $P/result608-native && sha256sum -c` against the committed `result-files.sha256`: 10 of 10 OK. The tree also
  has exactly 10 files, so nothing is missing from the list.
- Committed non-binary copies equal the originals. Plain files compared with cmp; `.gz` files compared after zcat.
  That covers exit-code.txt, the three native/*.json files, result598-native/receipt.json, compaction-tests.log,
  lifetime-retention-negative.log and strict542-checks/native-rebuild.log.
- `native/stage-receipt.json` contains: kind JOB608_STAGE_RECEIPT, exit_code 0, run_id `stage608-native-tsccwdf6a4`,
  source_commit `f6a4de2ebc6924d16fe559f9858bf8c50dce1eba`, manifest_sha256 `b51a34e9...f9f6` (equal to the README and
  preflight), source_export_sha256 `e81e07d2...8145` (the same export as the checks stage), and stage_inputs `{}`.
  Its output hashes match the files.
- `native/receipt.json` has complete=true, compaction_tests_exit 0, lifetime_tests_exit 0 and
  retention_negative_detected true. It records `addon_sha256` `0b6607e7...e042`, which equals the actual sha256 of
  both binding copies (`native/` and `result598-native/`). The two copies are identical at 24303312 bytes.
  `result598-native/receipt.json` is byte-identical to `native/receipt.json`.
  `libtests-receipt.json` has native_lib_tests_exit 0.
- Test logs: the compaction tests report `2 passed; 0 failed`. In native-rebuild.log the positive lifetime tests
  report `7 passed; 0 failed` and the compaction tests report `2 passed; 0 failed`. The release build finished in
  20m 36s.
- The result size is 48652053 bytes, under the 64 MiB (67108864) return cap.
- The README claims (rc, exit code, STEP608, size, binding hash, identical copies, compaction 0 failed, binary not
  committed) are all accurate.

## Note (not a discrepancy)
- `lifetime-retention-negative.log` shows `3 failed`. This is the intended negative control, not a failure of the run.
  build-native608.py mutates the helper to retain ASTs until table drop. It then asserts a nonzero rc and that
  `unused_is_released_before_first_render` and `repeated_module_survives_...` both FAILED. The receipt records this
  as retention_negative_detected=true. The un-mutated lifetime tests have 0 failures.

## Scope and limits
- This accepts the native run only. It does not approve install, seal, package or application.
- The runtime stage at f6a4de2e is next, through unchanged gates, on a fresh worker.
- 595 MUST NOT APPLY.
- The review was read-only. No offload, builds, tests or services were run.

VERDICT: ACCEPT native tsccwdf6a4 at f6a4de2e (rc 0, 10/10 hashes OK, identity and addon hash verified; 595 MUST NOT APPLY)
