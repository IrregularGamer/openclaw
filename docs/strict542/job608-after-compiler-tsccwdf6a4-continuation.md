# Job608 continuation after accepted compiler tsccwdf6a4 — 595 MUST NOT APPLY

Supersedes the NEXT sections of job608-unified-0-tsccwdf6a4-launch.md and
job608-compiler-tsccwdf6a4-launch.md. This is ongoing executable build preparation,
not installation authority, a wait for HQ/another job, or a queue-counter repair.

## Completed, SPENT: never replay
Frozen source f6a4de2ebc6924d16fe559f9858bf8c50dce1eba; common export
e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145.

- checks ACCEPTd9a3822e; native ACCEPT57742314; runtime ACCEPT5824b14b.
- unified-0 actual client/result0, +422s/pass, 647069-byte complete result;
  evidencec362cd3a+d597e6eb, independent ACCEPTffc14e61.
- compiler actual client/result0, five real Node invocations10/10 tests, zero
  fail/cancel/skip/todo, complete26748-byte result; evidence5212bbb0+ad057e66,
  independent ACCEPTdd34e5e4. Each invocation's complete membership was checked.
- Complete888-path source inventory9a2f9994 independently approvedad775c34.
  This does not substitute for the final artifact/installed-target inventory.

P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private.
The exact producing manifests, small committed results and complete SHA256 lists
are in docs/strict542/job608-{unified-0,compiler}-tsccwdf6a4/.
Raw logs may be ignored by Git: use explicit tracking or deterministic gzip;
retain exact original bytes (including phase-trace trailing blank line).

## NEXT FRESH WORKER: FIRST heavy action unified-1
Five successor exports prepared37784051, independent batch preflight
APPROVE40bd39fae248e5ac80f90960d97a996a053fd103. They are UNUSED, no result/log/rc.
Exact full manifest pins and shared source/native/runtime inputs are in
job608-unified1-5-tsccwdf6a4-preflight.json. All five preparation/input/syntax
checks exit0; compiler acceptance now satisfies the preflight's previously
pending compiler gate. Do not refreeze for these evidence/review commits.

Unified-1 exact manifest:
41793290b24ca68cd61e2bf3027e14951a44efd2e84d0be8677d1a104146b75b.
Live prelaunch gates, checked again in the fresh worker:
1. health up; remote watchdog healthy; no competing remote run.
2. `df -B1 /`: >=1GB available (Decision655). If below, preserve df output and
   end BLOCKED as directed; never delete another job's exports or change budgets.
3. From source552: `python3 -I -B docs/strict542/storage608.py check --root /srv/encrypted/dev-move-98/agentq-source608-20261028-private --stage unified-1` exits0.
4. From exact stage directory: `python3 -I -B stage608.py verify-inputs`,
   `sh -n run608.sh` exit0; manifest SHA256 exactly above. Confirm exact
   result608-unified-1, sibling unified-1-tsccwdf6a4-offload.log and .rc absent.
5. `offload deadline`: >=2655s left AFTER preflight. This worker had1672s left;
   no2460s run was attempted/refused. Use the fresh worker, never a detached run.

Then launch ONCE:

```sh
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-unified-1-tsccwdf6a4
offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-1 -- timeout -k 15s 2400s sh run608.sh > ../unified-1-tsccwdf6a4-offload.log 2>&1
printf '%s\n' "$?" > ../unified-1-tsccwdf6a4-offload.rc
```

Mark the stage spent in launch/evidence records (immutable manifest remains
prelaunch UNUSED). Capture actual rc/log, storage-return0, full inventory,
exact receipt/source/common/run/manifest/input/output and owned group checkpoint,
commit/push evidence, then independent acceptance. No acceptance without actual
complete returned evidence; unknown completion must be reconciled, not replayed.

Next2..5 use their already-reviewed exact exports sequentially, fresh same live
gates and independent acceptance of each actual run; full commands in the batch
preflight. Do not replay accepted stages, relabel receipts, reduce checks/floors,
force owner identity, or edit DB/status/counters. After all6 unified groups are
accepted, prepare/review/run middle with accepted native/runtime/unified0..5;
then sdk0/1, tail, package. Keep all original gates and finite offload budgets.

## Final application remains gated
Need actual deterministic package/artifact receipt, exact old/new installed-target
inventory, independent source/action/privilege/whole-original-seal/next-seal and
ACTUAL automatic queue reviews, then reconciled ordered HQ595 handoff.
The detailed original seal, backup, rollback, natural settled-gap foreground
nonqueue HQ procedure and fresh post-restart owner/accepted-run acknowledgements
remain mandatory; historical installer pins are not current application commands.
587 fd3/socket transport replaces586 request-time sudo; native-owner-read.patch
is unapplied history. Keep575/588/592 by reference and553 sole SAME510 continuation.
No installed/sealed/root/unit/sudo/service/gateway/scheduler/provider/auth/config
or production changes were made. 595 MUST NOT APPLY.
