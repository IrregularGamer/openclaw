# job608 checks stage result at singleThreaded freeze a46cd576 (EVIDENCE)

SOURCE ONLY; 595 MUST NOT APPLY. Stage evidence, not package/install authority.

- Launched 2026-10-29T00:2xZ as FIRST step of a fresh worker exactly per
  preflight 841ba12b (review cdcaaa19): pre-launch sha256 manifest 5f6e0974…,
  runner eb662d81…, helper a558db9a…, verify-inputs 0.
  `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-checks -- timeout -k 15s 2400s sh run608.sh`.
- Actual client rc 0 (`../checks-singlethreaded-a46c-offload.rc`), result
  exit-code.txt 0, log ends `STEP608 installed-checks-pass`.
- `storage608.py result --stage checks --result <abs result608-checks>` exit 0,
  logical return 310281 B (cap 16 MiB).
- Receipt `checks/stage-receipt.json` sha256 222c210f…7e1c1961: kind
  JOB608_STAGE_RECEIPT, exit_code 0, manifest 5f6e0974…, run_id
  stage608-checks-a46c, source a46cd576…, source_export 88279fe1…,
  stage_inputs {}; outputs installed.json 6e3b8969…0eb30740 and tests.log
  36387b18…7e3031b4 (on-disk sha256 match; strict542-checks/ copies identical).
- Python: 12 unittest runs, 135 tests, all OK (matches the 135 estimate).
- Node (node --test): 167 tests, 167 pass, 0 fail/skip/cancelled (165
  estimate + the 2 net added by the singleThreaded emitter fixtures).
- installed.json (vitest): ALL seven suite files present and passed:
  build-all-bounded608 4, compiler-input-snapshot 39,
  native-declaration-boundary 14 + 3 skipped, tsdown-build 165,
  tsdown-declaration-resolution 21 + 4 skipped, write-plugin-sdk-entry-dts 15,
  write-unified-entry-dts 14. Totals 279 = 272 passed + 7 pending, 0 failed,
  success true. The previous r2 inventory had 198 (4+165+15+14); the 81 added
  are the native/compiler suites. The 7 skips are all Windows-only platform
  cases (8.3 alias, namespaced executable, directory alias) skipped on Linux;
  no other skip/omission.
- Gateway/supervisor IPC refusal, cancellation, settlement and owner cases are
  among the passing Node/Python cases (e.g. "refuses missing, swapped, failed or
  disagreeing stage receipts", "failed and incomplete phases never publish a
  checkpoint", "source mutation ... refusal remain fail-closed").

Status: candidate ACCEPT pending exact independent acceptance review.
Next (each FIRST in a fresh worker): native per
job608-native-singlethreaded-a46c-preflight.md (approved bf290a63), then
runtime, then unified-0 per job608-after-singlethreaded-continuation.md.
