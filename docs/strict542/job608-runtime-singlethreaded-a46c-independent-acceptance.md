# job608 runtime result a46c: independent acceptance (review of c21c5d59)

SOURCE ONLY; 595 MUST NOT APPLY; no install/package/reseal authority.

Checked against the actual files (read-only). No offload, build or test was run:

- Preflight `job608-runtime-singlethreaded-a46c-preflight.md` (review 1422d684, VERDICT APPROVE):
  manifest f9ed6da9…940713b4, run_id stage608-runtime-a46c, source a46cd576…, source_export 88279fe1….
  The launch command matches the preflight exactly: `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-runtime -- timeout -k 15s 2400s sh run608.sh`.
  I found this command in the launching worker transcript. It was the only `offload run … result608-runtime` form used, so no larger mem/cpus/timeout was used.
  The same transcript shows the pre-launch sha256 lines, `verify=0` and `offload deadline` 3582 s left (>= 2655).
- `~/.local/state/offload/runs.log`: `2026-10-29T02:14:00Z run remote rc=0 1410s …/stage-runtime-singlethreaded-a46c`.
  That puts the start at ~01:50:30Z, and 1410 s is well under the 2400 s bound.
- The stage-dir inputs on disk still match the preflight: run608.sh eb662d81…, stage608.py a558db9a…,
  native598.tar d73e4e35…, rolldown608-source.tar.gz 203aa483…. export-manifest.json is still sha256 f9ed6da9…940713b4.
  The export contains no `__pycache__`, .env or .pem files.
- The client rc file `../runtime-singlethreaded-a46c-offload.rc` is 0, and `result608-runtime/exit-code.txt` is 0.
  The raw log (2114 B, sha256 ccab1a12…f585) holds two cgroup archive-release records and ends `STEP608 runtime-pass`.
  0 lines match `not ok|FAIL` in the raw log or in runtime/build.log.
- `runtime/stage-receipt.json` has sha256 837374b9529b8a696b9399b1078050ea064d9c067d292c8cb6654e85b4b426d7. Its fields:
  kind JOB608_STAGE_RECEIPT, stage runtime, exit_code 0,
  manifest_sha256 f9ed6da9… (= sha256 of the export's export-manifest.json), run_id stage608-runtime-a46c,
  source_commit a46cd5765702f3b019d5a433b82d19ac57821a8d, source_export_sha256 88279fe1…20d9e.
  All of these equal the manifest fields.
- The receipt `stage_inputs` equal the manifest stage_inputs and the on-disk sha256 of the accepted native a46c outputs
  (`stage-native-singlethreaded-a46c/result608-native/native/*`, acceptance 35dbdbf6):
  stage-receipt 7d1573ac…, receipt 4a651254…, libtests-receipt 2f81179f…, addon 0b6607e7…. All 4 match.
- Receipt outputs vs on-disk sha256: runtime/checkpoint.tar.gz 43926fbe…476b (88503772 B, 8959 tar entries)
  and runtime/build.log d2c9216e…cf1c. Both match the receipt and the README.
- The committed copies in `job608-runtime-singlethreaded-a46c/` match the private files:
  - stage-receipt.json is byte-identical (`cmp`) to the private one.
  - `zcat build.log.gz` gives sha256 d2c9216e…, equal to the private build.log.
  - `zcat runtime-offload.log.gz` gives sha256 ccab1a12…, equal to the raw offload log.
- build.log phase timings: total 15m 22.5s (tsdown-packages 7m 53.7s, tsdown-unified 6m 16s, tsdown-ai 57.7s).
  The 1bed build.log gives total 16m 7.7s. The 1bed checkpoint is e8ae538c… with 8959 entries.
  Both values are as the README states.
- I reran `python3 -I -B docs/strict542/storage608.py result --stage runtime --result <abs result608-runtime>`.
  It exited 0 with logical_return_bytes 88570823 and return_cap_bytes 134217728, so the result is under the cap.

README accuracy: every factual claim checked is correct. One minor point: "deadline 3582 s" is the
`offload deadline` remaining-time reading, not a configured deadline. No inaccuracies were found.

Every claim in c21c5d59's README is confirmed.

**VERDICT: ACCEPT** (runtime stage evidence at a46cd576 only; grants no unified-0 launch, install, package or reseal authority).
