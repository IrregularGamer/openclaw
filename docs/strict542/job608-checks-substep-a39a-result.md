# job608 checks stage result at substep-budget freeze a39ad5ee (EVIDENCE)

SOURCE ONLY; 595 MUST NOT APPLY. Stage evidence, not package/install authority.

- Launched 2026-10-29T02:31Z as FIRST step of a fresh worker (offload deadline
  3578 s) exactly per preflight e5a8dbf9 (independent APPROVE 086997d8):
  pre-launch sha256 manifest 322e58a9…, runner e2ed7e13…, helper a558db9a…,
  verify-inputs 0.
  `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-checks -- timeout -k 15s 2400s sh run608.sh`.
- Actual client rc 0 (`../checks-substep-a39a-offload.rc`), result
  exit-code.txt 0, log (314 lines) ends `STEP608 installed-checks-pass`.
  Post-run export digests unchanged (322e58a9…, e2ed7e13…, a558db9a…).
- `storage608.py result --stage checks --result <abs result608-checks>` exit 0,
  logical return 309965 B (cap 16 MiB).
- Receipt `checks/stage-receipt.json` sha256 176ac198aa4f731cbd71196702b8c90494f845b2426947600a18f0c5a32862f7:
  kind JOB608_STAGE_RECEIPT, stage checks, exit_code 0, manifest 322e58a9…,
  run_id stage608-checks-a39a, source a39ad5ee95609193502850d0dbb87b5dcbb5e3e3,
  source_export d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62,
  stage_inputs {}; outputs installed.json
  0c56a168736678a98b3fc048b127a5708a4c23724abebefae324471a53533f3c and tests.log
  bf90e55ed34f8fdd4ea19249cfc6ee7671fab48b793c424b82f66ac24d5e5313 (on-disk
  sha256 match; strict542-checks/ copies byte-identical).
- Python: 12 unittest runs (15+18+13+19+17+3+5+2+6+14+16+7) = 135, all OK.
- Node (node --test): 101+28+38 = 167 tests, 167 pass, 0 fail/cancelled/skip/todo.
- installed.json (vitest): success true, 17/17 suites, 279 = 272 passed + 7
  pending, 0 failed; all seven files passed: build-all-bounded608 4,
  compiler-input-snapshot 39, native-declaration-boundary 14 + 3 skipped,
  tsdown-build 165, tsdown-declaration-resolution 21 + 4 skipped,
  write-plugin-sdk-entry-dts 15, write-unified-entry-dts 14. Identical counts to
  accepted a46c (f73bc268); the a39a delta is only the unified-0 runner
  substep markers/inner timeout (dd881aba), which the checks stage does not run.
  The 7 skips are the same pre-existing platform skips (6 Windows-gated, 1
  case-insensitive-filesystem alias).
- Gateway/supervisor IPC refusal, cancellation, settlement and owner cases pass
  as before (test_native_owner_server, test_native_preparation,
  test_root_owner_supervisor; Node receipt/checkpoint/fail-closed refusals).

Status: candidate ACCEPT pending exact independent acceptance review.
Next (each FIRST in a fresh worker): native, runtime, unified-0 at a39a per
job608-after-substep-budget-continuation.md.
