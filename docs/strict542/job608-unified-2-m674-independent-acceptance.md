# job608 unified-2 m674 at 674840b6 - independent acceptance

Reviewer: independent (read-only; no launches, installs, or modifications; checkpoint listed only, never extracted).
Evidence commit: b737aff1 (docs/strict542/job608-unified-2-m674/). Preflight: docs/strict542/job608-unified-2-m674-preflight.json,
independent APPROVE c10b2716 (manifest b9ae8e5a94fdf6d1c12abff1e8b134dc395d66e8d62206f3a05601bf737c247d).
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private. Model: job608-unified-1-m674-independent-acceptance.md.

## 1. Receipt and hashes
- sha256(P/stage-unified-2-m674/export-manifest.json) = b9ae8e5a... = receipt manifest_sha256 = preflight manifest_sha256.
- Receipt: kind JOB608_STAGE_RECEIPT, stage unified-2, run_id stage608-unified-2-m674, source_commit
  674840b669c43af54a62e30b4028f219f4a428c9, source_export_sha256 e1a6de35...4461b, exit_code 0.
- stage_inputs recomputed from live accepted results, all match: native m674 (libtests-receipt 2f81179f, receipt 4a651254,
  addon 0b6607e7, stage-receipt 0bb266db) and runtime m674 (build.log c6436d6a, checkpoint 6178cfd9, stage-receipt 935e56f1).
- result-files.sha256: all 5 entries sha256sum -c OK against live result608-unified-2; live tree has exactly those 5 files.
  Receipt outputs build.log bf1a73b1... and checkpoint.tar.gz de6fd118... equal the live files.
  Committed exit-code.txt (0), pnpm-path.txt, stage-receipt.json are cmp-identical to live.

## 2. Run completion
- Committed unified-2-offload.rc = P/unified-2-m674-offload.rc = 0; committed log gz decompresses byte-identical to the live log.
- offload runs.log: one entry for this stage, `2026-10-30T00:20:35Z run remote rc=0 602s .../stage-unified-2-m674`.
- Log: STEP608 unified-2-stage-native-start +11s, restore-build-done +20s, build-start budget=2257s +23s,
  build-done +425s, unified-2-pass.

## 3. Launch caps
- Preflight launch and README: offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-2 --
  timeout -k 15s 2400s sh run608.sh; unchanged from preflight and tsccwdf6a4 caps. 602s wall within budget.

## 4. Modes
- `find result608-unified-2 -perm /022` = 0 entries.
- `tar -tvzf unified-2/checkpoint.tar.gz` (list only): 36 entries, 0 group/other-writable. Sorted name list md5 equals that of
  P/stage-unified-2-tsccwdf6a4/result608-unified-2/unified-2/checkpoint.tar.gz (same name set).

## 5. Secrets
- Committed log gz: 0 matches for token/secret/password/private key/api key/ghp_/AKIA/bearer (only cgroup stats and STEP lines).
  checkpoint.tar.gz and build.log are not committed.

Verdict: ACCEPT
