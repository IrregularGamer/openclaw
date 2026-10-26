# Post-metadata AST lifetime correction608 (source only)

Actual combined source68982a3d, export42dab6ad, settled rc1/2070s. Its
230 checks and exact46d32ba6 native rebuild passed; AI+main0..14 passed,
config15 was SIGKILL after179599ms and workers were never reached.
See job608-native-early-finalizer-outcome.json and independent outcome review.
The final sampled interval has0.384134s user CPU versus28.041168s system CPU,
RSS2024955904, V8heap21543320 and cgroup2145452032 bytes with almost no file
cache. This supports reclaim pressure, not a primarily useful-CPU stall.
Sampled OOM counters are zero; the precise killer and native subphase are unproved.
The export is SPENT. No unchanged retry, raised budget or package promotion.

The previous pruning occurs only inside finalize_modules, after cross-links,
namespace merging, export computation and symbol deconfliction. In the exact
pinned generate_stage/mod.rs, ast_table is moved out of self at160 and its
last earlier reader is compute_wrapped_esm_init_metadata at161. Later functions
until finalize_modules cannot read that local table. Source review establishes
that they neither set metas.is_included true nor add chunk.modules; the runtime
is_included=false sweep occurs in the earlier finalize_chunk_plan.

The new insertion releases unused ASTs immediately after that metadata reader,
before cross-link allocations. Its conservative union retains every normal
included module, required-order runtime, and every normal module of every chunk.
It omits the strict-live-chunk restriction, retaining a superset of the exact
later finalizer predicate. Canonical index assertions and the existing helper
remain; the temporary mask is dropped immediately. The exact later finalizer,
its additional pruning, renderer, ordering, graph and output policies are unchanged.
The patch refuses drift in its exact pinned source boundary.

Two initial regressions were RED before implementation; the independent review
also caught a wrong parent-module helper path. Its separate scope regression
was RED before correction. All5 source contract tests and9 focused Node policy
tests are GREEN. These are not Rust compile, library, parity or memory-fit proof.
prepare-native608.py changes, so every prior native receipt/addon is invalid
for this candidate. Use fresh reviewed compile and libtests exports, normal
2GiB/1CPU admission, then one newly reviewed complete combined diagnostic with
all scoped checks, typed inventory, real parity/lazy/minifier fixtures and all
AI+57main configs. No caller controls, AST reader, test or budget is waived.

Only complete accepted combined success permits the planned native bounded
package wiring. Full typed build/frozen package, exact artifact/action/current
old-new hashes, separate source/action/privilege/seal and real automatic queue
reviews still precede595. job608-to595.md and job598-HQ-HANDOFF.md retain the
finite natural-gap procedure, fresh genuine post-restart owner AND accepted-run
acknowledgements, backup/rollback/reseal rules and downstream references.
