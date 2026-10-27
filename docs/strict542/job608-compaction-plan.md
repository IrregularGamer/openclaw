# Source-owned scan-to-link compaction608

This supersedes only the next-run paragraph of job608-native-phase-outcome.md.
Recovered phase evidence is job608-native-phase-recovered.json (source00d5fe9f).
All238 checks passed; AI and main0..45 passed. Main46 was SIGKILL after155208ms,
with scan buildEnd RSS1853698048 and later RSS2012164096, V8heap~16MB, cgroup~2GiB.
The run is SPENT. Exact killer remains unknown; zero sampled OOM counters do not
prove memory safety. Existing per-config process isolation, worker minifier split
and lazyBarrel were already active. Generation AST cleanup cannot reduce the
resident pre-link scan graph. No unchanged retry or cap/floor/check change.

The existing native AST owner now provides clone_with_compact_arena using its
canonical clone_in_with_semantic_ids into Allocator::default. Old cache cloning
retains its original capacity policy through a shared private implementation.
LinkStage::new serially replaces every present AST BEFORE allocating linker
metadata; each old arena drops before the next clone. No module or source is
removed, no transform repeats and no semantic IDs regenerate. Source ArcStr,
source_type and AST spans survive. Upstream internal-docs/ast-mutation/
implementation.md explicitly says cross-pass references use IDs, not AST pointers.
Both new upstream files are exact SHA256 pins; changed context refuses.

The real Rust regression parses imports, require, dynamic import and new URL,
assigns semantic IDs, injects64KiB abandoned allocation, compares code and
scope/symbol/reference/node IDs, measures used bytes AND allocated capacity,
and verifies validity after dropping the original. It exercises the old reserved
capacity clone as a negative control. Allocator::capacity/used_bytes APIs were
verified from checksum-pinned oxc_allocator0.150.0 crate8c5deaaa43f0813b6d4a18dcc5f41bea1996f193f0a55d0242831d7f29bfa16d.
The full ecmascript lib suite and exact named regression must pass in every
compile/libtests run before a complete receipt. A missing/failed compaction
receipt refuses native consumers. Old receipts are invalidated by owner pins.

Local:2 patch-policy tests RED on missing behavior then GREEN;3 native-receipt
and3 consumer checks PASS; syntax/diff checks PASS. Real Rust regression and
resource fit remain UNRUN until admitted offload. Serial replacement adds at
most one module clone to the resident graph; default2GiB fit is not guaranteed.

Next: independent exact source/export review, ONE fresh secretless compile stage
with ordinary2GiB1CPU admission and outer2400s timeout while>=46min foreground
lifetime remains. Then matching libtests, full combined238+2 checks/parity/AI+
all57main/fourworkers and actual complete typed frozen package. No standalone
lifetime rerun. No binary/cache/toolchain/dependencies uploaded. No local build.
Only complete independently accepted diagnostic success permits the existing
package promotion plan. Exact artifact/action/privilege/seal/automatic reviews
and ordered595 natural-gap/fresh post-restart HQ owner+accepted-run acknowledgements
remain mandatory in job608-to595.md.575/588/592 and553 remain by reference.
No installed/sealed/root/unit/sudoers/service/config/provider or queue mutation.
