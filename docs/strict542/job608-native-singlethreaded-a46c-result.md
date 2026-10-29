# job608 native stage result at singleThreaded freeze a46cd576 (EVIDENCE)

SOURCE ONLY; 595 MUST NOT APPLY. Stage evidence, not package/install authority.

- Launched 2026-10-29T01:04Z as FIRST step of a fresh worker exactly per
  preflight d83eb771 (review bf290a63): pre-launch sha256 manifest 3f48b86f…,
  runner eb662d81…, helper a558db9a…, native598.tar d73e4e35…,
  rolldown608-source.tar.gz 203aa483…, verify-inputs 0.
  `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh`.
- Actual client rc 0 (`../native-singlethreaded-a46c-offload.rc`), result
  exit-code.txt 0, log ends `STEP608 native-rebuild-pass` (no FAIL/not ok).
- `storage608.py result --stage native --result <abs result608-native>` exit 0,
  logical return 48652047 B (cap 64 MiB).
- Receipt `native/stage-receipt.json` sha256 7d1573ac…19455: kind
  JOB608_STAGE_RECEIPT, exit_code 0, manifest 3f48b86f…, run_id
  stage608-native-a46c, source a46cd576…, source_export 88279fe1…,
  stage_inputs {}. Outputs (on-disk sha256 match):
  receipt.json 4a651254…31ed9e, libtests-receipt.json 2f81179f…dd946,
  rolldown-binding.linux-x64-gnu.node 0b6607e7…0de042.
- Determinism: receipt.json, libtests-receipt.json and the addon hash are
  byte-identical to the accepted 1bed native evidence (job608-native-1bed/),
  i.e. the singleThreaded emitter change (TS-side) does not alter the native
  artifact and the native rebuild reproduces across exports.
- The addon binary itself stays in the private result dir (not committed),
  same as 1bed.

Status: candidate ACCEPT pending exact independent acceptance review.
Next (each FIRST in a fresh worker): prepare runtime export at a46cd576 with
stage_inputs native = this stage-receipt, independently review its preflight,
launch runtime, then unified-0 (measured config-15) per
job608-after-singlethreaded-continuation.md.
