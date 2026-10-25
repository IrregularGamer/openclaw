# strict542 source integration

The maintained fork now contains the native socket transport, selected-session
memory read and usage.preflight source. Source completion does not establish
runtime availability. Quota remains UNKNOWN until the separately supervised
installation and original live gates succeed. Nothing was installed here.
Ordinary usage.status is unchanged.

## Current maintained source

The branch strict542-source552 descends from authenticated release
bcfc88812a35243893585dbeca87ca41b48272ca. Job574 supplies the selected in-memory
session/auth lease; job586 supplies exact542 preflight; job587 replaces its
unverified request-time sudo path with a fork-owned native socket adapter.

* src/gateway/strict542/native-owner-transport.ts uses the fixed root-owned
  /run/agentq-safety/owner542.sock endpoint. It launches no process. It requires
  a correlated settled receipt and channel completion before the shared
  absolute monotonic deadline, at most 10 seconds. Cancellation requires an
  explicit cancelled and settled receipt. Missing acknowledgement refuses.
* src/gateway/strict542/native_owner_server.py owns only transport and bounded
  subprocess lifetime. A separately authorized dedicated root supervisor must
  supply its fixed listening socket at fd3 and place it in HQ's exact gateway
  cgroup. No socket creation, privilege transition or installation is supplied.
  SO_PEERCRED derives the gateway peer PID. Existing Native510.owner_check with
  caller=True invokes Preservation.owner twice and checks fixed service MainPID.
  The adapter constructs neither Controller nor a competing ownership predicate.
* The native module is an EXTERNAL pinned reference to the existing generated
  ABH handoff maintenance.py, SHA256
  bca40971a35d160ad87b5d18fd1cc7f7730a7f90d2bb5b8480f3d7d79d11c182.
  The bytes checked are the bytes compiled. The generated module also reads its
  own source for its loaded hash; tests bind that identity to their source
  archive. native-targets.json retains the exact generator input pins.
* The root endpoint retains the native leader unreaped until all process-group
  signals finish. As a dedicated serial Linux subreaper it reaps adopted
  descendants, including escaped sessions, using kernel child ownership and
  pidfds. It sends no settlement receipt if settlement cannot be proved in time.
* The actual session/AuthStorage owners supply selected provider/model, route,
  usable memory credential, expiry and invalidation lease through the existing
  active-run projection. No provider-wide storage selection or second registry
  is used. Capture/refusal and before/after GET checks perform no store reload,
  materialization, refresh, fallback or persistence.
* usage.preflight requires authenticated operator.read policy, a live authority
  guard and cancellation. Request and connection cancellation are combined.
  It checks the session lease and native identity before and after the single
  bounded provider GET, rejects incomplete applicable windows, and publishes
  no credential. Freshness is at most 15 seconds from provider observation.

## Source-only verification

See job587-independent-review.md and job587-source-handoff.md for exact commit,
remote acceptance/refusal results and limitations. The tests use actual pinned
native predicates with synthetic proc identity and harmless subprocesses. A real
Node to Python Unix transport test covers acceptance, cgroup refusal and settled
cancellation. The ordinary preflight tests cover schema/policy, session/auth
invalidation, applicable windows, fake clocks and deadline/freshness refusal.
No test result is a live HQ owner, usable credential or quota observation.

The earlier native-owner-read.patch and test_native_preparation.py are retained
as historical preparation of the same external owner contracts. That unapplied
CLI patch is not the transport used by current fork source. Historical job566,
574, 578 and 586 notes describe their exact reviewed commits, not current head.

## Unchanged release restrictions

ABH remains evidence-only; no executable ABH tool or native predicate changed.
No new action/hash approval exists. HOLD497/503/504,507/509/512/521/524/516/539,
actual HQ Pinch outside queue, historical discrepancies and all SAME535 fresh,
exact-review, installed/loaded-resume, settlement/preservation and fresh497
requirements remain. Approval1529 is ONLY INTERNAL_REPORT_URL/API_BASE_URL.
Only497 later submits scheduler-request.

No provider probe, HQ/model turn, auth store read/refresh/fallback/persistence,
535 generation/stage/retry, credential/config/registry/journal/unit/seal write,
installation/build/link/onboarding/restart/provider setup, Docker/deploy/email or
production change is authorized by this source work. The job587 handoff records
an initial regression test's accidental attempt of the OLD sudo path explicitly.
Unsupported native, session, provider or settlement boundaries remain UNKNOWN.
