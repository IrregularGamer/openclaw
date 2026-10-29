# job608 unified-1 m674 at 674840b6 — independent acceptance

Reviewer: independent (read-only; no launches, installs, service/sudo/seal changes; checkpoint never extracted).
Evidence commit: 514da3ba (docs/strict542/job608-unified-1-m674/). Preflight: docs/strict542/job608-unified-1-m674-preflight.json,
independent APPROVE 12e8caac (manifest d0db834fc98f9f09489059103fcf533910851c5eb69fdbbbd6eece6432d38965).
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private. Model: job608-unified-0-m674-independent-acceptance.md.

## 1. Receipt and hashes
- sha256(P/stage-unified-1-m674/export-manifest.json) = d0db834f...8965 = receipt manifest_sha256 = preflight manifest_sha256.
- Manifest execution_state `UNUSED`, launch_history `none (fresh finite export)`, run_id stage608-unified-1-m674; since the
  live manifest still hashes to the preflight-approved d0db834f, it has not been edited since preflight.
- Receipt (unified-1/stage-receipt.json 75e9441c...1f71): kind JOB608_STAGE_RECEIPT, stage unified-1, run_id
  stage608-unified-1-m674, source_commit 674840b669c43af54a62e30b4028f219f4a428c9, source_export_sha256
  e1a6de35...4461b (same as unified-0/runtime m674), exit_code 0. Committed receipt is cmp-identical to live.
- Receipt outputs: unified-1/build.log 4ce55763139b...cd6 and unified-1/checkpoint.tar.gz
  4208af9f795f5a64a311e7670b8330582c019f4a1986f25335dff5b10b24b9f7 equal sha256 of the live files.
- stage_inputs recomputed from live accepted results:
  - P/stage-native-m674/result608-native/native: libtests-receipt 2f81179f, receipt 4a651254, addon 0b6607e7,
    stage-receipt 0bb266db — all match.
  - P/stage-runtime-m674/result608-runtime/runtime: build.log c6436d6a, checkpoint.tar.gz 6178cfd9, stage-receipt
    935e56f1 — all match.
- Committed result-files.sha256: all 5 entries `sha256sum -c` OK inside P/stage-unified-1-m674/result608-unified-1; live
  tree has exactly those 5 files. Committed exit-code.txt, strict542-checks/pnpm-path.txt, unified-1/stage-receipt.json
  are cmp-identical to live (build.log and checkpoint.tar.gz kept in P only, by design). exit-code.txt = 0.

## 2. Run completion
- Committed unified-1-offload.rc = P/unified-1-m674-offload.rc = 0. unified-1-offload.log.gz decompresses
  byte-identical to P/unified-1-m674-offload.log.
- ~/.local/state/offload/runs.log: exactly one entry for this stage,
  `2026-10-29T23:51:37Z run remote rc=0 598s .../stage-unified-1-m674` (single admitted run).
- Offload log: BEFORE/AFTER_ARCHIVE_RELEASE608 cgroup stats, then STEP608 unified-1-stage-native-start +11s,
  restore-build-done +20s, build-start budget=2256s +24s, build-done +443s, `STEP608 unified-1-pass` (last line).
  Note: as in the unified-0 model, the STEP608 pass marker is emitted to the offload log (run608.sh stdout), not to
  build.log; build.log is the run-build-stage608.sh output and ends with `[build-all] phase timings: no phases ran`,
  identical in shape to accepted unified-0 m674.
- build.log (242 lines): 0 lines matching error/fail/fatal/panic/ERR!/timedOut:true; tsdown-build invocation 1/1
  finished in 307.5s.

## 3. Launch caps
- README launch = preflight `launch` array exactly: `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts
  result608-unified-1 -- timeout -k 15s 2400s sh run608.sh`. 598s wall well within budget. launch.txt records one launch
  (2026-10-29T23:41:42Z, manifest d0db834f, APPROVE 12e8caac).

## 4. Modes
- `find P/stage-unified-1-m674/result608-unified-1 -perm /022` = 0 entries.
- `tar -tvzf unified-1/checkpoint.tar.gz` (listing only): 29 entries; modes drwx------ (1), drwxr-xr-x (9),
  -rw------- (2), -rw-r--r-- (17); 0 group/other-writable.

## 5. Secrets
- Committed evidence (README, launch.txt, rc, result-files.sha256, exit-code, pnpm-path, receipt, offload log) scanned
  for token/secret/password/private key/api key/ghp_/AKIA/bearer: 0 matches. Offload log holds only cgroup memory stats
  and STEP lines. Export successor_paths contain no secret/.env/key paths (only a false-positive "immediate" match).
  checkpoint.tar.gz not committed.

VERDICT: ACCEPT
Reasons: rc 0 (client rc file, runs.log, exit-code.txt, receipt), receipt bound to manifest d0db834f = preflight, run_id
stage608-unified-1-m674, source 674840b6, stage_inputs = accepted native m674 (addon 0b6607e7) and runtime m674
(checkpoint 6178cfd9), output hashes = actual build.log/checkpoint = result-files.sha256, STEP608 unified-1-pass, single
admitted run, caps equal preflight (2460/14g/4), zero group/other-writable entries in result tree and 29-entry checkpoint
listing, no secrets in committed evidence.
