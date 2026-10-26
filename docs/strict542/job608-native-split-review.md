# Job608 native split: independent review (source 88a35ad3, export manifest d9c33abd)

Reviewer did not author the change. Diff reviewed: 1ce600f6..88a35ad3. Nothing heavy was run locally (no cargo/npm builds).

## Checks
1. `build-native608.py <compile|libtests>`: argv must be exactly one stage. Both stages keep the same
   fresh-export refusal, the inherited CARGO_/RUST*/NAPI_RS_/ROLLDOWN_/CC/CXX/LD/LD_PRELOAD/LD_LIBRARY_PATH
   refusal, the pinned source archive, the Rust 1.98.1 and cmake 3.31.6 wheel digests, the patch preparation,
   the lifetime red-green tests and the cargo policy (locked, jobs 1, lto off, cgu 64, opt 3). The pin file,
   prepare-native608.py and last-use-ast608.rs are unchanged since 1ce600f6. `compile` runs only
   `cargo build ... -p rolldown_binding` and records `addon_sha256`. `libtests` runs only
   `cargo test --locked --release --jobs 1 -p rolldown --lib` and is the only stage that sets
   `native_lib_tests_exit`. The receipts are accurate: the compile receipt makes no lib-test claim. Cleanup is now `rmtree(root)`.
2. `native-compiler608.mjs`: every check from the old single-receipt version is still applied to BOTH
   receipts (kind and stage, complete, pin commit/source/rust digests, lifetime exit 0, retention negative,
   cargo policy, exact owner inventory, owner digests). It also requires lib-test exit 0 on the lib-test receipt,
   identical patched_sources/rustc/cmake/cmake_wheel_sha256 (each must be defined), and an addon digest equal
   to the compile receipt's. No check was weakened.
3. Runners: `run-native608-stage.sh` validates the stage, refuses a non-fresh export (result dir, source,
   .native608), checks both archive digests against the manifest before extracting, and on EXIT copies out the
   receipt/log, then removes source and .native608. It uses no secrets and makes no network calls beyond the
   build script's existing pinned Rust and cmake downloads. `run-native608.sh` drops its own compile and
   installs only the stage outputs whose digests match the manifest (`native_stage_outputs`: regular file, not a symlink, sha256 match).
   `mkdir ../.native608` fails if it already exists, and the existing cleanup removes it. 2g/1CPU is still
   set by the lease, and the manifest purpose says default2g1CPU. The 5400s deadline: finite (`timeout -k 15s`),
   applies to each stage separately, and justified, because the single 2400s window covered tests, toolchain,
   the dependency graph and both cargo invocations, and it ended inside crate rolldown with no assertion failure.
4. Export `/home/deploy/agentq/tmp/export608-native-compile` (manifest byte-identical to committed d9c33abd copy, sha256 929f2ba7...):
   - successor598.tar `03affdfd4531c3fe22c8a6e875c874460250b9ada98fb9cb7b143cee9a344a5b` = manifest. It is
     byte-identical (cmp) to `git archive 88a35ad3 -- <144 successor_paths>` and holds all build owner inputs.
   - rolldown608-source.tar.gz `203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac` = manifest = pin.
   - run608.sh `dd20d376d907e6fc5000bf068fcd5d128c142e1fbb2ee3334c8f006792b0148d` = manifest runner_sha256,
     byte-identical to docs/strict542/run-native608-stage.sh at 88a35ad3.
   - Tar listings (150 entries in successor, plus the source tarball): no .env, key, pem, db/sqlite, npmrc or credential files.
5. `node --test` native-compiler608 (2), disposable-inputs608 (3), serial-probe598 (10): 15/15 pass.
   `sh -n` passes on both runners. `py_compile build-native608.py` passes.

## Findings (non-blocking)
- The libtests stage rebuilds from the same pinned inputs and does not test the compile stage's own artifact.
  The consumer ties the two stages together only through equal pins, patched_sources and toolchain. This is acceptable for a diagnostic.
- The libtests stage downloads cmake again. The download is pinned and identical, so no new network surface.
- Nothing shows that 5400s is enough. The plan already forbids an unchanged retry if the stage fails.

## Verdict
APPROVE ONE compile-stage run of this export exactly as pinned (source 88a35ad3, manifest d9c33abd).
