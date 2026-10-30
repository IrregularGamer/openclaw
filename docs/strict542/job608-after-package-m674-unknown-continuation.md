# Job608 continuation after package m674 completion_unknown — 595 MUST NOT APPLY

Supersedes the NEXT pointer of job608-after-package-moderefusal-continuation.md. All earlier gates, caps, reviews apply.

## What happened (2026-10-30)
- Decision661 deletions gave room; package m674 prepared (manifest 352ae639, runner b04abd4d, helper a558db9a),
  gates 0 (storage608 check --stage package rc0, free 4362960896), preflight independent APPROVE 0a30b8b7
  (first REJECT e12d8ed1: log/rc pointed at tail-m674 files; fixed 3f2790f8).
- ONE launch ~03:56Z: `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-package --
  timeout -k 15s 2400s sh run608.sh`. Client exited 75 at 04:00:07Z: `offload_status completion_unknown,
  retry_requires_reconciliation true` (ssh rc 255 after `STEP608 builder-start`). Evidence: job608-package-m674/.
- No result608-package was pulled (client pulls only on rc0); runs.log has no entry for this slug. Nothing accepted.
- The stage is SPENT. Its offload slug must not be reused (a killed run returns exit75 on the same slug).

## NEXT (fresh worker, FIRST heavy action, >=2655s left)
1. Reconcile: `offload status` up and no competing remote run; confirm runs.log still has no stage-package-m674 entry
   and P/stage-package-m674 has no result608-package. Record in NOTES. Do not touch the remote by hand.
2. Precedent unified-5r1: `cp -al P/stage-package-m674 P/stage-package-m674b` (same manifest 352ae639, new slug), or re-prepare under a NEW tag (e.g. `--dest P/stage-package-m674b`, same --base/--commit 674840b6/--stage package
   and the same four --input results). Storage: if the free reserve refuses, the spent P/stage-package-m674 export may
   be trashed (its manifest and evidence are committed here; check its inodes are singly linked first, Decision661
   lesson). Never lower FREE_RESERVE or the package cap.
3. Gates, preflight json with log/rc = P/package-m674b-offload.{log,rc}, independent preflight APPROVE,
   ONE launch with identical caps (bg Bash timeout >= 2800s), evidence, independent acceptance (incl. checkpoint
   `tar -tvzf` zero group/other-writable). If completion_unknown repeats, get the remote cause (ssh drop vs.
   remote OOM/kill at builder-start) from the friend VPS operator path before a third launch; do not loop.
4. Then: final artifact receipt + old/new hash inventory, action/privilege/seal/reseal reviews, automatic queue
   review, genuine ordered HQ595 handoff. 587 fd3/socket transport replaces 586 sudo; never add the 586 rule.
