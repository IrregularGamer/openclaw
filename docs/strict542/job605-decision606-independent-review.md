# Independent job605 Decision606 diagnostic review

Reviewer: Rook `/root/review605`, independent from the implementation and runner.
Reviewed compiled source: `918bcd113d3f53506a64d6b6e0ff08069f5f2633`.
Decision606 authorizes one ordinary admitted diagnostic at the unchanged default
2GiB/1CPU. This review grants no application, production, action, privilege-policy,
seal or artifact approval.

## Source/export verdict: APPROVE_FOR_SINGLE_DIAGNOSTIC_ONLY

The reviewed source preserves the fail-fast floor `1625784320`, fixed native
pools of one, process-local `MIMALLOC_ALLOW_THP=0`, the complete ordered original
configuration census, the unchanged unified config15 graph, and the shared900s
compiler deadline. Inherited compiler controls and caller arguments remain
refused. No unit, cgroup, budget, owner predicate or cancellation rule is changed.
The telemetry adds read-only begin/running/end observations, never graph hooks
that transform modules or change output.

I independently checked the final manifest and every one of the86 successor
archive files against `git show` of the exact compiled source. The path set is
exactly the base-to-source diff; there are no deletions or renames. Runner bytes
match the committed `run-isolated598.sh`. The native archive hash and exact
`tools/scheduler_handoff/candidate/maintenance.py` pin were recomputed.
The690MB base archive was not rehashed again by this reviewer: its existing pin,
prior provenance and the lead's fresh rehash are relied upon, and the remote
runner independently verifies all three archive digests before extraction.

| Input | Exact identity |
| --- | --- |
| Base source commit | `c790ba44938bd90f75fb41f2f2eeaaff287df546` |
| Base source archive SHA256 | `e79a0e45a4eaea4afe325ca94ba201d5ae43d09d8c15dc07d0695c87ba743de3` |
| Compiled source commit | `918bcd113d3f53506a64d6b6e0ff08069f5f2633` |
| Successor archive SHA256 | `3cb79344cc55a859c00cdc9ab814b387b0954122540def4430cbc1421c71e111` |
| Native archive SHA256 | `d73e4e35720ffcb71856ce8168e75fa3b4fd49251fd78c811e1abded8b2701de` |
| Native handoff maintenance SHA256 | `bca40971a35d160ad87b5d18fd1cc7f7730a7f90d2bb5b8480f3d7d79d11c182` |
| Runner SHA256 | `4ddaa154badc56d2c8f1fc62def549fa52e9e8e7e7383000cb5793dc95a4c037` |
| Export manifest SHA256 | `4bdf05de7e2f01d06d8d3eb7c020f0c0538c73a62bdd2b0c384abb427236457a` |

The source-only supervisor spot-check confirms fixed self-only endpoint placement
in the preexisting exact HQ cgroup; the root parent remains in its bounded system
unit. Peer identity remains kernel SO_PEERCRED plus unchanged native predicates,
with genuine gateway MainPID/start/cgroup checks and pidfd lifetime monitoring.
Socket root:deploy0660 is not owner authority. Existing realistic tests cover
parent SIGKILL/native-tree cancellation and real fd3 escaped-descendant settlement.
The runner includes these tests and all relevant selected-session, transport,
preflight, native, application and policy tests before the diagnostic.

## Outcome and remaining gates

At the time of this source/export review the single admitted run is in progress.
No test or build success is asserted here. Actual outcome evidence requires a
separate review below when available. The reviewer did not execute offload,
full tests/build, services, runtime changes, root commands or sealed-file changes.

Even a passing isolated diagnostic is explicitly `DIAGNOSTIC_ONLY_NOT_BUILD_EVIDENCE`.
It cannot establish a complete typed build/package, deterministic artifact receipt,
exact old/new action, next seal, or loaded generation. Existing job598 source and
privilege-design approvals remain limited to those scopes. Actual independent
source/action/privilege/seal reviews and automatic queue review must precede
application. Fresh genuine post-restart foreground HQ owner binding and accepted-run
acknowledgements remain mandatory; historical510/515 identities cannot be reused.

## Actual single-run outcome review

Verdict: APPROVE_EVIDENCE_ONLY. Job605 installation preparation remains incomplete.
This is not an artifact, action, privilege-policy, seal or application approval.

I independently reviewed the recovered actual outputs under
`runs/605/decision606-final`, checked their hashes, source identity and test
summaries against the earlier independently copied partial evidence. The runner
completed101 Node tests, Python groups15+18+13+19+9, and14 policy/selection Node
tests:189 passing, no failures, skips or cancellations. Real parent-SIGKILL/native
tree cancellation, real fd3 escaped-descendant settlement, gateway MainPID change,
and idle/parent-death refusal tests are present and pass. This is review of actual
execution evidence, not a reviewer rerun of the suite.

| Actual recovered output | SHA256 |
| --- | --- |
| strict542-checks/tests.log | `ab253239ca70e6e665b9bb9fddad3c216bae380b50dcf176749e00d524ab2ac6` |
| strict542-checks/evidence.json | `c17f5866ed8df46c14ac65d9d4da31471b0e94813230346610a17d8ae2963b5a` |
| result598-isolated/probe.log | `ecdb4fdead84b96acfab45c1df4b3fa40096f895d9eb3c3b7bce1bd0337b49f9` |
| result598-isolated/exit-code.txt | `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865` |
| decision606-ancestors-after-refusal.json | `061066e8f84eab2fec5718b931c0ee8d9cc310c6c9d49842e916c6ccd8b13d07` |

The pinned pnpm12.5.1 frozen installation completed. The probe then exited1 at
`admitUnifiedGraphCapacity` before any compiler invocation. The log contains no
`ISOLATED_CONFIG_DIAGNOSTIC` or diagnostic-plan marker, and no isolated-probe598.json
was created. This run did not execute config15, time it out or OOM it. The exact
capacity value at refusal is unavailable because the source throws before
recording it. Do not infer that value from later measurements or previous runs.

The separate AFTER-REFUSAL ancestor snapshot confirms the Decision606 parent now
has memory.high=memory.max=2147483648, swap.max0, cpu.max100000/100000 and pids.max512.
Its memory.current80490496 is after cleanup, not at admission. Its memory.peak
2150412288 and memory.events are cumulative parent counters, not this run's peak,
config15 measurements, or evidence that this run OOMed. No greater-than2GiB budget
request is justified by this outcome alone.

The owning reader distinguishes capacityBytes (hard/high ceiling) from limitBytes
(remaining child allowance after competing usage, crediting only inactive_file
and this wrapper's RSS). The floor checks limitBytes. Thus the fixed2GiB ceiling
alone does not prove the floor should pass. Dependency-install active cache/slab
is a hypothesis, not an observed root cause. Comparing against capacityBytes or
crediting more reclaimable memory would change the approved guard and is not
approved here. A source correction should first preserve exact capacity and
bounded kernel evidence before admission refusal; the fixed floor stays unchanged.
No repeated unchanged diagnostic is approved by this review.

## Natural-gap continuation source status

Read-only review of agentq-ops `feature/598-external-install` commit
`3c18a585e2fed637b1fca41b60211bb28213f46b` confirms its finite optional
EXTERNAL_INSTALL_WAIT source has separate source review and129 admitted passing
tests. It is explicitly uninstalled and has no reviewed initial installation
path; it cannot bootstrap its own first gap or confer HQ authority. The initial595
procedure supports at most one available existing timed slot AFTER an actual
finite foreground HQ acknowledgement, or normal source-preparation completion
with actual HQ handoff. Natural settlement and the native admission lock must
observe a real gap; another worker winning admission is a refusal. No gap is
reserved, no detached continuation exists, and no repeated docs-only retry is
supported. The575/588 exact reviewed source/package/evidence and592 review remain
references;553 retains sole SAME510 continuation. No direct DB/status/counter
edit or historical installer is authorized by this source preparation.

## Successor refusal-message source review

Reviewed commit: `ba38e2b7cc642bbf5cbca031599ecedb1a2155d6`.
Verdict: APPROVE_SOURCE_ONLY for its two-file executable/test diagnostic correction;
APPROVE_EVIDENCE_ONLY for its preserved outcome. No new admitted run is approved
or claimed by this addendum.

The policy correction changes only the refusal message to include the already
computed capacityBytes, limitBytes, unresolved, usageKnown and unchanged fixed
floorBytes. The exact condition remains finite limitBytes strictly above1625784320.
No admission, config selection, deadline, allocator, pools, environment refusal,
cancellation, owner predicate, unit, privilege or budget behavior changes. These
numeric/boolean diagnostics contain no runtime credentials or authentication data.
The existing boundary test now verifies exact capacity/limit/floor inclusion.

Independently reran only the small affected Node policy/selection tests:
`node --test docs/strict542/serial-probe598.test.mjs docs/strict542/isolated-config598.test.mjs`.
All14 pass, zero failures/skips/cancellations. The189-test suite is the actual
prior admitted run's evidence at918bcd11; it was not rerun or relabeled as ba38e2b7.

Exact successor file SHA256 identities:

| Source | SHA256 |
| --- | --- |
| serial-probe598-policy.mjs | `07bd183a7331ba70272ede4e34e8079679c964c153167de9d0b3fd7c0e5001a5` |
| serial-probe598.test.mjs | `42e829a45841b95addb4e61fe61bdcff415d763cf2ff19ab39a382ee735c2bdc` |
| job605-decision606-outcome.json | `0ad4c1a040af088d112afd1799a4180ef2253c9856291fff4947d25abff40fe8` |

All six hashes recorded by outcome.json were recomputed and match their committed
files. The probe, offload, ancestor and two test-evidence files byte-match the
actual recovered run files. The outcome accurately states compiler/config15 never
started, exact admission value unobserved, single run, no runtime tree/action/next
seal, and all remaining build/application/HQ gates open. The successor diagnostic
message improves the NEXT supported measurement; it does not retrospectively
supply the missing admission value or turn this refusal into config15 OOM/timeout.

## Final continuation documentation review

Verdict: APPROVE_SOURCE_AND_EVIDENCE_ONLY for the final continuation note and
current-status notice at the top of the historical job598 handoff. Reviewed exact
`job605-decision606.md` SHA256
`67727f189a100b5d2972165d315cc9b41725aad46e59c5d1ce323a1a6c20586d` and
`job598-HQ-HANDOFF.md` SHA256
`5659f6eb30231be6839bfe9256a0699cdf52480764858ef7f433afcb7a06d8ea`.

The final note explicitly labels the command historical and consumed under606,
names the independent review directly, and describes prior approvals as source
and privilege-design only. It accurately records189 passing checks followed by
pre-compiler refusal, unchanged floor, unknown effective limit, cumulative parent
peak, and no second admitted run. It grants no future run, larger budget, runtime
artifact/action/seal approval, executable595 completion or production authority.
Actual complete build/package/receipt and exact independent/automatic reviews
remain open. Genuine natural-gap HQ ownership, fresh post-restart owner binding
and accepted-run acknowledgements, original seals/guards/backups/rollback/reseal,
and the reference-only575/588/592 plus sole553 continuation gates remain intact.
No tests rerun for these documentation-only changes.
