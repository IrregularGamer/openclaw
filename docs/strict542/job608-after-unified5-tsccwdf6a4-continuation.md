# Job608 continuation after all six unified groups — 595 MUST NOT APPLY

Supersedes only the "NEXT" pointer of job608-after-unified3-tsccwdf6a4-continuation.md
and job608-unified5r1-tsccwdf6a4-continuation.md; every gate in
job608-after-compiler-tsccwdf6a4-continuation.md still applies.
Accepted: checks d9a3822e, native 57742314, runtime 5824b14b, unified-0 ffc14e61,
compiler dd34e5e4, unified-1 8d229ccb, unified-2 16819bd2, unified-3 6cfa1e2d,
unified-4 5b2d123a (re-accept after build.log fix 5e70391f), unified-5 c7e554ab
(retry 5r1 evidence 78e9a6f7; first launch exit75 lease-revoked, 4191978f).
Accepted unified-5 receipt 0dc9bea0102a4d80e4a491d1a7baecd19a71c207e273491fd308e469a53a9e34,
checkpoint 2b480ad8... in P/stage-unified-5r1-tsccwdf6a4/result608-unified-5 (not the spent
stage-unified-5-tsccwdf6a4, which has no result).

## NEXT: prepare + independently review the middle stage (source-only, no launch)
Build the middle stage export from the frozen source f6a4de2e with the accepted
native/runtime/unified-0..5 checkpoints (note the 5r1 path above), using the same
storage608/stage608 tooling and finite caps; commit its manifest and get an independent
preflight review. Run it ONCE as the FIRST heavy action of a fresh worker with >=2655s,
same live gates as before. Then sdk0/1, tail, package; then the final artifact/old-new
inventory, action/privilege/seal/reseal and automatic queue reviews and the genuine
ordered HQ595 handoff. Do not `git pull` source552 inside a worker. 595 MUST NOT APPLY.
