# Job608 continuation after accepted sdk-0/sdk-1 — 595 MUST NOT APPLY

Supersedes only the NEXT pointer of job608-after-sdk0-tsccwdf6a4-continuation.md; every gate
there and in job608-after-compiler-tsccwdf6a4-continuation.md still applies.
Accepted and SPENT (never replay): sdk-0 (b9decdd6, receipt 08530815, ACCEPT abd8eff8),
sdk-1 (f28a50ab, receipt e57265f3, ACCEPT 8cbbaacd).

## NEXT FRESH WORKER: FIRST heavy action tail
Export P/stage-tail-tsccwdf6a4 UNUSED, manifest add772f5f0e861bf1a28f8ecdf1d616aea4a505af745579e192bc9e17fe3bbdb
(preflight 40043eb9, independent APPROVE 4a45d64c). Re-verify every live gate and launch ONCE exactly
as job608-tail-tsccwdf6a4-preflight.md says (>=2655s left). Recorded risk: an empty private-QA
sdk-2 partition is accepted by the declaration join; if a later tail step needs it the run fails
loudly — fix source-only, never set OPENCLAW_BUILD_PRIVATE_QA or waive checks.
Then evidence + independent acceptance; then prepare/review/run package (native, checks,
compiler, tail); then final artifact/old-new inventory, action/privilege/seal/reseal and
automatic queue reviews and the genuine ordered HQ595 handoff. Do not `git pull` source552
in a worker. 595 MUST NOT APPLY.
