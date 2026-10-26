# Job608 native608 lifetime-stage export: independent review (2026-10-26)

Verdict: **APPROVE** (diagnostic run only). This is NOT compiler, package or
application acceptance; a lifetime receipt grants no addon, lib-test or install authority.

## 1. Source (74d93ffa vs eb45f4f0)
- Diff touches only `docs/strict542/run-native608-stage.sh` (+3/-2): header comment and the
  `case` allowlist (`compile|libtests|lifetime`). Fresh-export refusal, sha256 checks of both
  archives against the manifest, the EXIT cleanup trap, and the `timeout -k 15s 5400s` inner
  deadline are all unchanged.
- `build-native608.py` (from eb45f4f0): `lifetime` maps to kind `NATIVE_COMPILER608_LIFETIME_STAGE`.
  After the toolchain and cmake pins, it runs the standalone last-use-ast608 tests plus the
  old-retention negative control (two named FAILED tests are required). It then sets complete,
  removes the work root and `raise SystemExit(0)` before any `cargo build` (addon) or `cargo test --lib`.
- `scripts/lib/native-compiler608.mjs` accepts only `NATIVE_COMPILER608_COMPILE_STAGE`/`compile`
  and `NATIVE_COMPILER608_LIBTEST_STAGE`/`libtests` (kind+stage+complete), so a lifetime receipt
  cannot satisfy either identity.

## 2. Export (/home/deploy/agentq/tmp/export608-native-lifetime), recomputed sha256
- successor598.tar          cc55c8ec61144dd93867ddd7e71bf4749adab02dba7e9fc20149c4ad4ad884a7 (= manifest)
- rolldown608-source.tar.gz 203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac
  (= manifest = rolldown-source-pin608.json source_archive_sha256)
- run608.sh                 2c6e313a9aa7dddfbbdfe36986325bed7f46346d6e05822d4c032ca344290e57
  (= manifest; byte-equal to HEAD = 74d93ffa `docs/strict542/run-native608-stage.sh`)
- Tar: 145 members that exactly match manifest successor_paths. Each one is byte-equal to
  `git show 74d93ffa:<path>`, and `git archive 74d93ffa <paths>` reproduces the tar sha256
  exactly. No .env, key, pem, db or credential files.

## 3. Command
`offload run --artifacts result-native608-lifetime -- timeout -k 15s 1500s sh run608.sh lifetime`
is appropriate and finite. The outer 1500s+15s bound sits under the inner 5400s bound, the
stage builds no cargo targets (single rustc test binaries fit 2 GiB/1 CPU), and network
fetches are pinned and verified with 60s socket timeouts. One run only, from a fresh export.
If it refuses or times out, record the outcome and do not rerun in the same export.
