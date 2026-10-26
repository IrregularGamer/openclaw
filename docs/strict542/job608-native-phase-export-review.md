# Independent exact native phase-trace export review608

VERDICT: APPROVE ONE future full source-only combined diagnostic from `/home/deploy/agentq/tmp/export608-native-phase-trace`, conditional on normal controller/lease admission, a fresh qualifying worker with at least51 minutes of genuine foreground lifetime remaining at launch, and the outer `timeout -k 15s 2700s` bound. This review supplies no package, application, action, privilege-policy, seal or automatic-queue acceptance. No run was launched.

## Manifest and source

- Export `export-manifest.json` is byte-equal (`cmp`) to committed `b5ad41b9:docs/strict542/job608-native-phase-export.json`, SHA256 `5291b14769c92e56e4a2f306e087846debb7387c372264552a8d458a37f9556c`.
- `source_commit` `00d5fe9f5a99ff7fda6fc3a365ab7edb3d78ea29` is an ancestor of HEAD `b5ad41b9`; `git diff --stat 00d5fe9f HEAD` shows only that manifest added (270 lines).
- `b1416481` is an ancestor of `00d5fe9f`.

## Recomputed input hashes (all match manifest)

- Runner `run608.sh`: `1125cc3c0ffde8222fe6ce87aaa723fd0027725daed37a22e9966b7a61a41157`; byte-equal to `00d5fe9f:docs/strict542/run-native608.sh` and identical to the runner hash in the prior accepted post-metadata review (runner unchanged).
- Successor `successor598.tar`: `f55896f1ee78cab1f0651ff94b25cc321f2fb2455ded7989d88251b2d37dabdc`. Recreating `git archive --format=tar 00d5fe9f` over the 253 distinct manifest `successor_paths` reproduces these bytes exactly (so run-native608.sh and serial-probe598-policy.mjs inside equal the commit). 253 regular members, 6 directories, no links.
- Native fixture `native598.tar`: `d73e4e35720ffcb71856ce8168e75fa3b4fd49251fd78c811e1abded8b2701de`.
- Upstream `rolldown608-source.tar.gz`: `203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac`.
- `native608-stages/compile/receipt.json`: `bc741801b805fb6792e0e67fc4f8e3b88425096d41e6e6216927cff140f9d9b6`.
- `native608-stages/libtests/receipt.json`: `84a8d51f34da3e788482de3e817b5583917a9351a22cb8ad2f7cf1b1ec218a93`.
- Base `source598.tar` was not rehashed. Its device2049/inode1583918/size689664000 (link count15) equals `/home/deploy/agentq/tmp/export608-native-early-finalizer/source598.tar`; inherit the reviewed pin `e79a0e45a4eaea4afe325ca94ba201d5ae43d09d8c15dc07d0695c87ba743de3` (base `c790ba44`). Inherited raw pin, not a new digest claim.

## Export hygiene

- Exactly eight regular files: manifest, runner, four archives, two receipts. No symlinks; no result/cache/node_modules/target directories; no `.env`/`*key*`/`*.pem` filenames.
- Secret-pattern scan `tar -xOf successor598.tar | grep -aE 'BEGIN .*PRIVATE KEY|ghp_|sk-[A-Za-z0-9]{20}'`: 0 hits.

## Source change 00d5fe9f

13 files, +337/-62. Code changes are limited to:

- `serial-probe598-policy.mjs`: `admitProbe` now also refuses inherited `RD_LOG`/`RD_LOG_OUTPUT` (case-insensitive); new frozen `NATIVE_PHASE_TRACE608` = `RD_LOG=rolldown::stages::link_stage=debug,rolldown::stages::generate_stage=debug`, `RD_LOG_OUTPUT=stdout`; `nativePhaseTraceEnv608(env,index)` applies it only when index===15 and returns a copy otherwise.
- `isolated-probe598.mts`: main-config env goes through `nativePhaseTraceEnv608`; the receipt records the trace policy; main-config-15 asserts propagation of both keys. The existing pool/allocator propagation check, `900_000` ms deadline and admission path are unchanged.
- `serial-probe598.test.mjs`: two new tests (inherited-refusal over 4 keys x 4 values; config15-only, frozen and non-mutating). There are now 12 policy tests in total.
- `native-codegen608.test.mjs` + new `native-phase608.fixture.mjs`: real synthetic-input fixture asserting link/generate spans and enter/close on stdout, writing `result598-native/release-phase-trace.log`. It is UNRUN and not counted as evidence, matching the plan.
- The rest is docs/evidence: plan, red/green/focused logs, inventory, handoff.

The four native owner files are unchanged between `b1416481` and `00d5fe9f` (`git diff --quiet`), and their digests match the prior review: prepare `cd172e32...49be`, helper `8d293f92...2da4`, pin `644d4ab9...88ca`, build `f213797e...269c`. No removed diff line between `b1416481` and `00d5fe9f` touches 900/2700/1625784320/2GiB/CPU/cancellation. `UNIFIED_GRAPH_THRASH_LIMIT_BYTES = 1625784320` is still present. Runner bytes are unchanged, so the inner 5400s, outer 2700s+15s, 2GiB/1CPU defaults and cancellation/settlement are not weakened.

## Notes (non-blocking)

- Plan check count 238 = prior 235 + 2 policy tests + 1 native fixture, which is consistent.
- Trace overhead may change config15 timing. Locate the phase from the raw spans only. Missing or unsupported tracing, refusal, timeout or partial output is not success. Any failure needs outcome preservation, with no unchanged retry.

Reviewer performed read-only git/hash/stat/archive inspection only, with no tests, offload, build, install, service or network actions.
