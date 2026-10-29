# job608 native result a46c: independent acceptance (review of 85060841)

SOURCE ONLY; 595 MUST NOT APPLY; no install/package/reseal authority.

Checked against the actual files (read-only):

- Preflight `job608-native-singlethreaded-a46c-preflight.md` (review bf290a63, VERDICT APPROVE):
  manifest 3f48b86f…d3bd488, run_id stage608-native-a46c, source a46cd576…,
  source_export 88279fe1…; launch command line matches the preflight (`--timeout 2460 --mem 4g --cpus 1`, `timeout -k 15s 2400s sh run608.sh`).
- Stage-dir inputs on disk still match the preflight: run608.sh eb662d81…, stage608.py a558db9a…,
  native598.tar d73e4e35…, rolldown608-source.tar.gz 203aa483…; export-manifest.json still sha256 3f48b86f…d3bd488.
- Client rc file `native-singlethreaded-a46c-offload.rc` = 0; `result608-native/exit-code.txt` = 0;
  log ends `STEP608 native-rebuild-pass`; 0 lines match `FAIL|not ok`.
- `native/stage-receipt.json` (sha256 7d1573ac…f19455): kind JOB608_STAGE_RECEIPT, stage native, exit_code 0,
  manifest_sha256 3f48b86f…, run_id stage608-native-a46c, source_commit a46cd5765702f3b019d5a433b82d19ac57821a8d,
  source_export_sha256 88279fe1…20d9e, stage_inputs {}.
- Receipt outputs vs on-disk sha256: receipt.json 4a651254…31ed9e, libtests-receipt.json 2f81179f…dd946,
  rolldown-binding.linux-x64-gnu.node 0b6607e7…0de042 -- all 3 match.
- Committed copies in `job608-native-singlethreaded-a46c/` (receipt.json, libtests-receipt.json, stage-receipt.json)
  are byte-identical (sha256) to the private ones.
- Determinism vs `job608-native-1bed/`: receipt.json and libtests-receipt.json sha256-identical; addon hash in the
  1bed stage-receipt is the same 0b6607e7…0de042. (stage-receipt.json itself differs, as expected: run/manifest/source fields.)
- Rerun `python3 -I -B docs/strict542/storage608.py result --stage native --result <abs result608-native>`: exit 0,
  logical_return_bytes 48652047, cap 67108864.
- stage608.py has no argparse/verify subcommand (it executes `sys.argv[1:]`), so no read-only receipt verifier was run.

Every claim in 85060841's result doc is confirmed.

**VERDICT: ACCEPT** (native stage evidence at a46cd576 only).
