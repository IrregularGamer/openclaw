# Job608 independent privilege-policy and unit review

Reviewer: Rook `/root/privilege_review`, separately dispatched from the builder,
package runner, action reviewer and seal reviewer. Review date: 2026-10-28 UTC.
Exact source: `591158cfe4a569c9e857780e9cc185cb4590b9b7`. I compared the reviewed
files with this commit; the working-tree bytes agree. Later evidence commits do
not extend this review to changed executable source.

Verdict: **APPROVE_PRIVILEGE_SOURCE_POLICY_ONLY**. No blocking finding in the
reviewed fixed privilege/unit procedure. Final artifact/action/tree identities
must be independently bound in the addendum before this supplies the actual
`privilege-policy` review entry. This document alone authorizes no installation,
service operation, gateway restart, seal amendment or scheduler request.

| Reviewed source | SHA256 |
| --- | --- |
| `src/gateway/strict542/root_owner_supervisor.py` | `0d8bdeda5e916ddc25bda48b1e3da36252a710c88dfe36f875c1b05290709fdc` |
| `src/gateway/strict542/native_owner_server.py` | `a145387432fbf8e17fffbf1e552328e651054e9d603b1d9bdad2d8494dc6a373` |
| `docs/strict542/strict542-owner.service` | `ab297fe2afe0559c467ddc6e32a4c041a0cd143daad612ceabcf23571ae4f469` |
| `docs/strict542/90-strict542-598.conf` | `45634d116cd636458352514b15bc081fe9b78070444655b4ae2d069e18732ecc` |
| `docs/strict542/application598.py` | `4a6512d153a5692964f2f4ce0e5795157e18da2bcba627a86d3f1a9c36750cb9` |
| `docs/strict542/apply598.py` | `10ff28fc821c8bcf9bcb4f288a39ef7d9f82b79bcff24a43e95b3cfb0f500153` |

The executable root service command is only `/usr/bin/python3 -I
/usr/local/libexec/agentq-safety/root_owner_supervisor542.py`, with no command
arguments accepted by its source. The proposed gateway drop-in replaces only
ExecStart with `/usr/bin/node --max-old-space-size=2304
/opt/openclaw-strict542/598/runtime/dist/index.js gateway --port 18789`.
Existing gateway unit, stop/budget and heap drop-ins remain separately guarded.
No sudoers rule, caller-selected root command, new tool, capability delegated to
the gateway, worker migration or change to worker budgets is introduced. The
obsolete586 request-time sudo transport and its historical native-owner patch
remain excluded; reviewed587 fd3 transport is the preparation being installed.

The parent requires root and its exact dedicated system-unit cgroup. Its unit
retains Restart=no, RuntimeMaxSec=900, TimeoutStopSec=5, KillMode=mixed,
MemoryMax=64M, MemorySwapMax=0, CPUQuota=5%, TasksMax=16, NoNewPrivileges=yes,
LimitCORE=0, LimitNOFILE=64, ProtectSystem=strict, PrivateTmp=yes and AF_UNIX only.
ProtectControlGroups=no is an explicitly reviewed root privilege needed for the
fixed cgroup.procs migration, not a claim that the endpoint remains accounted to
the parent's unit. Only the freshly forked endpoint writes its own PID to the
preexisting exact HQ gateway cgroup. It verifies actual placement before serving;
no process identity is forged and no owner predicate is relaxed. The moved
endpoint remains in the existing gateway cgroup and receives RLIMIT_AS=96MiB,
RLIMIT_CPU=30s and no core dumps. The parent monitors aggregate descendant CPU
against30s, gateway pidfd/start/cgroup/MainPID and the900s lifetime. These bounds
are distinct from the parent's64MiB/5%/16-task cgroup caps; the report does not
claim those parent cgroup caps follow a migrated process.

The socket is a fixed `/run/agentq-safety/owner542.sock`, root:deploy (0:1000),
0660, beneath root-owned directories without group/other write access. Existing
nodes refuse; bind never unlinks another invocation's endpoint. Cleanup unlinks
only the socket inode created by this invocation. fd3 conveys the listening
socket and fd4 a pidfd for parent liveness. Connection access alone conveys no
authority: SO_PEERCRED supplies the kernel peer PID, and the endpoint derives
start identity from procfs. The unchanged native owner check runs twice with
caller=True, preserving root, exact Pinch/HQ session, owner PID/start/cgroup,
endpoint caller cgroup and fixed user-service MainPID checks. A queue label or a
different deploy peer fails these predicates.

I extracted the native file from the committed secretless checks6 input archive
and independently verified SHA256
`bca40971a35d160ad87b5d18fd1cc7f7730a7f90d2bb5b8480f3d7d79d11c182`.
I inspected its actual `Preservation.owner` and `Native510` checks. It is compiled
from those pinned bytes at the isolated new598 native path, never substituted
for the installed safety maintenance generation. The documented ABH inputs stay
pinned to commita1d99e8e0460747293ec22a5a8dd8d14231c89d2,
reservation.py5f54474f8df103ae97f96e01dc76c895d7e5e321e0b0658d4d71de84f79ec1e0
and build_candidate.py6adfba9ed1630897c68d0862f067626a2b2dd470fb145861263eba017a853e7c.

IPC accepts only the bounded operator-read schema and cancellation. Native
subprocess execution accepts only the literal systemctl MainPID query; request
fields cannot select a command. Absolute framing and request deadlines,
disconnect/invalid-input cancellation, parent death and endpoint expiry refuse
continued authority. Unreaped leader identity, subreaper adoption and pidfds
settle both owned groups and escaped descendants before a settled receipt.
Unproved settlement or expired request emits no successful receipt. Startup and
shutdown include the fork-before-setsid race protection; the supervisor does not
synthesize an owner or accepted-run acknowledgement.

The application helper is separately finite, takes the existing admission lock
nonblocking, requires actual finite foreground nonqueue HQ owner checks and
actual queue approval, validates the whole original seal and exact baseline,
and repeats native registered-worker/fixture/remote settlement before writes.
Targets and execution helper hashes are fixed in the action. Privileged target
rename traverses ancestors with no-follow pinned directory descriptors.
Backups, original absence markers and the poison journal precede writes.
Rollback requires exact complete disk-only application, original owner,
unchanged service history, exact backups/new targets and same lock/gap/reviews;
partial or post-activation recovery requires independent reconciliation.
No service action is performed by apply598.py itself.

The ordered HQ handoff must retain separately reviewed fixed daemon-reload,
gateway restart and finite endpoint-start actions, performed only by actual HQ
after a natural settled gap. Restart invalidates510/515 owner PID bindings and
run acknowledgements. Fresh genuine post-restart owner binding AND accepted-run
acknowledgements are prerequisites to endpoint activation; none may be copied or
manufactured. Later scheduler release remains497's separately reviewed action.

Evidence inspected, not rerun locally: checks6
`result608-checks/checks/tests.log`, SHA256
`04633629cf13e1f9d98f752e250299fb69229b083a96e5b7296f64f608892ace`,
bound by its stage receipt to the exact source above and manifest
`0a462117ffae69c84f12aac6dfb5b670c450c94f543a25e2cf9275657afc24f6`.
All13 supervisor tests passed, including real fd3 IPC with escaped-descendant
settlement and genuine parent SIGKILL cancellation. The native-owner and
application suites in that receipt also pass. Their placement/owner fixtures
are synthetic; they establish refusal/lifecycle behavior without claiming live
HQ identity, root installation or provider execution. I started no service,
changed no root/installed/sealed file, ran no offload/full suite and read no
runtime auth/config/credential data during this review.

## Final artifact binding

Pending package6 receipt and exact action/tree identities. Historical598
baseline/control/seal hashes are not current installation authority. Any current
baseline drift requires independently reviewed reconciliation and exact action
regeneration; silently refreshing a baseline is not approved.
