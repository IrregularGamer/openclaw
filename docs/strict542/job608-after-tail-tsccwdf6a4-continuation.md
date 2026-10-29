# Job608 continuation after accepted tail — 595 MUST NOT APPLY

Supersedes only the NEXT pointer of job608-after-sdk-tsccwdf6a4-continuation.md. All earlier gates
still apply. Accepted and SPENT (never replay): tail (836b3d66, receipt 8df9caa8, cap fix 8f4fb3b3,
ACCEPT 6fdaddd5).

## NEXT FRESH WORKER: FIRST heavy action package
Export P/stage-package-tsccwdf6a4 UNUSED, manifest 9064b9ea579d366f5d04978030a2a95a5fc1b3eb43f8758386bcb303a3ff9a38.
Launch ONCE exactly as job608-package-tsccwdf6a4-preflight.md says, and only once its independent preflight
review ends with APPROVE. Then evidence and independent acceptance, then the final artifact and old/new
inventory, the action/privilege/seal/reseal and automatic queue reviews, and the genuine ordered HQ595
handoff. Do not `git pull` source552 in a worker. 595 MUST NOT APPLY.

Package preflight independent APPROVE 1cc5bf20. Carry its risks into acceptance. R1: there is no inner
build budget, so a kill by the outer 2400s limit is rc124/137 and fails loudly. R2: a result over the 2048MiB
cap is REFUSED; never raise the cap after the fact. R3: the receipt has no output hashes, so acceptance must
pin them via result-files.sha256/tree.json.
