# Job598 to595: exact source-only application preparation

This is a foreground HQ handoff, never an installation receipt. No installed,
sealed, root-owned, unit, sudoers, gateway runtime or provider state was changed.
Automatic queue598 review must APPROVE before ANY application. Soft dependency
release and approval1529 do not authorize installation or scheduler release.
Source review and exact action/privilege review are different gates.

## Reviewed source and immutable native authority

Job587 source556d4f46 (handoff8705e3dd) replaces586 request-time sudo. Current
combined source includes selected-session read574, preflight586 and corrected
socket transport587, plus598 supervisora035ef95 and application successors.
Original586 review589 and actual587 review590 are source-only; read their actual
runs/589/NOTES.md and runs/590/NOTES.md alongside this source's review receipts.
The historical native-owner-read.patch remains unapplied. Never install its CLI
or obsolete sudo rule. No general sudo, caller-selected command or new tool exists.

External generated native maintenance.py is exactly SHA256
bca40971a35d160ad87b5d18fd1cc7f7730a7f90d2bb5b8480f3d7d79d11c182,
from committed ABH tools/scheduler_handoff/candidate/maintenance.py. Generator
inputs and ABH commit a1d99e8e0460747293ec22a5a8dd8d14231c89d2 are pinned in
native-targets.json: reservation.py5f54474f8df103ae97f96e01dc76c895d7e5e321e0b0658d4d71de84f79ec1e0;
build_candidate.py6adfba9ed1630897c68d0862f067626a2b2dd470fb145861263eba017a853e7c.
Install only an isolated copy at /opt/openclaw-strict542/598/native/maintenance.py;
never replace installed safety maintenance.py (different original generation).
The bytes hashed are the bytes compiled. The endpoint executes unchanged
Native510.owner_check(caller=True), Preservation.owner, and fixed gateway MainPID
checks twice. SO_PEERCRED supplies peer PID; it is never supplied by a request.
The genuine native owner remains Pinch in the exact native HQ session/cgroup.

## Exact preparation and affected inventory

build598.sh requires admitted offload2GiB/1CPU, pnpm12.5.1, frozen original lock,
Node>=24.16 within24 or>=26.1, fixed epoch and complete relevant passing logs.
Do not relax dependency cooldown, lifecycle policy or build/workload limits.
Its tree receipt includes each file hash/mode and relative internal link, exact
source/export/lock/toolchain/admission/log identities. It rejects absent builds,
fixtures, secrets/state names, outside/broken links, hardlinks and writable modes.
Canonical receipts are deterministic for identical bytes; a single successful
build is not evidence that two independent builds are byte-reproducible.

Assemble a SECRETLESS local stage only after receiving the actual built runtime:

- runtime/: exact production dependency tree from result598-build/runtime.
- maintenance.py: exact committed generated native above.
- native_owner_server542.py: src/gateway/strict542/native_owner_server.py.
- root_owner_supervisor542.py: src/gateway/strict542/root_owner_supervisor.py.
- strict542-owner.service and90-strict542-598.conf: these exact source files.
- apply598.py and application598.py: exact reviewed preparation successor source.
- tree.json: actual BUILT receipt, never FIXTURE_ONLY.

With this directory as STAGE, run application598.py action --tree STAGE/tree.json
--stage STAGE --baseline docs/strict542/job598-observed-baseline.json --output
STAGE/action.json. CLI arguments above are literal option names; substitute only
STAGE's local source-preparation path, never any privileged application target.
The action records all SIX fixed changed targets, complete old/new hashes/modes/
ownership and seven unchanged guard identities. All six old targets were absent;
existing gateway package/unit/dropins and installed safety generation stay guarded.
Any baseline byte, metadata, boot or seal drift requires new exact independent
review, never silent baseline refresh or historical installer replay.

The exclusive backup path is /var/backups/strict542-598/<action identity>.
Back up original whole validation.json, each present target, all seven guards,
and original absence markers. Preserve bytes, uid/gid, mode, xattrs, mtime and
original metadata receipt. ctime is recorded identity, not restorable metadata.
No file outside this inventory may be replaced. The application journal is fixed
/var/lib/agentq-safety/strict542-598-application.json,0600 root-only, poisoned on
any incomplete action; do not delete it or replay to recover.

Independently review the actual source, actual action/tree/staged helpers and
PRIVILEGE POLICY in separate scopes. reviews.json requires three APPROVE entries
bound to source_commit, tree_receipt_sha256, action_sha256 and an authentic exact
review_receipt_sha256, with different author/reviewer. Record actual automatic
queue598 APPROVE receipt as automatic_queue_review=APPROVE598 in each review only
after it exists. These are references to real reviews, never self-issued proof.

Build validation.next.json locally from the actual original complete seal: retain
all existing fields and installed hashes, add only five fixed new file hashes
(native, server, supervisor, system unit, gateway dropin), and runtime package.json
and dist/index.js hashes from tree.json; append exactly one amendment
{kind:strict542-598, action_sha256:<actual>}. The independent privilege-policy
review must bind its exact file SHA256 as next_seal_sha256. apply598.py rejects
any other ledger delta. Original seal SHA256 is recorded in the baseline, along
with full metadata; validate EVERY original installed_hashes entry first.
Sealing the two runtime entry files is supplemented by verification of the ENTIRE
root-owned runtime tree against the action's canonical inventory.

## Privilege and supervisor policy, separately reviewed

The only root service is fixed strict542-owner.service, Restart=no,900s lifetime,
64MiB/zero-swap/5percentCPU/16tasks parent limits. It runs one fixed Python path
with no argv/environment-selected command. It binds only /run/agentq-safety/owner542.sock,
root:deploy0660 beneath a root-owned non-writable parent; an existing node refuses.
Access to the socket does not confer identity: unrelated deploy peers still fail
kernel PID/cgroup/native service MainPID checks. Supervisor source is hash pinned.

The parent stays in /system.slice/strict542-owner.service. Only its newly forked
root endpoint migrates its OWN PID using the kernel cgroup.procs API to the
PREEXISTING exact native HQ gateway cgroup. This is the reviewed source correction
that satisfies caller=True; no worker/gateway/unrelated process is migrated, and
no owner predicate is changed. The root-only unit necessarily permits this fixed
cgroup.procs write; no gateway delegation/control-file permission is granted.
Endpoint inherits96MiB address-space/30sCPU limits and the existing gateway
budget; parent monitors aggregate descendant CPU and gateway pidfd/start/MainPID,
and settles children using unreaped group identity, subreaper ownership and
pidfds. fd3 is the fixed listener and fd4 the parent pidfd. Deadline/parent death,
MainPID replacement, malformed IPC or unproved cancellation never yields success.
Do not alter existing heap2304MiB, gateway cgroup limits or worker1GiB slice.

## Ordered finite natural-gap execution owned by595 and actual HQ

1.595 verifies source/action/privilege and automatic598 reviews and obtains an
ACTUAL foreground nonqueue Pinch HQ acknowledgement. Read current MainPID/start,
boot and genuine native session binding from the owner; never construct an ack
from a queue ops label or reuse510/515 PID evidence. Bind the actual action digest
and dual wall/monotonic finite window <=900seconds. No provider/auth read needed.
595 must arrange the existing-HQ handoff while it is still a worker, then exit
normally; it must not perform this application itself.
2. Follow owning dispatcher source docs/job598-external-wait.md in agentq-ops,
branch feature/598-external-install, commit3c18a58, by REFERENCE ONLY. The initial
gap uses at most one actually available existing timed REQUEUE slot after a real
handoff; it does not reserve admission. Do not use its uninstalled new marker,
direct DB/status/counter edits, bare2099, forced stop/resume, detached installer,
scheduler request or repeated docs-only retry. If no timed slot remains, preserve
source-preparation completion and actual HQ handoff; do not claim installation.
3. Only after all workers naturally end and settle, actual foreground HQ may
stage the reviewed files under the FIXED root-protected
/var/lib/agentq-safety/strict542-598-input. No credentials/config/state transfer.
Preserve exact hashes and root ownership of all staged source/artifacts/receipts.
Supply real root-protected hq-ack.json with exactly scope,owner,boot_id,
created_wall,expires_wall,created_mono,expires_mono,action_sha256. Scope is
strict542-gateway-install598; owner is the unchanged native owner object. The
ack must be generated by the actual owner, not a worker or this document.
4. That same genuine HQ process invokes the exact reviewed fixed script with
/usr/bin/python3 -I /var/lib/agentq-safety/strict542-598-input/apply598.py preflight,
then apply, then verify. Existing authorized root invocation is required; no new
sudoers grant is prepared. Each invocation takes admission.lock nonblocking,
rechecks true caller cgroup/MainPID twice, full seal, valid reconciled worker,
native broker fixture inventory, stopped+revoked remote settlement, DB and units.
Checks repeat before writes. A process alarm bounds the entire invocation to900seconds
and then the lesser remaining genuine HQ wall/monotonic window, including copies. If a worker wins admission or any guard refuses,
exit and record actual refusal; do not hold the lock while waiting for a gap.
The helper changes DISK ONLY, never controls services, sends messages or releases
another job. Its last state DISK_APPLIED_SERVICES_UNCHANGED is not runtime success.
5. Separately reviewed HQ unit actions reload only the system unit definitions
and deploy user's gateway definitions, then restart the gateway through its
existing service manager. Fixed commands: systemctl daemon-reload;
systemctl --user --machine=deploy@.host daemon-reload;
systemctl --user --machine=deploy@.host restart openclaw-gateway.service.
These commands are FUTURE595 application actions, never queue598 commands. The
restart ends old HQ process/run bindings and may terminate its foreground caller;
never launch a detached continuation to hide that boundary.
6. Acquire a FRESH genuine post-restart foreground Pinch HQ owner binding AND
FRESH accepted-run acknowledgements before further root actions. Record real
MainPID/start/boot/cgroup, actual service ExecStart and full tree/seal hashes and
loaded-generation verification. Disk hashes alone do not prove loaded source.
Never copy/fabricate510/515 acknowledgements or treat a queue ops job as HQ.
Only then may that fresh HQ start the exact finite strict542-owner.service with
systemctl start strict542-owner.service; no enable/timer/automatic restart. Verify
real parent/system cgroup and child/HQ cgroup, fixed socket inode/ownership/mode,
limits and fresh kernel peer acceptance. A refusal is UNKNOWN, never waived.
7. Record595's exact completed steps, backups, original/new seal, review receipts,
new loaded-generation evidence, fresh owner and accepted-run receipt identities,
and actual supervisor/IPC result. Synthetic tests establish no live credential,
quota or provider observation. No live provider call belongs to this procedure.

Rollback before restart is a separately reviewed fixed reversal under the same
native lock/owner/settlement checks: restore only exact backup bytes/mode/uid/gid/
xattrs/mtime and original whole seal; remove only recorded-new targets whose
current bytes exactly match the reviewed action. Record unavoidable ctime drift.
After restart, partial seal action or uncertain application, preserve poison/
backups and independently review reconciliation with fresh HQ binding. No blind
automatic rollback, repeated installer, synthetic receipt or ownership bypass.

## Downstream authority remains unchanged

Integrate575/588 only by reference to source604ffc9/package1b22c4d/evidenced1304c7
and independent592 review. Do not retarget that package or duplicate553's sole
SAME510 continuation.497 alone later submits a fresh independently reviewed
scheduler-request AFTER every original freshness, exact source/action review,
installed/loaded-resume, preservation, cancellation/settlement and original hold
gate.503/504 observe. Approval1529 is ONLY INTERNAL_REPORT_URL/API_BASE_URL.
No soft hold release is install/release authority. Source work needs no S-only
infrastructure permission, but provides no production mutation authority.

## Current execution gate:175 tests pass, full build resource-refused

Actual admitted execution evidence is job598-execution-evidence.json, with full
synthetic job598-execution-tests.txt, job598-pinned-execution-tests.txt and actual
job598-build-refusal.txt. Exact
executable source remains de7369e4883abb96ac4cacac9a0ea89e2ae2ee29, independently
reviewed in6766a334. Both fresh runs passed all175 relevant tests. The second
run used exact pnpm12.5.1 through npm's temporary package runner, installed1469
frozen-lock dependencies and hit upstream's memory preflight before generating
build output. It exited1; this is NOT a passing build or implementation assertion.

The unchanged full builder requires4352MB heap and reports measured4.7GB peak;
the admitted broker permits2GiB/1CPU. scripts/tsdown-build.mts documents that
smaller2816MiB/4GiB slices were killed in unified runtime generation. The full,
package,ciArtifacts and strictSmoke profiles share this resource preflight.
Do not set OPENCLAW_TSDOWN_MAX_OLD_SPACE_MB to force an attempt, relax any budget,
use local/Docker builds, rerun the costly dependency installation blindly or
produce a synthetic runtime/tree/action. No complete supported gateway artifact
within the admitted budget was established. A source-reviewed bounded build
correction or supported admitted build path is still needed before retrying.
This remains598 preparation work; it is not an S-only permission question and
not an installation boundary waiver.595 must not apply this incomplete package.

Preserved immutable secretless exports are tmp/export598-acceptance and
tmp/export598-build-pinned under agentq. Their manifests bind identical exact
source/native archive digests. The second run's wrapper uses the pinned temporary
pnpm runner and cleans only disposable extracted source on exit, preserving
result598 logs/evidence. The initial follow-up scan refused public source/.npmrc;
no command ran in that refused follow-up. Logs were recovered read-only through
the forced rsync artifact path. No offload scan, ownership predicate or build
resource guard was weakened. Automatic queue598 review, actual artifact/action/
next-seal review and all original application gates remain unfulfilled.

## Corrected diagnostic (86c1a4db, reviewed ce824d35): no outcome yet

The first execution of the corrected diagnostic, from the unchanged
tmp/export598-serial-probe-fixed export, passed all179 admitted checks, finished
the pinned install and started serial tsdown (pid339). The worker was then killed
at 2026-10-25T19:24Z by an agent usage limit, so the remote run was cancelled
without settling: no compiler, memory or artifact result exists
(runs/598/serial-probe-fixed-live.log). One rerun of the same export was refused
before any command ran: `refusing: secret-like file in tree: source/.npmrc`,
offload_status remote_environment_blocked, retry_requires_reconciliation, exit75
(job598-serial-probe-rerun-refusal.txt). The local export has no source/ tree,
so the leftover is remote state from the killed run. Per policy, there was no
retry, no scan bypass and no new export path. Next step: once the queue/broker
has cleaned up the remote workspace, run one fresh admitted run of the same
reviewed export, followed by independent evidence review. All gates for598
and595 above remain open.

## Second rerun after requeue (2026-10-25T20:10Z): still unreconciled

With offload health `up`, one admitted run of the same unchanged export
(manifest source 86c1a4db, base e79a0e45, successor 8ac591b3, native d73e4e35)
was refused again before any command ran: `refusing: secret-like file in tree:
source/.npmrc`, remote_environment_blocked, retry_requires_reconciliation, exit75
(job598-serial-probe-second-rerun-refusal.txt). The leftover is still remote
source/ from the killed 19:24Z run (run598.sh extracts source598.tar into
source/ remotely and its EXIT trap never ran). No bypass, scanner change, new
export path or further retry. Next step: broker/remote-watchdog
reconciliation of the friend-VPS workspace (operator action outside this
worker), then one fresh admitted run, then independent evidence review. All
598/595 gates remain open.
