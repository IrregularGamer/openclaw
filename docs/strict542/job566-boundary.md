# Job566 exact unsupported boundary

Status: INCOMPLETE. Native gateway transport UNSUPPORTED. Session-selected auth
read UNSUPPORTED. Quota UNKNOWN. No usage.preflight implementation or completion
claim. Existing usage.status and all executable sources remain unchanged.

The inspected base is67c66ba838cdc182e4f137d8dc0abed8520ed029 on
IrregularGamer/openclaw strict542-source552, based on release
bcfc88812a35243893585dbeca87ca41b48272ca. Existing native-targets.json remains
the exact source pin. The558 native patch remains unapplied.

The concrete native source owner is still ABH tools/scheduler_handoff/reservation.py
and its build_candidate.py generator, incorporating the existing
tools/scheduler_preservation/preservation.py predicate. The fork contains their
preparation patch, not a migrated maintained native source owner. Job566 forbids
changing executable ABH tools and copying the predicate into a competing owner.
Neither an independent OpenClaw predicate nor applying the patch in ABH would
satisfy that source-ownership boundary. No source migration was performed or
implicitly authorized by this receipt.

The actual predicate at preservation.py:112-122 requires euid0, fixed Pinch/HQ
identity, current gateway cgroup/start, and, with caller=True, the caller's own
exact HQ gateway cgroup. Native510.owner_check at reservation.py:86-93 additionally
checks service MainPID. A root queue process with a valid gateway target still
fails the caller check. A separate root broker service would also need to satisfy
this existing caller boundary; root alone is insufficient.

The inspected OpenClaw host spawn adapter
src/agents/bash-tools.exec-host-spawn.ts:6-40 returns shell/argv/env/cwd/stdin
options, without authenticated root elevation. Process-tree cleanup in
src/process/child-process-tree.ts:24-48 invokes platform signaling and reaping;
it is not an authenticated privileged read protocol. These facts do not prove
settlement of a sudo descendant across a privilege boundary. No sudo experiment,
native live request, or privilege-policy write was attempted. No injectable
success callback, default owner, caller echo or PID-only substitute was added.

The second prerequisite remains independently unresolved. At
src/agents/sessions/auth-storage.ts:450-458 runtime override writes are separate
from stored provider credentials. getApiKey at715-743 checks that override first,
then readiness and stored/fallback resolution; resolveStoredOrFallbackApiKey
at747 onward can reload. getAuthStatus at624 onward checks stored credentials
first and can call a fallback resolver. Neither is a suitable selected session
snapshot. No resolver or storage instance was constructed or called.
src/agents/harness/types.ts:20-25 exposes modelRef and auth ownership only,
without the selected usable in-memory credential or an auth invalidation epoch.
Provider-wide get, configured status, run authority and a second registry do not
establish session provider/model/auth coherence before and after a provider GET.

Three additional preparation tests separate the gateway target from the caller:
root with a valid gateway but queue caller, caller cgroup loss at the second
owner check, and root loss at that check. They exercise the existing predicates
and the exact unapplied read patch using synthetic identity, never host authority.
Passing them proves refusal behavior only. Remote receipt and independent review
are recorded separately. These tests do not establish either missing mechanism.

The next integration must occur at an actual maintained native owner and provide
an authenticated operator-read to root/HQ-caller transport with acknowledged
cancellation and settlement. The actual session selection owner must provide its
current provider/model/selected usable memory auth and invalidation across GET.
Only after both exist can exact542 schema/operator policy, applicable provider
windows, shared10s cancellation deadline and15s freshness be implemented. No
provider endpoint or credential can be selected safely from the present evidence.

All558 restrictions and HOLD497/503/504,507/509/512/521/524/516/539 remain.
Actual HQ Pinch stays outside queue. SAME535 freshness, exact independent review,
installed/loaded generation, validated resume, settlement/preservation receipts
and fresh497 gates remain mandatory. Approval1529 covers ONLY
INTERNAL_REPORT_URL/API_BASE_URL; only497 later submits scheduler-request.
No auth materialization, refresh, fallback, persistence, provider probe, HQ turn,
535 generation/stage/retry, credential/config/registry/journal/unit/seal write,
runtime installation/build/link/onboard/restart/provider setup, Docker/deploy,
email or production change occurred. No new S question or approval is requested.
