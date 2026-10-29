# job608 continuation after unified-0 substep-budget correction

SOURCE ONLY; preparation incomplete; **595 MUST NOT APPLY.** Supersedes only the
freeze choice (a46cd576) of job608-after-singlethreaded-continuation.md; every
other gate, procedure, floor, budget and historical receipt stays as written.

## Current continuation at 2026-10-29

Executable freeze remains `a39ad5ee95609193502850d0dbb87b5dcbb5e3e3`, common
export `d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62`.
New evidence/review commits do not select a new executable freeze.

- Checks ACCEPT `2e19dbd1`, native ACCEPT `4f54ce46`, runtime ACCEPT `9f5d4331`.
  All three producing exports are SPENT/SUCCESS. Do not replay them or relabel
  older receipts. Runtime receipt is `eb4488f2`, checkpoint `85f3d1e3`;
  runtime build-all took 15m 16s, client/result both 0.
- The NEW `stage-unified-0-substep-a39a` export is UNUSED, manifest
  `900edc324f8e2068521a9d4fc19b0c80d0fbca91cfa01ba5c618d2528fb0b4fd`.
  It carries exactly the accepted native and runtime outputs. Its launch is
  gated on the exact preflight and independent review in
  `job608-unified-0-substep-a39a-preflight.md` and its adjacent review.
- Next worker: as its FIRST heavy step, read those two files, require live
  `offload deadline` >= 2655 s, verify inputs, and execute their ONE bounded
  launch block. The current worker has insufficient time for that launch.
  The older `stage-unified-0-singlethreaded-a46c` remains superseded; never launch it.
- After actual successful unified-0 acceptance, the complete remaining graph
  is compiler, unified-1 through unified-5, middle, sdk-0, sdk-1, tail, package.
  Each needs a new export at the SAME freeze/common identity, the exact
  predecessor receipts required by `stage608.py:STAGES`, preflight/review,
  admitted bounded execution and independent result acceptance. These are
  unrun at a39a; the successful runtime emissions do not replace declarations
  or the compiler's separate suites. No partial output promotion is allowed.

Then reconcile the actual complete package/tree/source inventory, baseline and
whole original/next seal; prepare the exact old/new action and obtain independent
source/artifact, action, privilege-policy and seal reviews, followed by the
ACTUAL automatic queue review. The candidate95 command pins in
`job608-final-HQ-HANDOFF.md` are historical, blocked templates and must be
reconciled to the successful freeze before any final review or application.
The ordered genuine nonqueue HQ/natural-gap, fresh post-restart owner AND
accepted-run acknowledgement, backup, rollback and reseal gates there remain.
No complete package/action/seal or application authority exists yet.

## Historical state at 2026-10-29T02:25Z
- At a46cd576: checks ACCEPT f73bc268, native ACCEPT 35dbdbf6, runtime rc0
  receipt 837374b9 (c21c5d59) ACCEPT 7c9a647e. build-all 15m 22.5s on 1 CPU.
- a46c unified-0 export `stage-unified-0-singlethreaded-a46c` (manifest
  23ac58b5…, verify-inputs 0) prepared but NOT launched: a46c's runner lacked
  the required substep markers / inner build timeout. Superseded; do not launch.
- Correction dd881aba (run-stage608.sh only), independent APPROVE a39ad5ee.

## Historical next-step plan (superseded by the current continuation above)
1. New freeze = a39ad5ee (contains dd881aba + its approval).
2. With the committed preparer (sha256 1e701de0…, unchanged) prepare NEW
   `-substep-a39a` exports for checks, then native, then runtime, then
   unified-0, each with its own preflight + independent review, exactly the
   a46c pattern (preflight docs job608-*-singlethreaded-a46c-preflight.md).
   Native/runtime are expected to reproduce (native addon 0b6607e7).
3. unified-0 (measured config-15) now prints `STEP608 unified-0-* +Ns` markers
   and, on an inner timeout, the build-all/tsdown/dts progress and build.log
   tail. If it still exceeds the budget, split by config subset in stage608.py
   (reviewed), never by lowering the floor or dropping checks.
4. Then package, deterministic receipt, old/new hashes, IPC refusal and
   cancellation suites, action/privilege/seal reviews, automatic queue review,
   and the ordered 595 HQ handoff (unchanged requirements).
