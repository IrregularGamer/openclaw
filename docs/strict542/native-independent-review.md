# Independent native preparation review

Verdict: APPROVE_SOURCE_PREPARATION_ONLY.
Exact reviewed commit: e29b79c81f6b10ccff525dba511b0a6e37df633c. The adjacent JSON
pins the patch, target receipt, tests and README. Exported copies match all four
pins and both ABH native target hashes. The reviewer inspected the actual bounded
remote log: 15 tests in 0.743s, OK. The implementer reports remote exit0.
Log SHA256: cde40f581abab24350a83a3e38674a22976d030eaf2a489a0be5a49f6529e18e.
The reviewer did not execute acquired code or native calls.

The patch invokes unchanged Preservation.owner through Native510.owner_check,
derives gateway PID/start locally, accepts no caller owner claims, and dispatches
before Controller construction and its potentially mutating error handler.
No authority bypass was found in this limited source preparation.

NR1 resolved: actual harmless Python child tests cover cancellation and timeout,
asserting reaping and absent PID; the timer starts under installed read handlers
and is cancelled/joined. NR2 resolved: identity mutation is tested during the
second actual owner_check. Missing/malformed proc and nonzero service tests pass.

Job558 overall remains INCOMPLETE. The two native checks do not bracket actual
HQ route/auth or provider observation. No authenticated cancellable root gateway
bridge or actual live session selection read has been established. usage.preflight
is unimplemented. README explicitly preserves these unsupported boundaries.
The patch remains unapplied evidence and does not migrate native source ownership.
No availability, installation, release, SAME535 retry or other gate approval is
granted. Quota remains UNKNOWN. Runtime and sealed files remain untouched.
