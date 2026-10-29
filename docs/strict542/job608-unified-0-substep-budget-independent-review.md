# job608 unified-0 substep budget candidate — independent review

SOURCE ONLY; review only; nothing launched or installed. **595 MUST NOT APPLY.**

Reviewed: dd881aba (`docs/strict542/run-stage608.sh` +15/-2, candidate doc),
against job608-after-singlethreaded-continuation.md step 2 and
job608-unified-0-1bed-outcome.md. Reviewer did not write the change.

## Verdict: APPROVE

## Requirement (step 2)
- Per-substep markers: `STEP608 <stage>-{stage-native-start, restore-build-done,
  build-start budget=Ns, build-fail <rc>, build-done} +Ns` in the
  runtime/unified-[0-5]/middle/sdk-[0-1]/tail branch. pnpm exec + identity eval
  time is visible as the gap between restore-build-done and build-start. Met.
- Inner timeout shorter than outer: `timeout -k 15s ${BUILD_LEFT608}s` with
  BUILD_LEFT608 = 2280 - (now - START608). The build is TERMed by +2280 s and
  KILLed by +2295 s, leaving >=105 s before the outer 2400 s for the
  progress grep, `tail -80 build.log` (stdout) and the EXIT trap, which writes
  exit-code.txt as its first action (before any rmtree). Met.

## Nothing weakened
- Diff touches only the build-stage branch plus two lines at entry. No check,
  receipt, archive-build, STAGES map (stage608.py untouched), memory floor,
  mem/cpu budget or outer `timeout -k 15s 2400s` changes. Exit status is
  preserved (`status=$?; ... exit "$status"`); timeout gives 124 (137 if the
  -k KILL is needed). The refuse path (<=60 s left) exits 124, i.e. it fails
  closed, never skips the build.
- Budget is a literal constant (2280) minus measured elapsed; no env var,
  argument or manifest field feeds it. Not caller-selected.
- Passing outputs unchanged: build.log still receives the same redirected
  stdout/stderr; markers go to script stdout only (offload local log), not to
  build.log, receipt or result tree. `env -i` still clears the build env;
  `timeout` only wraps it.

## set -eu / shell correctness
- `sh -n docs/strict542/run-stage608.sh`: OK (dash).
- `step608` is defined before `STAGE=` but first called only inside the
  build branch of `case "$STAGE"`, so `$STAGE` is always set (no `-u` abort).
- `$(( 2280 - ($(date +%s) - START608) ))` is valid POSIX arithmetic; negative
  results are handled by `[ ... -gt 60 ] || { ...; exit 124; }` (the `[` failure
  is on the left of `||`, so `-e` does not fire).
- Failure branch: `grep ... | tail -40` returns tail's status, so a grep with no
  match does not abort under `-e` before the full tail and `exit "$status"`.

## Local behavioural test (plain sh/dash, fake build, no npm/offload)
Extracted the exact step608/budget/timeout/`|| {}` pattern into a temp script
under /home/deploy/agentq/tmp with a fake build (prints `[build-all]`/`tsdown dts`
lines, then a grandchild `sleep`) and a tiny budget; EXIT trap writes exit-code.txt:
- timeout (budget 2 s, sleep 5): `build-fail 124` marker, filtered progress
  lines and build.log tail on stdout, rc 124, exit-code.txt 124; the grandchild
  sleep was gone afterwards (timeout signals its process group).
- pass: `build-start`, `build-done`, `unified-0-pass`, rc 0, exit-code.txt 0.
- budget exhausted: `build-budget-exhausted`, rc 124, exit-code.txt 124.
- non-timeout failure with no grep match: rc 3 preserved, tail printed.
Temp files removed.

## Notes (non-blocking)
- The candidate's caveat about orphaned grandchildren is conservative: GNU
  (and uutils) `timeout` without `--foreground` signals the whole process group,
  so only children that call setsid escape it; the outer timeout/cgroup remains
  the backstop.
- Measured from START608 (a few ms after the outer timeout starts); the drift
  is negligible against the 105 s margin.
- Applying this needs a NEW freeze; the a46c unified-0 export stays UNUSED, and
  checks/native/runtime re-run at the new freeze per the unchanged STAGES map.
  If unified-0 still times out, step 3 (split by config subset) applies.

SOURCE ONLY; 595 MUST NOT APPLY.
