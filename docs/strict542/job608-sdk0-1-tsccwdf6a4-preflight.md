# Job608 sdk-0/sdk-1 tsccwdf6a4 preflight — 595 MUST NOT APPLY

Two NEW UNUSED exports prepared 2026-10-29T18:2xZ by unchanged prepare-stage608-export.py
(sha256 1e701de0…, == f6a4de2e) under ulimit -v 512MiB, both rc0:
`--base P/stage-unified-0-tsccwdf6a4 --commit f6a4de2e --stage sdk-N
 --input P/stage-native-tsccwdf6a4/result608-native --input P/stage-middle-tsccwdf6a4/result608-middle`
(STAGES['sdk-N'] = native, middle). Middle actual f6a6802d, receipt 9eb3083c, independent ACCEPT 28eb3762.
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private.

| stage | directory | manifest sha256 |
|---|---|---|
| sdk-0 | P/stage-sdk-0-tsccwdf6a4 | 933ed22177cbb1121faeed9922d28bbd493b945c6bb6d806dd35e43dabd5891f |
| sdk-1 | P/stage-sdk-1-tsccwdf6a4 | 1474cff7f4da3873e348d8662f5e85a6a4f918cba405292ee532a020c5e461f0 |

Copies: job608-sdk-{0,1}-tsccwdf6a4-export-manifest.json. Same freeze, source_export e81e07d2.
Fresh at preparation: verify-inputs0, sh -n0, storage608 check --stage sdk-N 0 (return cap 32MiB).
Unchanged runner keeps its fixed 2280s inner build budget and all gates.
No result/log/rc exists. This worker had 2146s left: NOT launched.

## One stage per admitted finite run, sdk-0 then sdk-1
Fresh worker FIRST heavy action, all live gates of job608-after-compiler-tsccwdf6a4-continuation.md
(health up, no competing run, df / >=1GB, storage608 check0, verify-inputs0, sh -n0, exact
manifest pin above, result/sibling log/rc absent, >=2655s left AFTER preflight). Replace N
only with the manifest-selected 0 or 1:
```sh
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-sdk-N-tsccwdf6a4
offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-sdk-N -- timeout -k 15s 2400s sh run608.sh > ../sdk-N-tsccwdf6a4-offload.log 2>&1
printf '%s\n' "$?" > ../sdk-N-tsccwdf6a4-offload.rc
```
One launch spends that stage. After each: actual evidence commit then separate independent
acceptance. If a worker has >=2655s left after an accepted run, the next stage may launch in
the same worker (middle took +309s build, ~12 min total). Never detached.
