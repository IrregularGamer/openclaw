# job608 runtime stage receipt (singleThreaded freeze a46cd576) (EVIDENCE)

SOURCE ONLY; **595 MUST NOT APPLY.** Stage evidence, not package/install authority.

- Launched ~01:50Z as FIRST step of a fresh worker exactly per preflight
  de398b3a/726f9c8a (independent APPROVE 1422d684): pre-launch sha256 manifest
  f9ed6da9…, run608.sh eb662d81…, stage608.py a558db9a…, native598.tar
  d73e4e35…, rolldown608-source.tar.gz 203aa483…, verify-inputs 0, deadline 3582 s.
  `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-runtime -- timeout -k 15s 2400s sh run608.sh`.
- Client rc 0 (`../runtime-singlethreaded-a46c-offload.rc`), result exit-code.txt 0,
  final `STEP608 runtime-pass`, no `not ok`/FAIL lines. Finished by 02:14Z.
  build-all timings: total 15m 22.5s (tsdown-packages 7m 53.7s,
  tsdown-unified 6m 16s, tsdown-ai 57.7s) vs 1bed 16m 7.7s.
- `storage608.py result --stage runtime --result <abs result608-runtime>` exit 0,
  logical return 88570823 B (cap 128 MiB).
- Stage receipt sha256 837374b9…26d7 (copy here): kind JOB608_STAGE_RECEIPT,
  exit_code 0, manifest f9ed6da9…, run_id stage608-runtime-a46c, source
  a46cd576…, source_export 88279fe1…, stage_inputs = accepted native a46c
  outputs (stage-receipt 7d1573ac…, receipt 4a651254…, libtests 2f81179f…,
  addon 0b6607e7…).
- Outputs: runtime/checkpoint.tar.gz 43926fbe…476b (88503772 B, 8959 entries,
  private staging only, not committed); runtime/build.log d2c9216e…cf1c (gzip
  copy here). Raw offload log sha256 ccab1a12…f585 (gzip copy here).
- Determinism note: checkpoint hash differs from 1bed (e8ae538c…), expected
  because the freeze changed (singleThreaded emitter, TS-side); entry count is
  identical (8959).

Status: candidate ACCEPT pending exact independent acceptance review.
Next: prepare unified-0 export at a46cd576 with `--input` native + runtime
result dirs, independent preflight review, then launch FIRST in a fresh worker
(measured config-15) per job608-after-singlethreaded-continuation.md.
