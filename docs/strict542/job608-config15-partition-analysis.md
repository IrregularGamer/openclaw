# job608 config15 link-stage partition analysis (source-only)

Inputs: combined2 outcome 9e6c1ddf (SIGKILL at 2GiB in rolldown
link_stage::bind_imports_and_exports, timedOut:false), tsdown.config.ts at HEAD.

## Identity of config15
`main-config-15` is the first `TSDOWN_UNIFIED_CONFIG_GROUP` config in
tsdown.config.ts: core entrypoints, plugin-sdk subpaths, bundled plugin
entrypoints and bundled hooks built "in one graph so runtime singletons are
emitted once". tsdown.bounded608.config.ts already states "Never repartition
its graph".

## Why splitting is not an acceptable source correction
Rolldown binds imports across the whole module graph in a single pass. Splitting
the entry set into several builds produces a separate copy of every shared module
(registries, plugin-sdk state, gateway owner/settlement state) per partition. That
breaks the singleton identity the config exists to guarantee, and it would also
silently change owner predicates and cancellation/settlement state sharing. The
task forbids that. A per-entry split is therefore a weakening, not a bound.

## Output-preserving levers already exhausted
- threads: ROLLDOWN/RAYON/TOKIO workers = 1 (BOUNDED_COMPILER_ENV)
- allocator: MIMALLOC_ALLOW_THP=0, reviewed allocator slot (job598): no effect
- native compaction addon (job608): built, loaded, still killed at link stage
- lazyBarrel: prunes only unused reexports in declared side-effect-free barrels
- minify: off for config15; sourcemap: OUTPUT_SOURCE_MAPS env-gated, override refused
- dts: OPENCLAW_RUN_NODE_SKIP_DTS_BUILD=1 for the unified stage
Lowering UNIFIED_GRAPH_THRASH_LIMIT_BYTES does not reduce the link stage's real
working set, so it would only turn the refusal into the same kill.

## Conclusion
Within one 2 GiB / 1 CPU offload lease, the full singleton graph cannot finish
link_stage. No source change that keeps the graph whole and its output identical
fits the budget. The remaining options are budget decisions, not source fixes:
(a) one reviewed offload lease above 2 GiB (e.g. 4 GiB, 1 CPU) for the single
unified stage only; or (b) an approved build host with that capacity. Both
belong to S (offload policy: "larger requests are refused"). No relaunch of an
unchanged export until one of these is approved.
