# Independent exact libtests3 outcome review608

VERDICT: APPROVE the exact libtests3 outcome as successful matching native library tests only. The ONE reviewed run settled rc0 at 2026-10-26T22:21:38Z in 1838 seconds. This accepts the post-metadata source's test stage alongside the separately accepted compile4 stage. Combined diagnostic/config15 resource fit, complete typed/frozen package, action, privilege, seal and real automatic queue acceptance remain unproved. No application authority is granted.

Reviewed evidence commit `b75a082b9ddf78e5d589286dac426fae977c35af` and its parent `d6a41ca7`, the exact export review, accepted compile4 receipt/outcome review and post-metadata continuation. Personally inspected retained `/home/deploy/agentq/tmp/export608-native-libtests3/result-native608-libtests`: its only three regular result files are `build.log`, `lifetime-retention-negative.log` and `receipt.json`. Each is byte-equal to its committed counterpart. The final build-log JSON equals the complete retained receipt, whose kind is `NATIVE_COMPILER608_LIBTEST_STAGE`, stage is `libtests` and `native_lib_tests_exit` is 0. No addon is produced by this stage.

Freshly recomputed all six outcome evidence SHA256 values; every value matches:

- Broker: `1b6eeb94d751e2f330faa9cec158f5c2116021e9bfd6358b82541a29cf01b4f6`.
- Complete build log: `7c6cff64de4254caaf4946a95ea1e23d3fdf3aabbb6a65199af8095be040b244`.
- Export manifest: `3047f378a219497f392994bbe6ef36d7ffe6e23b5aaaf1e51681b8136076fb94`.
- Offload log: `5400a589c752492c469089cd3a3d59d21b6b296ee8ab96257edf8959d1b643ac`.
- Libtests3 receipt: `84a8d51f34da3e788482de3e817b5583917a9351a22cb8ad2f7cf1b1ec218a93`.
- Retention negative control: `bb57ceaa264092e04c35cdb07d0fcf3fa41d973a389693087958dd6ffedfef46`.

The offload evidence is byte-equal to `/home/deploy/agentq/tmp/libtests3-run.log`. The broker evidence equals the unique entry for this exact export in `/home/deploy/.local/state/offload/runs.log`: `2026-10-26T22:21:38Z run remote rc=0 1838s /home/deploy/agentq/tmp/export608-native-libtests3`. Launch notes record the ONE foreground run at 21:50:59Z with worker expiry 22:49:56Z, providing more than the reviewed 51-minute minimum. This review did not launch or repeat it.

The actual build log records release compilation in 28m47s, then 112 distinct native test lines, all `ok`, with zero failed, ignored, measured or filtered tests. These include the seven helper tests within the native crate. The separate initial helper invocation has seven distinct `ok` lines and zero failures. The negative-control log contains precisely the three expected failures: `early_reader_union_retains_finalizer_only_renderer_only_and_both`, `repeated_module_survives_until_last_render_then_drops_before_next_module`, and `unused_is_released_before_first_render`. Its other four tests pass. These failures detect deliberately retained ASTs; they are expected negative-control evidence, not product test failures.

Independently compared all eleven shared receipt fields against accepted compile4: `owner_inputs`, `patched_sources`, `cargo_policy`, `rustc`, `cmake`, `cmake_wheel_sha256`, `upstream_commit`, `source_archive_sha256`, `rust_archive_sha256`, `lifetime_tests_exit`, and `retention_negative_detected`. Every complete value matches exactly. Thus toolchains remain Rust1.98.1 and cmake3.31.6 with the same archive/wheel digests; Cargo remains locked release jobs1/codegen_units64/LTO false/opt_level3; lifetime exit is 0 and negative detection is true. The changed generate module remains `db07fa1eaaf7e079a7645813ce25032105c522a557fbff7a854d2c1a4842c5b7`, with identical finalizer, renderer and helper identities to compile4.

The four owner hashes independently match receipt, successor archive, exact source commit `b1416481c38ba1480d8c881ca36e96785512fc47` and current checkout:

- `scripts/lib/prepare-native608.py`: `cd172e32b7376e89300ee794c3e85ee6740a557951c81f72e8f8fb9a82e649be`.
- `scripts/lib/last-use-ast608.rs`: `8d293f921d754f3ffca6f60eaec8b61fc577ebef779d9c5714db5f46c4cf2da4`.
- `docs/strict542/rolldown-source-pin608.json`: `644d4ab9b970df0aaa34070cd8db96add012fb82db9f72bce7878571549988ca`.
- `docs/strict542/build-native608.py`: `f213797ea4b8eb45bb2b93564734714b41d3a3b8d2b2b2a20c3b3b8c531f269c`.

Recomputed retained successor/upstream/runner hashes match the reviewed manifest: respectively `29c3853b9715326cd7323547058d3b7fd448a9ca8a653682fad92da98eff65e6`, `203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac`, and `2c6e313a9aa7dddfbbdfe36986325bed7f46346d6e05822d4c032ca344290e57`. Manifest bytes equal the committed manifest; runner bytes equal committed `run-native608-stage.sh`. Recreating `git archive --format=tar` at the exact source with all manifest paths reproduces the successor archive byte for byte.

Accepted compile4 receipt SHA256 is `bc741801b805fb6792e0e67fc4f8e3b88425096d41e6e6216927cff140f9d9b6`; its addon identity remains `17df206117097742019de475e8cd194fb1022f48d9c2b507195100abd13eb627`. These are the matching compile identities, not a new addon check from libtests3. Recomputed old libtests2 receipt SHA256 remains `d2a8c010e96cf561179b6021fd89dd6bbb7032889e62fff189beb088c6ca240d`; that old source receipt does not satisfy the changed prepare owner.

Libtests3 is SPENT. Disposable `source` and `.native608` directories are absent; exact result originals remain retained. The reviewed export approval and continuation's unused-libtests wording describe the pre-run state and must not authorize another run now. Next work requires a NEW separately reviewed combined source-only export with exactly the accepted compile4/libtests3 receipt JSON inputs, a rebuilt byte-equal compile receipt and addon, every affected check, parity/lazy/minifier coverage and all57 main configs including all workers and settled minifiers. This review does not approve that future export or run. Preserve normal admission, 2GiB/1CPU, zero new swap, existing compiler deadlines/floor, and every later package/application gate. Reviewer performed read-only evidence/archive/source/hash inspection and wrote this review only: no tests, offload, runtime, installed, privilege, service, provider or seal mutations.
