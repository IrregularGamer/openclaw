# Independent native preparation review

Verdict: APPROVE_SOURCE_PREPARATION_CONDITIONAL_REMOTE_TESTS.
The adjacent JSON pins the exact patch, target receipt, tests and README inspected.
The reviewer inspected source and hashes, without executing acquired code or native
calls. All synthetic tests must pass in the approved remote secretless export.

The patch invokes unchanged Preservation.owner through Native510.owner_check,
derives gateway PID/start locally, accepts no caller owner claims, and dispatches
before Controller construction and its potentially mutating error handler.
No authority bypass was found in this limited source preparation.

NR1 resolved in source: real harmless Python child tests exercise cancellation
and timeout through actual subprocess.run, asserting reaping and absent PID.
The SIGTERM timer starts after child creation under installed read handlers and
is cancelled/joined. NR2 resolved: identity mutation now occurs during the second
actual owner_check. Missing/malformed proc and nonzero service tests were added.
Execution results must be recorded separately, without implying reviewer execution.

The two native checks do not bracket actual HQ route/auth or provider observation.
No authenticated cancellable root gateway bridge or actual live session selection
read has been established. README explicitly preserves those unsupported boundaries.
The patch remains unapplied evidence and does not migrate native source ownership.
No usage.preflight completion, availability, installation, release, SAME535 retry
or other gate approval is granted. Quota remains UNKNOWN. Runtime and sealed files
remain untouched.
