# job608 tail m674 at 674840b6 — independent acceptance

Reviewed evidence commit 20581094 (docs/strict542/job608-tail-m674/) live against
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private, stage P/stage-tail-m674.
Preflight docs/strict542/job608-tail-m674-preflight.json (b7d710e3), independent APPROVE 9658c9c9;
launch record 5c3ea971. Read-only review; nothing extracted, installed or sealed.

## 1. Exit status and markers
- P/tail-m674-offload.rc = 0; result608-tail/exit-code.txt = 0.
- STEP608 markers (offload log, 7 lines): tail-stage-native-start +11s, tail-restore-build-done +23s,
  tail-build-start budget=2255s +25s, tail-build-done +236s, tail-pass. tsccwdf6a4 tail: build-done +237s.
- As in the sdk-0/sdk-1 m674 precedents, markers are in the offload log (run608.sh stdout), not in build.log; by design.
- build.log (827 lines, 84209 bytes): `grep -ciE 'error|fail|cancel'` = 1, the known benign asset line
  `../dist/control-ui/assets/update-failure-report-CM8mG5Su.js`; 0 matches after excluding `update-failure-report-`
  (tsccwdf6a4 has the same single match, `update-failure-report-BOWrK2mD.js`). Ends with
  "[build-all] phase timings: total 1m 43.1s; slowest ui:build 43.3s; ..." (tsccwdf6a4: total 1m 45.8s).

## 2. Hashes and committed copies
- `cd P/stage-tail-m674 && sha256sum -c <committed result-files.sha256>`: all 5 OK (exit-code.txt,
  strict542-checks/pnpm-path.txt, tail/build.log, tail/checkpoint.tar.gz, tail/stage-receipt.json); these are
  every file in live result608-tail (find -type f = 5).
- Note (not a defect): there is no result-files.sha256 file in P/stage-tail-m674 itself (as in the sdk-0 and
  middle m674 stages; sdk-1 m674 had one). The README does not claim a live copy; the committed list was checked
  directly against the live files above.
- Committed exit-code.txt, strict542-checks/pnpm-path.txt, tail/stage-receipt.json and tail-offload.rc are
  byte-identical (cmp) to the live files.
- tail-offload.log.gz decompresses byte-identical to P/tail-m674-offload.log.

## 3. Modes and checkpoint listing
- `find result608-tail -perm /022` = 0 entries. Result size 161608377 bytes (du -sb), matches README,
  under 192 MiB (201326592).
- `tar -tvzf checkpoint.tar.gz` (not extracted): 18159 entries = 15907 regular files + 1069 dirs + 1183 symlinks;
  0 group/other-writable files/dirs. All 1183 symlinks have relative targets (0 absolute), all resolve inside
  `tail/` (0 escaping) and to an entry present in the archive (0 dangling).
- Entry count equals P/stage-tail-tsccwdf6a4 checkpoint (18159). Raw name sets differ only under
  `tail/data/dist/control-ui/assets/`; after normalizing the 8-char content hash suffix (`-XXXXXXXX.{js,css}`)
  the sorted name sets are identical (diff empty, md5 9ff307cb1b9635f761cfc9e4389e8866 both).
- checkpoint.tar.gz sha256 54b49d6895c96d4bed2f372038e3b0fef2d60b9e79038c24dedf92489175c40b = README = receipt.

## 4. Stage receipt
- kind JOB608_STAGE_RECEIPT, stage tail, run_id stage608-tail-m674, exit_code 0,
  source_commit 674840b669c4... = preflight and export-manifest source_commit,
  manifest_sha256 4a3b2833... = sha256 of live export-manifest.json = preflight manifest_sha256.
- outputs build.log d55aa756... and checkpoint.tar.gz 54b49d68... equal the live files; receipt sha256
  0d454a11... matches committed result-files.sha256.
- All 13 stage_inputs hashes (middle build.log e4d68407, checkpoint b80f8116, stage-receipt 9195d45f;
  native libtests-receipt 2f81179f, receipt 4a651254, rolldown binding 0b6607e7, stage-receipt 0bb266db;
  sdk-0 build.log 4b74075c, checkpoint 307e76bf, stage-receipt f5104901; sdk-1 build.log 47e56d0d,
  checkpoint 8a0f1f2e, stage-receipt c4911678) are present in the manifest, equal the live stage608-inputs files
  (exactly these 13 files), and equal the source files in P/stage-{native,middle,sdk-0,sdk-1}-m674/result608-*
  (the preflight `--input`s). sdk-1 hashes equal the sdk-1 m674 acceptance; source_export_sha256 e1a6de35 is in
  the manifest.
- run608.sh b04abd4d and stage608.py a558db9a equal preflight runner_sha256/stage_helper_sha256; no __pycache__
  in stage.
- Structure identical to the tsccwdf6a4 tail receipt (same keys and value types, same 2 outputs keys, same 13
  stage_inputs keys); only manifest_sha256/run_id/source_commit/source_export_sha256 and stage hashes differ;
  native libtests/receipt/binding hashes unchanged.

## 5. README claims and scope
- All README claims verified (rc 0, markers +236s vs +237s, single benign match, build.log tail, 161608377 bytes,
  0 writable entries, 18159/15907/1069/1183 listing, normalized name-set identity, checkpoint hash, every
  returned file listed, offload log gzip). Launch in README equals the preflight `launch` and tail tsccwdf6a4
  README line 12 (`--timeout 2460 --mem 14g --cpus 4 ... timeout -k 15s 2400s sh run608.sh`); launch.txt gates
  (health up, no competing run, vi0 shn0 storage0, manifest 4a3b2833, 3233s left >= 2655) match README.
- Evidence commits 5c3ea971..20581094 touch only docs/strict542/job608-tail-m674/; no install/seal/root/unit/
  sudo/service changes; README retains "595 MUST NOT APPLY".

Next: package m674 in a fresh worker (one launch per worker). 595 MUST NOT APPLY.

Verdict: ACCEPT
