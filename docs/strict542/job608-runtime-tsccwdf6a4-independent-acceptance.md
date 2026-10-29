# Job 608 runtime tsccwdf6a4: independent acceptance

This covers the runtime stage only, at source f6a4de2e (evidence 6c1d0b04, launch c45c5fd8, preflight review 396aa580).

## Verified
- `P/runtime-tsccwdf6a4-offload.rc` = 0. The committed `runtime-offload.rc` is also 0. `exit-code.txt` = 0.
- `zcat runtime-offload.log.gz | cmp - P/runtime-tsccwdf6a4-offload.log` shows them byte-identical. The log has the
  STEP608 sequence native-start, restore-build-done, build-start (budget=2267s), build-done +729s and
  `runtime-pass`. It contains no timeout, kill, OOM, signal or exit75 lines.
- `cd P/stage-runtime-tsccwdf6a4/result608-runtime && sha256sum -c result-files.sha256`: 5 of 5 OK. The tree also has
  exactly 5 files (exit-code.txt, runtime/build.log, runtime/checkpoint.tar.gz, runtime/stage-receipt.json,
  strict542-checks/pnpm-path.txt), so nothing is missing from the list. The result is 88563594 bytes.
- The committed small copies (exit-code.txt, runtime/stage-receipt.json, strict542-checks/pnpm-path.txt) are
  cmp-equal to the live files.
- `runtime/stage-receipt.json` (sha256 3e284e2c..., as the README says) contains: kind JOB608_STAGE_RECEIPT, stage runtime,
  exit_code 0, run_id `stage608-runtime-tsccwdf6a4`, source_commit `f6a4de2ebc6924d16fe559f9858bf8c50dce1eba`,
  source_export_sha256 `e81e07d2...8145`, and manifest_sha256 `d0d4d630...fbf7`, which equals the actual sha256 of the
  stage's export-manifest.json. Its stage_inputs are equal key by key to the manifest's stage_inputs, which are the
  4 accepted native pins: binding `0b6607e7...e042`, receipt `4a651254...`, libtests `2f81179f...` and native
  stage-receipt `1047485796...`. Its output hashes for build.log (`242dfc93...`) and checkpoint.tar.gz (`9e028d03...`)
  equal the actual files.
- `runtime/build.log` (456 lines) ends with `[build-all] phase timings: total 10m 26.2s` (tsdown-packages 6m 0.1s,
  tsdown-unified 3m 32.6s). There are 0 matches for `error TS|ERR!|failed|exit code`. The 58 "error" matches are all
  `"error":null` / `"timedOut":false` fields in the BOUNDED_PACKAGE_COMPILER JSON records. The 33 "warn" matches are
  the pnpm "TypeScript N.N does not yet ..." support notice and the preinstall-package-manager-warning script name.
- Comparison with the accepted fullsize5aff1 runtime build.log.gz: also 456 lines, 0 failure matches, 58 error and
  33 warn matches, and an identical normalized error/warn pattern set. Its total was 10m 19.9s. The two build logs
  have the same shape.
- The README claims (rc 0, STEP608 timing, the receipt and output hashes, the 4 native pins, a checkpoint of about
  88 MB that is not committed, and the stage being SPENT) are all accurate.

## Note (not a discrepancy)
- The stage's `export-manifest.json` still has `execution_state: UNUSED` and still hashes to d0d4d630. This is
  expected: the run does not mutate the manifest. The fact that the stage is spent is recorded by this evidence
  and the README, not by the manifest.

## Scope and limits
- This accepts the runtime run only. It does not approve install, seal, package or application.
- Next comes unified-0 preparation (inputs result608-native + result608-runtime), through unchanged gates.
- 595 MUST NOT APPLY.
- The review was read-only. No offload, builds, tests or services were run.

VERDICT: ACCEPT runtime tsccwdf6a4 at f6a4de2e (rc 0, 5/5 hashes OK, receipt identity/inputs/outputs verified, build log comparable to fullsize5aff1; 595 MUST NOT APPLY)
