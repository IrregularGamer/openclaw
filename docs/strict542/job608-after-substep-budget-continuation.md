# job608 continuation after unified-0 substep-budget correction

SOURCE ONLY; preparation incomplete; **595 MUST NOT APPLY.** Supersedes only the
freeze choice (a46cd576) of job608-after-singlethreaded-continuation.md; every
other gate, procedure, floor, budget and historical receipt stays as written.

## State at 2026-10-29T02:25Z
- At a46cd576: checks ACCEPT f73bc268, native ACCEPT 35dbdbf6, runtime rc0
  receipt 837374b9 (c21c5d59) ACCEPT 7c9a647e. build-all 15m 22.5s on 1 CPU.
- a46c unified-0 export `stage-unified-0-singlethreaded-a46c` (manifest
  23ac58b5…, verify-inputs 0) prepared but NOT launched: a46c's runner lacked
  the required substep markers / inner build timeout. Superseded; do not launch.
- Correction dd881aba (run-stage608.sh only), independent APPROVE a39ad5ee.

## Next (each launch FIRST in a fresh worker, 2460/2400 s + 195 s settle)
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
