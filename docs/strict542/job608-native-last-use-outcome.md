# Job608 native last-use admitted run: tooling refusal, no measurement

Export `export608-native-last-use` (manifest f6d8951e…, runner 34b7c4a1…, reviewed in
9a4723f4) ran once through normal offload at default 2GiB/1CPU,
2026-10-26T05:53:12Z rc=1 after 1381s. Raw stdout: job608-native-last-use-offload.txt.

- All archive digests verified remotely; 18 policy checks shown passed (earlier
  suites ran before the tail; the runner prints only the last lines).
- Rust 1.98.1 installed; lifetime tests and retention-negative step reached
  `save()` before cargo (receipt artifacts were not returned on failure).
- `cargo build -p rolldown_binding` failed in libmimalloc-sys2 build script:
  `cmake` is not installed in the offload image. No bundler, parity, config15 or
  memory result exists. This is a build-tool gap, not a source assertion.

Correction (this commit): build-native608.py fetches the official cmake 3.31.6
manylinux2014 x86_64 wheel, verifies sha256
1c8b05df0602365da91ee6a3336fe57525b137706c4ab5675498f662ae1dbcec, unpacks it as
data, adds its bin to PATH and records/asserts `cmake version 3.31.6`. No pip,
no allocator/feature change, no budget, floor or check change. Wheel layout and
binary verified locally (light, no build).

Next: independent review of this exact recipe change and a regenerated committed
export (runner/manifest hashes change because build-native608.py is a successor
member), then ONE admitted run. No unchanged retry of the old export.
