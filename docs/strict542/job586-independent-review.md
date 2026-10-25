# Job586 independent exact source review

Reviewer: separate independent review agent (read-only), not the implementer.
Scope: exact commits c789545c and 2e6544a3 on strict542-source552 against the
exact542 contract (ABH docs/reliability/scheduler-quota542-independent-handoff.md).

Round 1 (c789545c): CHANGES. Handler did not forward caller cancellation or
check client authority; unrecognised/extra windows were ignored; the token
destination was not tied to the session route; utilization above 100 was
UNKNOWN not UNAVAILABLE; provider body read before the size check.

Round 2 (2e6544a3): APPROVE at source level only, no runtime claim. All six
findings addressed; 44 local strict542 tests pass. Confirmed: TypeScript never
evaluates ownership (decodes the native Native510.owner_check result only);
one monotonic deadline from handler entry covers session capture, native
before, provider GET, revalidation and native after; no store read, refresh,
fallback, cache, retry or redirect; secrets and provider bodies not returned.

Non-blocking residuals: signal and hasCurrentClientAuthority are optional in
handler options, so a transport without them only cancels at the deadline;
sudo does not relay SIGKILL to the root child (bounded by its own earlier
deadline, not enforced by the gateway); the strict field list may keep the
live result UNKNOWN until the real response shape is verified.

Not runtime-supported: owner542-read and its sudoers rule are not installed,
so live calls end UNKNOWN; the provider endpoint was never contacted; nothing
was built or deployed. Quota remains UNKNOWN.
