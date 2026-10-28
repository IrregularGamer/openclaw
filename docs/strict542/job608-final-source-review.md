# Job608 exact final source review (independent)

Reviewer: Rook `/root/source_review`, separate from the implementation, package6
runner, action preparation and the other privilege/seal review lanes.
Reviewed executable source: `591158cfe4a569c9e857780e9cc185cb4590b9b7`.
Evidence-only successor inspected: `ec950e2c`; its four changed paths are review,
stage-launch, native5 log and native5 result documents. No executable delta exists
between those commits. This review does not cover future executable corrections.

**Verdict: APPROVE SOURCE ONLY.** No unresolved source blocker was found in the
scope below. This receipt does not approve an artifact, action, privilege policy,
next seal, automatic queue review, application, service action or scheduler release.
Package6 was still running when this source receipt was prepared; no completion
or deterministic runtime-tree result is inferred from earlier stage success.

## Issues before corrections

No new critical or important source finding was identified. I checked the actual
589/590 notes and the maintained review chain rather than treating historical586
as the current transport. Prior rejected designs remain resolved: native587
`556d4f46`/handoff `8705e3dd` replaces request-time sudo; leader-only settlement
was replaced by unreaped group ownership plus adopted-descendant pidfds; the
standalone native test self-hash uses only its source fixture; rollback now checks
this-boot supervisor journal history as well as systemd properties; the package
census uses a strict SHA256 digest instead of an oversized environment string.
The historical `native-owner-read.patch` is not part of application inventory.
No obsolete sudo rule, general command transport or owner exception was added.

A nonblocking observation from the fresh 17-test application run is Python3.14
ResourceWarning messages for synthetic SQLite connection objects. All assertions
passed. These warnings are retained here; they are not claimed as independently
verified production failure or a reason to waive a gate.

## Owner, socket and finite supervisor source

I read both complete Python endpoint/supervisor implementations and the gateway
transport/preflight sources. The parent accepts only root/no-argument execution
inside its fixed system unit, pins the server bytes, validates the external native
HQ cgroup, and tracks the actual gateway MainPID, start identity and pidfd. Only
its newly forked endpoint writes its own PID to the preexisting fixed cgroup.procs;
no worker, gateway or unrelated PID migrates. Placement is checked after the write.
The parent stays in `/system.slice/strict542-owner.service`. Required actual kernel
permission and effective loaded-unit verification remain application prerequisites,
not facts established by source tests.

The fixed socket remains beneath root-owned nonwritable ancestry and is created
root:deploy0660; existing nodes refuse. Source-only unit policy requires the parent
directory to exist. Actual595 preflight must repeat existence, ancestry and deploy
search permission rather than changing shared directory ownership implicitly.
The inherited fd3 listener and fd4 parent pidfd carry no caller-selected command.
SO_PEERCRED supplies the peer PID; the endpoint reads its real start identity and
repeats unchanged pinned `Native510.owner_check(..., caller=True)`, including
Preservation ownership, cgroup and fixed gateway MainPID checks. Socket access
alone grants no HQ owner, accepted run, installation or provider authority.

Framing, operations, output and deadlines are bounded. Unexpected input cancels.
Success racing cancellation is rejected by the client; no receipt means unsettled.
Native children retain unreaped leader/group ownership until all group signals
finish, then adopted descendants are checked/killed using child ownership and
pidfds. Settlement must complete before any acknowledgement. Parent death,
endpoint deadline, MainPID replacement and CPU exhaustion terminate the lifecycle.
The unit's 900s/64MiB/zero-swap/5percent CPU/16-task parent bounds, inherited endpoint
96MiB address-space and30s CPU limits, aggregate descendant CPU monitor and existing
HQ cgroup budget remain. Gateway heap2304MiB and worker limits are unchanged.

Exact external native authority remains generated maintenance SHA256
`bca40971a35d160ad87b5d18fd1cc7f7730a7f90d2bb5b8480f3d7d79d11c182`,
ABH `a1d99e8e0460747293ec22a5a8dd8d14231c89d2`, reservation
`5f54474f8df103ae97f96e01dc76c895d7e5e321e0b0658d4d71de84f79ec1e0`,
generator `6adfba9ed1630897c68d0862f067626a2b2dd470fb145861263eba017a853e7c`.
The isolated application copy never replaces the installed safety generation.

## Fixed application and rollback source

Read complete application598.py/apply598.py and compared their exact delta against
previous policy review `f81194b0`: the added guarded rollback/application-owner
journal is the sole behavior addition. The action reconstructs all six fixed
targets, old/new identities, seven unchanged guard backups, exact helper hashes,
whole original seal and exclusive backup identity. Full runtime inventory rejects
escaping/broken links, hardlinks, writable/special modes and secret/state names.
Fixture evidence cannot be promoted to BUILT. Five separate exact review scopes
bind source/tree/action/receipt; real automatic608 review additionally checks actual
read-only queue rows, parent identity, exact result hash and its first APPROVE.
A label, soft hold or fabricated receipt cannot replace that gate.

Application is disk-only under the nonblocking original admission lock. It repeats
unchanged native ownership, finite dual-clock acknowledgement, registered worker,
fixture/remote settlement, queue/unit inventory, original boot, guards, original
seal bytes/metadata and every original seal entry. The next seal accepts only the
fixed additive ledger delta and independently reviewed next-seal byte digest.
Backups preserve bytes, ownership/mode, xattrs, mtime and original ctime evidence;
poison is persisted before mutation. The guard-preserving parent-descriptor writes
refuse symlink ancestors. No service-management command or root-command option
exists in the application helper.

The executable rollback requires exactly complete disk-only application, original
owner/start/boot, all six originally absent targets, exact new runtime/files/seal,
exclusive original backups, no supervisor activation/history, unchanged guards and
all original quiet/review gates. It poisons first and atomically quarantines exact
new targets, restoring only the original whole seal and restorable metadata.
EXDEV, partial application/reversal, drift, changed owner/restart or unknown state
preserve poison/backups; no recursive deletion, blind replay or automatic rollback
exists. Original ctime is evidence and is explicitly not restorable.

## Bounded build, stage and retained result evidence

Inspected required-native compiler receipt validation, native consumer rebuild,
full typed bounded package owner, per-config census driver, worker two-phase
owner, frozen-package guard, finite stage helper and exact runner. The dedicated
route preserves complete canonical typed phases and both declaration writers,
assets/UI/postbuild/publication/import/export checks; runtime-only skips and
inherited controls refuse. Full original config objects/graphs remain intact.
The SHA256 census is recomputed over the same serialization by the child. Native
AST early release, last-use counting and compact cloning preserve graph/module/
semantic identity; worker lazy-barrel and minifier phases retain source-owned
side-effect/singleton/dynamic-export policies and settle sequentially.

Required native compilation stays source-rebuilt with exact compile/libtest and
addon byte equality; no arbitrary inherited NAPI binding can be selected. Capacity
still requires observed admitted bytes above1625784320 and at most authorized4GiB,
1CPU, zero swap; heap overrides refuse. Ordinary upstream full-build4352MiB admission
is unchanged. Package parent2700000ms and compiler-stage900000ms absolute deadlines
remain, with original process-tree settlement and finite admitted outer deadline.
The four stages retain every original required check. Later stages require the
exact staged file set, pinned producing receipt/source/output identities, original
independently pinned native receipts and exact addon. Frozen original lock,
workspace/.npmrc and pnpm12.5.1 are retained; legacy deploy/fallback refuses.

I independently streamed all listed output hashes and validated receipt stage,
source591158cf and exit0 for the retained exact results:

| Stage | Stage receipt SHA256 |
| --- | --- |
| native5 | `23ff1288a1e45669e8ace6799008c6e24702084c5d44abf15ef5ebaa351feaac` |
| checks6 | `ad1915045916f15242c0d517cb46950ac1da20ca1422ca6c52f09e2fc5305c17` |
| compiler5 | `1c148a60629f96ca8b4549ea57c9aabd1b899bb04f51f00286cff4a066ba73d2` |

Original roots are respectively export608-stage-native-035255/result608-native,
export608-stage-checks-054258/result608-checks and
export608-stage-compiler-043520/result608-compiler under agentq/tmp.
Native receipt owner-input hashes match all four current source files. Its addon
is `0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042`;
complete compile/lifetime/compaction/negative-control identities remain present.
Installed tooling JSON records success,198 total/198 passing,0 failed/pending/todo.
Checks logs contain actual native-owner15, supervisor13, preparation18, application19,
apply17 and other policy suites. Compiler log records all ten real fixture checks,
including byte-equal codegen, phase spans and stock/rebuilt lazy/minifier modes.
These are reviews of retained actual results, not fresh full-suite reruns.

Fresh independent small checks at this source all exited0: supervisor13 (including
real parent SIGKILL/fd3/escaped-descendant settlement), apply17 (including rollback,
queue/quiet/seal/refusal cases), and bounded-package6 (including census/override/
typed-gate/refusal checks). Both Python runs used TMPDIR=/var/tmp and a30s timeout;
Node had30s timeout. No dependency installation, full suite/build/offload, host
cgroup write, root/service/unit/seal mutation or provider/runtime-auth operation
was performed by this review lane.

## Package6 runner annotation reconciliation

Independently compared the actual package6 export
`/home/deploy/agentq/tmp/export608-stage-package-0649` against591158cf Git blobs.
Original manifest SHA256 is
`117f527b50cdc39fad21ca6774d086945764403a7d0954bc78a63c431df98651`.
Its actual `run608.sh` SHA256
`d06e24a58bda1c787fc382d7e620758307ebd4a940869e4c045c794a553e83fb`
is byte-identical to591158cf:docs/strict542/run-stage608.sh. Actual stage608.py
SHA256 `d86232c0506dd91a7e277fbc490ac0265d544b14f6c35d1d3056f06ba5858b59`
is byte-identical to591158cf:docs/strict542/stage608.py. These are the corrected
compiler directory and census-digest era runner/helper bytes.

The manifest inherited stale descriptive `runner_commit=6648474b...` and
`source_correction_review=5ec111ba ... pending` annotations. Neither field drives
execution or the helper's stage/source/output acceptance. Actual source_commit is
591158cf, runner_sha256 matches the bytes above, and source correction reviews
c5d5b84e (checks race) and4a38e973 (census) exist. Preserve the original manifest
unchanged and bind this independent provenance reconciliation into final evidence.
The stale annotations warrant this correction receipt, not a build rerun, provided
the actual package/output/receipt gates all succeed. This paragraph does not
assert they have succeeded.

## Handoff boundary

The ordered595 handoff preserves actual finite foreground nonqueue HQ ownership
and a natural settled gap. The existing dispatcher external-wait owner remains
referenced at3c18a58; an uninstalled marker cannot bootstrap its own installation.
Read current installed dispatcher on_success alongside that historical owner:
friend-up REQUEUE now queues continuation for the next tick (2minutes), not the
old30minute delay. Therefore final595 handoff must use the referenced owner's
explicitly supported ordinary completion of SOURCE PREPARATION followed by actual
foreground HQ's natural-settled-gap attempt. Do not claim an initial timed REQUEUE
slot or reserved gap, and do not use uninstalled EXTERNAL_INSTALL_WAIT. A refused
HQ attempt records its last completed step; it cannot justify a documentation
retry loop. No direct DB/status/counter edit, detached continuation or stop/resume
bypass is supported. Restart invalidates510/515 bindings: fresh
genuine post-restart HQ owner binding AND accepted-run acknowledgements are required
before further root actions or supervisor start. Actual loaded generation, socket,
limits and parent/child placement must be verified then.575/588 remains reference
604ffc9/package1b22c4d/evidenced1304c7/review592;553 alone owns SAME510 continuation.
497 alone later submits a fresh independently reviewed scheduler request after
all original gates;503/504 observe. Approval1529 is only the two named report URLs.

The current handoff files contain explicitly superseded historical status text;
root's final update must lead with the actual package/action/review identities.
Nothing in this source approval makes package6 succeed or waives exact artifact,
action, privilege/seal or mandatory automatic queue review. No application is
approved by this receipt. A later exact-artifact binding addendum is separate.

## Current final HQ handoff review

Independently read corrected current `job608-final-HQ-HANDOFF.md`, SHA256 `097b0b1d0192b1f89267a651f5f23228ec141c24f0853c008e13a2288f2741ed`.
Approve its ordered SOURCE-PREPARATION procedure subject to its explicit pending
package/action/tree/next-seal and exact review gates. It correctly supersedes
historical status text, binds current baseline/seal proposals by reference,
requires genuine finite nonqueue ownership before ordinary worker exit, recognizes
current next-tick continuation semantics, and never claims a reserved gap. The
initial reviewed version7359dc51 included a conditional historical-timed-slot
alternative; review found that current friend-up continuation supplies no such
30minute slot. Root corrected that text before commit:595 now finishes source
preparation normally after the genuine handoff, retains it in actual HQ, and
explicitly records that no current timed gap has been established. I independently
verified this exact correction. The supported route is ordinary completion, then
the actual foreground HQ owner's nonblocking attempt in a naturally settled gap.
No new tests were run for this documentation-only correction; all original source
findings and verification results above remain unchanged.

The command sequence remains disk preflight/apply/verify, separately reviewed
service-manager actions, fresh post-restart genuine owner AND accepted-run
acknowledgements, finite supervisor start, then actual runtime/tree/seal/socket/
placement evidence and595 receipt. Refusal preserves last completed step; rollback
is restricted to complete unchanged pre-restart disk application with original
owner, verified backups, quarantine and seal. No root/action approval follows
from this source-procedure review. Final artifact identities must replace PENDING
before595 can treat this as an application-ready handoff; changed final handoff
bytes need the corresponding exact final binding review.

## Exact source identities

| Source path | SHA256 |
| --- | --- |
| `src/agents/sessions/selected-runtime-auth-read.ts` | `ed8db44e21a9d143542758cf840697dd62dbac6e88d65bc8970e203bb2cca1df` |
| `src/gateway/strict542/native-owner-transport.ts` | `bc880ed99f105872548d15669c233b7e7f568c7175f42a3f4e23332368301242` |
| `src/gateway/strict542/native_owner_server.py` | `a145387432fbf8e17fffbf1e552328e651054e9d603b1d9bdad2d8494dc6a373` |
| `src/gateway/strict542/root_owner_supervisor.py` | `0d8bdeda5e916ddc25bda48b1e3da36252a710c88dfe36f875c1b05290709fdc` |
| `src/gateway/strict542/usage-preflight.ts` | `b017b54b506a4e7a1b914b9a0fce47fc4a3441122333b96c19292b6342949450` |
| `docs/strict542/native-targets.json` | `0be3cc91f743677bd9f6ce0c688cfff399cd15efa7c71631ec4d64eac42da132` |
| `docs/strict542/application598.py` | `4a6512d153a5692964f2f4ce0e5795157e18da2bcba627a86d3f1a9c36750cb9` |
| `docs/strict542/apply598.py` | `10ff28fc821c8bcf9bcb4f288a39ef7d9f82b79bcff24a43e95b3cfb0f500153` |
| `docs/strict542/strict542-owner.service` | `ab297fe2afe0559c467ddc6e32a4c041a0cd143daad612ceabcf23571ae4f469` |
| `docs/strict542/90-strict542-598.conf` | `45634d116cd636458352514b15bc081fe9b78070444655b4ae2d069e18732ecc` |
| `docs/strict542/build598.sh` | `26dead6ff1fa4f17c0c9a5386ca1e16b61f873bef588c6dc2bccc5a364c1c976` |
| `docs/strict542/stage608.py` | `d86232c0506dd91a7e277fbc490ac0265d544b14f6c35d1d3056f06ba5858b59` |
| `docs/strict542/run-stage608.sh` | `d06e24a58bda1c787fc382d7e620758307ebd4a940869e4c045c794a553e83fb` |
| `docs/strict542/prepare-native-consumer608.py` | `3b5a7250e0d50e3b87466b578b4dd0ca55354712bbed545a2e0d20a2f3aaf06c` |
| `docs/strict542/frozen-package608.py` | `d50f132546dd4b6489c207f7d1ec8d4a9629abab1f97ecf1a32d64fcf0089c84` |
| `scripts/lib/native-compiler608.mjs` | `c3670b0b3448f64a3e247beac48c62f93596620bbb2ee92d362f45bfee77ce0a` |
| `scripts/lib/bounded-package608.mjs` | `4f35b9baaf1262f6f631f2bcf722665bdfbf2acc6a7179f864f87f70bf5c6774` |
| `scripts/lib/worker-phases608.mjs` | `61f8d142a4ca089d0ca0e61f637f748ae6c5049555c76daee5ef2f187919f0b6` |
| `scripts/lib/prepare-native608.py` | `2b3e703e536345ca023c2e47cd0c081689a4eb542fab32a664fe56674892ec94` |
| `scripts/lib/last-use-ast608.rs` | `8d293f921d754f3ffca6f60eaec8b61fc577ebef779d9c5714db5f46c4cf2da4` |
| `scripts/tsdown-bounded608.mts` | `16b3a6690878f186356ed58f8e10bde36095d100a54e142c0ae404014c2307f1` |
| `tsdown.bounded608.config.ts` | `deca5c73ac01443d72ea51778cfef01857e8b4171d8ec323bde9ab8835b9543d` |
