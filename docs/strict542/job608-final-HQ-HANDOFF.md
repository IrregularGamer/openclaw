# Job608: exact preparation handoff to595

This is SOURCE preparation. No application, root/unit/sudoers/seal change,
service operation, gateway restart, provider call or scheduler release occurred.
This document supersedes status and next-run paragraphs in job608-to595.md and
job598-HQ-HANDOFF.md; their detailed fixed-owner restrictions still apply.

## Exact evidence and remaining gates

The production source is `591158cfe4a569c9e857780e9cc185cb4590b9b7` on maintained
`IrregularGamer/openclaw:strict542-source552`. Native5, checks6 and compiler5
receipts all bind that source. Checks6 has198/198 installed tooling checks,
plus the complete scoped gateway/native/supervisor/refusal/cancellation and
application checks. Native5 reproduces the independently pinned addon
`0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042`.
Package5 and package6 are consumed/lost interrupted executions, never retry
authority. Their existing launch manifests remain historical evidence. The
finite package7 continuation is recorded in job608-stage-package7-launch.md
and its immutable manifest3588339e70c8d7a5a78464e613e779eae98c8c14d4bfd9edacf1de7c55cd9004.
Package7 build/tree/action/next-seal bindings are PENDING until returned results
are verified and independently reviewed. No partial result supplies a gate.

Current explicit baseline proposal is job608-final-baseline-proposal.json,
SHA256428ced690f0b3a3cb8a7a2a4fc38570ffa71fa98d7298423376a26fd3ee6a9c9.
Current whole original seal is job608-final-seal-original.json,
SHA25651170230064a8da20e074497eae6a6c968d293d262e9e31523dd7365a5c128d3.
The independent reconciliation preserves original598 baseline/seal, validates
all56 current entries and replays original31 to current38 amendments including
installed639. It does not assume pending641 is installed. Any subsequent seal,
metadata, guard, boot or target drift requires explicit reconciliation and new
exact action/seal review. Never silently refresh an approved baseline.

Source, action, privilege-policy and seal reviews must each approve the same
exact source/tree/action. The seal review also binds validation.next.json.
The ACTUAL automatic queue608 review runs after preparation finishes; record its
real review job, exact result SHA256 and first APPROVE verdict. No future ID,
copied label, synthetic review or self-issued automatic approval is supplied.
The application helper reads these queue facts read-only and refuses otherwise.

## Transport, inventory and privilege

Reviewed587 source556d4f46/handoff8705e3dd replaces586 request-time sudo.
The historical native-owner-read.patch stays unapplied. Only inherited fd3 Unix
socket transport is used. External generated maintenance.py remains exactly
bca40971a35d160ad87b5d18fd1cc7f7730a7f90d2bb5b8480f3d7d79d11c182;
native-targets.json retains ABH commita1d99e8e and generator input pins. Install
only its isolated598 copy, never replace installed safety maintenance.py.

application598.py action fixes SIX targets: the complete isolated runtime tree,
isolated native file, server, supervisor, system service and gateway dropin.
It binds every old/new hash/metadata, all seven unchanged guard backups, both
execution helper hashes, full runtime file/mode/internal-link inventory and
exclusive /var/backups/strict542-598/<identity>. The exact canonical action is
the affected inventory; no caller-selected root command or general sudo grant
is introduced. Existing authorized HQ root invocation is required.

The fixed root service parent stays in its system cgroup with64MiB, no swap,
5%CPU,16tasks, Restart=no and900s lifetime. Only its freshly forked endpoint
moves its OWN PID through the fixed preexisting HQ cgroup.procs path. It retains
96MiB address-space/30sCPU limits, parent aggregate CPU/death/MainPID monitoring
and existing gateway budgets. No worker/gateway/unrelated PID is moved. Native
caller=True predicates, Preservation.owner, SO_PEERCRED PID/start/cgroup and
fixed gateway MainPID checks run unchanged. Socket root:deploy0660 access alone
is insufficient. fd4 proves parent liveness; no settlement means no success.
Full separate policy review: job608-final-privilege-review.md.

## Ordered finite natural-gap procedure,595 and genuine HQ only

1.595 verifies the completed exact package/action/tree/reviews and obtains an
actual foreground NONQUEUE Pinch HQ acknowledgement, binding the exact action,
genuine owner PID/start/cgroup/boot and dual wall/monotonic window <=900s. A queue
ops label does not supply HQ ownership. No ack or accepted-run record is created
by this handoff.595 exits normally; it must not apply from its worker.
2. Refer only to the separately reviewed owning dispatcher preparation,
agentq-ops feature/598-external-install commit3c18a58,
docs/job598-external-wait.md. Its EXTERNAL_INSTALL_WAIT marker is UNINSTALLED
and cannot bootstrap this gap. Current dispatcher continuations may run on the
next tick when the friend is up: do not assume the historical30minute delay or
reserve admission.595 finishes its source preparation normally after the genuine
handoff and retains it in actual HQ. No current timed gap has been established.
Never direct-edit
DB/status/counters, force stop/resume, start a detached installer, repeatedly
REQUEUE docs or install the optional dispatcher successor to arrange itself.
3. After all workers/fixtures/remote runs naturally settle, genuine foreground
HQ stages only reviewed secretless bytes at the fixed root-protected
/var/lib/agentq-safety/strict542-598-input. Validate original complete seal,
exact baseline metadata/guards, tree/action/helper/review hashes and native
registered-worker/fixture/remote settlement. Require fixed socket absence and
root-owned nonwritable directory ancestry with deploy search permission. The
read-only socket-parent observation records current0755 root:root ancestry;
repeat it, never silently change shared ownership/permissions. Stage the REAL root-protected
hq-ack.json with exact scope,owner,boot_id,created_wall,expires_wall,
created_mono,expires_mono,action_sha256. Scope=strict542-gateway-install598.
The actual execution acknowledgement must be fresh at this step: renew it
through the genuine HQ owner if the earlier handoff window expired;595
acknowledging a future handoff does not reserve or extend a900s application
window. No config/auth/credential/state transfer or provider call is needed.
4. The SAME genuine HQ owner invokes ONLY these fixed reviewed commands:

   ```sh
   /usr/bin/python3 -I /var/lib/agentq-safety/strict542-598-input/apply598.py preflight
   /usr/bin/python3 -I /var/lib/agentq-safety/strict542-598-input/apply598.py apply
   /usr/bin/python3 -I /var/lib/agentq-safety/strict542-598-input/apply598.py verify
   ```

   Each invocation takes native admission.lock nonblocking, checks genuine
   caller twice, full seal and natural quietness, and repeats checks before
   writes; lifetime is bounded by900s and remaining REAL dual-clock ack window.
   If a worker wins admission or any check refuses, exit with the actual refusal;
   do not wait holding the lock. The script changes disk only. Its
   DISK_APPLIED_SERVICES_UNCHANGED journal is not loaded-generation proof.
5. Only separately reviewed genuine HQ service actions follow disk verification:

   ```sh
   systemctl daemon-reload
   systemctl --user --machine=deploy@.host daemon-reload
   systemctl --user --machine=deploy@.host restart openclaw-gateway.service
   ```

   Restart may terminate the foreground caller. It invalidates old510/515 owner
   PID acknowledgements and accepted runs. Never hide this with a detached
   continuation. Before ANY further root action obtain FRESH genuine
   post-restart foreground HQ owner binding AND fresh accepted-run
   acknowledgements; record real MainPID/start/boot/cgroup and loaded ExecStart/
   generation evidence. Never reuse/fabricate old or queue-derived bindings.
6. Only that fresh genuine HQ may run `systemctl start strict542-owner.service`.
No enable/timer/restart loop. Verify fixed socket inode/root:deploy0660, parent
system cgroup, endpoint HQ cgroup, inherited descriptors, budgets, real kernel
peer checks, full tree/seal and loaded-generation identity. Native, IPC or
cancellation refusal remains UNKNOWN; synthetic test success is not live owner,
credential, quota or provider evidence.
7.595 records the real ordered application result in runs/595/HQ-RECEIPT.md:
all exact receipt/review/action/tree/source identities, backup path and metadata,
old/new whole seal, loaded generation, fresh owner/accepted-run identities,
supervisor/socket/settlement result and the last completed step. Missing or
partial receipt cannot release downstream installation gates.

## Backup, rollback and reseal

Before writes preserve whole original seal and every guarded/present target's
bytes, mode,uid/gid,xattrs,mtime, plus original absence markers and metadata.
Record ctime; it cannot be restored. The fixed0600 poison journal persists on
incomplete actions. Do not delete it or replay installers.

Prepare validation.next.json from the exact reviewed current whole original:
retain ALL fields/hashes, add only five fixed new file hashes and runtime
package.json/dist/index.js, append exactly one strict542-598/action_sha256
amendment. Independent seal review binds its exact bytes. Full original
validation precedes reseal; full tree and new whole seal validate afterwards.

Before restart/supervisor activation ONLY, guarded `apply598.py rollback` may
reverse a complete disk application within the same original owner/window,
lock/settlement/review gates. It verifies exact new targets/tree/seal/backups,
atomically quarantines recorded-new targets and restores original whole seal
bytes/ownership/mode/xattrs/mtime. Preserve quarantine and ctime evidence.
After restart, partial action, changed owner, activation, EXDEV or uncertainty,
preserve poison/backups and obtain independent exact reconciliation with fresh
HQ binding. No blind reversal or historical installer replay.

575/588 stays BY REFERENCE ONLY: source604ffc9/package1b22c4d/evidenced1304c7
and actual592 review.553 alone owns SAME510 continuation.497 alone later submits
a FRESH independently reviewed scheduler-request after every original gate;
503/504 observe. Approval1529 covers ONLY INTERNAL_REPORT_URL/API_BASE_URL.
Soft dependency release, source completion and this handoff confer no install
or release authority. No production mutation is performed by job608.
