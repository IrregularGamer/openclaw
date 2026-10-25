# Job586 strict542 usage.preflight source implementation

Source only. Nothing was installed, built, linked, restarted or deployed. No
provider, native root operation, sudo rule, credential, config or HQ session
was touched. Quota remains UNKNOWN at runtime.

Implementation commits on strict542-source552 (descending from authenticated
release bcfc88812a35243893585dbeca87ca41b48272ca): c789545c and 2e6544a3.

## Mechanism

- `src/gateway/strict542/native-owner-transport.ts`: fixed, shell-free argv
  `/usr/bin/sudo -n /usr/bin/python3 /usr/local/libexec/agentq-safety/control.py
  owner542-read --deadline-ns N`, the CLI prepared in native-owner-read.patch.
  That native read calls the EXISTING `Native510.owner_check(caller=True)`
  (Preservation.owner plus gateway MainPID) twice. TypeScript only decodes the
  strict owner record; it never evaluates ownership. The native side gets the
  shared deadline minus 1.5 s; the gateway sends SIGTERM there (the native
  cancellation acknowledgement), SIGKILL 0.5 s before the shared deadline, and
  resolves only on child close. Unsettled at the deadline is UNKNOWN.
- `src/gateway/strict542/usage-preflight.ts`: exact542 request keys, one
  monotonic deadline from handler entry (at most 10 s). Order: agent/session
  and owner shape; job574 in-memory lease of the concrete active HQ session
  (provider, model, api, baseUrl, OAuth expiry); native owner before; lease
  assertCurrent; single provider GET; lease assertCurrent; native owner after
  (must equal before); lease assertCurrent; clock and freshness checks
  (expiresAt = providerObservedAt + 15 s). Verified identity fields are null
  unless the whole chain passes.
- Provider read: one GET to the default Anthropic OAuth usage endpoint with
  the already selected in-memory token, only when the session route is the
  default Anthropic route. No redirect, cache, retry, refresh, fallback, store
  read or persistence; error bodies discarded; 64 KiB streamed cap.
- Windows: unrecognised non-null fields are UNKNOWN; any reported window at or
  above 100% is UNAVAILABLE; otherwise 5h, 7d and the selected model family's
  weekly window must all be present and finite, else UNKNOWN.
- `usage.ts`: `usage.preflight` handler, authenticated operator reader only,
  forwards caller cancellation and drops the result if client authority ends.
  `core-descriptors.ts`: appended operator.read row. `usage.status` handler is
  byte-identical (sha256 pinned in tests).

## Verification

Remote offload (friend VPS, source-only export): 44 strict542 tests (synthetic
identity, auth, fake clock, transport, real child processes for SIGTERM,
SIGKILL and settlement), 59 job574 memory tests and 18 native preparation
tests, exit 0. Independent exact review: job586-independent-review.md.

## Still unsupported at runtime (UNKNOWN)

- owner542-read is a prepared patch, not installed; no sudoers rule exists.
  Every live call therefore returns `owner_native_unavailable` or
  `owner_native_refused`.
- A SIGKILL to sudo is not relayed to the root child; the native side bounds
  itself with its own earlier deadline and subprocess timeout.
- The live Anthropic usage response shape was never contacted or verified.
- The outer caller (at most 15 s with transport cancellation) belongs to the
  later 497/535 caller and is not part of this source.

Any installation requires separate supervised authorization. HOLD497/503/504
and 507/509/512/521/524/516/539 remain; all SAME535 and fresh497 gates remain.
