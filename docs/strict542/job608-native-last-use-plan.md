# Job608 native last-use AST implementation plan

Goal: bound code-generation overlap without splitting the unified graph or changing
owner, build, privilege, cancellation, settlement or admission checks.

Architecture: patch the exact Rolldown1.2.9 commit
5b4746e442989d770c606ce08d2737e6aafbd25d in disposable offload source. Its current
last reader retains all AST arenas while collecting all generated module outputs.
Count every chunk/module use, then render in original order, dropping each arena
after its final use and unused arenas before rendering. No new purity, external,
entry or chunking policy. Sequential codegen matches this one-CPU compiler lease.

- [ ] Add actual generic lifetime-owner tests for unused, repeated, missing and
  final-use ASTs. Demonstrate failure with the old retain-until-function-exit
  behavior and success with early release, in admitted offload only.
- [ ] Add exact-context/digest-checked native source patch and a fixed build
  recipe: immutable source, Rust1.98.1, Cargo.lock --locked, jobs1, release LTO
  disabled and 64 codegen units to bound the native compiler/linker. No cgroup
  changes. Retain source/patch/toolchain/addon hashes and logs.
- [ ] Independently review exact source and committed secretless export before
  one admitted changed-source run. All existing relevant checks plus actual
  stock/patched bundler equality, singleton, effects, dynamic import, ESM/CJS,
  source-map and minification tests must pass before config15 executes.
- [ ] Measure actual native and graph build outcomes. Preserve normal4352MiB
  full-build guard and unchanged1625784320-byte diagnostic floor. No unchanged
  retry or success claim on refusal. Only measured successful output can support
  a separately reviewed full-profile admission correction.
- [ ] Complete the canonical typed build/frozen package, deterministic receipt,
  exact old/new action and original/new seals, independent source/action/
  privilege/seal and actual automatic608 reviews before595 can apply.

The ordered foreground HQ procedure remains job608-to595.md. Native compiler
artifact identity is separate from unchanged587 external owner-native pins.
Historical586 request-time sudo is never used. No live install, service, seal,
unit, sudoers, auth/config transfer, provider call or scheduler action here.
