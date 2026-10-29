# job608 native result a39a: independent acceptance (review of c2cbb9cb)

SOURCE ONLY; 595 MUST NOT APPLY; evidence only, not install/package/reseal authority.

Checked against the actual files (read-only):

- Preflight `job608-native-substep-a39a-preflight.md` (bce656a3, review cf871679):
  manifest 9ede9116…9a16a476, run_id stage608-native-a39a, source a39ad5ee…,
  source_export d2875624…c0ef3f62; launch line `--timeout 2460 --mem 4g --cpus 1`, `timeout -k 15s 2400s sh run608.sh`.
- Stage-dir inputs on disk still match the preflight: export-manifest.json 9ede9116…, run608.sh e2ed7e13…,
  stage608.py a558db9a…, native598.tar d73e4e35…, rolldown608-source.tar.gz 203aa483….
- Client rc file `native-substep-a39a-offload.rc` = 0; `result608-native/exit-code.txt` = 0;
  log contains (and ends with) `STEP608 native-rebuild-pass` (1 line); 0 lines match `not ok`, 0 match `FAIL`.
- `native/stage-receipt.json` (sha256 a301fb35…a120f93): kind JOB608_STAGE_RECEIPT, stage native, exit_code 0,
  manifest_sha256 9ede911608384d13b2fe736fb547a2135c61b611586342e2f948166c9a16a476, run_id stage608-native-a39a,
  source_commit a39ad5ee95609193502850d0dbb87b5dcbb5e3e3,
  source_export_sha256 d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62, stage_inputs {}.
- Receipt outputs vs on-disk sha256: receipt.json 4a651254…31ed9e, libtests-receipt.json 2f81179f…dd946,
  rolldown-binding.linux-x64-gnu.node 0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042 -- all 3 match.
- Committed copies in `job608-native-substep-a39a/` (receipt.json, libtests-receipt.json, stage-receipt.json)
  are byte-identical (sha256) to the private ones.
- Determinism vs accepted `job608-native-singlethreaded-a46c/` (35dbdbf6): receipt.json and libtests-receipt.json
  sha256-identical; the a46c stage-receipt `outputs` map is identical, including addon 0b6607e7…0de042.
  (stage-receipt.json itself differs, as expected: manifest/run_id/source/export fields.)
- Rerun `python3 -I -B docs/strict542/storage608.py result --stage native --result <abs result608-native>`: exit 0,
  logical_return_bytes 48652047, cap 67108864.
- No offload, install, service or sudo run; no gate/floor/budget changed.

Every claim in c2cbb9cb's result doc is confirmed.

**VERDICT: ACCEPT** (native stage evidence at a39ad5ee only; evidence, not install authority).
