# Job608: unified-0 declaration step exceeds the admitted offload ceiling

SOURCE/EVIDENCE RECORD ONLY; **595 MUST NOT APPLY.** Rook, 2026-10-29 UTC, at
source head 366088ee. Nothing new ran: no offload, build, install, seal, root,
unit, sudoers, service or provider action.

## Basis (already independently accepted, not re-run)

- `job608-single-config-owner-analysis.md`: unified-0 is one canonical config
  (`openclaw-dts-base`, emit root `src/index.ts`). It cannot be split further
  without dropping imports, ambient roots or checks, and that is not allowed.
- `job608-native-api-a39a-independent-outcome-review.md` (daadb5f1). This is the
  largest admitted lease, 4 GiB and 1 CPU. Peak memory was 4287950848 B against
  the 4294967296 B cap. CPU time was 577 s system against 278 s user, with 356 s
  throttled. Memory and CPU pressure both grew. First global diagnostics, which
  force full semantic checking in the pinned `session.go`, did not return
  within the 900 s compiler bound. The kernel-dominated CPU time while memory
  sat at the cap is consistent with reclaim thrash, not a bounded compute cost.
- The previous rounds did not establish any further split, bound or cache fix
  that keeps every check. A CPU profile (adapter 366088ee) would only add
  evidence. The reviewer asked for no more evidence-only rounds.

## Decision needed (S): resource authority only, no check is waived

Choose one:

1. Approve ONE admitted offload lease above the current ceiling for exactly
   the unified-0 declaration stage (proposed 8 GiB, 2 CPU, timeout <= 3000 s, from a
   committed secretless export). All other stages, checks, the floor and the
   seal and privilege gates stay unchanged.
2. Commission a separate product-source job to change the declaration
   emitter, for example an isolated per-file declaration emit. This changes
   the owning build and needs its own freeze and review. It is outside job608's
   preparation scope.

Until then the build receipt, old and new package hashes, the IPC refusal and
cancellation tests on the real artifact, the action, privilege and seal
reviews, the automatic queue review and the final ordered 595 handoff cannot
be produced. The handoff requirements in `job608-final-HQ-HANDOFF.md`
(fresh post-restart owner binding and acknowledgements, backups, rollback,
reseal, natural-gap procedure) remain binding and unchanged.
