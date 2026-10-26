# Job605 root-cause independent review

Reviewed commit: `d0952609c22bbbf36bb19fe0d54288e4a7566b7c` (branch strict542-source552).
Scope: EVIDENCE/SOURCE ONLY. This does not approve any build, artifact, application, or install.

## Verdict: CHANGES (documentation only; the code change is acceptable as-is)

The conclusion is supported: config15 stalls in memory.high reclaim and is not CPU-starved.
Several numbers in `job605-config15-root-cause.md` come from the wrong run or are described
wrongly. Fix the doc before anyone relies on it.

## Checks run

- `git show d0952609`: four files (policy +8, probe +1 call, test +5, new root-cause doc).
- Parsed the six config-15 `ISOLATED_CONFIG_DIAGNOSTIC` lines in
  `runs/598/isolated-corrected-final/result598-isolated/probe.log` with `python3 -I`
  (log lines 355-357, 373, 379, 381).
- Parsed `docs/strict542/job598-native1-ancestor-pressure.json` ancestors.
- Read `isolated-corrected-final/.../isolated-probe598.json` capacity, the tail of
  `allocator-reconciliation/result598-isolated/probe.log`, and `allocator-reconciled-run.log`.
- `node --test docs/strict542/serial-probe598.test.mjs docs/strict542/isolated-config598.test.mjs`:
  14/14 pass. No build, offload, install, service, or sudo action was run.

## Evidence confirmed

- Per-sample rss / heapUsed / memory.current / d user / d system match the table within rounding
  (sample 1 d system is 9.3 s, the doc says 10). Final leaf cpu.stat: user 130.9 s, system 859.3 s,
  nr_throttled 9463/10391. These match.
- Over the config15 window itself (begin to last sample): user +37.7 s, system +785.4 s.
  About 95% of CPU time is system, so the reclaim-thrash conclusion holds.
- Ancestor `offload-work.slice`: memory.high=1610612736, memory.current=1610919936, high events
  2387469, memory.max=2147483648. The leaf scope has memory.high=max. These match.
- Config0 begin: memory.current 1051 MiB, rss 178 MiB, so about 873 MiB was not RSS (the doc
  says about 880). Config15 leaf memory.peak is 1625784320, which is above the parent high.
- The 869346 ms timeout appears in `allocator-reconciled-run.log` line 55. The
  isolated-corrected-final run timed out at 868110 ms.

## Discrepancies

1. **limitBytes is attributed to the wrong run.** The config15 timeout run
   (isolated-corrected-final) recorded `limitBytes=1507000320`. The value `1549328384` comes
   from the reconciled-final serial probe (`reconciled-final/result598-probe`, receipt
   `job598-reconciled-probe-receipt.json`). The threshold still refuses 1507000320, but the doc
   should state both values and their sources.
2. **The allocator-reconciliation evidence does not show a limit.**
   `allocator-reconciliation/result598-isolated/probe.log` (133 lines) ends in pnpm install
   progress. It has no config15 lines and no limitBytes. The 869346 ms timeout appears only in
   `runs/598/allocator-reconciled-run.log`, which also has no limitBytes.
3. **The samples are not 30 s apart.** About 15 "still running" lines (about 7-8 minutes) fall
   between samples 2 and 3, and the gaps between the later samples are uneven. Sample 3's
   +523 s system time covers that long window, not 30 s.
4. **Final cpu.stat is cumulative for the leaf cgroup** (config15 begin already shows user 93 s,
   system 74 s). It is not config15-only. The ratio over the config15 window (above) is the
   correct support.
5. **The ancestor-pressure JSON is a separate native1 snapshot** (pid 2584919). It is not the
   same moment as the config15 samples. That is fine as evidence of the slice configuration,
   but the doc should say so.

## Code review

- Nothing is weakened. `admitProbe`, `probeSucceeded`, the env refusals, the allocator and pool
  policy, and the existing tests are unchanged. The new check is an extra fail-closed refusal
  that runs before `admitProbe`. NaN or undefined limits are refused.
- Build output is unchanged. tsdown config, entries, minify, treeshake, and chunking are not
  touched, and config15 is not split. There is no caller-controlled input: the threshold is a
  module constant and the probe still rejects argv and env controls.
- Threshold soundness: this is a known-bad floor, not a known-good bound. A limit only slightly
  above 1549328384 would be admitted and would probably still thrash. The config15 leaf peak was
  1625784320 and the parent high was 1610612736. Treat passing this check as "not known-bad",
  never as evidence that there is enough capacity. A tighter bound based on the observed peak
  working set (about 1.63 GB plus headroom) would be more defensible. This is a note, not a
  blocker.
- Scope note: the refusal happens at admission, so it stops the whole isolated probe,
  including configs 0-14 diagnostics, not only the unified graph. The error text says
  "unified graph refused". Consider saying "probe refused" to avoid confusion.

## Required to move to APPROVE

Correct discrepancies 1-5 in `job605-config15-root-cause.md`. No code change is required.
