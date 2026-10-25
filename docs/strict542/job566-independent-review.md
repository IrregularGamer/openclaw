# Job566 independent exact source review

Reviewer: independent Codex subagent, source-only review on 2026-10-25.
Reviewed fork commit: 414710046668334ae2d73dc37389ba2f14714e2c,
including the exact diff from67c66ba.
Release source remains bcfc88812a35243893585dbeca87ca41b48272ca.
Native input pins remain those in native-targets.json, ABH
a1d99e8e0460747293ec22a5a8dd8d14231c89d2. This review approves only the
additional preparation tests and the accurate unsupported-boundary record.
Job566 is INCOMPLETE. Native transport and session-selected auth snapshot remain
UNSUPPORTED; quota remains UNKNOWN. No usage.preflight approval is given.

## Exact ownership and transport findings

The native preparation targets the existing ABH reservation.py and generator,
not an actual migrated native owner maintained in this fork. The README and
native-targets.json agree with that source layout. Applying the patch to ABH
would violate evidence-only scope; copying Preservation.owner into OpenClaw
would create a competing predicate owner. Neither is an integration solution.

The actual ABH Preservation.owner at
tools/scheduler_preservation/preservation.py:112-122 checks effective root,
fixed Pinch/HQ identity, gateway cgroup and process start. Its caller=True
branch independently requires /proc/self/cgroup to be the exact HQ cgroup.
Native510.owner_check at tools/scheduler_handoff/reservation.py:86-93 calls
that actual predicate and additionally checks current service MainPID. A valid
gateway target plus a root queue caller still fails. A separate root service
cannot claim the existing caller requirement merely by possessing root.

Inspected OpenClaw transport has real ordinary-process cleanup mechanisms:
src/process/exec-spawn.ts:125-175 awaits child settlement and retained cleanup,
and propagates cleanup failure; src/process/exec-runner.ts:157-159 requires
process-tree ownership for extinction, and298-304 awaits termination settlement.
These are useful primitives, not authenticated privileged native authority.
src/process/spawn-broker/execa-types.ts:9-39 exposes no uid/gid elevation option.
src/process/exec-spawn.ts:368-432 forwards argv and options to the broker or
execa, with cancellation and custody retention. The host preparation adapter at
src/agents/bash-tools.exec-host-spawn.ts:6-40 returns shell argv/env/cwd/stdin
settings. None of these inspected surfaces authenticates operator-read context
to the existing root/HQ-caller native read or proves cross-privilege sudo child
cancellation acknowledgement and settlement. No live experiment was performed.
This is a bounded source finding, not a claim about all possible transports.

## Exact session/auth findings

src/agents/harness/session-runtime-ownership.ts:12-60 fences its registered
harness/session binding, but may use a previous-session row lookup. Its return
type at src/agents/harness/types.ts:20-25 contains optional modelRef and auth
ownership classification only, not a selected usable memory credential or
invalidation epoch. It is not the requested coherent auth snapshot.

src/agents/sessions/auth-storage.ts:399-411 is provider-keyed and construction
reloads storage. Runtime overrides are a separate private map, mutated at450-459.
get at567 reads stored provider data and omits that higher-priority override.
getApiKey at715-743 checks runtime overrides first, then readiness and resolution;
resolveStoredOrFallbackApiKey at747 onward can reload refresh-fenced credentials.
Consequently neither provider-wide get nor a fresh facade nor getApiKey is a
permitted replacement for an owner-provided selected session snapshot. No auth
storage instance, resolver, fallback or refresh was invoked in this review.

## Exact test review and limits

The4147100 diff adds three negative tests without changing predicates or the
unapplied native patch: valid target plus queue caller, second-check caller
cgroup loss, and second-check root loss. I inspected each assertion. The first
separates target identity from caller identity; the second and third prove
the actual second owner predicate rejects lost caller/root authority. Their
expected subprocess counts also reject passing by skipping the relevant check.

I independently inspected /home/deploy/agentq/runs/566/remote-tests.log, which
reports18 tests run and OK. Its SHA-256 is
7c71c69c1463bbacd0a81857f0335e72f46ea18bafea5761af5e337a8998af57.
The tested file SHA-256 is
e1898171bf4d71ea0bb7c0b8f8b91059cd3c302fbaca90d2039c2530585fd8da.
The builder reports offload session30709 completed with exit0. The suite remains synthetic preparation coverage,
including harmless child cancellation, not privileged transport, session/auth,
provider GET, quota, installed runtime or usage.preflight coverage. Exact remote
execution/export receipts belong to the accompanying builder receipt.

No blocking defect was found in this preparation-only diff. Both concrete
prerequisites remain absent at the inspected boundary. Implementing schema,
provider windows, shared10s cancellation deadline and15s freshness must wait
for those actual mechanisms. Existing usage.status and executable sources are
unchanged. No installation or overall558/566 completion is approved.

All558 restrictions, HOLD497/503/504,507/509/512/521/524/516/539, actual HQ
Pinch outside queue, SAME535 freshness/exact review/loaded-resume/settlement/
preservation and fresh497 gates remain. Approval1529 covers only
INTERNAL_REPORT_URL/API_BASE_URL; only497 may later submit scheduler-request.
No new action hash, native request, provider probe, HQ turn, auth read or write,
config/registry/journal/unit/seal write, generation, installation, restart,
Docker, deployment, email or production operation was performed or authorized.
