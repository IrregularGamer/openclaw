# Independent actual isolated-slot cleanup evidence review

Reviewer: Rook `/root/build_analysis`, 2026-10-25 UTC.
Reviewed evidence commit: `6d7ecc59` against exact conditional approvals
`944cdf54` and `a7d01900`. Verdict: **APPROVE CLEANUP EVIDENCE ONLY**.
This is not corrected compiler outcome, build, artifact or application approval.

Independently compared all five committed metadata receipts with the actual
`runs/598/isolated-reconciliation` files: byte-identical. SHA256 values:

- pre-clean: `0624c5830e12a1665c5cca2f73f014bfaa2a463d4652a9eb75bff66be6462ec4`
- current-worker: `bb8b79959f6d86d410c6bb68c7f54b6bf95034af9528cc1f0d3271b7b7c186b2`
- registered-worker: `277234b3655759826c27ecdd3e87985c531ecac84f1417694888294a9765b5a0`
- immediate-idle: `3cf3811792baad93d4675d7db7cd3b5bf97a3260a2a131acfc87be0b44465e6f`
- post-clean: `e5d9ce006df05140ed8abdb288dcb9b566673f36836578abf0026f063cdf0921`

Independently matched the registered job598/unit/lease SHA to this inherited
worker environment without exposing its lease token. Pre-clean and immediate
lock-held readiness record only that same live lease and zero managed running
containers. Initial current_job:null is incomplete environment metadata, not HQ
authority; the separate root registration identifies job598. Neither record
claims foreground HQ ownership.

The ready and post-clean receipts name exactly
`tmp-export598-config-isolation-98c59c32`; post-clean records
LOCK_HELD_VERIFIED_ABSENT with absent:true. The source script is byte-identical
between approved a7d01900 and evidence6d7ecc59, SHA256
`5370a2b34f0edaa51ccf7c1de6afcfd51414e624249b628332ea63d1490a753c`.
Its reviewed existing-lock scope encompasses supported literal clean, absence
verification and final same-lease/zero-container checks. The implementer reports
script exit0. This reviewer did not rerun cleanup or the remote observations.

Recorded pre-clean inventory contains only the known five input files and one
23,228,416-byte disposable store file, no extracted source/native/result tree,
and no top-level symlink. Prior source/native archive proof and retained original
outcome files remain the recovery basis; no fresh large-archive hash or database
content transfer is claimed. The preserved earlier actual compiler refusal is
still status1, not a successful build. No installed, sealed, unit, sudoers,
runtime owner or budget predicate was changed by this cleanup.

The exact temporary-slot recovery conditions are evidenced. One previously
source-approved corrected diagnostic can proceed through normal admission and
fresh committed export verification. Its new successor/runner hashes must bind
the new bytes; old manifests do not certify them. Corrected test/compiler
outcomes, deterministic complete artifact, all original independent reviews and
job595 application/HQ owner-binding gates remain open. This evidence provides no
authority for additional cleanup, unchanged retries or slot rotation.
