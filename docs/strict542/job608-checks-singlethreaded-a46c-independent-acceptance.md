# job608 independent acceptance: checks result at singleThreaded freeze a46cd576

Verdict: ACCEPT (stage evidence only; SOURCE ONLY, 595 MUST NOT APPLY; not
package/install authority).

Reviewed: `job608-checks-singlethreaded-a46c-result.md` (commit 7a4bceba) against the
actual returned result `/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-checks-singlethreaded-a46c/result608-checks`
and `../checks-singlethreaded-a46c-offload.{log,rc}`, using the rules in
`job608-after-native-admission-continuation.md` lines 66-78. Read-only; no offload or
build was launched.

Independently verified:

1. Client rc file `0`; result `exit-code.txt` `0`; log (343 lines) ends
   `STEP608 installed-checks-pass`.
2. Export digests now: export-manifest.json 5f6e09743454e75b306f0b4e937c5fbf321dc52898ce95321299cd1ec28013e4,
   run608.sh eb662d8191b7abeb5474e61546e1a97811e4bdb621aa6687e36982bc76644b01,
   stage608.py a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4 -
   identical to preflight 841ba12b.
3. `checks/stage-receipt.json` sha256 222c210fffa069be6b275603f2e6963e1ae7e15c544b90c98c0020a40b7c1961:
   kind JOB608_STAGE_RECEIPT, stage checks, exit_code 0, run_id stage608-checks-a46c,
   manifest 5f6e0974..., source_commit a46cd5765702f3b019d5a433b82d19ac57821a8d,
   source_export 88279fe17ba6263f5e982c8bb7bad16a13e8f5ad8cf367eebb1921caded20d9e,
   stage_inputs {}. Outputs installed.json 6e3b89695e9cf9eb2d8f268163fbf755fe42c143f9cb481065f5ab588eb30740
   and tests.log 36387b181acc8c9381bf9ae294db0d71b9a128a54ba98545e3291d3d3e7031b4
   match on-disk sha256; strict542-checks/ copies are byte-identical.
4. Rerun `python3 -I -B docs/strict542/storage608.py result --stage checks --result <abs>`:
   exit 0, logical_return_bytes 310281, cap 16777216.
5. Python: 12 unittest runs (15+18+13+19+17+3+5+2+6+14+16+7) = 135, all OK.
6. Node: three node --test summaries 101+28+38 = 167 tests, 167 pass, 0 fail/
   cancelled/skipped/todo.
7. installed.json: success true, 17/17 suites passed, 279 tests = 272 passed +
   7 pending, 0 failed. All seven suite files present and passed:
   build-all-bounded608 4, compiler-input-snapshot 39, native-declaration-boundary
   14+3 skipped, tsdown-build 165, tsdown-declaration-resolution 21+4 skipped,
   write-plugin-sdk-entry-dts 15, write-unified-entry-dts 14. 4+165+15+14 = 198
   prior inventory; +81 native/compiler cases.
8. Skips: all 7 are pre-existing platform skips (source lines blame to the
   boundary commit bcfc8881, unchanged at a46cd576): 6 gated by
   `skipIf(kind.includes("Windows") && platform !== "win32")` or
   `runIf(platform === "win32")` (8.3 alias x2, directory alias targeting 8.3 x2,
   namespaced executable, extended-length executable path), and 1 runtime
   `skip("Filesystem does not expose a case-insensitive checkout alias")` for
   "directory alias targeting a case alias" on case-sensitive Linux. No new
   skip or omission. Minor wording note: the result doc calls all 7 "Windows-only";
   the case-alias one is a case-insensitive-filesystem skip, still a pre-existing
   platform skip. Not a blocker.
9. Gateway/supervisor IPC refusal, cancellation, settlement and owner tests are
   present and pass, e.g. test_native_owner_server (cancel_ack reaped, escaped
   descendant settled with pidfd, mainpid/cgroup/nonroot refusals), test_native_preparation
   (cancel refuses and restores handlers, second owner check refusals),
   test_root_owner_supervisor (parent SIGKILL cancels native tree before receipt,
   descendants settle on shutdown, pin-drift refusals), and Node cases "refuses
   missing, swapped, failed or disagreeing stage receipts and a changed addon",
   "failed and incomplete phases never publish a checkpoint", "source mutation,
   hardlinked output and read-error refusal remain fail-closed with fd cleanup".

All numbers and hashes in 7a4bceba reproduce exactly. Next steps per that doc
(native, then runtime, then unified-0, each FIRST in a fresh worker) may proceed.
