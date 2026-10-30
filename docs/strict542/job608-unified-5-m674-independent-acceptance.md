# job608 unified-5 m674 at 674840b6 - independent acceptance

Reviewer: independent (read-only; no launches, installs, or modifications; checkpoint listed only, never extracted).
Evidence commits: bc6f1ce2, 70290de4 (docs/strict542/job608-unified-5-m674/). Preflight: docs/strict542/job608-unified-5-m674-preflight.json,
independent APPROVE a699cf94 (manifest 0a57d40c4c41e84f473af238b429001041df3fef1a9647d2077f4340c896e590).
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private. Model: job608-unified-4-m674-independent-acceptance.md (0302c32f).

## 1. Receipt and hashes
- sha256(P/stage-unified-5-m674/export-manifest.json) = 0a57d40c... = receipt manifest_sha256 = preflight manifest_sha256.
- Receipt: kind JOB608_STAGE_RECEIPT, stage unified-5, run_id stage608-unified-5-m674, source_commit
  674840b669c43af54a62e30b4028f219f4a428c9 (= preflight), source_export_sha256 e1a6de35...4461b, exit_code 0.
  stage_inputs (7) identical to the accepted unified-4 m674 inputs (native 2f81179f/4a651254/0b6607e7/0bb266db,
  runtime c6436d6a/6178cfd9/935e56f1).
- Receipt outputs build.log 99b56226... and checkpoint.tar.gz 737515b7... equal sha256 of the live files.
- `sha256sum -c result-files.sha256` from live result608-unified-5: 5/5 OK; `find . -type f | sort | xargs sha256sum`
  diff against committed list empty. Committed exit-code.txt, strict542-checks/pnpm-path.txt, unified-5/stage-receipt.json
  are cmp-identical to live.

## 2. Run completion
- Committed unified-5-offload.rc = P/unified-5-m674-offload.rc = 0; live exit-code.txt = 0; committed log gz decompresses
  byte-identical to P/unified-5-m674-offload.log; `grep -c "STEP608 unified-5-pass"` = 1.
- offload runs.log: `2026-10-30T01:27:14Z run remote rc=0 574s .../stage-unified-5-m674`.
- STEP608 markers: stage-native-start +11s, restore-build-done +20s, build-start budget=2257s +23s,
  unified-5-build-done +423s, unified-5-pass.

## 3. Launch caps
- Preflight launch = README = offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-5 --
  timeout -k 15s 2400s sh run608.sh (same as unified-4 m674). launch.txt gates: vi0 shn0 storage0, manifest 0a57d40c,
  APPROVE a699cf94, ONE launch, 3250s left (>= 2655). 574s wall within budget.

## 4. Modes
- `find result608-unified-5 -perm /022` = 0 entries.
- `tar -tvzf unified-5/checkpoint.tar.gz` (list only): 25 entries, 0 group/other-writable. Sorted name list identical
  (cmp equal) to P/stage-unified-5r1-tsccwdf6a4/result608-unified-5/unified-5/checkpoint.tar.gz (25 entries).

## 5. Scope and secrets
- a699cf94..70290de4 touches only docs/strict542/job608-unified-5-m674/ (0 non-docs paths): no install/seal/root/unit/sudoers change.
- Committed log gz: 0 matches for token/secret/password/private key/api key/ghp_/AKIA/bearer.
  checkpoint.tar.gz and build.log are not committed.

Verdict: ACCEPT
