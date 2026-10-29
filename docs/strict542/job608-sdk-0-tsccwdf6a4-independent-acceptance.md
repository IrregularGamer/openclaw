# Independent acceptance: job608 sdk-0 tsccwdf6a4 actual run

Reviewer: independent. I did not produce this evidence. Scope: evidence commit `b9decdd6`
(`job608-sdk-0-tsccwdf6a4/`). P = /srv/encrypted/dev-move-98/agentq-source608-20261028-private.
Result directory P/stage-sdk-0-tsccwdf6a4/result608-sdk-0. All checks were read-only. No
offload was launched and nothing under /srv was modified. The checklist follows the middle
tsccwdf6a4 acceptance.

## Checks

- PASS: preflight. `job608-sdk0-1-tsccwdf6a4-preflight.md` (856fe90d) has an independent
  review `job608-sdk0-1-tsccwdf6a4-preflight-review.md` (647d59af) ending `VERDICT: APPROVE`,
  with sdk-0 PASS for inputs `middle` and `native`.
- PASS: manifest. `P/stage-sdk-0-tsccwdf6a4/export-manifest.json` SHA256 is
  `933ed22177cbb1121faeed9922d28bbd493b945c6bb6d806dd35e43dabd5891f`, equal to the pin and
  to the receipt manifest_sha256. The staged `stage608.py` is `cmp`-identical to the
  committed `docs/strict542/stage608.py`.
- PASS: return codes. The committed `sdk-0-offload.rc`, the private
  `P/sdk-0-tsccwdf6a4-offload.rc`, and result `exit-code.txt` (private and committed) all
  contain `0`.
- PASS: offload log. The decompressed committed `sdk-0-offload.log.gz` is `cmp`-identical to
  the private `P/sdk-0-tsccwdf6a4-offload.log` (7 lines). It records the BEFORE/AFTER archive
  release cgroup snapshots, sdk-0-stage-native-start +10s, sdk-0-restore-build-done +23s,
  sdk-0-build-start (budget 2256s) +24s, `STEP608 sdk-0-build-done +465s` and
  `STEP608 sdk-0-pass`. Nothing matches refus, exit75 or error. Limit: the log itself
  does not echo the admission parameters. The 14g/4CPU/`--timeout 2460` command line comes
  from the README. A 465s run is consistent with the 2400s inner timeout, and rc 0 shows
  the run was admitted and completed.
- PASS: result file hashes. The private result contains exactly five regular files.
  `sha256sum -c result-files.sha256`, run inside the private result directory, reports OK for
  all five: exit-code.txt, sdk-0/build.log, sdk-0/checkpoint.tar.gz, sdk-0/stage-receipt.json
  and strict542-checks/pnpm-path.txt. Recomputing those five reproduces the committed file
  exactly.
- PASS: committed copies. exit-code.txt, sdk-0/stage-receipt.json and
  strict542-checks/pnpm-path.txt are `cmp`-identical to the private originals and tracked by
  git. build.log (243 lines) and the 1760089-byte checkpoint stay private. They are bound by
  result-files.sha256 and the receipt.
- PASS: stage receipt. Its SHA256 is `08530815eecb839d20085cae5ccd53fccd356eeb45b775548bd68587c0ce96b0`.
  It contains kind `JOB608_STAGE_RECEIPT`, stage `sdk-0`, exit_code 0 and run_id
  `stage608-sdk-0-tsccwdf6a4`. It binds source_commit `f6a4de2ebc6924d16fe559f9858bf8c50dce1eba`
  and source_export_sha256 `e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145`.
  Both equal the manifest fields. Its outputs are exactly `sdk-0/build.log` =
  `766e2130...c990` and `sdk-0/checkpoint.tar.gz` = `09f9d2b8...38c3ec`. Both equal the
  actual SHA256 of the private files.
- PASS: stage inputs. The receipt has 7 stage_inputs. middle/build.log `9d1fdaf9...e301`,
  middle/checkpoint.tar.gz `32ea0475...6e220` and middle/stage-receipt.json
  `9eb3083c...d2cf` equal the private accepted middle result, and that receipt is the one
  accepted in `job608-middle-tsccwdf6a4-independent-acceptance.md`. native/libtests-receipt.json
  `2f81179f...`, native/receipt.json `4a651254...`, native/rolldown-binding.linux-x64-gnu.node
  `0b6607e7...` and native/stage-receipt.json `10474857...` equal
  P/stage-native-tsccwdf6a4/result608-native.
- PASS: checkpoint listing. `tar -tzf` exits 0 and lists 379 entries. None is absolute or
  contains `..`. All 379 fall under `sdk/openclaw-dts-plugin-sdk-1`, which is exactly
  stage608.py `checkpoint_path('sdk-0')`. Inner receipt.json has schema
  `strict542-declaration-group608-v1`, status `COMPILED_GROUP_NOT_PUBLISHED` and group
  `openclaw-dts-plugin-sdk-1`, and it binds source f6a4de2e and export e81e07d2. The
  build608.json binding has the same identity and nativeCompileSha256 `4a651254...`, which is
  the accepted native receipt.
- PASS: build log. The only `error|fail|cancel` match (case-insensitive) is line 21, a pnpm
  `[WARN]` for a transient registry HTTP 502 on `@types/ms-2.1.0.tgz`, retry attempt 1. I
  judge this acceptable. pnpm retried it and the install finished ("Done in 49.2s"). There is
  no ERR_PNPM or ELIFECYCLE, the tsdown sdk-1 group invocation finished in 321.3s, and the
  receipt and checkpoint hashes are self-consistent. `phase timings: no phases ran` is
  expected because this stage builds only the declaration group.
- PASS: storage check. `python3 -I -B docs/strict542/storage608.py result --stage sdk-0
  --result <private result>` exits 0 with logical_return_bytes 1770948, under the
  33554432-byte cap.
- PASS: commit scope. `git show --stat b9decdd6` touches only 7 files under
  `docs/strict542/job608-sdk-0-tsccwdf6a4/`. It makes no installed, sealed, unit or sudoers
  change.
- PASS: README claims. rc0, +465s, sdk-0-pass, receipt 08530815, build.log and checkpoint
  hashes, the 1760089-byte checkpoint, 1770948 bytes under the cap, the manifest, the
  inputs and the single 502 WARN all match what I observed.

## Scope and limits

No build, offload, extraction, installed-state change or queue mutation was run. The only
change is this document. Stage sdk-0-tsccwdf6a4 is SPENT and must never be replayed. sdk-1
has not been launched. No install or release authority. 595 MUST NOT APPLY.

VERDICT: ACCEPT
