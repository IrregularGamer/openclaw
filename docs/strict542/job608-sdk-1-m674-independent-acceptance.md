# job608 sdk-1 m674 at 674840b6 — independent acceptance

Reviewed evidence commit 2bf54db8 (docs/strict542/job608-sdk-1-m674/) live against
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private, stage P/stage-sdk-1-m674.
Preflight docs/strict542/job608-sdk-1-m674-preflight.json (6eb72338), independent APPROVE 735c912a.
Read-only review; nothing extracted, installed or sealed.

## 1. Exit status and markers
- P/sdk-1-m674-offload.rc = 0; result608-sdk-1/exit-code.txt = 0.
- STEP608 markers (offload log): sdk-1-stage-native-start +11s, restore-build-done +24s,
  build-start budget=2252s +28s, sdk-1-build-done +136s, sdk-1-pass.
- As in the sdk-0 m674 precedent, markers are in the offload log (run608.sh stdout), not in build.log; by design.
- build.log (236 lines, 8955 bytes): `grep -ciE 'error|fail|cancel'` = 0. Ends with
  "[tsdown-build] invocation 1/1 finished in 2.3s" / "[build-all] phase timings: no phases ran" (as tsccwdf6a4).

## 2. Hashes and committed copies
- `cd P/stage-sdk-1-m674 && sha256sum -c result-files.sha256`: all 5 OK (exit-code.txt, sdk-1/build.log,
  sdk-1/checkpoint.tar.gz, sdk-1/stage-receipt.json, strict542-checks/pnpm-path.txt); these are every file
  in live result608-sdk-1. Committed result-files.sha256 is byte-identical to the live one.
- Committed exit-code.txt, sdk-1/stage-receipt.json, strict542-checks/pnpm-path.txt and sdk-1-offload.rc
  are byte-identical (cmp) to the live files.
- sdk-1-offload.log.gz decompresses byte-identical to P/sdk-1-m674-offload.log.

## 3. Modes and checkpoint listing
- `find result608-sdk-1 -perm /022` = 0 entries. Result size 42043 bytes (du -sb), matches README.
- `tar -tvzf checkpoint.tar.gz` (not extracted): 8 entries = 4 regular files + 4 dirs, 0 symlinks,
  0 group/other-writable entries. Matches README.
- Sorted name set (md5 229441323b1cea732d668fc8b4bded76) identical (diff empty) to
  P/stage-sdk-1-tsccwdf6a4/result608-sdk-1/sdk-1/checkpoint.tar.gz.

## 4. Stage receipt
- kind JOB608_STAGE_RECEIPT, stage sdk-1, run_id stage608-sdk-1-m674, exit_code 0,
  source_commit 674840b669c4... = preflight and export-manifest source_commit,
  manifest_sha256 23f06cb0... = sha256 of live export-manifest.json = preflight manifest_sha256.
- outputs build.log 47e56d0d... and checkpoint.tar.gz 8a0f1f2e... equal the live files; receipt sha256
  c4911678... matches README.
- All 7 stage_inputs hashes (middle build.log e4d68407, checkpoint b80f8116, stage-receipt 9195d45f;
  native libtests-receipt 2f81179f, receipt 4a651254, rolldown binding 0b6607e7, stage-receipt 0bb266db)
  are present in the manifest, equal the live stage608-inputs files, and equal the source files in
  P/stage-middle-m674/result608-middle and P/stage-native-m674/result608-native (the preflight `--input`s);
  same native/middle hashes as the sdk-0 m674 acceptance. source_export_sha256 e1a6de35 is present in the manifest.
- run608.sh b04abd4d and stage608.py a558db9a equal preflight runner/stage_helper hashes; no __pycache__ in stage.
- Structure identical to the tsccwdf6a4 sdk-1 receipt (same keys, same 2 outputs, same 7 stage_inputs keys);
  only hashes/run_id/commit differ, native libtests/receipt/binding hashes unchanged.

## 5. README claims and scope
- All README claims verified (rc, markers +136s, build.log tail, 0 matches, 42043 bytes, receipt hash,
  checkpoint hash and listing, name-set identity). Launch in README/launch.txt equals the preflight `launch`.
- Nit (not a defect): README says "3143s left", launch.txt says "3135s left"; both >= 2655 minimum.
- No install/seal/root/unit/sudo/service changes in the evidence; README retains "595 MUST NOT APPLY".

Next: tail m674 in a fresh worker (one launch per worker). 595 MUST NOT APPLY.

Verdict: ACCEPT
