# Independent job598 disposable-workspace reconciliation review

Reviewer: Rook independent reviewer `/root/reconcile_review`, 2026-10-25 UTC.
Reviewed maintained HEAD before this documentation: `7625e9ff`.

Verdict: **APPROVE PLAN ONLY**, including the exact whole-slot successor below,
with the mandatory preconditions below. This
does not establish that cleanup is currently safe or that any diagnostic passed.
Stop without mutation or another diagnostic if idle/settlement is uncertain.

The exact approved mutation is a forced jailed rsync of an empty local directory
with `--delete` into ONLY
`offload:tmp-export598-serial-probe-fixed-38fd4ee7/source/`, followed by one
standard admitted run of the unchanged reviewed export. No exclude file is
applied to that exact cleanup transfer. Do not add `--delete-excluded` to the
normal transfer, change scanners, create an alternate export, modify installed
code/brokers/seals/units, relax budgets or use local execution.

The existing `/home/deploy/.local/bin/offload` uses `rsync -az --delete` for
source transfer and jailed rsync for artifact retrieval. Both reviewed dispatcher
copies (`runs/432/offload-agent.candidate` and `offload-agent.installed-copy`)
explicitly route `rsync` to `/usr/bin/rrsync` jailed to `/srv/offload/work` before
run admission/scanning. Their relevant run/status/clean implementations match;
their only diff is the candidate's mail-broker dispatch. This is a supported
transfer interface, not a scanner bypass or new remote command. The prior
handoff's operator-only conclusion is unsupported as an interface constraint;
it correctly requires reconciliation before another run.

The existing `clean SLUG` handler is broader: `tree()` accepts a single validated
slug, not `slug/source`, and `clean()` removes the whole slug without checking a
lease or holding the runner slot. Neither cleanup method independently proves an
idle workspace. The successor approval below replaces source-only deletion with
this established exact whole-slot cleanup after additional inventory evidence.

Mandatory execution conditions, in order:

1. Establish authoritative no-active-run and settled old-lease state before any
   deletion. Preserve the normal sole-global-worker admission guarantee throughout
   reconciliation; stop if another worker/run can concurrently use this slot.
   Read the actual current remote dispatcher and LeaseStore/runner-slot predicates
   using existing read-only administrative access if needed. Historical source
   copies and a healthy watchdog alone do not prove present idle state. Any
   unresolved live/renewable old lease, occupied runner slot, failed observation
   or unknown completion blocks cleanup. Use the existing settlement protocol
   where necessary; this review does not approve inventing a new remote command.
2. Record a read-only dry-run inventory of the exact `source/` subtree before
   mutation; verify the literal destination, trailing slash, and absence of path
   traversal or symlink ambiguity. Keep this inventory and recovery evidence
   outside the disposable export so the next standard push cannot remove it.
3. Preserve and verify actual result artifacts using the existing jailed rsync
   retrieval interface. In particular, `run598.sh` moves
   `source/strict542-checks` and `source/result598-probe` into `result598` only
   during its EXIT trap. A killed run can leave `result598` empty while the real
   `tests.log`, `probe.log` and diagnostic output remain inside `source/`.
   Inventory and recover those subtrees and any actual diagnostic receipt before
   deleting their parent; recover `result598` as well. Preserve real bytes and
   hashes, not a synthetic success or compiler result.
4. Preview an empty-directory rsync with `--dry-run --delete --itemize-changes`
   against that exact `source/` destination; reject any item outside it. Then
   perform the same transfer without `--dry-run`, without broad exclusions or
   ancestor deletion. Verify via read-only inventory and a second empty-directory
   dry-run that no child remains. On failure/uncertainty, stop and preserve the
   result; do not retry the diagnostic or choose a fresh export path.
5. Reverify unchanged local export/archive identities and use exactly the normal
   admitted command from `/home/deploy/agentq/tmp/export598-serial-probe-fixed`:
   `offload run --artifacts result598 -- sh run598.sh`. One execution only;
   ordinary 2GiB/1CPU resource admission, leases and scanners remain operative.
   A refusal, loss of transport, or uncertain result requires reconciliation
   again. Actual evidence still needs independent review.

Exact supported read-only health RPC: `ssh offload status`. Independently invoked
during review: protocol 2, placement approved and watchdog healthy. It provides
no active-container count, lease listing or workspace lock state. Likewise,
`sudo -n /usr/local/sbin/agentq-control status` reported RUNNING epoch168 with
resource_ready/validation_passed true, but its current `status()` implementation
does not report worker or remote settlement. These observations do **not** satisfy
condition 1. `offload health` is unsuitable as a read-only check because it updates
health/outage state and can send alerts; cached `offload status` is only health.

The implementing parent subsequently reported read-only inspection of the actual
remote implementation: nonblocking acquisition of the existing runner lock,
zero live leases according to `LeaseStore.valid`, and zero running containers
with `agentq.managed=1`. These are the appropriate additional predicates for
condition 1, subject to the sole-global-worker guarantee and no concurrent run.
The parent's initial shallow inventory was insufficient: deeper excluded trees,
including node_modules and other directories, remain under `source/`. Full-depth
inventory and the exact artifact checks in condition 3 remain necessary; absence
of files at shallow depth does not establish historical artifacts were removed.
The parent reported the remaining `source/.npmrc` SHA256 matched the public source
archive entry. Preserve that known public file and its hash outside the export
as reconciliation evidence. If historical artifacts prove missing, record them
as lost; cleanup cannot reconstruct compiler results. These remote observations
were supplied by the implementer, not performed by this reviewer.

No remote mutation was performed by this reviewer. This approval covers only
disposable test-workspace reconciliation and one previously source-approved
admitted diagnostic. All job598 build/artifact/action/next-seal reviews, automatic
queue review and job595 application/release gates remain open.

## Reviewed successor: exact disposable whole-slot cleanup

**APPROVE** the existing supported command
`ssh offload clean tmp-export598-serial-probe-fixed-38fd4ee7` under the same
mandatory idle/settlement, exclusion of concurrent runs, preservation, unchanged
export and admitted-run conditions above. This successor supersedes the earlier
restriction to deleting only `source/` and its empty-directory rsync procedure.
It authorizes no other slug or cleanup path. No installed handler changes are
needed: `clean()` calls validated `tree()` then `shutil.rmtree` on that exact
disposable export. The secret scanner applies only to `run()`, so this supported
cleanup can remove the leftover without bypassing the next run's scanner.

The implementer supplied additional actual read-only results: all four exact
artifact locations (`result598`, `source/strict542-checks`,
`source/result598-probe`, `source/serial-probe598.json`) are absent. Full os.walk
inventory counted 106308 leftover files, 2594533756 bytes, including excluded
dependency/ignored remnants. The source-only rsync preview generated excessive
inventory output. Preserve a bounded inventory/count/digest record and the
matching public `.npmrc` evidence locally before cleanup. Record old diagnostic
artifacts as unavailable; absence establishes no compiler outcome.

Before cleanup, verify the local unchanged manifest and every reviewed archive
digest again, and verify all non-source inputs in this exact remote slot are
retained in that local reviewed export. If an unrecognized input or result exists,
preserve it or stop. Existing local reviewed archives replace the disposable
remote copies through the next ordinary push. Immediately before cleanup repeat
the actual zero-live-leases, zero-managed-runners and available-runner-lock
observations under the sole-global-worker guarantee; clean does not enforce these
itself. Any failed check or concurrency uncertainty blocks action.

After clean, verify the exact slot no longer exists through read-only jailed
transfer inventory (a missing-source result is expected). The implementation
uses `ignore_errors=True`, so successful SSH exit alone is insufficient. Only
after verified removal perform one normal admitted run of the same unchanged
export, which recreates this same slot. Stop on failure or uncertain completion;
do not loop, alter limits or create a replacement export path. This is disposal
and retransfer of temporary source-test material, within the authorized source
testing scope, not a production deployment or installation action.
