# job608 independent review: 5ec111ba sigterm-race test fix + checks2 export (e457a069)

Verdict: **APPROVE**

## 1. Test-only change
- `git diff 7b72c7a7 5ec111ba -- src/` touches only `src/gateway/strict542/test_native_owner_server.py` (+12/-3).
- `native_owner_server.py` is byte-identical at 5ec111ba^ and 5ec111ba. e457a069 adds only docs (checks1 log + checks2 manifest).
- checks1 log confirms the sole failure: `test_ignored_sigterm_is_killed_and_reaped_before_ack`, `-15 != -9` (15 tests ran).

## 2. Not weakened
- `assertTrue(receipt['cancelled'])` and `assertEqual(returncode, -9)` are unchanged.
- The ready wait is bounded: each poll asserts `monotonic_ns() < request deadlineNs` (800 ms default), so it fails loudly and never waits forever.
- `ready=None` default leaves every other test unchanged. The fixed 80 ms sleep is kept, and cancel still goes over the same socketpair to the real `server.serve_connected`. Only *when* cancel is sent changes, so the test cannot hide a server bug. If the child never becomes ready, the test fails; it does not skip.
- Local (NATIVE_SOURCE=/home/deploy/agentq/tmp/nativesrc608.sru5): `Ran 15 tests ... OK`.
- Contention on 1 CPU (`taskset -c 0` + 3 pinned busy loops), interleaved 5x each: old test version failed the sigterm test 4/5. 5ec111ba passed 5/5. With 2 fresh busy loops, both versions passed 5/5.
- Residual, not a blocker: under extreme accumulated contention (around 8 busy loops on 1 CPU), two *unchanged* 800 ms deadline tests (`accept_root_gateway_peer`, `exited_leader_...`) also flaked. They pre-date this change and did not fail in the checks1 run.

## 3. checks2 export manifest
Differs from the predecessor `/home/deploy/agentq/tmp/export608-stage-checks-223945/export-manifest.json` only in:
`successor_paths` (+ exactly `src/gateway/strict542/test_native_owner_server.py`, order otherwise identical), `successor_archive_sha256`, `source_commit`, `source_export_sha256`, `run_id`, `predecessor_manifest_sha256`, `predecessor_package_attempt`, `source_correction_review`. `execution_state` is unchanged (`UNUSED`). Runner, stage helper, native, compiler and base archive identities are unchanged.

Hashes verified:
- source_commit `5ec111ba29ba738b37a8d0c8371536b3ab956865`
- successor_archive_sha256 `397f7f164267d4b55c841944f31b8c9d5f976254733e358f45c130a9e8bc90b8` = sha256 of `export608-stage-checks-000307/successor598.tar` = `git archive --format=tar 5ec111ba <successor_paths>` (reproduced)
- base_source_archive_sha256 `e79a0e45a4eaea4afe325ca94ba201d5ae43d09d8c15dc07d0695c87ba743de3` = sha256 of `source598.tar` in that dir
- source_export_sha256 `1388a1693265918d7e93ecee53e42d8b397cb46c9a05c550034dc4787721b81f` recomputes as the canonical-JSON composite of {base_source_archive_sha256, source_commit, successor_archive_sha256}
- predecessor_manifest_sha256 `f3b479ea544bc5248beadd501fdcbd1de8c798f425e42a47cbf8a0bbce3bbe57` = sha256 of the predecessor manifest
- The committed manifest is byte-identical to `export608-stage-checks-000307/export-manifest.json`. That dir was only read, never modified.
