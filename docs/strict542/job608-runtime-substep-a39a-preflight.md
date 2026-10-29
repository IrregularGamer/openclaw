# job608 runtime-stage preflight at substep-budget freeze a39ad5ee (UNUSED)

SOURCE ONLY; nothing launched; 595 MUST NOT APPLY. No application, install,
package or reseal authority.

- Freeze a39ad5ee95609193502850d0dbb87b5dcbb5e3e3 (as checks/native a39a).
- Predecessor: native a39a result (c2cbb9cb), independently ACCEPT 4f54ce46.
- `storage608.py check --root <private> --stage runtime` before prep: unique
  1215214158 B, free 6108688384 B, reserve 2 GiB, cap 4 GiB, return cap
  128 MiB, OK.
- Export: `<private>/stage-runtime-substep-a39a`, prepared 2026-10-29T03:5xZ
  with committed `prepare-stage608-export.py` (sha256 1e701de0…, unchanged)
  `--base <private>/base --commit a39ad5ee… --stage runtime
  --input <private>/stage-native-substep-a39a/result608-native --dest <that path>`
  under ulimit -v 512MiB, rc 0; `__pycache__/` removed.
- Manifest sha256 df2f0a367ab77a16a597baa0c9756d9853c7090642ac1f20c3c276fe46395243:
  stage runtime, execution_state UNUSED, run_id stage608-runtime-a39a,
  source a39ad5ee…, source_export d2875624…f3f62 (same common export as
  checks/native a39a), required_checks 14.
- stage_inputs (STAGES['runtime']=['native']), hard links (link count 2, same
  inodes 395804-395807 as stage-native-substep-a39a/result608-native/native/*):
  stage-receipt a301fb35…, receipt 4a651254…, libtests-receipt 2f81179f…,
  addon 0b6607e7… = the accepted native a39a outputs.
- On-disk sha256: run608.sh e2ed7e13…, stage608.py a558db9a…, native598.tar
  d73e4e35…, rolldown608-source.tar.gz 203aa483…, source598.tar e79a0e45…,
  successor598.tar e44987e3… (all identical to the native a39a export).
- `python3 -I -B stage608.py verify-inputs` exit 0. No .env/.db/key/pem files.

Launch (FIRST step of a fresh worker, only after independent review of this
preflight and `offload deadline` >= 2655 s):

```sh
set -eu
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-runtime-substep-a39a
sha256sum export-manifest.json run608.sh stage608.py native598.tar rolldown608-source.tar.gz
python3 -I -B stage608.py verify-inputs
offload deadline
set +e
offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-runtime -- timeout -k 15s 2400s sh run608.sh > ../runtime-substep-a39a-offload.log 2>&1
status608=$?
printf '%s\n' "$status608" > ../runtime-substep-a39a-offload.rc
exit "$status608"
```

Afterwards `storage608.py result --stage runtime --result <abs result608-runtime>`
before acceptance. Acceptance/failure rules unchanged from the a46c runtime
preflight (f9ed6da9 / accepted 7c9a647e); on timeout or failure do not rerun
unchanged. Then unified-0 per job608-after-substep-budget-continuation.md.
