# Job587 source handoff

Implemented and pushed on IrregularGamer/openclaw strict542-source552. Exact
source head: 556d4f46bb9d63bc0f25659df83c7075827f0a54. Independent verdict: APPROVE_SOURCE_ONLY.
Runtime quota remains UNKNOWN. ABH executable tools and all native predicates
are unchanged. Ordinary usage.status is byte-identical under its pinned test.

## Changes and decisions

native-owner-transport.ts replaces request-time sudo with one fixed root Unix
socket. native_owner_server.py adapts the actual external pinned native module,
using kernel gateway peer identity and the original caller=True checks twice.
Its dedicated serial endpoint settles its owned child tree before any ACK.
The source entry consumes a fixed inherited fd3; a separately approved root
supervisor and exact HQ cgroup placement remain runtime prerequisites. There is
no installation, privilege policy or unit change here.

usage.ts now requires a live client-authority guard and cancellation signal and
combines request/disconnect signals. The existing session owner/AuthStorage read
provides the exact selected usable memory lease; usage.preflight brackets GET
with invalidation checks, native checks and shared 10-second deadline and 15-second freshness rules.
No reload, refresh, fallback, second selection registry or credential response
is introduced. Nondefault/unresolved routes and unsupported states refuse.

Tests changed: native-owner-transport.test.mjs, test_native_owner_server.py and
usage-preflight.test.mjs. They cover actual Node/Python IPC, exact external
predicates with synthetic proc facts, cancellation, grandchild/adopted-child
settlement, root/cgroup/MainPID/start refusal, strict framing, invalidation,
provider-window completeness and clocks. The native patch remains historical
unapplied preparation; it is not the new transport implementation.

## Verification and reproduction

Run from a fresh committed source-only export through offload. Relocate the
pinned src/secrets/sentinel.ts source to source-owner-fixtures/sentinel.ts for
the existing offload transfer filter, verify its SHA256 from the adjacent review
receipt, and export ABH HEAD tools into native-source. Never copy env/auth files.

```sh
STRICT542_SENTINEL_SOURCE=../source-owner-fixtures/sentinel.ts NATIVE_SOURCE="$PWD/native-source" node --disable-warning=ExperimentalWarning --test --test-reporter=spec src/agents/sessions/selected-runtime-auth-read.test.mjs src/agents/sessions/selected-runtime-auth-integration.test.mjs src/gateway/strict542/native-owner-transport.test.mjs src/gateway/strict542/usage-preflight.test.mjs
NATIVE_SOURCE="$PWD/native-source" python3 src/gateway/strict542/test_native_owner_server.py -q
NATIVE_SOURCE="$PWD/native-source" python3 docs/strict542/test_native_preparation.py -q
```

All 101 Node tests, 15 native transport tests and 18 preparation tests passed
remotely with exit 0. No application build, full upstream OpenClaw suite, ABH
suite or live endpoint verification was run or claimed; no application or ABH
runtime changed. The complete scoped suites above are the synthetic evidence.

## Test exceptions and limitations

The first red Node regression case for an overlong deadline attempted the old
fixed sudo argv before the adapter was replaced. This was outside the requested
source-only boundary. No successful native owner read was observed. The test
loader now rejects production child_process imports, and source has no exec path.
Initial local imports of generated native source also read the installed native
code file solely for its self-hash. No auth/provider data was read. The remote
fixture exposed that assumption; tests now bind __file__ to source archive only.
Two initial remote fixture runs failed and are not passing acceptance evidence.

The root endpoint is not installed and no live owner/session/provider availability
was established. No provider or HQ/model request, auth store operation, runtime
installation, deployment, email or production change was performed by this work.
The exception above must not be summarized as no native attempt.

## Security and follow-ups

Assets: native ownership and selected session credentials. Boundaries:
authenticated operator to gateway, kernel peer to fixed root endpoint, exact
native owner to observation, and session lease to one GET. Refusals cover
cross-process impersonation, owner replacement, stale auth, process-tree leaks,
malformed/late receipts and missing cancellation settlement. No secrets added.

Only a separately authorized supervised release may provision the dedicated
root endpoint, fixed socket and external native generation. Runtime unsupported
states stay UNKNOWN. All HOLD497/503/504,507/509/512/521/524/516/539, actual HQ
Pinch outside queue, SAME535 freshness/exact review/loaded-resume/settlement/
preservation and fresh497 gates remain. Approval1529 is ONLY INTERNAL_REPORT_URL/
API_BASE_URL. Only497 later submits scheduler-request. No new approval is sought.
