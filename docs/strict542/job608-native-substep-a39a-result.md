# job608 native stage result at substep-budget freeze a39ad5ee (EVIDENCE)

SOURCE ONLY; 595 MUST NOT APPLY. Stage evidence, not package/install authority.

- Launched 2026-10-29T03:12Z as FIRST step of a fresh worker exactly per
  preflight bce656a3 (independent review cf871679): pre-launch sha256 manifest
  9ede9116…, runner e2ed7e13…, helper a558db9a…, native598.tar d73e4e35…,
  rolldown608-source.tar.gz 203aa483…, verify-inputs 0, `__pycache__` removed.
  `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh`.
- Actual client rc 0 (`../native-substep-a39a-offload.rc`), result
  exit-code.txt 0, log ends `STEP608 native-rebuild-pass`, 0 `not ok`/`FAIL` lines.
- `storage608.py result --stage native --result <abs result608-native>` exit 0,
  logical return 48652047 B (cap 64 MiB).
- Receipt `native/stage-receipt.json` sha256 a301fb35…a120f93: kind
  JOB608_STAGE_RECEIPT, exit_code 0, manifest 9ede9116…, run_id
  stage608-native-a39a, source a39ad5ee…, source_export d2875624…f3f62,
  stage_inputs {}. Outputs (on-disk sha256):
  receipt.json 4a651254…31ed9e, libtests-receipt.json 2f81179f…dd946,
  rolldown-binding.linux-x64-gnu.node 0b6607e7…0de042.
- Determinism: receipt.json, libtests-receipt.json and the addon are
  byte-identical to accepted a46c (35dbdbf6) and 1bed native evidence; the
  substep-budget correction does not alter the native artifact. Only the
  stage-receipt differs (new manifest/run_id/source/export, as expected).
- Addon binary stays in the private result dir (not committed).

Status: candidate ACCEPT pending exact independent acceptance review.
Next (each FIRST in a fresh worker): runtime export at a39ad5ee with
stage_inputs native = this stage-receipt, independent preflight review,
launch runtime, then unified-0 per job608-after-substep-budget-continuation.md.
