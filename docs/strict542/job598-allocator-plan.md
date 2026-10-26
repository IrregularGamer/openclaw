# Fixed allocator diagnostic successor (source only)

Actual source8ce523c0 is still running unchanged. Its complete outcome must settle
and receive independent review before a successor may run. The186-test checkpoint
and independent94275bea review do not approve a compiler/build/application.

Read-only process and ancestor samples are committed adjacent as
job598-native1-thread-sample.json, pressure.json and ancestor-pressure.json.
Observed: one runnable Rolldown worker, fourteen total threads, about1.4GiB RSS,
no swap, no leaf high/max/OOM events. However the existing parent offload-work.slice
has memory.high1610612736 and memory.max2147483648; its high counter is2387469.
The leaf memory.stat shows anon1526468608, anon_thp1231028224, file925696,
pgscan_direct7476097, workingset_refault_file4319174. Process read_bytes is about
9.0GiB and major faults75110. This is evidence of reclaim/refault pressure below
the leaf max. It does not establish that THP alone causes the compiler timeout.
The aggregate high counter is cumulative, not a per-run delta or OOM count.

Existing supported option preflight:
- Pinned [Rolldown1.2.9 allocator source](https://raw.githubusercontent.com/rolldown/rolldown/v1.2.9/crates/rolldown_binding/src/lib.rs)
  uses mimalloc-safe; its [Cargo configuration](https://raw.githubusercontent.com/rolldown/rolldown/v1.2.9/crates/rolldown_binding/Cargo.toml)
  enables v3 on Linux x64. The [exact lock](https://raw.githubusercontent.com/rolldown/rolldown/v1.2.9/Cargo.lock)
  pins mimalloc-safe0.1.66/libmimalloc-sys2 0.1.62.
- [Maintained allocator documentation](https://github.com/microsoft/mimalloc#environment-options)
  supports MIMALLOC_ALLOW_THP=0 to disable process transparent huge pages and
  identifies THP as a possible RSS increase. This reuses an upstream option;
  no native dependency patch, preload, package upgrade or custom allocator.

Source successor refuses every inherited MIMALLOC_ control (case insensitive,
even empty/matching values), then generates only fixed MIMALLOC_ALLOW_THP=0.
Review correction: dynamically import the tsdown build owner only after admission
and parent policy assignment, so its transitive native imports cannot initialize
earlier. Parent config evaluation and every compiler child receive it before importing
Rolldown; each invocation asserts exact propagation. Receipt/markers record it,
and child telemetry adds memory.stat/pressure. Fixed native pools1, full ordered
whole-config census, graph identity, computed heap, total900s deadline, original
normal build4352MiB guard and every cancellation/settlement owner stay unchanged.
No cgroup, host THP, service, lease or runtime settings are changed. This does not
raise/bypass the ancestor1.5GiB high or leaf2GiB maximum. Hypothesis: less THP RSS
may leave room for executable/file pages and avoid reclaim; empirical result
remains unknown until a normally admitted fresh committed secretless export runs.

Thirteen lightweight selector/policy tests pass locally, including inherited
allocator-control refusals and generated policy/caller preservation. Independent
exact source review is required. If the current run succeeds, reconsider whether
another diagnostic satisfies an outstanding proof obligation before running it.
Any later success remains diagnostic only: complete owning build/profile,
declarations, postbuild, package, deterministic tree/action/privilege/seal review,
automatic598 review and fresh genuine post-restart HQ acknowledgements remain.
