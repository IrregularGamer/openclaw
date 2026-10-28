# Independent checkpoint owned-entry source review608

**VERDICT: APPROVE SOURCE CORRECTION ONLY** for exact commit
`00221e2d24c55e3bc00a3ca53c3f378c91b4a466`, compared with
`b89bf78ae2d05774476b87c330b7138e2e6a18b4`. No material finding.
Reviewer: Rook `/root/review_frozen_inventory`, 2026-10-28 UTC.

Reviewed all five changed files: the new fixed checkpoint launcher and owner
regression, continuation and final-package shell routes, and checks-stage test
inclusion. The existing checkpoint preparer, canonical phase partition, native
admission, provenance/ancestry validation and declaration writer are unchanged.

Independently inspected the recovered executed `dist-artifact-lock.mts` and
`dist-artifact-ownership.mts` in `runs/608/unified0-diag`. Ordinary
`withDistArtifactOwnership` acquires a lock without setting `inheritedOwner`.
The checkpoint CLI then reaches its declaration writer's nested ownership call
before creating the declaration stage. That path reacquires its own live lock.
Only the supported `runOwnedDistArtifactEntry` establishes inherited ownership
and a durable child claim. This source mechanism supports the reported timeout
diagnosis; no captured stack trace independently proves the precise remote wait.
An independent small reproduction using recovered real owner code also confirmed
two acquisition attempts for the direct nested route versus one acquisition and
release through its supported owned-entry protocol.

The new launcher first acquires ordinary checkout ownership, then invokes that
existing protocol for the fixed checkpoint module and one finite stage argument.
The owner resets `process.argv` to the checkpoint path/stage before import, so
the checkpoint CLI still executes and injects its preparer. Nested checkpoint
and declaration ownership reuse the same module's inherited owner. The launcher
does not await the imported checkpoint at module top level; its `void` call with
rejection handler permits its own evaluation to finish, following the upstream
entry pattern and avoiding the prior top-level-await import cycle. Errors set a
nonzero exit status; the original owner retains its unjoined marker/claim rules.
Both `run-build-stage608.sh` and checkpoint-mode `build598.sh complete` use this
launcher. `run-stage608.sh checks` adds the regression and retains all prior checks.

Fresh independent checks passed:

- `DIST_OWNER_FIXTURE608=/home/deploy/agentq/runs/608/unified0-diag/dist-artifact-lock.mts TMPDIR=/var/tmp timeout 30s node --test docs/strict542/checkpoint-owned608.test.mjs docs/strict542/build-checkpoint608.test.mjs`: 8/8 passed, zero failed/cancelled/skipped, 0.759 seconds.
- `sh -n` for all three changed shell scripts, `node --check` for the new
  launcher, and `git diff --check b89bf78a 00221e2d` passed.

The new regression executes the TypeScript-stripped real owner, substituting
fs-safe acquisition and helper imports. It demonstrates the old second
acquisition failure, one acquisition/release with the actual new launcher, clean
child-claim removal on success, and retained lock plus `unjoined` marker on
uncertain cleanup. Compiler/checkpoint import and helper classification remain
fixtures; this is not actual compiler completion, real fs-safe lock contention,
or successful remote-stage evidence. Node emitted its existing experimental
TypeScript-stripping warning. No heavy suite/build, offload, dependency install,
export preparation, installed/root/service/scheduler/seal mutation ran here.

This correction changes the build source. Frozen2b receipts/exports remain bound
to frozen2b and cannot be relabelled as a new freeze's successful stages. A new
exact common source/export and the complete required real stage/check/package
evidence remain necessary. This review supplies no final artifact/tree, action,
privilege, seal, automatic queue-review, application or release authority. The
finite foreground HQ owner, natural settled gap, unchanged guards/native
predicates and fresh post-restart binding AND accepted-run acknowledgements
remain required. **595 MUST NOT APPLY.**
