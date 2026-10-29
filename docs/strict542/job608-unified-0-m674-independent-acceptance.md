# job608 unified-0 m674 at 674840b6 — independent acceptance

Reviewer: independent (read-only; no launches, installs, service/sudo/seal changes; checkpoint never extracted).
Evidence commit: 93a37171 (docs/strict542/job608-unified-0-m674/). Preflight: docs/strict542/job608-unified-0-m674-preflight.json
(1f478251), independent APPROVE 639aa75c (manifest 2465e31010967d9374270f3573b80acf76aeb896363c1685f1a8e1ac4fda9c1c).
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private. Model: job608-runtime-m674-independent-acceptance.md.

## 1. Receipt and hashes
- sha256(P/stage-unified-0-m674/export-manifest.json) = 2465e310...9c1c = receipt manifest_sha256 = preflight manifest_sha256.
- Receipt (unified-0/stage-receipt.json d55b0c93...1550): kind JOB608_STAGE_RECEIPT, stage unified-0, run_id
  stage608-unified-0-m674, source_commit 674840b669c43af54a62e30b4028f219f4a428c9, source_export_sha256
  e1a6de35...4461b (same as runtime m674), exit_code 0. Committed receipt is cmp-identical to live.
- Receipt outputs: unified-0/build.log 93eaba39...366d and unified-0/checkpoint.tar.gz b22eb141...cd07 both equal
  sha256sum of the actual live files.
- stage_inputs recomputed from live accepted results:
  - P/stage-native-m674/result608-native (accepted 5a412599, exit-code 0): libtests-receipt 2f81179f, receipt 4a651254,
    addon rolldown-binding.linux-x64-gnu.node 0b6607e7...e042, stage-receipt 0bb266db — all match.
  - P/stage-runtime-m674/result608-runtime (accepted 388d36b8, exit-code 0): build.log c6436d6a, checkpoint.tar.gz
    6178cfd9...9a0e, stage-receipt 935e56f1 — all match.
- Committed result-files.sha256: all 5 entries `sha256sum -c` OK in P/stage-unified-0-m674/result608-unified-0; live
  tree has exactly those 5 files. Committed result608-unified-0/ is `diff -r` identical to live except build.log and
  checkpoint.tar.gz (kept in P only, by design). exit-code.txt = 0.

## 2. Run completion
- Committed unified-0-offload.rc = P/unified-0-m674-offload.rc = 0. launch.txt cmp-equal to P/unified-0-m674-launch.txt
  (one launch, 23:15:57Z, manifest 2465e310, preflight APPROVE 639aa75c). unified-0-offload.log.gz decompresses
  byte-identical to P/unified-0-m674-offload.log.
- ~/.local/state/offload/runs.log: one entry for this stage,
  `2026-10-29T23:26:05Z run remote rc=0 605s .../stage-unified-0-m674`.
- Offload log: STEP608 unified-0-stage-native-start, restore-build-done, build-start budget=2260s, build-done +430s,
  `STEP608 unified-0-pass` (last line).
- build.log (246 lines): 0 lines matching error/fail/timedOut:true; tsdown-build invocation 1/1 finished in 291.3s.

## 3. Launch caps
- README launch = preflight `launch` array exactly: `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts
  result608-unified-0 -- timeout -k 15s 2400s sh run608.sh` (caps_source tsccwdf6a4). 605s wall well within budget.

## 4. Modes
- `find P/stage-unified-0-m674/result608-unified-0 -perm /022` = 0 entries.
- `tar -tvzf unified-0/checkpoint.tar.gz` (listing only): 9 entries (4 dirs, 5 files, no links); modes drwx------,
  drwxr-xr-x, -rw-------, -rw-r--r--; 0 group/other-writable, 0 absolute paths, 0 `..` components.

## 5. Secrets
- Committed evidence (README, launch.txt, rc, result-files.sha256, exit-code, pnpm-path, receipt, offload log) scanned
  for token/secret/password/private key/api key/ghp_/AKIA/bearer: no matches. Contents are hashes, paths, cgroup
  memory stats and STEP lines only. checkpoint.tar.gz not committed.

VERDICT: ACCEPT
Reasons: rc 0 (client rc file, runs.log, exit-code.txt, receipt), receipt bound to manifest 2465e310 = preflight, run_id
stage608-unified-0-m674, source 674840b6, stage_inputs = accepted native m674 (addon 0b6607e7) and runtime m674
(checkpoint 6178cfd9), output hashes = actual build.log/checkpoint = result-files.sha256, STEP608 unified-0-pass,
caps equal preflight (2460/14g/4), zero group/other-writable entries in result tree and checkpoint listing, no secrets
in committed evidence.
