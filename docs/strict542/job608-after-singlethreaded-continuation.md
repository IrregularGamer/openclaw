# job608 continuation after singleThreaded emitter candidate

SOURCE ONLY; preparation incomplete; 595 MUST NOT APPLY. Supersedes only the
"Frozen candidate is 95e62f8b" choice in job608-after-native-admission-continuation.md;
every other gate, procedure and historical receipt there stays as written.

## State at 2026-10-29T00:20Z

- API-phase diagnostic of unchanged 1bed: `API.createSnapshot` returned after
  ~104.6 s; config/program diagnostics returned; `Program.getGlobalDiagnostics`
  (forced full semantic pass) was running when the window closed. Evidence only.
- Owning-source correction: 7cbbb99c sets `singleThreaded: true` last in the
  native emitter's virtual compiler options (rationale and upstream source pins
  in job608-native-singlethreaded-candidate.md, fixture RED/GREEN in a97beadd).
  Focused `node --test docs/strict542/native-admission608.test.mjs`: 9/9 PASS
  (re-run 2026-10-29 by this worker). Independent source review:
  job608-native-singlethreaded-independent-review.md.
- No diagnostic, root set, seal, cancellation, memory floor or budget changed.
  Nothing launched, installed or sealed by this worker.

## Next (each step FIRST in a fresh worker, 2460/2400 s + 195 s settle)

1. New freeze = the reviewed commit that contains 7cbbb99c (only if the
   independent review is APPROVE; otherwise fix and re-review first).
2. With the committed preparer, prepare a NEW checks export and a NEW native
   export at that freeze (same procedure/paths pattern as the candidate95
   section, new `-singlethreaded` suffixes), independently review each
   preflight, then launch checks, then native, then runtime, then unified-0
   per the unchanged STAGES map. Unified-0 is the measured config-15 run: it
   must carry per-substep STEP608 markers and an inner build timeout shorter
   than the outer one so a timeout still returns build.log tail.
3. If unified-0 still exceeds 2400 s at 1 CPU, split it by config subset in
   stage608.py (reviewed), never by lowering the floor or dropping checks.
4. Then package, deterministic receipt, old/new hashes, IPC refusal and
   cancellation suites, action/privilege/seal reviews, automatic queue review,
   and the ordered 595 HQ handoff (fresh post-restart owner binding and
   accepted-run acks, backups, rollback, reseal, natural-gap nonqueue HQ).
