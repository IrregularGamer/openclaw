# Job608 continuation after accepted sdk-0 — 595 MUST NOT APPLY

Supersedes only the NEXT pointer of job608-after-middle-tsccwdf6a4-continuation.md; every
gate there and in job608-after-compiler-tsccwdf6a4-continuation.md still applies.
Accepted: sdk-0 (actual b9decdd6, receipt 08530815eecb839d20085cae5ccd53fccd356eeb45b775548bd68587c0ce96b0,
checkpoint 09f9d2b8… in P/stage-sdk-0-tsccwdf6a4/result608-sdk-0, independent ACCEPT abd8eff8).
sdk-0 stage SPENT; never replay it.

## UPDATE: sdk-1 also ran in the same worker (evidence f28a50ab, ACCEPT 8cbbaacd); NEXT is tail per job608-tail-tsccwdf6a4-preflight.md

## (historical) NEXT FRESH WORKER: FIRST heavy action sdk-1
Export P/stage-sdk-1-tsccwdf6a4 prepared UNUSED, manifest
1474cff7f4da3873e348d8662f5e85a6a4f918cba405292ee532a020c5e461f0 (preflight 856fe90d,
independent APPROVE 647d59af). Re-verify all live gates (health up, no competing run,
df / >=1GB, storage608 check --stage sdk-1 0, verify-inputs0, sh -n0, exact manifest pin,
result608-sdk-1 and sibling sdk-1-tsccwdf6a4-offload.log/.rc absent, >=2655s left), then ONCE:
```sh
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-sdk-1-tsccwdf6a4
offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-sdk-1 -- timeout -k 15s 2400s sh run608.sh > ../sdk-1-tsccwdf6a4-offload.log 2>&1
printf '%s\n' "$?" > ../sdk-1-tsccwdf6a4-offload.rc
```
Then actual evidence commit and separate independent acceptance. Then prepare/review/run
tail (inputs native, middle, sdk-0, sdk-1), then package (native, checks, compiler, tail);
then final artifact/old-new inventory, action/privilege/seal/reseal and automatic queue
reviews and the genuine ordered HQ595 handoff. Do not `git pull` source552 in a worker.
595 MUST NOT APPLY.
