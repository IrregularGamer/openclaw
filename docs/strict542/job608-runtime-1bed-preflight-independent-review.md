**VERDICT: APPROVE**

# Independent review: job608 runtime stage preflight (UNUSED export, frozen 1bed)

Reviewed claim document: `docs/strict542/job608-runtime-1bed-preflight.md` (commit 612c97be).
Export reviewed read-only: `/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-runtime-1bed`.
Nothing was run, built, offloaded or changed in the export. The running compiler stage in `stage-compiler-1bed` was not touched (only its manifest and input inodes were read). source598.tar was not hashed; only its inode was compared.

This review grants no install, build-package, application or reseal authority. It only says the runtime export is fit for its one planned launch. **595 MUST NOT APPLY.**

## Findings

1. Manifest hash matches the claim: `export-manifest.json` sha256 is 7deb2f4d5603208df276c9590ae587c875447f74563c2add88d49aeed5f3e7b5.
2. Manifest fields match the claim: stage `runtime`, execution_state `UNUSED`, run_id `stage608-runtime-1bed`, source_commit and runner_commit both 1bed4d1bb53eff145f724cc6a448dc73b3609015, source_export_sha256 5d7e9d57fb660e2b54f5595e81ddf332027e21b303937c2cd6bc7f718f311263, predecessor_manifest_sha256 20111ce5....
3. stage_inputs in the manifest list exactly four native files: stage-receipt e8198c1d..., receipt 4a651254..., libtests-receipt 2f81179f..., addon 0b6607e7.... I hashed the four files in `stage608-inputs/native/` and each matches its pin.
4. Each input file has the same inode as the matching file in `../stage-native-1bed/result608-native/native/` (395570-395573), so they are hard links, not copies.
5. The staged stage-receipt.json is byte-identical to the committed `docs/strict542/job608-native-1bed/stage-receipt.json` (sha256 e8198c1d..., recorded in commit 8866a036). The receipt's three output pins match the other three staged inputs.
6. `run608.sh` is byte-identical to `git show 1bed4d1b:docs/strict542/run-stage608.sh`, and `stage608.py` is byte-identical to `git show 1bed4d1b:docs/strict542/stage608.py`.
7. In the staged stage608.py, `STAGES['runtime'] == ['native']`, which agrees with the single `native` input set.
8. The export has no `result608-runtime` directory and no `__pycache__`. A find for `.env*`, `*.db`, `*.sqlite*`, `*key*`, `*.pem`, `id_*`, `*token*` and `*secret*` returned nothing. The top level holds only the expected archives, scripts, manifest and input directories.
9. source598.tar has inode 395540, the same as `../base/source598.tar`.
10. Compared with `../stage-compiler-1bed/export-manifest.json`, both manifests have the same keys. Only `stage` (runtime vs compiler) and `run_id` (stage608-runtime-1bed vs stage608-compiler-1bed) differ. That fits the fact that `STAGES['compiler']` is also `['native']`. The compiler export's inputs are the same inodes too.
11. The planned command `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-runtime -- timeout -k 15s 2400s sh run608.sh` is bounded. It has 4g memory and 1 CPU, and the inner 2400 s timeout plus the 15 s kill grace ends before the 2460 s offload timeout. It is character-for-character the same as the `command` in `docs/strict542/job608-stage-runtime-owned-launch.json` (the cf8907d3 launch). The only differences between the two launches are the export, the source commit and the manifest, which is expected. The 2655 s worker-life floor covers 2460 s plus margin.
12. Minor, does not block: the claim document says the input files have "link count 2". They actually have link count 3, because the compiler export (prepared just before this one) links the same inodes. The inode identity, which is the claim that matters, holds.
13. Not independently re-run: `stage608.py verify-inputs`, the storage check and the preparer run. Re-running them would execute code from the export, and this review is read-only. The static checks above agree with what those runs are said to verify.

## Scope

Approval covers only this UNUSED preflight and the single bounded runtime launch it plans, in a fresh worker after the compiler result is recorded. If that run fails or times out, it must not be rerun unchanged. This review grants no install, package, application or reseal authority. **595 MUST NOT APPLY.**
