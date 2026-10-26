# Job608 native compile split (follows job608-native-cmake-outcome.md)

The single admitted run (tests + toolchain + dependency graph + `cargo build` + `cargo test`)
hit its own 2400s deadline at crate `rolldown` on 1 CPU. No source assertion failed.

Change (source only, diagnostic, not build/package/application authority):
- `build-native608.py <compile|libtests>`: common pinned source/patch/toolchain/cmake and the
  lifetime red-green tests run in both; `compile` builds only `rolldown_binding` and returns the
  addon + `NATIVE_COMPILER608_COMPILE_STAGE` receipt; `libtests` runs only
  `cargo test --release -p rolldown --lib` and returns a `NATIVE_COMPILER608_LIBTEST_STAGE` receipt.
  Cargo policy (locked, jobs1, lto off, cgu64, opt3) unchanged.
- `run-native608-stage.sh <stage>`: needs only successor598.tar + pinned rolldown source; deadline
  5400s per stage (reviewed increase from one 2400s window covering everything; 2g/1CPU unchanged).
- `native-compiler608.mjs`: consumer accepts only BOTH stage receipts, each checked against the pin,
  owner-source digests, cargo policy and lifetime evidence, and requires identical patched_sources,
  rustc, cmake and cmake wheel; lib tests exit 0; addon digest equals the compile receipt.
- `run-native608.sh` (consumer stage): installs only manifest-pinned (`native_stage_outputs`)
  stage outputs into `../.native608`; no compile in that run. New refusal tests:
  `native-compiler608.test.mjs` (accept + 9 refusals).

Order: independent review -> ONE compile stage -> ONE libtests stage -> commit outputs + digests
-> consumer export with pinned digests -> ONE consumer run (parity/lazy-barrel/config15).
Not authorized: retry of a failed stage unchanged, larger CPU/RAM, lower checks or floors.
