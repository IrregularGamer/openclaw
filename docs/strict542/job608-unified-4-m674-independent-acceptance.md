# job608 unified-4 m674 at 674840b6 - independent acceptance

Reviewer: independent (read-only; no launches, installs, or modifications; checkpoint listed only, never extracted).
Evidence commit: 3471cde6 (docs/strict542/job608-unified-4-m674/). Preflight: docs/strict542/job608-unified-4-m674-preflight.json,
independent APPROVE f48fb963 (manifest e829ea958fbb546548c2afe273cab7dbd5a7698b6a875c82f5324dc144e4b469).
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private. Model: job608-unified-3-m674-independent-acceptance.md.

## 1. Receipt and hashes
- sha256(P/stage-unified-4-m674/export-manifest.json) = e829ea95... = receipt manifest_sha256 = preflight manifest_sha256.
- Receipt: kind JOB608_STAGE_RECEIPT, stage unified-4, run_id stage608-unified-4-m674, source_commit
  674840b669c43af54a62e30b4028f219f4a428c9 (= preflight), source_export_sha256 e1a6de35...4461b, exit_code 0.
  stage_inputs (7) identical to the accepted unified-3 m674 inputs (native 2f81179f/4a651254/0b6607e7/0bb266db,
  runtime c6436d6a/6178cfd9/935e56f1).
- Receipt outputs build.log cc7ef481... and checkpoint.tar.gz bebc68d0... equal sha256 of the live files.
- `sha256sum -c result-files.sha256` from live result608-unified-4: 5/5 OK; `find . -type f | sort | xargs sha256sum`
  diff against committed list empty. Committed exit-code.txt, strict542-checks/pnpm-path.txt, unified-4/stage-receipt.json
  are cmp-identical to live.

## 2. Run completion
- Committed unified-4-offload.rc = P/unified-4-m674-offload.rc = 0; live exit-code.txt = 0; committed log gz decompresses
  byte-identical to P/unified-4-m674-offload.log.
- offload runs.log: `2026-10-30T01:00:34Z run remote rc=0 578s .../stage-unified-4-m674`.
- Run log (offload log = run608.sh stdout): STEP608 unified-4-stage-native-start +11s, restore-build-done +20s,
  build-start budget=2256s +24s, unified-4-build-done +419s, unified-4-pass.
  Note: STEP608 markers live in the offload log, not unified-4/build.log (same as unified-3 m674, whose build.log
  also has 0 STEP608 lines); build.log ends with tsdown-build finished 286.5s. Not a defect.

## 3. Launch caps
- Preflight launch = README = offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-4 --
  timeout -k 15s 2400s sh run608.sh (same as unified-3 m674). launch.txt gates: vi0 shn0 storage0, manifest e829ea95,
  APPROVE f48fb963, ONE launch. 578s wall within budget.

## 4. Modes
- `find result608-unified-4 -perm /022` = 0 entries.
- `tar -tvzf unified-4/checkpoint.tar.gz` (list only): 32 entries, 0 group/other-writable. Sorted name list identical
  (diff empty) to P/stage-unified-4-tsccwdf6a4/result608-unified-4/unified-4/checkpoint.tar.gz (32 entries).

## 5. Scope and secrets
- f48fb963..3471cde6 touches only docs/strict542/job608-unified-4-m674/ (0 non-docs paths): no install/seal/root/unit/sudoers change.
- Committed log gz: 0 matches for token/secret/password/private key/api key/ghp_/AKIA/bearer.
  checkpoint.tar.gz and build.log are not committed.

Verdict: ACCEPT
