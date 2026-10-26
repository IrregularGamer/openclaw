# Job605: config15 stall root cause (source analysis of committed job598 evidence)

SOURCE ONLY. No build, artifact, action, privilege or application success is claimed.

## Finding: memory.high reclaim thrash, not CPU starvation

Config15 is the original unified runtime graph (`tsdown.config.ts`, the
`TSDOWN_UNIFIED_CONFIG_GROUP` entry that builds core, plugin-sdk, bundled plugins and
hooks in one graph so runtime singletons are emitted once). It has `dts:false`, so the
stall is Rolldown JS bundling only.

Evidence, `runs/598/isolated-corrected-final/result598-isolated/probe.log`
(config-15 `ISOLATED_CONFIG_DIAGNOSTIC` samples, 30 s apart):

| sample | rss MiB | V8 heapUsed MiB | cgroup current MiB | d user s | d system s |
|---|---|---|---|---|---|
| 1 | 1353 | 36 | 1535 | 21 | 10 |
| 2 | 1362 | 28 | 1521 | 2 | 33 |
| 3 | 1446 | 35 | 1542 | 10 | 523 |
| 4 | 1449 | 26 | 1543 | 3 | 175 |
| 5 | 1443 | 23 | 1535 | 1 | 45 |

Final cpu.stat for the leaf: user 131 s, system 859 s, nr_throttled 9463/10391.
`job598-native1-ancestor-pressure.json` shows the parent
`offload-work.slice` with `memory.high=1610612736` (1.5 GiB) under the leaf's 2 GiB
`memory.max`, `memory.current=1610919936` (at high), and a high counter of 2387469. The owner's
capacity reader reports `limitBytes=1549328384`.

So after the first ~minute, config15 spends ~95% of its CPU time in kernel reclaim
(memory.high throttling) and ~1-5% compiling. RSS is native Rolldown memory (V8 heap stays
under 110 MiB). The other ~880 MiB charged at config0 begin is reclaimed before the stall,
so freeing page cache would not help. The compiler alone fills the 1.5 GiB effective
ceiling and then refaults its own text/file pages. That is why the earlier remedies did not
work: the one-CPU pool (pool=1) did not help, and THP-off allocator source 6305e30c
timed out the same way at 869346 ms. The job598 builder suspected CPU. This evidence
shows memory-ceiling thrash.

## What is ruled out (would weaken or alter reviewed output)

- Splitting config15: this breaks the emit-singletons-once invariant the graph exists for.
- Turning off minify or treeshake, or changing entries or chunking: the reviewed artifact
  hashes would change.
- Raising the deadline: user-CPU progress is about 1% of wall time, so the run is not
  making bounded progress.
- Lowering checks, or caller-selected pools or allocators (the admission policy refuses these).

## Source correction (this job)

`serial-probe598-policy.mjs` `admitUnifiedGraphCapacity` refuses the probe up front
when the observed limit is at or below `UNIFIED_GRAPH_THRASH_LIMIT_BYTES=1549328384`.
Before this, each attempt burned about 14.5 minutes. Now it fails immediately with an
honest refusal. Wired into `isolated-probe598.mts`. Tests: `serial-probe598.test.mjs`
(new case) plus `isolated-config598.test.mjs`, 14/14 pass locally (small node --test only).

## Remaining requirement (capacity, not code)

The deterministic full build/package receipt needs one offload slot whose effective
ancestor `memory.high` is above the leaf's working set. Today the offload advertises a
2 GiB leaf but caps the parent at 1.5 GiB, and offload refuses larger requests. That
ceiling belongs to the friend-VPS placement (`offload-work.slice`), not to this source.
This job does not change units or cgroups. Until the ceiling is raised, the admitted
build/package step, the receipt, the action/privilege/seal reviews and the job595 HQ handoff
cannot be truthfully completed. The handoff must not be written as if the build succeeded.
