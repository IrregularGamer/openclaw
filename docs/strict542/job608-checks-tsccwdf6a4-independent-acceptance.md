# Job 608 checks tsccwdf6a4: independent acceptance

VERDICT: ACCEPT. This covers the checks stage only, at source f6a4de2e (evidence 92aeda26).

## Verified
- `$P/checks-tsccwdf6a4-offload.rc` = 0. The committed copy is also 0. `runs.log` has `2026-10-29T13:03:59Z run remote rc=0 871s .../stage-checks-tsccwdf6a4`. `R/exit-code.txt` = 0.
- `stage-receipt.json` contains: kind JOB608_STAGE_RECEIPT, exit_code 0, run_id `stage608-checks-tsccwdf6a4`,
  manifest_sha256 `c22d7696...1833`, source_commit `f6a4de2ebc69...`, source_export_sha256 `e81e07d2...8145`
  (the manifest and export hashes equal the preflight values), and stage_inputs `{}`.
- Receipt outputs, recomputed relative to `R/`, match: `checks/installed.json` 2f5411ec..., `checks/tests.log` 156c53ed...
- The committed `result-files.sha256` is byte-identical to `cd R && find . -type f | sort | xargs sha256sum` (7 files).
- The result size is 309501 bytes, under the 16 MiB cap.

## Test results
- Both installed JSONs (`checks/`, `strict542-checks/`) report success=true, 17 suites with 0 failed,
  279 tests (272 passed, 0 failed, 7 pending, 0 todo).
- 7 pending is the established baseline, not a new skip. The 7 skips are 3 in `native-declaration-boundary.test.ts`
  and 4 in `tsdown-declaration-resolution.test.ts`. All are Windows-only cases (8.3 alias, namespaced or
  extended-length executable, case alias). They are gated by `it.skipIf(kind.includes("Windows") &&
  process.platform !== "win32")` or `runIf(win32)`. Neither file changed between bcfc8881 (2026-10-07, when the
  files were added) and f6a4de2e. The prior evidence in job608-checks-singlethreaded-a46c, -substep-a39a and
  -fullsize5aff1 has the same 279/272/7/0 counts and the same 7 test names.
- Required checks: `test/scripts/write-unified-entry-dts.test.ts` has 14 of 14 assertions, all passed (manifest required_checks 14).
- usage-window-types608: "actual usage window parser typechecks with checked indexed access" passed.
- The real supervisor IPC tests in `strict542-checks/tests.log` all ran ok, including test_root_owner_supervisor
  parent_sigkill_cancels_real_native_tree_before_receipt, real_fd3_endpoint_and_escaped_descendant_settle_on_shutdown,
  placement_mismatch_refuses_without_limits_or_serving, endpoint_idle_lifetime_and_parent_death_refuse,
  server_pin_drift_refuses_before_execution and socket_parent_writable_refuses_before_bind. Also ok:
  native_owner_server cancel_ack and endpoint refusals, and node cancellation settlement.
  All 12 unittest groups report OK. All node test groups report fail 0 and skipped 0.
  The only noise is ResourceWarnings (unclosed sqlite) in test_apply598, which are not failures.

## Scope and limits
- This accepts the checks stage only. It does not approve any package or application.
- The native stage comes next. It MUST be the FIRST heavy step of a NEXT fresh worker, not this one.
- 595 MUST NOT APPLY.
- The review was read-only. No offload, builds, services or sudo were used.
