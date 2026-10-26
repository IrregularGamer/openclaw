# Independent installer and supervisor source-policy review, 2026-10-26

Reviewed source at `f81194b0648766f0f8ab04153b4122e7c620b4bc`, including
implementation source157b93a8 and its original-seal-link correction c32bea1e.
This review found no confirmed source blocker within the scope below. It is
source preparation only: no actual runtime tree, action, privilege-policy,
next-seal, loaded-generation or application approval is granted.

## Exact reviewed identities

| Source | SHA-256 |
| --- | --- |
| application598.py | `b5591e9d010e050d09075d7ac94339f3b22995882a42a54c38b854d850a304fc` |
| apply598.py | `9a3f6ef6e51345f0e2b607c6b79bc120e6e020882bdfc11affaad919627ad092` |
| job598-HQ-HANDOFF.md | `2881a9618c9ccf7d7d5de293b524c82fbe968111d9a9658930e237c93be128cc` |
| job608-to595.md | `223d8f15385bc02a76b30fed095c2f1163151570f8aaaafc3fbfb228e0a6461d` |
| root_owner_supervisor.py | `0d8bdeda5e916ddc25bda48b1e3da36252a710c88dfe36f875c1b05290709fdc` |
| native_owner_server.py | `a145387432fbf8e17fffbf1e552328e651054e9d603b1d9bdad2d8494dc6a373` |
| strict542-owner.service | `ab297fe2afe0559c467ddc6e32a4c041a0cd143daad612ceabcf23571ae4f469` |
| 90-strict542-598.conf | `45634d116cd636458352514b15bc081fe9b78070444655b4ae2d069e18732ecc` |

The Python supervisor/server paths above are under `src/gateway/strict542/`;
the other files are under `docs/strict542/`. The unchanged external generated
maintenance source remains pinned to
`bca40971a35d160ad87b5d18fd1cc7f7730a7f90d2bb5b8480f3d7d79d11c182`.
Its owner predicates were inspected in the retained secretless native source
archive, not in runtime/provider/auth state. Generator references remain
docs/strict542/native-targets.json; no external source was changed.

## Source findings and boundaries

`root_owner_supervisor.py:99-107` uses the real cgroup-v2 `cgroup.procs`
interface, writes only its newly forked endpoint's own PID, then checks exact
placement. The parent stays in its dedicated system unit (`:157-169`). The
candidate unit `:23-29` explicitly permits the fixed write and does not grant
cgroup delegation to the gateway. Only the migrated child leaves the parent's
unit accounting: inherited 96MiB RLIMIT_AS, 30s RLIMIT_CPU, zero core size,
parent aggregate-descendant CPU monitoring (`:120-152`), finite 900s lifetime,
and the existing gateway cgroup remain relevant. These source policies do not
prove host kernel migration permission, effective loaded unit policy or live
placement; those must be checked in the real reviewed handoff.

`native_owner_server.py:215-248` derives peer PID from SO_PEERCRED and start
identity from procfs, then repeats unchanged native owner checks with
caller=True. The native predicates retain exact HQ caller/peer cgroup and fixed
gateway MainPID checks. The supervisor also tracks gateway pidfd/start/cgroup
and MainPID. Socket access supplies no session, accepted-run or application
authority. Request framing and operation are bounded; child settlement uses
unreaped group identity, subreaper ownership and pidfds (`:50-112`, `:160-188`).
Unproved settlement emits no successful acknowledgement. Parent death,
deadline and endpoint shutdown retain their cancellation/settlement paths.

`apply598.py:123-148` validates every entry of the original whole seal and
accepts only the exact additive fixed-target next seal, independently bound
by its file digest. The original devstack link exception is fixed to its
preexisting link string, non-link target and sealed bytes. Initial checks
also bind original seal bytes/metadata, boot, seven guards and target states
(`:178-187`). `:260-294` uses exclusive backups, recorded absence markers,
a persistent poisoned journal, repeated native owner/settlement checks, fixed
inventory writes and final whole-tree/guard/seal verification. It changes disk
only. The action binds exact helpers and five distinct review scopes
(`application598.py:173-225`); real automatic608 review is checked read-only
against the queue (`apply598.py:150-168`).

Rollback remains a separately reviewed exact guarded reversal before restart,
with unavoidable ctime drift recorded; restart, partial-seal action or uncertain
application requires preserved poison/backups and independent reconciliation
(`job598-HQ-HANDOFF.md:182-188`). No rollback implementation or actual rollback
action is approved by this source review.

The ordered handoff requires a real finite foreground nonqueue HQ owner,
natural worker settlement, then separately reviewed service-manager actions.
Restart invalidates historical owner bindings. Fresh genuine post-restart
owner AND fresh accepted-run acknowledgements are mandatory before further
root actions and supervisor start (`job598-HQ-HANDOFF.md:125-180`,
`job608-to595.md:55-86`). Dispatcher external-wait remains existing owning
source by reference only: commit3c18a58, docs/job598-external-wait.md. No
uninstalled marker, detached continuation, forced stop/resume or queue edit
is authorized here.

## Prerequisite and verification limitations

The socket parent must both remain protected and allow gateway traversal.
`root_owner_supervisor.py:74-79` checks root ownership/nonwritability, but not
deploy search permission. `strict542-owner.service:29` requires the directory
to exist and does not create it. The primary reported a read-only observation
at 11:08 UTC: `/run/agentq-safety` is a directory, uid0/gid0, mode0755, no
symlink, and effective-uid1000 `os.access(X_OK)` is true. This resolves the
current reported prerequisite only. Repeat its existence, protected ancestry
and gateway traversal checks in actual application preflight; do not change
shared runtime-directory ownership or permissions implicitly.

Bounded offline verification completed with exit0 and no diagnostics:

    SYSTEMD_OFFLINE=1 SYSTEMD_LOG_LEVEL=warning timeout -k 2s 15s systemd-analyze verify --man=no docs/strict542/strict542-owner.service

This checks unit syntax/dependencies, not the Python script argument's installed
bytes, effective host cgroup permissions, live socket connectivity, resource
accounting or endpoint acceptance. No services were started/reloaded and no
runtime/auth/provider state was read by this reviewer. No full suite, compiler
or offload ran for this policy review.

The actual full typed production package/tree remains absent. Exact artifact,
staged-helper, action, privilege-policy, seal and automatic-queue approvals,
whole-seal/baseline revalidation, original lock/fence/settlement, exclusive
backups, loaded generation and fresh genuine owner/run acknowledgements all
remain mandatory. A source review or diagnostic result cannot replace them.
