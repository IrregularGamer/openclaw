# Job608 native608 compile2 export: independent review (source bd8a3a9f)

Scope: diagnostic only. This review grants no package, install or application authority. The reviewer ran nothing heavy: no offload, cargo, rustc or network.
Export: /home/deploy/agentq/tmp/export608-native-compile2 (export-manifest.json sha256 3c481df46f219536cd8297f0891cfaf494381f41b01ef7bd4327b6d69e3a43fe).

## Recomputed hashes
- successor598.tar `574baeeafa8289c7885821d1a1401356ddc9a90e4885141e20fb43fd8263a7ff` = manifest. `git archive --format=tar HEAD <145 successor_paths>` reproduces the same sha256.
- run608.sh `2c6e313a9aa7dddfbbdfe36986325bed7f46346d6e05822d4c032ca344290e57` = manifest runner_sha256. It is byte-equal (cmp) to HEAD docs/strict542/run-native608-stage.sh.
- rolldown608-source.tar.gz `203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac` = manifest compiler_upstream_archive_sha256 = rolldown-source-pin608.json source_archive_sha256.
- Manifest fields: source_commit = bd8a3a9fca07187fcee2d726832a6658e16c9fab (full HEAD), stage = compile. successor_paths is identical (same list and order) to docs/strict542/job608-native-lifetime2-export.json.
- The owner inputs at HEAD match the hashes in the accepted lifetime2 receipt: prepare-native608.py db1c2df8..., last-use-ast608.rs 8d293f92..., pin 644d4ab9..., build-native608.py f213797e.... The commits 33335af7..HEAD add evidence and review files only.

## Secrets and archive shape
- Successor tar: 151 entries (6 dirs, 145 files) with no .env, key, pem, npmrc or credential members.
- Rolldown tar: has 2 relative in-tree symlinks (CLAUDE.md -> AGENTS.md and one test fixture). It has no absolute or `..`-escaping member names, and no secret-like files. The `token` matches are only upstream test fixture .js files. Extraction uses tarfile filter='data'.

## Compile stage (build-native608.py lines 100-149)
- prepare() checks the pinned upstream file digests, then patches render_chunk_to_assets.rs, mod.rs and finalize_modules.rs (patched_finalizer, the eb45f4f0 early release). It records all 4 in patched_sources.
- Before cargo, the stage still runs the lifetime tests and the block-comment retention negative control (33335af7). `compile` runs only `cargo build --locked --release --jobs 1 -p rolldown_binding`. It sets kind NATIVE_COMPILER608_COMPILE_STAGE and addon_sha256, copies the addon out, and only then sets complete=True.
- Compared with the approved split review (88a35ad3), nothing in this path is weakened:
  - The env refusal, pins, Rust/cmake digests, cargo policy and fresh-export guards are unchanged.
  - The only changes are the added `lifetime` early-exit branch, the mutation comment style, and the finalizer patch.
  - The stage runner only adds `lifetime` to its case list. The 5400s inner deadline is unchanged.
  - native-compiler608.mjs is unchanged.
- Non-blocking: run-native608.sh (the consumer) changed after 88a35ad3. This review does not cover it, and it is not part of this stage.

## Verdict
APPROVE ONE compile-stage run of this export exactly as pinned: `offload run --artifacts result-native608-compile -- timeout -k 15s 2700s sh run608.sh compile` (default 2g/1CPU).
The reviewer did NOT run it (no-offload constraint). Accept only rc 0 with a receipt that has complete=true, kind NATIVE_COMPILER608_COMPILE_STAGE, the 4 patched_sources entries above, and a new addon_sha256. The outer 2700s limit is narrower than the inner 5400s deadline, and the prior compile took about 26 min, so a timeout is a plausible failure. Do not retry unchanged.
