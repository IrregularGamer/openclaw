# Job608 tail tsccwdf6a4 preflight — 595 MUST NOT APPLY

NEW UNUSED export prepared 2026-10-29T19:0xZ by unchanged prepare-stage608-export.py
(sha256 1e701de0…, == f6a4de2e) under ulimit -v 512MiB, rc0:
`--base P/stage-unified-0-tsccwdf6a4 --commit f6a4de2e --stage tail
 --input P/stage-native-tsccwdf6a4/result608-native --input P/stage-middle-tsccwdf6a4/result608-middle
 --input P/stage-sdk-0-tsccwdf6a4/result608-sdk-0 --input P/stage-sdk-1-tsccwdf6a4/result608-sdk-1
 --dest P/stage-tail-tsccwdf6a4`
(STAGES['tail'] = native, middle, sdk-0, sdk-1). Accepted inputs: middle 28eb3762 (receipt 9eb3083c),
sdk-0 abd8eff8 (receipt 08530815), sdk-1 8cbbaacd (receipt e57265f3).
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private.

| stage | directory | manifest sha256 |
|---|---|---|
| tail | P/stage-tail-tsccwdf6a4 | add772f5f0e861bf1a28f8ecdf1d616aea4a505af745579e192bc9e17fe3bbdb |

Copy: job608-tail-tsccwdf6a4-export-manifest.json. Same freeze, source_export e81e07d2.
Fresh at preparation: verify-inputs0, sh -n0, storage608 check --stage tail 0 (return cap 128MiB),
export 856693612 bytes. No result/log/rc exists. Not launched (1597s left).

Open point for review (sdk-1 acceptance concern 1): the sdk-1 checkpoint
sdk/openclaw-dts-plugin-sdk-2 has an empty data/dist and empty compiler-inputs because
private-QA SDK has no emit roots without OPENCLAW_BUILD_PRIVATE_QA=1 (unset). extract_checkpoint
accepts it (only ownership/safety checks). The reviewer must confirm the tail build consumes
that partition without requiring outputs, or else REJECT and require a source-only fix; never
set the private-QA flag or waive checks.

## Launch: fresh worker FIRST heavy action
All live gates of job608-after-compiler-tsccwdf6a4-continuation.md (health up, no competing run,
df / >=1GB, storage608 check --stage tail 0, verify-inputs0, sh -n0, exact manifest pin above,
result608-tail and sibling tail-tsccwdf6a4-offload.log/.rc absent, >=2655s left AFTER preflight):
```sh
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-tail-tsccwdf6a4
offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-tail -- timeout -k 15s 2400s sh run608.sh > ../tail-tsccwdf6a4-offload.log 2>&1
printf '%s\n' "$?" > ../tail-tsccwdf6a4-offload.rc
```
One launch spends the stage. Then actual evidence commit and separate independent acceptance;
then prepare/review/run package (native, checks, compiler, tail). Never detached.
