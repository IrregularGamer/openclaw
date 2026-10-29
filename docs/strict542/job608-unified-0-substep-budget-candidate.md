# job608 unified-0 substep markers + inner build budget (CANDIDATE)

SOURCE ONLY; candidate pending independent review; nothing launched;
**595 MUST NOT APPLY.**

Why: job608-after-singlethreaded-continuation.md step 2 requires unified-0 to
"carry per-substep STEP608 markers and an inner build timeout shorter than the
outer one so a timeout still returns build.log tail". At freeze a46cd576 the
runner `docs/strict542/run-stage608.sh` (export run608.sh eb662d81…) is unchanged
since 1bed, whose unified-0 hit rc 124 with no build tail (job608-unified-0-1bed-outcome.md).
The prepared a46c unified-0 export (`stage-unified-0-singlethreaded-a46c`,
manifest 23ac58b5…, verify-inputs 0, UNUSED) was therefore NOT launched.

Change (run-stage608.sh only, build stages runtime/unified/middle/sdk/tail):
- `START608` at entry; `STEP608 <stage>-<substep> +Ns` markers at
  stage-native start, restore-build done, build start (with budget), build
  fail/done.
- The build command is wrapped in `timeout -k 15s ${BUILD_LEFT608}s`, where
  BUILD_LEFT608 = 2280 - elapsed (fixed constant, not caller-selected); the
  build ends >=120 s before the 2400 s outer limit, so on timeout the failure
  branch prints the [build-all]/tsdown/dts progress lines and the last 80
  build.log lines to stdout (captured in the local offload log), and the EXIT
  trap writes exit-code.txt. Under 60 s left it refuses with rc 124.
- Exit statuses, checks, receipts, stage map, memory floor, mem/cpu budgets
  and the outer `timeout -k 15s 2400s` are unchanged. A passing build is
  byte-identical in outputs (markers go to stdout, not to build.log/receipt).
- Caveat: `timeout` signals its direct child; orphaned build grandchildren are
  ended by the unchanged outer timeout / offload cgroup teardown.

Effect on the chain: run608.sh is taken from the freeze commit, so this needs
a NEW freeze (this commit, after APPROVE). Checks/native/runtime must be
re-run at the new freeze per the unchanged STAGES map (native/runtime are
expected to reproduce: native addon 0b6607e7 was identical across 1bed/a46c).
Superseded UNUSED export: stage-unified-0-singlethreaded-a46c (do not launch).
