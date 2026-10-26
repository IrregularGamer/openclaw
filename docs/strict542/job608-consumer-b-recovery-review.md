# Independent consumer-b recovery evidence review — 2026-10-26

Reviewed at source HEAD `7bc637bc2431fb8ae82fb0239f8dab81b56e9a0e` against the retained original `/home/deploy/agentq/tmp/export608-native-consumer-unitfast-b/result598`. Evidence inspection only; no build/test rerun, offload, service/config change, installation or release.

**Verdict: recovered evidence is authentic to the retained output and supports the limited successes below. The overall consumer run remains failed (exit 1); full build acceptance is not established.**

All six recovered files are byte-identical to their retained counterparts. SHA-256:

| Recovered suffix (`job608-consumer-b-`) | SHA-256 |
| --- | --- |
| `native-receipt.json` | `e210de64481feece6ae64ee192c0e14626cc112f2ef4c47c7fac526f7fc7faad` |
| `parity.json` | `3b01c8102d22f14548a1662efb4bb330b236f811cb36fca141f1e6fe4a486df0` |
| `probe.json` | `30bab8050627b7063b4d542cbcd7a313d451e9dce354c2c1c6b58f9e3896b44c` |
| `checks-evidence.json` | `47f1433b031ec86136882aad4b5ebf74ff0ff8a71fefc06384c8c9baa9313ff7` |
| `checks.txt` | `6edb52488f2f70e9eda0060544900deaecb04e4c3d15395547fc2d9e322ad166` |
| `probe.txt` | `fbb8a962f5ddacf2a48acc3283a74353223d64fb0e7b9d95b52592d398372fdd` |

The native receipt is also byte-for-byte equal to the original pinned `job608-native-compile-receipt.json`, not merely equivalent JSON. The retained native addon hashes to `f8b7634b1ccf713ec593f2a802373e16bffc92f1a63edd82704232c4960adcc6`, matching that receipt and the parity record. The probe embeds the same receipt. This verifies the recovered compile-stage identity; it does not convert a compile-stage receipt into later build acceptance.

The parity record contains exactly all eight ESM/CJS × sourcemap off/on × minification off/on variants (44 output records). `native-codegen608.test.mjs` writes this record only after both compiler child exits are zero and `assert.deepEqual` compares all eight patched results with stock. The retained probe log records that test passing (1/1). It also records lazy-barrel tests passing twice (2/2 stock, 2/2 patched), and bounded-package unit-fast tests passing 3/3 in one file.

The scoped checks evidence records exit 0 and source commit `0041793a1dfb63fc6594b3c954754717f143b17d`; its test-log digest matches the recovered log above. That log contains 101/101 initial Node tests, seven Python groups of 15, 18, 13, 19, 11, 2 and 6 tests (84 total, each `OK`), then 24/24 runner-policy Node tests. These are scoped checks (209 recorded tests), not a full suite/build claim.

The diagnostic census contains 57 main configs, but execution stopped after `ai` and main configs 0–46: 48 results, 47 successful and one failed. All captured results report no ineffective dynamic import and no fatal unresolved import. Main configs 47–56 remain unexecuted here.

- **Config 15 actually succeeded:** `status: 0`, no signal/error/timeout, elapsed 320003.792784 ms, and a `closed` diagnostic after `build-end`. Peak sampled RSS was 2020900864 bytes; final closed RSS was 1705717760 bytes. Its 1138-entry unified config has `dts: false`. This is successful isolated diagnostic execution, not full graph/package acceptance.
- **Config 46 failed:** `status: null`, `signal: SIGKILL`, `timedOut: false`, elapsed 63474.408607 ms; the log reports process-group state `dead`. RSS grew from 1319755776 while running to 1855733760 at `build-end`, then 2038317056 afterward; last sampled cgroup usage was 2145615872 against capacity 2147483648. There is no `closed` diagnostic. The failure is consistent with reaching the 2 GiB lease; sampled pre-kill `memory.events` remains zero, so these samples alone do not independently prove a kernel OOM cause. Overall retained exit code is 1.

Correction to the preliminary outcome interpretation: config 46 is a one-entry `openclaw-unified` config, `worker/worker` → `src/worker/worker-deploy-entry.ts`, with `dts: false`. Growth after `build-end` is observed, but the recovered evidence does not establish declaration generation or a particular post-build owner as its cause. Further source diagnosis must identify that owner before selecting a correction. The preliminary outcome correctly withheld unstreamed successes; recovery now supplies the bounded evidence above while preserving the overall refusal.
