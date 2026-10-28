# job608 full checks stage (r2) receipt

Evidence for source preparation only. **595 MUST NOT APPLY.**

- This is a relaunch of the interrupted 18:5xZ run (that worker was cut off by a usage limit before it wrote an rc). It ran from a `cp -al` copy `tmp/export608-stage-checks-carrier-r2` of the reviewed base `export608-stage-checks-carrier-next`.
- Command: `offload run --timeout 1500 --mem 4g --cpus 1 --artifacts result608-checks -- timeout -k 15s 1440s sh run608.sh`. Exit code 0, finished 19:16Z.
- Receipt: stage checks, source 1bed4d1bb53eff145f724cc6a448dc73b3609015, export 5d7e9d57fb660e2b54f5595e81ddf332027e21b303937c2cd6bc7f718f311263, manifest 20111ce5f68e7764e7176a670df6e9097deafa51d02291810bf65dd41c8c7c2d.
- Vitest: 13/13 suites, 198/198 tests. Node test runner: 158 pass, 0 fail, 0 cancelled.
- Raw sha256: installed.json 9843dc48…, stage-receipt.json c8ad16cd…, tests.log 3712c046….
- Open: earlier NOTES call this the "canonical491" checks. The 356 assertions counted here are not yet reconciled with that figure. The next independent review must confirm the inventory before the native stage uses this receipt.
