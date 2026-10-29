# job608 runtime-stage preflight at singleThreaded freeze a46cd576 (UNUSED)

SOURCE ONLY; nothing launched; 595 MUST NOT APPLY. No application, install,
package or reseal authority.

- Freeze a46cd5765702f3b019d5a433b82d19ac57821a8d (as checks/native a46c).
- Predecessor: native a46c result (85060841), independently ACCEPT 35dbdbf6.
- `storage608.py check --root <private> --stage runtime` before prep: unique
  1019871514 B, free 6304395264 B, reserve 2 GiB, cap 4 GiB, return cap
  128 MiB, OK.
- Export: `<private>/stage-runtime-singlethreaded-a46c`, prepared
  2026-10-29T01:4xZ with committed `prepare-stage608-export.py` (sha256
  1e701de0…, unchanged) `--base <private>/base --commit a46cd576… --stage runtime
  --input <private>/stage-native-singlethreaded-a46c/result608-native` under
  ulimit -v 512MiB, rc 0; the import-created `__pycache__/` was removed (as 1bed).
- Manifest sha256 f9ed6da9cc5529981b164327a3ef06ea0ab6a291f6c0838b8049b84d940713b4:
  stage runtime, execution_state UNUSED, run_id stage608-runtime-a46c,
  source a46cd576…, source_export 88279fe1… (same common export as checks and
  native a46c), required_checks 14.
- stage_inputs (STAGES['runtime']=['native']), hard links (link count 2, same
  inodes as stage-native-singlethreaded-a46c/result608-native/native/*):
  stage-receipt 7d1573ac…, receipt 4a651254…, libtests-receipt 2f81179f…,
  addon 0b6607e7… = the accepted native a46c outputs.
- On-disk sha256: run608.sh eb662d81…, stage608.py a558db9a…, native598.tar
  d73e4e35…, rolldown608-source.tar.gz 203aa483…, source598.tar e79a0e45…,
  successor598.tar dcc959c7… (all identical to native a46c export).
- `python3 -I -B stage608.py verify-inputs` exit 0. No .env/.db/key files.

Launch (FIRST step of a fresh worker, `offload deadline` >= 2655 s):

```sh
set -eu
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-runtime-singlethreaded-a46c
sha256sum export-manifest.json run608.sh stage608.py native598.tar rolldown608-source.tar.gz
python3 -I -B stage608.py verify-inputs
offload deadline
set +e
offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-runtime -- timeout -k 15s 2400s sh run608.sh > ../runtime-singlethreaded-a46c-offload.log 2>&1
status608=$?
printf '%s\n' "$status608" > ../runtime-singlethreaded-a46c-offload.rc
exit "$status608"
```

Afterwards `storage608.py result --root <private> --stage runtime --result <abs result608-runtime>`
before acceptance. Acceptance/failure rules unchanged from the 1bed runtime
preflight; on timeout or failure do not rerun unchanged. Then unified-0
(measured config-15) per job608-after-singlethreaded-continuation.md.
