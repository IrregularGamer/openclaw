# Job608 libtests2 export review (independent; diagnostic only)

Export: /home/deploy/agentq/tmp/export608-native-libtests2. Baseline: the approved export608-native-compile3 (job608-compile3-export-review.md).

1. Hashes match the manifest pins and compile3 byte for byte:
   - run608.sh `2c6e313a9aa7dddfbbdfe36986325bed7f46346d6e05822d4c032ca344290e57` = runner_sha256 = compile3
   - successor598.tar `5eb5a44e1e3ec2b6c506c128aff0f18ce1cc5ee5b62a7c407f6fbf6f575ef2e5` = successor_archive_sha256 = compile3
   - rolldown608-source.tar.gz `203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac` = compiler_upstream_archive_sha256 = compile3
2. Manifest (sha 47c89ed1…): compared as parsed JSON with compile3's manifest (324e3cd4…). Only `stage` (compile -> libtests) and `purpose` differ. The libtests file is pretty-printed, which is a whitespace difference only. source_commit 40947f38830cd19e75ac6925bb2590d9f7d34a28 and all 145 successor_paths are identical.
3. `git -C source552 archive --format=tar 40947f38 -- <successor_paths>` gives sha256 `5eb5a44e…f2e5`, which reproduces the successor tar exactly.
4. Runner and stage: run608.sh is unchanged from compile3. It verifies the archive hashes, requires a fresh export, and calls `build-native608.py libtests` under a 5400s timeout. The libtests branch runs only `cargo test --locked --release --jobs 1 -p rolldown --lib`, plus the shared standalone lifetime and negative-retention checks. It does not build the addon. CARGO_BUILD_JOBS=1. The script refuses inherited CARGO_/RUST*/LD_* environment variables. There is no memory or CPU override, so the 2g/1CPU offload defaults apply.
   - Network: the only fetches are the digest-pinned Rust 1.98.1 dist, the cmake 3.31.6 wheel, and `--locked` crates. This is the same set as approved compile3, and none of it uses credentials or secrets.
   - "install.sh" installs the toolchain only under the disposable `.native608`. The script does no system install, seal, sudo, systemctl or service action.
5. Secret scan (private keys, AKIA, gh*/github_pat, xox*, sk-/sk-ant-, AIza, glpat, npm_, password/secret/token/api_key assignments, .env/.pem/.key/.netrc/.npmrc/credentials files) across the successor tar contents, the upstream tar, the runner and the manifest found no real secrets. The scan had 1 hit, a false positive: `AKIA…` matched inside base64 wasm data in upstream `examples/yarn-pnp/.pnp.cjs` line 4520. That file is the same pinned upstream archive approved in compile3.
6. Fresh export: none of result-native608-*, source or .native608 exist in the export dir or in /home/deploy/agentq/tmp.

ONE run: `offload run --artifacts result-native608-libtests -- timeout -k 15s 2700s sh run608.sh libtests` (same outer-cap caveat as compile3).

VERDICT: APPROVED
