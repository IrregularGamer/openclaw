# strict542 native read preparation (job558)

Status: PREPARATION_ONLY. Gateway binding UNSUPPORTED. Quota UNKNOWN.
`usage.preflight` is deliberately unimplemented: its native and route/auth
prerequisite has not been established. Ordinary `usage.status` is unchanged.
This is not completion of job558's requested live-route binding.

## Exact source preparation

The maintained branch remains based on authenticated release source
bcfc88812a35243893585dbeca87ca41b48272ca, acquired by552. No locator or
acquisition was repeated. `native-targets.json` pins the existing native
owner's source inputs in ABH a1d99e8. The patch is retained here as preparation
because ABH is evidence-only and its tools own the current native generator.
It changes no executable ABH source, generated candidate or sealed/live file.
No maintained native owner source has been migrated into this OpenClaw fork.

The patch appends one read to the existing native component and extends its
existing generator. It derives PID/start from the fixed gateway service and
proc identity. It calls existing `Native510.owner_check` with `caller=True`
twice, thereby using existing `Preservation.owner` unchanged. It accepts no
owner claim and constructs no Controller. CLI dispatch occurs before both
Controller construction and the normal error path, which can stop the system.
The shared absolute host-monotonic deadline must have at most10 seconds left.
Each systemctl child uses the remaining budget; cancellation raises inside
`subprocess.run`, whose exception path kills and waits for its child. It reads
no config, auth store, fence, registry, journal or generation. Successful output
is only a native owner observation, never a quota or route/auth attestation.

## Concrete missing binding, no fake availability

The native CLI has only mutation-oriented preservation/reservation operations.
There is no inspected supported authenticated operator-read transport to this
new read. A direct gateway subprocess is not root. A sudo wrapper has not
established cancellation acknowledgement and reaping across the privilege
boundary. A caller callback, PID-only reader or default owner would manufacture
authority. None is supplied. The prepared CLI command is NOT an available
bridge and was never invoked against the host. Its eventual native integration
must use the existing owner source and receive its own exact independent
review; this file approves no installation or privilege-policy change.

Actual session selection is a second distinct boundary. At the pinned source:

* `src/agents/harness/session-runtime-ownership.ts:15` delegates to the registered
  harness and fences its current session binding. The return type at
  `src/agents/harness/types.ts:20` reports model ownership and optional modelRef,
  plus auth ownership classification, without a usable credential or auth epoch.
  Its predecessor lookup can read a session row; it is not a pure in-memory
  route/auth snapshot for this task.
* `src/agents/sessions/auth-storage.ts:567` has an in-memory `get(provider)`.
  This alone is not the selected credential: `getApiKey` at715 gives runtime
  overrides precedence, performs readiness assertions, and delegates to a path
  at747 that can reload refresh-fenced credentials. Calling that resolver is
  forbidden here. A provider-wide `get` is not a verified session auth binding.
* `src/agents/embedded-agent-runner/run-state.ts:124` registers run/tool
  authority. It does not expose a session model plus selected usable credential
  snapshot. Upstream run/placement authority is not native HQ Pinch ownership.

This is a bounded inspected-source result, not an exhaustive absence claim.
The exact remaining correction is an owner-provided, nonpublishing session read
that fences actual model/provider and selected already-usable credential
identity, expiry and invalidation before/after GET, together with the native
transport above. It must cover runtime override, native-harness auth ownership,
session replacement, auth invalidation and ambiguous/unavailable selections.
Do not add a second selection registry or resolve credentials on a read miss.
The gateway must invoke that actual owner read from authenticated operator-read
context under one cancellation/deadline scope. Only after both boundaries exist
may exact542 protocol/schema/policy/provider parsing and all acceptance/refusal
cases be implemented. No always-success fixture establishes availability.

## Validation and threat model

`test_native_preparation.py` applies the patch to exact source hashes, runs the
source-only native generator in a secretless export, and uses the resulting
actual `Preservation.owner` and `Native510.owner_check` in synthetic cases.
It tests identity derivation, root, cgroup, start/MainPID changes, deadline,
cancellation and CLI separation from mutation paths. It is not a live native,
transport, provider, quota or route/auth test. Run only under approved remote
placement with `NATIVE_SOURCE` pointing at an ABH HEAD source archive:

```sh
NATIVE_SOURCE="$PWD/native-source" python3 docs/strict542/test_native_preparation.py -q
```

Assets: native owner identity and future read-only quota authority. Boundaries:
operator authentication, root/native cgroup identity and private session/auth
selection. Caller echo, queue-owner substitution, stale identity, expired or
mutating auth resolution, detached cancellation and late publication must
refuse. This preparation removes none of those gates. No credential values,
profile IDs, account email or raw provider errors are returned. No product,
authentication, tenant or billing behavior changes. No dependencies added.

HOLD497/503/504 and507/509/512/521/524/516/539, historical discrepancies,
actual HQ Pinch outside queue, and all SAME535 freshness/exact reviews,
installed/loaded generation, validated resume, settlement and preservation
receipts remain mandatory before fresh497 gates. No new action hash exists.
Approval1529 is ONLY INTERNAL_REPORT_URL/API_BASE_URL. Only497 later submits
scheduler-request. No native request, HQ/model turn, provider probe, auth store
read/refresh/fallback/persistence, runtime/config/registry/journal/unit/seal write,
535 generation/staging/retry, manual494/chattr, installation/build/link/onboard,
restart, Docker/deploy, email or production change is authorized or performed.
