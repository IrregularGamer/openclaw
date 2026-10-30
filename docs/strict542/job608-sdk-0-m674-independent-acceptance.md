# job608 sdk-0 m674 at 674840b6 — independent acceptance

Reviewed evidence commit e9031145 (docs/strict542/job608-sdk-0-m674/) live against
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private, stage P/stage-sdk-0-m674.
Preflight docs/strict542/job608-sdk-0-m674-preflight.json, independent APPROVE eeac5eab. Read-only review;
nothing extracted, installed or sealed.

## 1. Exit status and markers
- P/sdk-0-m674-offload.rc = 0; result608-sdk-0/exit-code.txt = 0.
- STEP608 markers (offload log): sdk-0-stage-native-start +10s, restore-build-done +23s,
  build-start budget=2256s +24s, sdk-0-build-done +448s, sdk-0-pass.
- Note: these markers are written by run608.sh to stdout (offload log), not into sdk-0/build.log; this is
  by design (run608.sh line 10 step608(), line 157) and matches the middle m674 precedent and the earlier
  sdk-0 tsccwdf6a4 build.log (also 0 STEP608 lines). Not a defect.
- build.log (246 lines, 9768 bytes): `grep -niE 'error|fail|cancel'` = 0 matches. Ends with
  tsdown-build invocation 1/1 finished in 301.5s and the build-all phase-timings line (same as tsccwdf6a4).

## 2. Hashes and committed copies
- `cd P/stage-sdk-0-m674 && sha256sum -c result-files.sha256`: all 5 OK (exit-code.txt, sdk-0/build.log,
  sdk-0/checkpoint.tar.gz, sdk-0/stage-receipt.json, strict542-checks/pnpm-path.txt); these are every file
  in live result608-sdk-0.
- Committed exit-code.txt, sdk-0/stage-receipt.json, strict542-checks/pnpm-path.txt and sdk-0-offload.rc
  are byte-identical (cmp) to the live files.
- sdk-0-offload.log.gz decompresses byte-identical to P/sdk-0-m674-offload.log.

## 3. Modes and checkpoint listing
- `find result608-sdk-0 -perm /022` = 0 entries.
- `tar -tvzf checkpoint.tar.gz` (not extracted): 379 entries = 374 regular files + 5 dirs, 0 symlinks,
  0 group/other-writable entries. Matches README.
- Sorted name set md5 36a85ffbca780b1c67733b7c310993a7, identical to
  P/stage-sdk-0-tsccwdf6a4/result608-sdk-0/sdk-0/checkpoint.tar.gz.

## 4. Stage receipt
- stage sdk-0, run_id stage608-sdk-0-m674, exit_code 0, source_commit 674840b669c4...,
  manifest_sha256 7714f4b6... = sha256 of live export-manifest.json = preflight manifest_sha256.
- outputs build.log 4b74075c... and checkpoint.tar.gz 307e76bf... equal the live files.
- All 7 stage_inputs hashes (middle build.log e4d68407, checkpoint b80f8116, stage-receipt 9195d45f;
  native libtests-receipt 2f81179f, receipt 4a651254, rolldown binding 0b6607e7, stage-receipt 0bb266db)
  are present in the manifest and equal the live stage608-inputs files; middle hashes agree with the
  middle m674 acceptance. source_export_sha256 is present in the manifest. Preflight records inputs by
  reference (native ACCEPT 5a412599, middle ACCEPT dc75babf) rather than hashes; consistent.

## 5. Caps and scope
- The offload log shows only cgroup memory snapshots and STEP608 lines; the cap flags themselves are not
  visible there. The launch recorded in README/launch record (offload run --timeout 2460 --mem 14g --cpus 4
  --artifacts result608-sdk-0 -- timeout -k 15s 2400s sh run608.sh) equals the preflight `launch` exactly.
- No install/seal/root/unit/sudo/service changes in the evidence; README retains "595 MUST NOT APPLY".

Next: sdk-1 m674 in a fresh worker (one launch per worker). 595 MUST NOT APPLY.

Verdict: ACCEPT
