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

## Third rerun after requeue (2026-10-25T20:44Z): still unreconciled

offload health `up`; one admitted run of the same unchanged export with the
same command (`offload run --artifacts result598 -- sh run598.sh`) was refused
before any command ran, identical to 20:10Z: `refusing: secret-like file in
tree: source/.npmrc`, remote_environment_blocked, retry_requires_reconciliation,
exit75 (job598-serial-probe-third-rerun-refusal.txt). The local export still has
no source/ tree. The leftover remote source/ from the killed 19:24Z run has not
been cleaned up by the queue or broker across two requeues, so requeueing alone
won't clear it. An operator with broker/friend-VPS access must reconcile that
workspace (remove the leftover source/ for this run slot) before any
further attempt. No bypass, scanner change, new export path or extra retry.
All 598/595 gates remain open.

## Root cause of the persistent remote leftover (2026-10-25T21:2xZ, no rerun)

No fourth run: nothing changed and the leftover cannot self-heal. The source
tracks `.npmrc` (git ls-files), so run598.sh's `tar -xf source598.tar -C source`
creates `source/.npmrc` in the remote workspace. The 19:24Z run was killed before
its EXIT trap removed `source/`. `offload` pushes with `rsync -az --delete
--exclude-from=offload.exclude`, and offload.exclude lists `.npmrc`; rsync never
deletes excluded receiver paths without `--delete-excluded`, so `source/.npmrc`
(and its parent `source/`) survive every push and the agent's tree scan refuses.
Operator action required (friend VPS / broker, not this worker): delete the
remote workspace `tmp-export598-serial-probe-fixed-38fd4ee7/source/` (slug from
offload slug_for of /home/deploy/agentq/tmp/export598-serial-probe-fixed),
then requeue for one fresh admitted run of the unchanged export. Infra follow-up
for the offload owner (sealed, not changed here): reconcile killed-run leftovers
of excluded paths (e.g. `--delete-excluded` or post-kill workspace wipe).
No new export path, scanner change, bypass or retry. All 598/595 gates open.

## Supported disposable reconciliation completed (2026-10-25)

Independent review50593fc9 supersedes the earlier operator-only assumption.
The existing forced `clean` command supports exact disposable-slot cleanup; no
installed broker change is needed. Actual current runner lock was available,
zero leases were live and zero managed runner containers existed. The public
leftover npmrc matched the reviewed archive; full source inventory also found
106308 ignored dependency/generated files (2594533756 bytes), not only npmrc.
All four actual result locations were absent before cleanup; historical compiler
results cannot be recovered or claimed. Local archives were independently
rehashed and matched the unchanged manifest, and all remote input files matched
retained local inputs. Exact `ssh offload clean
tmp-export598-serial-probe-fixed-38fd4ee7` exited0; a separate read-only check
proved the exact slot absent. See job598-reconciliation-evidence.json. No
scanner, budget, installed file, seal, service or unit changed. Next: one normal
admitted diagnostic from the SAME unchanged export, then independent actual
evidence review; no build/artifact/application approval follows from this cleanup.

## Actual reconciled diagnostic: finite timeout, not a build (2026-10-25T22:23Z)

One normal admitted unchanged86c1a4db diagnostic ran after verified cleanup.
All180 relevant checks passed (the fifth cache-policy test adds one to earlier
179 totals); exact logs are committed in4052b599. Pinned pnpm12.5.1 completed
its frozen1469-dependency install. The AI compiler invocation exited0. The
full main runtime invocation did not finish within the shared900s deadline: its
remaining895715ms expired, the owning wrapper sent SIGTERM then SIGKILL and
observed the process group dead. The actual diagnostic receipt says timedOut
true, signal SIGKILL; outer command exited1. Broker log: rc1 after1286s.
The container was capped at2147483648 bytes memory and equal memory+swap,
1CPU,512pids and oom_score_adj1000. One read-only intermediate sample showed
1.499GiB/2GiB and102.19% CPU; this is neither peak evidence nor proof of OOM.
This is a finite compiler timeout, not an implementation test assertion.

The normal wrapper EXIT trap completed, and actual final test/probe logs and
receipt were recovered through the existing forced jailed rsync artifact path.
No managed runner container remained. See job598-reconciled-outcome.json and
its exact hashed logs/receipt. No complete gateway/runtime/package/declaration/
postbuild artifact or accepted action/next-seal exists;595 MUST NOT apply.
Do not repeat this unchanged expensive diagnostic or raise its deadline/heap
without an evidenced source plan and exact independent review. Cleanup is now
resolved; an operator deleting the old slot is no longer the next step.

Independent local source assessment found every gateway-capable build-all
profile still includes main tsdown (scripts/build-all.mts:223-237,273-298);
run-node rebuilds through qaRuntime (scripts/run-node.mts:1714-1722), not a
supported direct-source distribution; tsconfig has noEmit. Existing AI/package
declaration cache hits still compile runtime, and the unified runtime has no
cache (build-all.mts:92-134). tsdown.config.ts:883-905 explicitly preserves
the shared singleton graph. No concrete small supported2GiB correction was
established. Next598 work is an owning-source bounded compiler/build-path
correction preserving that entire graph, followed by independent exact source
review, one admitted complete build/checks, actual deterministic artifact/tree/
action/next-seal review and automatic queue598 review. This is pending598 work,
not an S-only approval question, a request to waive any gate, or another
permission to retry unchanged source. Existing infrastructure/source installation
preparation and fresh genuine post-restart HQ owner/run requirements above stand.


## Whole-config isolation successor (598, still diagnostic only)

Source a069c344/f62d419c and separate independent review fe56d16f prepared
fresh compiler processes for each unchanged whole config, with original order,
complete census and unchanged900s/2GiB limits. Actual admitted fe56d16f run
passed184 relevant checks and pinned installation; AI compilation passed. First
main config refused13 UNRESOLVED_ENTRY errors before useful graph compilation.
The nested diagnostic config changed tsdown's default root to its own directory;
this was an implementation defect, not resource exhaustion or a test assertion.
The child exited1 and the owner observed its process group dead; normal export
cleanup completed. Actual logs/receipt are job598-isolated-first-*.

Correction moves only the diagnostic config beside the original root config and
adjusts its imports/selector path. It preserves original default-root semantics
without a caller root override, changed entries or omitted graphs. Independent
exact correction/evidence review must precede one corrected admitted run. No
unchanged repeat, normal build admission, artifact/action/next-seal approval or
595 installation is established. The original4352MiB full-build guard remains.


The first corrected-root attempt was refused before command execution with
exit75: leftover root .pnpm-store/v11/index.db from the preceding completed
diagnostic (job598-isolated-corrected-refusal.txt). Source/native cleanup worked;
pnpm's root store was outside those paths. Runner successor now removes that
fixed disposable cache during its EXIT trap too; it changes no installed broker,
scanner, source, dependency or resource policy. Existing exact-slot reconciliation
procedure is reused with a separately reviewed new literal slot
tmp-export598-config-isolation-98c59c32, current idle/lease/runner and full bounded
inventory evidence, retained input/archive hashes and recovered actual outcomes.
No database content is transferred. Only after independent exact cleanup and
runner review, verified removal, and unchanged reviewed archive identities may
one normal corrected diagnostic run proceed. Do not blindly retry or change slot.


Reviewed fixed-slot reconciliation completed: a7d01900 approved exact executable
1f4ed0cf. The actual existing runner lock remained held across fresh sole-current
lease/zero-managed-runner checks, supported clean and verified slot absence.
Current lease matched root worker registration job598/unit, not an invented owner
identity. Local recovered outcomes and all five remote input hashes were retained.
Receipts job598-isolated-{pre-clean,current-worker,registered-worker,immediate-idle,post-clean}.json
record only metadata/digests; no package database content or credential transfer.
One corrected normal admitted run is next; scanner/resource/lease rules remain.


## Corrected isolated result and reviewed native scheduling successor

Actual6d7ecc59 run passed184 relevant checks, pinned install, AI and all15
package configs0-14. Unified config15 preserved its full singleton graph but
timed out at remaining868110ms of the shared900s deadline. Owning cleanup sent
SIGTERM/SIGKILL and observed the compiler process group dead. No artifact exists.
Exact source/export/log/census/result and metadata are bound in
job598-isolated-corrected-outcome.json. Sampled kernel memory.events had0 OOMs;
final RSS~1.51GiB with25MiB V8heap. No peak/OOM or feasibility inference follows.

Actual6 runnable rolldown-worker threads were observed under1CPU quota. Exact
Rolldown1.2.9 source defaults its custom Tokio pool to physicalCPUs*3/2, matching
the4CPU affinity sample; this ignores the runner's quota. Successor3a4aaf3d/
36940dd8 generates fixed workers/blocking/Rayon/Tokio1 after refusing inherited
controls. Independent exact source review74da218e permits one fresh admitted
diagnostic ONLY after independent current-outcome review and verified normal
cleanup.11 source-policy tests pass. It changes scheduling, not the graph, heap,
4352MiB normal-build guard, deadline, scanner or settlement owner. Complete
profile/declarations/postbuild/package/tree/action/next-seal and automatic598
review still remain before595. Do not repeat6d7ecc59 unchanged.


## Native-pool experiment admission refusal; exact resumable preparation

After exact current-outcome approvals60ce18b4/8ce523c0, one normal fixed-pool
experiment was attempted from the SAME tmp/export598-config-isolation export.
Actual result was exit75, placement_blocked, retry_requires_reconciliation
(job598-native1-placement-outcome.json and exact refusal log). The local owner
checks placement before push_tree/remote run: no new transfer, tests or compiler
executed in this attempt. Later cached status reported up; the refusal's exact
cause was not recorded, so no outage cause or successful admission is inferred.
No immediate retry, override, new slot, local fallback or installed change.

Retain tmp/export598-config-isolation with manifest source8ce523c0, basec790ba44
archivee79a0e45a4ea..., successor697e339cf97a..., native archived73e4e35720f...;
full exact digests/paths are in job598-native1-export.json. The original archive
contains no new fixed-pool code: the committed successor overlay is REQUIRED.
The runner is the exact committed run-isolated598.sh (fixed cache cleanup).
After normal placement reconciliation/admission, the next command is exactly
`offload run --artifacts result598 -- sh run598.sh` from that retained export.
Keep this slot identity. Preserve actual186-check and per-config/thread outcome
receipts, independently review them, then implement/verify the complete supported
bounded build/profile and actual runtime/package/tree/action/next-seal receipts.
Current184 remote tests apply to6d7ecc59;11 new policy tests pass locally and
are independently source-reviewed, not a186-test admitted execution claim.
Automatic598 review and every595 application/HQ ownership gate remain open.
Do not apply an incomplete package or repeat6d7ecc59 unchanged.

## Resumed fixed-pool diagnostic, 2026-10-26

The retained exact source8ce523c0 export was normally admitted after the prior
placement refusal. Actual186 relevant checks pass; exact log and source-bound
hash receipt are job598-native1-resumed-tests.txt/json. Fresh local streaming
hashes of all three archives and runner match the retained manifest, and the
remote runner asserted the same archive hashes before tests. Compiler diagnostic
is still active; no compiler outcome, complete build or application approval is
claimed by this checkpoint. Do not concurrently retry or treat this checkpoint
as permission to apply. The original complete-build/action/review gates stand.

The resumed8ce fixed-pool diagnostic now settled:186 relevant checks pass;
AI and configurations0..14 pass, unified config15 timed out after869459ms.
The owning wrapper observed process-group death after SIGTERM. Actual remote
post-run inventory shows zero managed runners and normal source/native/store
cleanup. job598-native1-resumed-outcome.json binds exact logs and receipt.
This is no artifact or feasible-build claim; pool1 alone did not complete.
Source-only allocator successor1c27e206 (review6305e30c) addresses observed
THP/reclaim pressure without changing the existing1.5GiB high/2GiB max budgets.
Only one fresh normally admitted committed diagnostic follows independent
actual-outcome review. Do not repeat the unchanged failed source.

The exact6305 allocator diagnostic was normally admitted after independent
0590 outcome/cleanup reviewd79493db. Actual188 relevant checks pass;
job598-allocator-tests.txt/json and allocator-export.json bind the committed
source, input archives and log hash. Pinned install/compiler is still active;
no compiler, complete-build, action or application success is claimed here.

The 00:49 exact6305 allocator diagnostic was cut off by agent usage exhaustion
after its188 checks; no result598 artifacts returned and the remote was idle.
One identical rerun (manifest/runner4ddaa154/successorb599e23a/natived73e4e35
re-verified) was refused before execution with exit75
`remote_environment_blocked`: secret-like `source/.npmrc` left in the remote
slot by the interrupted run (local export holds only the five inputs).
job598-allocator-rerun-refusal.txt preserves it. No compiler/build outcome exists.
Next: normal placement reconciliation of the stale remote slot under its runner
lock (no manual override, no new slot, no local fallback), then the same
`offload run --artifacts result598 -- sh run598.sh` once, then independent outcome review.

## Interrupted allocator slot: results recovered, successor cleanup pending review (2026-10-26)

Read-only inventory of `tmp-export598-config-isolation-98c59c32` found the killed
00:49Z run's `source/` (public `.npmrc` 432 bytes) with only
`strict542-checks/tests.log` (= recorded188-check log1b30cade) and
`result598-isolated/probe.log` (b91e20b8). Both recovered byte-exact by jailed rsync
to runs/598/allocator-reconciliation/. The probe log ends inside `pnpm install`: no
compiler start, so no allocator outcome exists and one rerun is still required.
The once-approved reconcile-isolated-slot598.py refuses a slot holding `source/`, so
source-only successor `reconcile-allocator-slot598.py` (same lock/lease/container
predicates and literal `ssh offload clean` of that one slug; additionally admits
`source/` only if its sole result files equal the recovered hashes) awaits exact
independent review before its single execution. Evidence: job598-allocator-recovery.json.

Single execution of approved reconcile-allocator-slot598.py (51ee185c, review8863e79f)
refused before READY: `remote guard refused or disconnected`, exit1; no clean ran.
Read-only cause: remote LeaseStore has 0 valid leases (398 expired files), 0 managed
containers. The guard demanded exactly this worker's lease, which only exists after
an offload run in the same session. Source-only correction accepts zero live leases
(the original stricter rule) or only this worker's, and the post-clean check
requires the same lease set unchanged. Needs exact review before its one execution.

Approved corrected cleanup (69b1e08e, review707ed7da) executed once, exit0:
immediate-idle {"live_lease_sha256": [], "managed_running_containers": 0, "phase": "LOCK_HELD_READY", "runner_lock_available": true, "slot": "tmp-export598-config-isolation-98c59c32"}; post-clean
LOCK_HELD_VERIFIED_ABSENT absent=true. Then the same unchanged export (runner4ddaa154,
successorb599e23a, natived73e4e35, sourcee79a0e45) was started once with
`offload run --artifacts result598 -- sh run598.sh` (log runs/598/allocator-reconciled-run.log).
Its actual outcome still needs exact independent review; no build/artifact/application approval.

## Actual reconciled allocator diagnostic: same finite timeout (2026-10-26)

The single admitted run of the unchanged export exited1 (log
runs/598/allocator-reconciled-run.log, sha256 2532f203…3021). The13 allocator-policy
checks passed. Config14 closed (peak rss128MiB); configs0-13 have no records in this log. Unified main-config-15 ran with
MIMALLOC_ALLOW_THP=0 and four native pools at1, peaked at ~1439MiB rss, and was ended by
the existing869346ms deadline: SIGTERM then SIGKILL, process group observed dead,
cleanup=timeout. Because of the nonzero exit, no result598 artifacts were pulled. The remote EXIT
trap runs normally. Conclusion: the THP-off allocator successor does NOT fix the
config15 stall, so the unchanged allocator source must not be retried. No compiler, build, artifact,
action or application success. Next: an independent outcome review, then root-cause
config15 (CPU-bound graph vs memory) with source-only changes before any new admitted diagnostic.
