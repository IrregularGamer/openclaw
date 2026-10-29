# job608 runtime m674 at 674840b6 — independent acceptance

Reviewer: independent (read-only; no launches, installs, service/sudo/seal changes; checkpoint never extracted).
Evidence commit: ee84e508. Preflight: 651d63be (docs/strict542/job608-runtime-m674-preflight.json), independent
APPROVE 4b777a33 (manifest 7b4724f9b7dc55ff983c66ec096aa1e8c86fd69e6c211c462c8596300e91de70).
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private. Model: job608-compiler-m674-independent-acceptance.md.

## 1. Receipt and hashes
- sha256(P/stage-runtime-m674/export-manifest.json) = 7b4724f9...de70 = receipt manifest_sha256 = preflight manifest.
- Receipt (runtime/stage-receipt.json 935e56f1...95bd9): kind JOB608_STAGE_RECEIPT, stage runtime, run_id
  stage608-runtime-m674, source_commit 674840b669c43af54a62e30b4028f219f4a428c9, source_export_sha256
  e1a6de35...4461b, exit_code 0. Committed receipt is diff-identical to live.
- Receipt outputs: runtime/build.log c6436d6a...1f38 and runtime/checkpoint.tar.gz 6178cfd9...9a0e both equal
  sha256sum of the actual live files.
- stage_inputs = native m674 (accepted 5a412599): libtests-receipt 2f81179f, receipt 4a651254, addon 0b6607e7...e042,
  stage-receipt 0bb266db (same set as compiler m674).
- Committed result-files.sha256: all 5 entries `sha256sum -c` OK against P/stage-runtime-m674/result608-runtime;
  live tree has exactly those 5 files. Committed result608-runtime/ is `diff -r` identical to live except
  checkpoint.tar.gz (intentionally kept in P only, 88.6 MB). exit-code.txt = 0.

## 2. Run completion
- Committed runtime-offload.rc = P/runtime-m674-offload.rc = 0. launch.txt cmp-equal to P/runtime-m674-launch.txt
  (one launch, 22:48:55Z, manifest 7b4724f9). runtime-offload.log.gz decompresses byte-identical to
  P/runtime-m674-offload.log.
- ~/.local/state/offload/runs.log: exactly one entry,
  `2026-10-29T23:05:57Z run remote rc=0 1019s .../stage-runtime-m674`.
- Offload log: STEP608 runtime-stage-native-start, runtime-restore-build-done, runtime-build-start budget=2268s,
  runtime-build-done +726s, `STEP608 runtime-pass` (last line). No error/fail/timeout lines.
- build.log: 58 BOUNDED_PACKAGE_COMPILER records, all status 0, timedOut false, error null, no fatal unresolved
  imports; build-all total 10m 18.5s.

## 3. Launch caps
- README/launch record: `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-runtime --
  timeout -k 15s 2400s sh run608.sh` = preflight `launch` array exactly. Background Bash, 2800s timeout
  (>= 2460 + 300), as the compiler acceptance note required. 1019s wall well within budget.

## 4. Modes and names
- `find P/stage-runtime-m674/result608-runtime -perm /022` = 0 entries (dirs 755, files 644).
- `tar -tvzf runtime/checkpoint.tar.gz` (listing only): rc 0, 8959 entries (8765 files, 194 dirs, no links),
  0 group/other-writable, 0 absolute paths, 0 `..` components.
- Name scan: matches for secret/token/credential are compiled dist modules (e.g. dist/secrets/egress-proxy/
  proxy.worker.js, extensions/onepassword, vault); no .pem/.env/id_rsa or key material names.

## Notes (non-blocking)
- Manifest/preflight state still reads UNUSED (pinned, never hand-edited, as required).

VERDICT: ACCEPT
Reasons: rc 0 (client rc file, runs.log, exit-code.txt, receipt), receipt bound to manifest 7b4724f9, run_id
stage608-runtime-m674, source 674840b6 and accepted native m674 inputs, output hashes = actual build.log and
checkpoint.tar.gz = result-files.sha256, STEP608 runtime-pass, all 58 bounded compiles status 0, caps equal
preflight (2460/14g/4), zero group/other-writable entries in result tree and checkpoint listing, no absolute or
`..` tar entries.
