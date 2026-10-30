# job608 unified-3 m674 at 674840b6 - independent acceptance

Reviewer: independent (read-only; no launches, installs, or modifications; checkpoint listed only, never extracted).
Evidence commit: 988c5eb7 (docs/strict542/job608-unified-3-m674/). Preflight: docs/strict542/job608-unified-3-m674-preflight.json,
independent APPROVE 1d3f2b9b (manifest de4ec8896e749ea0361a4f623c3867db8239c417f5a3334c80f35a46c973f1f6).
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private. Model: job608-unified-2-m674-independent-acceptance.md.

## 1. Receipt and hashes
- sha256(P/stage-unified-3-m674/export-manifest.json) = de4ec889... = receipt manifest_sha256 = preflight manifest_sha256.
- Receipt: kind JOB608_STAGE_RECEIPT, stage unified-3, run_id stage608-unified-3-m674, source_commit
  674840b669c43af54a62e30b4028f219f4a428c9 (= preflight), source_export_sha256 e1a6de35...4461b, exit_code 0.
- stage_inputs recomputed from live accepted results, all 7 match: native m674 (libtests-receipt 2f81179f, receipt 4a651254,
  addon 0b6607e7, stage-receipt 0bb266db) and runtime m674 (build.log c6436d6a, checkpoint 6178cfd9, stage-receipt 935e56f1).
- `find . -type f | sort | xargs sha256sum` in live result608-unified-3 is identical (diff empty) to committed
  result-files.sha256 (5 entries). Receipt outputs build.log 202f659b... and checkpoint.tar.gz b5b3a5b1... equal the live files.
  Committed exit-code.txt (0), strict542-checks/pnpm-path.txt, unified-3/stage-receipt.json are cmp-identical to live.

## 2. Run completion
- Committed unified-3-offload.rc = P/unified-3-m674-offload.rc = 0; live exit-code.txt = 0; committed log gz decompresses
  byte-identical to P/unified-3-m674-offload.log.
- offload runs.log: `2026-10-30T00:40:51Z run remote rc=0 601s .../stage-unified-3-m674`.
- Log: STEP608 unified-3-stage-native-start +11s, restore-build-done +19s, build-start budget=2256s +24s,
  build-done +445s, unified-3-pass.

## 3. Launch caps
- Preflight launch and README: offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-3 --
  timeout -k 15s 2400s sh run608.sh; identical to job608-unified-3-tsccwdf6a4-launch.md caps. 601s wall within budget.

## 4. Modes
- `find result608-unified-3 -perm /022` = 0 entries.
- `tar -tvzf unified-3/checkpoint.tar.gz` (list only): 30 entries, 0 group/other-writable; sha256
  b5b3a5b1d59c9dd45553985e308f095917c7a5913923e9c4e6cbcccf90422617 (as expected). Sorted name list md5 37bea61a equals that of
  P/stage-unified-3-tsccwdf6a4/result608-unified-3/unified-3/checkpoint.tar.gz (same name set).

## 5. Secrets
- Committed log gz: 0 matches for token/secret/password/private key/api key/ghp_/AKIA/bearer (only cgroup stats and STEP lines).
  checkpoint.tar.gz and build.log are not committed.

Verdict: independent ACCEPT
