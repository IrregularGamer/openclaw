# Decision637: finite canonical cache-history cases

Supersedes ONLY review636's timeout acceptance. Baseline parity remains diagnostic;
all required assertions must pass. No timeout exception is implemented.

The owning `write-unified-entry-dts.test.ts` splits the cumulative case into four
sequential 120000 ms cases. One suite-owned fixture lifetime retains the exact
filesystem, native fixture, cache stamps, hashes and original declaration across
initial build + consumer, unchanged build, isolated edit and cold writer. All
31 original `expect` calls and the final `expectStagingClean` remain. A stage
assertion fails subsequent cases if any prerequisite body did not complete.
Per-case managed commands still own the abort signal and settle before teardown;
suite cleanup drains retained bodies before removing the shared fixture.
No fixture, compiler cache rule, graph floor, worker/CPU/swap budget or compiler
or parent deadline changes. Installed checks retain the tooling shard, one
worker, nonempty selection and failure logging. JSON results are retained.

Before another full package launch, require independent exact source/runner/export
review and a fresh admitted affected installed-test pass. New exports stage only
both pinned native receipt JSON files, verify their hashes before expensive work,
and transfer no addon/toolchain/auth/cache. Spent package1/2/3 exports stay spent.
Full package, exact artifact/tree/check/native receipts, old/new hashes and
independent action/privilege/seal plus automatic parent608 reviews remain required.
