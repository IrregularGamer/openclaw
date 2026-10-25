# Job587 source integration plan

The fork owns transport only. ABH remains the external owner of the exact
Preservation.owner and Native510.owner_check predicates. A root endpoint must
already be placed in the gateway cgroup by a separately authorized installation.
This job performs no installation, privilege setup or native request.

1. Replace request-time sudo with a fixed Unix socket transport. Authenticate
   the gateway peer through SO_PEERCRED and both existing owner checks with
   caller=True. Load only the pinned external generated native module, without
   Controller construction or the mutating CLI error path.
2. Use one absolute monotonic deadline of at most 10 seconds. A cancellation
   message receives a settled acknowledgement only after the native runner has
   terminated and reaped its fixed systemctl child. Refuse absent, malformed,
   late, unauthenticated or unacknowledged results. Never use a success callback.
3. Keep the existing session-owner memory lease and exact542 preflight, checking
   lease invalidation before and after the provider GET. Preserve usage.status.
4. Run source-only acceptance/refusal tests remotely, including actual pinned
   predicates over synthetic proc data, real harmless subprocess cancellation,
   session invalidation, applicable windows, freshness and deadlines. Commit and
   push each logical step, obtain independent exact review, fix findings.

Assets: native owner authority and selected private session credentials.
Boundaries: authenticated operator to gateway, gateway peer to root endpoint,
existing native owner to read-only observation, session lease to provider GET.
Refuse peer replacement, cgroup drift, root loss, pin drift, stale auth, expired
deadlines and unsettled cancellation. Return no credential or raw provider error.
All original holds, SAME535 gates, approval1529 limits and fresh497 gates remain.
Runtime quota stays UNKNOWN until separately authorized installed mechanisms
and all original live gates are proven. No production release is authorized.
