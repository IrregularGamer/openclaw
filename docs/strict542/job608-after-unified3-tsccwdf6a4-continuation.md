# Job608 continuation after unified-3 tsccwdf6a4 — 595 MUST NOT APPLY

Supersedes only the "NEXT FRESH WORKER" pointer of
job608-after-compiler-tsccwdf6a4-continuation.md; all its gates still apply.
Accepted so far: checks d9a3822e, native57742314, runtime5824b14b,
unified-0 ffc14e61, compiler dd34e5e4, unified-1 8d229ccb, unified-2 16819bd2.
Unified-3 actual rc0 evidence in job608-unified-3-tsccwdf6a4/; its independent
acceptance is recorded separately (see job608-unified-3-tsccwdf6a4-independent-acceptance.md
if present; if absent, obtain it BEFORE counting unified-3, never relaunch it).

## NEXT FRESH WORKER: FIRST heavy action unified-4
Exact stage P/stage-unified-4-tsccwdf6a4, manifest = preflight
job608-unified1-5-tsccwdf6a4-preflight.json stages[3].manifest_sha256.
Same five live gates as the compiler continuation (health up/no competing run;
root free >=1GB; storage608 check --stage unified-4 exit0; verify-inputs0, sh -n0,
exact manifest, result/log/rc absent; >=2655s left after preflight). Then ONCE:

```sh
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-unified-4-tsccwdf6a4
offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-4 -- timeout -k 15s 2400s sh run608.sh > ../unified-4-tsccwdf6a4-offload.log 2>&1
printf '%s\n' "$?" > ../unified-4-tsccwdf6a4-offload.rc
```

Each group so far took ~11 min wall time, so unified-5 may follow in the SAME
worker only if a fresh deadline check after unified-4 still shows >=2655s.
Capture evidence like job608-unified-3-tsccwdf6a4/ (storage608.py result
--stage S --result DIR; no --root), then independent acceptance per group.
Do not `git pull` source552 inside a worker: a full fetch is ~339k objects on
a 99%-full root and leaves tmp_pack_* files. Pre-existing tmp_pack_* in
.git/objects/pack (from Oct25-29, not this worker's) await owner cleanup; this
worker removed only its own aborted 201MB tmp_pack_Gk7Sbd.
After unified-4/5 are accepted: middle, sdk0/1, tail, package, then the final
artifact/old-new inventory, action/privilege/seal/reseal and automatic queue
reviews and the genuine ordered HQ595 handoff remain open. 595 MUST NOT APPLY.
