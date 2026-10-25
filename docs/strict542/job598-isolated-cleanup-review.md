# Independent exact isolated-slot reconciliation and runner review

Reviewer: Rook `/root/build_analysis`, 2026-10-25 UTC.
Exact runner successor reviewed: `37def2114ea6dd57da2fdbd558e9fbddd97f87c2`.
Read-only supplied evidence: `runs/598/isolated-reconciliation/pre-clean.json`
and `current-worker.json`. Verdict: **APPROVE CONDITIONAL PLAN AND SOURCE ONLY**.
This receipt does not assert that cleanup has occurred or currently remains safe.

The corrected-root command was refused before execution, exit75, by the normal
transfer scanner on `.pnpm-store/v11/index.db`. It ran no compiler. The prior
completed runner cleaned its source/native extraction but left pnpm's disposable
root store. The exact runner diff only adds fixed `.pnpm-store` to its existing
disposable EXIT cleanup; no configurable deletion path, installed code, scanner,
resource, privilege, lease, native-owner or cancellation policy changes.
Independently ran `sh -n docs/strict542/run-isolated598.sh`: PASS.

The exact supported mutation approved is solely:
`ssh offload clean tmp-export598-config-isolation-98c59c32`.
The existing clean handler validates one slug and removes that disposable export.
It does not acquire the runner lock or prove idleness, and ignore_errors means
SSH success alone cannot prove removal. No other slug, cache, shared directory,
installed state, lease record, credential or database content may be modified or
transferred under this approval. Do not inspect or copy index.db contents.

Supplied inventory reports only the known five input files and the root store;
source/native-source/result598 are absent. Store inventory is one23,228,416-byte
file. Remote input hashes match recorded source/native/runner inputs and the
prior successor export. Actual earlier outcome artifacts and local source/input
copies are retained outside this slot. This reviewer relies on prior exact
archive review and supplied current remote hashes, not a fresh large rehash.

The sole live lease SHA matches the inherited current worker's AGENTQ_LEASE_ID;
I independently computed that match without printing or retaining the token.
The current unit matches inherited AGENTQ_UNIT. Supplied observations show zero
managed containers and available runner lock. The local controller's existing
remote_admit/renew lifecycle retains that worker lease after a completed remote
command. A current admission lease is not an active compiler. The previous
zero-live-leases condition is refined for this exact disposable reconciliation:
zero OLD/OTHER live leases, with at most this genuinely current worker lease.
This changes no application/native owner predicate or settlement contract.

Mandatory ordered execution conditions:

1. Preserve local source, known inputs, actual outcome bytes and this bounded
   inventory outside the disposable slot. Keep the same sole worker, with both
   prior offload clients exited and no concurrent offload/rsync/installer command.
2. Acquire the actual existing remote LeaseStore.runner_slot lock nonblocking,
   using its established administrative access. Hold that existing lock through
   the following fresh observations, supported clean and absence verification.
   Do not change its implementation, create another lock or detach its holder.
3. While holding it, freshly verify zero managed running containers, zero old or
   other valid/renewable leases, and at most the sole live lease whose hash still
   matches this active worker. Recheck current unit/lease binding, completed old
   clients, exact nonsymlink slot/known inventory, retained inputs and results.
   A new actor, unknown result, occupied lock, uncertain status, unexpected file,
   lost access or failed check means stop without clean or another run.
4. Execute only the literal supported clean above while retaining the lock.
   Verify the exact slot is absent through read-only jailed inventory; do not
   infer deletion from command status. Record actual result and fresh evidence.
   Release the lock through its ordinary lifecycle after that verification.
5. Export the committed reviewed corrected-root source and updated runner using
   the same slot identity and ordinary secretless transfer. Verify source/delta/
   native/runner manifest bindings; prior runner/successor hashes do not certify
   the new bytes. Only then one normal admitted corrected diagnostic may run,
   under unchanged budget, lease, scanner and finite deadline. Stop on refusal or
   uncertain completion; no slot rotation, bypass or unchanged retry loop.

This approval covers temporary source-test workspace recovery only. It supplies
no native supervisor/application authority, normal build admission, artifact or
release approval. Actual cleanup, corrected diagnostic outcome and all original
job598/595 review, seal and genuine HQ ownership gates remain unproven.

## Exact executable implementation approval

Independently reviewed `docs/strict542/reconcile-isolated-slot598.py` from
`1f4ed0cf`, an ancestor of this receipt. **APPROVE** executing this exact source
once, subject to the mandatory operational preconditions above. This is source
review, not evidence that it was executed or cleanup succeeded.

The script acquires the actual existing LeaseStore.runner_slot context and holds
it across its ready handshake, the local literal supported clean request, and
remote slot-absence verification. It checks exact only-current lease digest and
zero managed containers before and after clean. Its slot and six expected root
items are fixed; slot/store symlinks refuse. Previously verified retained-input,
full store inventory, current-worker binding and exclusion of concurrent clients
remain required preconditions; the script does not replace those observations.
Only the current lease SHA crosses the administrative channel; its token does
not. The root command is fixed Python source executed as offload through existing
administrative access, not a newly installed privileged endpoint.

The remote holder has a120s alarm; local readiness/verification and clean have60s
bounds and child shutdown has finite waits. Loss of the controller, failed
assertion, occupied lock or uncertain verification stops rather than admitting a
compiler. Independent static parsing confirmed both local write and remote
comparison contain the same VERIFY string followed by byte10 (a real newline).
Local and embedded remote Python syntax pass without executing the script. No
mutation, remote service or compiler was launched by this review. Preserve actual
ready/absence receipts; a successful source review alone does not satisfy cleanup.
