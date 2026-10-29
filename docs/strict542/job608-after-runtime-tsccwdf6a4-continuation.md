# Job608 continuation after runtime tsccwdf6a4 — 595 MUST NOT APPLY

Supersedes job608-runtime-tsccwdf6a4-launch.md NEXT section.

- runtime tsccwdf6a4 (manifest d0d4d630, preflight 396aa580) ran ONCE: rc0, runtime-pass, build 10m26s.
  Evidence 6c1d0b04 (docs/strict542/job608-runtime-tsccwdf6a4/), independent ACCEPT 5824b14b. Stage SPENT.
- unified-0 prepared UNUSED: P/stage-unified-0-tsccwdf6a4, manifest
  3a1b42d1b104c977b258a82b82fedd85a02e15c7d2fdaaff754caad4e455708a, 7 pins (native 4 + runtime 3),
  verify-inputs 0, sh -n 0, independent preflight APPROVE ad22814a.

## NEXT FRESH WORKER, FIRST heavy step: unified-0
Fresh gates: offload health up, no competing run, `python3 -I docs/strict542/storage608.py check --root P --stage unified-0` 0,
no result608-unified-0 / log / rc, >=2655s left. Then:

```sh
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-unified-0-tsccwdf6a4
offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-0 -- timeout -k 15s 2400s sh run608.sh > ../unified-0-tsccwdf6a4-offload.log 2>&1
printf '%s\n' "$?" > ../unified-0-tsccwdf6a4-offload.rc
```
Then evidence + independent acceptance (unified-0 must pass and be accepted before compiler), compiler, unified1..5,
middle, sdk0/1, tail, package via prepare-stage608-export.py with accepted result608-* inputs; final
artifact/action/privilege/seal/automatic reviews and job608-final-HQ-HANDOFF.md bound to the actual package.
No install/seal/root/unit/sudo/service changes. Do not `git pull` in workers.
