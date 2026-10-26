# Exact608 continuation after first lifetime-only run — 2026-10-26

Supersedes the next-run section of job608-resume-after-workers.md. Export
/home/deploy/agentq/tmp/export608-native-lifetime (source74d93ffa, reviewed
job608-lifetime-export-review.md) is SPENT; never rerun it.

## Actual outcome (job608-native-lifetime-offload.txt)
Remote rc1. Toolchain pins verified; the real standalone helper tests for the
reviewed early-finalizer helper (eb45f4f0) compiled and passed 7/7, including
early_reader_union_retains_finalizer_only_renderer_only_and_both and
early_release_refuses_incomplete_reader_census. The old-retention NEGATIVE
CONTROL then failed to compile: build-native608.py replaced
`drop(value.take());` with a `//` line comment, which also removed the closing
brace of the new one-line `if !*required { ... }`. This is a test-harness defect,
not a helper or compiler failure; no lifetime receipt was produced.

## Correction (this commit)
The mutation now uses block comments; it still disables only ownership release
and never changes expected values. New focused test
RetentionNegativeControl evaluates the exact mutation expression from
build-native608.py and checks Rust delimiter balance: RED on the old mutation
(28 `{` vs 27 `}`), GREEN after; all 3 finalizer contract tests and 3
native-compiler608 Node tests pass. Changed owner input invalidates prior
native receipts, as before.

## Ordered next steps (each its own reviewed fresh export, default 2g/1CPU)
1. Independent review of this correction; fresh lifetime-only export from this
   commit built exactly as job608-native-lifetime-export.json (same path list,
   stage lifetime, run-native608-stage.sh as run608.sh); ONE
   `offload run --artifacts result-native608-lifetime -- timeout -k 15s 1500s sh run608.sh lifetime`.
   Accept only rc0 with complete receipt and retention_negative_detected.
2. Fresh compile stage (addon) then libtests stage for the patched finalizer,
   new receipts/addon pins; then ONE combined native-worker-lazy diagnostic
   (all checks + 57 configs incl. worker46) per job608-resume-after-workers.md.
3. Only after an accepted complete combined diagnostic: native bounded-package
   wiring, full typed build/frozen package, deterministic artifact receipt,
   old/new hashes, supervisor IPC refusal/cancellation tests, independent
   action/privilege/seal reviews, automatic queue review, then the ordered
   foreground HQ handoff in job608-to595.md.
4352MiB guard, 1625784320-byte floor and all application gates unchanged. No
install, seal, unit, sudoers, service, credential transfer or provider call.
