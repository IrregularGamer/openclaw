# job608 independent acceptance: checks result at substep-budget freeze a39ad5ee

Verdict: ACCEPT. This is stage evidence only. SOURCE ONLY; 595 MUST NOT APPLY.
It gives no package or install authority.

Reviewed: `job608-checks-substep-a39a-result.md` (commit 3b28b3fd) against the
returned result `/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-checks-substep-a39a/result608-checks`
and `../checks-substep-a39a-offload.{log,rc}`. The rules applied are in
`job608-after-native-admission-continuation.md` lines 66-78 (candidate95 checks
section), with preflight e5a8dbf9. The review was read-only: no offload, build,
test run or install was launched.

Independently verified:

1. The client rc file is `0` and the result `exit-code.txt` is `0`. The log has
   314 lines and ends with `STEP608 installed-checks-pass`.
2. Export digests after the run match preflight e5a8dbf9: export-manifest.json
   322e58a911817d9752932c07a11a807208faf3a8da0bd1043b80c75e2907e892, run608.sh
   e2ed7e1337f5d0564b56e61174d0837440655cd38f75416608bff3de82780605 (equal to
   `git show a39ad5ee:docs/strict542/run-stage608.sh`), stage608.py
   a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4.
3. `checks/stage-receipt.json` has sha256 176ac198aa4f731cbd71196702b8c90494f845b2426947600a18f0c5a32862f7.
   Its fields: kind JOB608_STAGE_RECEIPT, stage checks, exit_code 0, run_id
   stage608-checks-a39a, manifest 322e58a9..., source_commit
   a39ad5ee95609193502850d0dbb87b5dcbb5e3e3, source_export
   d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62,
   stage_inputs {}. The outputs installed.json 0c56a168736678a98b3fc048b127a5708a4c23724abebefae324471a53533f3c
   and tests.log bf90e55ed34f8fdd4ea19249cfc6ee7671fab48b793c424b82f66ac24d5e5313
   match their on-disk sha256. The strict542-checks/ copies are byte-identical
   (cmp). The committed copies under `job608-checks-substep-a39a/`
   (installed.json, stage-receipt.json) are byte-identical to the result files.
4. Rerunning `python3 -I -B docs/strict542/storage608.py result --stage checks --result <abs>`
   exits 0 with logical_return_bytes 309965 and cap 16777216.
5. Python: 12 unittest runs (15+18+13+19+17+3+5+2+6+14+16+7) total 135, all OK.
   No FAIL, ERROR or Traceback lines.
6. Node: three node --test summaries (101+28+38) total 167 tests. All 167 pass,
   with 0 fail, cancelled, skipped or todo.
7. installed.json: success true, 17/17 suites passed, 279 tests = 272 passed +
   7 pending, 0 failed. All seven suite files are present and passed:
   build-all-bounded608 4, compiler-input-snapshot 39, native-declaration-boundary
   14+3 skipped, tsdown-build 165, tsdown-declaration-resolution 21+4 skipped,
   write-plugin-sdk-entry-dts 15, write-unified-entry-dts 14.
8. Skips: the 7 skipped cases are the same pre-existing platform skips accepted
   at a46c (f73bc268). Six are Windows 8.3/namespaced/extended-length cases and
   one is the case-insensitive directory-alias case. The full installed.json
   (file, case, status) inventory is identical to the committed a46c
   installed.json. The Python and Node case lines in tests.log are identical to
   the a46c tests.log, apart from a memory address in one ResourceWarning and
   the timings. No new skip or omission.
9. Gateway/supervisor IPC refusal, cancellation, settlement and owner tests are
   present and pass. test_native_owner_server has 15 ok (cancel_ack reaped,
   escaped descendant settled with pidfd), test_native_preparation has 18 ok
   (cancel refuses and restores handlers), and test_root_owner_supervisor has
   13 ok (mainpid/cgroup/nonroot/systemctl refusals). The Node cases also pass:
   settled-acknowledgement and cancellation, wrong-correlation/nonsettled
   refusal, the stage-receipt/addon refusal, the no-checkpoint-on-failure case
   and the fail-closed fd cleanup case.
10. `git diff a46cd576 a39ad5ee --stat`: the only executable change is
    `docs/strict542/run-stage608.sh` (+15/-2). It adds the START608/step608
    marker helper, adds markers in the compiler/unified path, and wraps the
    unified-0 build with a fixed 2280 s inner `timeout` plus a fail-path log
    tail. The checks stage does not run this code. The remaining 22 files are
    a46c checks/native/runtime evidence docs and the unified-0 candidate and
    review docs. This matches the result doc's claim.

All numbers and hashes in 3b28b3fd reproduce exactly, and no discrepancy was
found. Next steps per job608-after-substep-budget-continuation.md may proceed:
native, then runtime, then unified-0 at a39a, each as the FIRST step in a
fresh worker.
