# job608 independent review: 591158cf census sha256 (package4 E2BIG)

Reviewer: independent (not the author). Read-only review. No offload was launched and no installed or sealed files were changed.

## Scope
Commit 591158cf, which touches `scripts/lib/bounded-package608.mjs`, `scripts/tsdown-bounded608.mts`,
`tsdown.bounded608.config.ts` and `docs/strict542/bounded-package608.test.mjs`, and adds the evidence log
`docs/strict542/job608-stage-package4-offload.log.gz`.

## Checks
1. **Diagnosis is plausible.** The package4 log tail shows `tsdown-ai` finishing with status 0. That stage's plan env is plain `process.env` with no census. `tsdown-packages` then fails 4.68s later with `spawn E2BIG` (errno -7) at `runTsdownBuildInvocation` (tsdown-build.mts:1168), called through `runWorkerPhases` from tsdown-bounded608.mts:50, on the first per-config child. The two invocations differ in only three places:
   - args: a fixed, small `--config tsdown.bounded608.config.ts --concurrency 1`;
   - `OPENCLAW_608_CONFIG_INDEX`: a short integer;
   - `OPENCLAW_608_CONFIG_CENSUS`: `JSON.stringify` of every config's full entry map.

   `runWorkerPhases` adds only `OPENCLAW_TSDOWN_TIMEOUT_MS`, which is also a short integer. The tsdown config census covers the plugin-sdk entrypoints plus the bundled plugin entries for about 164 extension directories (11,635 tracked files under `extensions/`). That makes a census larger than MAX_ARG_STRLEN (131072 bytes for one env string) credible. The base environment cannot be the cause, because the ai stage spawned successfully with it. The large census variable is the only credible E2BIG source.
2. **The guard is not weakened.** `selectTypedWholeConfig` still:
   - refuses a missing or malformed value (a new check: it must be exactly 64 lowercase hex characters, so `undefined`, `''`, `'[]'` and raw JSON are refused);
   - recomputes `typedConfigCensus(configs)` in the child and refuses any difference ("typed config census changed");
   - checks the index text, safe-integer status and range, in the same order as before.

   Comparing SHA-256 digests of the identical `JSON.stringify(census)` serialization is equivalent integrity for this purpose. A collision is computationally infeasible, and the producer and consumer use the same `typedConfigCensusDigest` helper.
3. **Every producer and consumer was updated.** `git grep -n CONFIG_CENSUS 591158cf` shows `OPENCLAW_608_CONFIG_CENSUS` used only as `_SHA256`, with one producer (tsdown-bounded608.mts:44) and one consumer (tsdown.bounded608.config.ts:6). No 608 reference to the old name remains.

   Not blocking: the separate `OPENCLAW_598_CONFIG_CENSUS` path (`tsdown.isolated598.config.ts`, `docs/strict542/isolated-probe598.mts`, `docs/strict542/worker-probe608.mts`) still passes the full JSON. Those are probe paths outside the package stage, so they are out of scope. If they are reused on the full config set, they would hit the same E2BIG.
4. **Nothing else was removed.** The diff removes no check, deadline (900 s absolute, per-phase remaining), budget, capacity admission, heap-override refusal, cancellation or result assertion. The old test assertions are kept or made stronger:
   - the valid selection is still identity-equal;
   - the census mismatch is now a valid digest of `[]` and must match `/census changed/`;
   - the old raw `'[]'` and raw-JSON values now must match `/census digest/`;
   - a new `undefined` case was added;
   - the out-of-range index `'3'` still throws;
   - a new regression assertion checks the digest length is 64.
5. **Tests.** `timeout 100 node --test docs/strict542/bounded-package608.test.mjs` gave 6 passed, 0 failed. `python3 -I docs/strict542/test_stage608.py` ran 10 tests and reported OK.

## Verdict
**APPROVE.** The fix targets the demonstrated E2BIG cause and keeps the census integrity guard at equivalent strength. It also adds a strict digest format check, and it removes no other safeguard.
