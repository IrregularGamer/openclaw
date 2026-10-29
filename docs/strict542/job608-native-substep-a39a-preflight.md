# job608 native-stage preflight at substep-budget freeze a39ad5ee (UNUSED)

SOURCE ONLY; nothing launched; 595 MUST NOT APPLY. No application, install,
package or reseal authority.

- Freeze: a39ad5ee95609193502850d0dbb87b5dcbb5e3e3 (runner correction dd881aba,
  independent APPROVE a39ad5ee; continuation f9c66345). Checks at this freeze:
  rc 0, evidence 3b28b3fd, independent ACCEPT 2e19dbd1.
- Export: `/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-native-substep-a39a`
  prepared 2026-10-29T03:0xZ with committed `prepare-stage608-export.py`
  (sha256 1e701de0…, unchanged) `--base <private>/base --commit a39ad5ee… --stage native --dest <that path>`
  under ulimit -v 512MiB, rc 0. (A first call without `--dest` was refused by
  argparse, rc 2, nothing written.)
- storage608.py check --stage native before prep: unique 1152030202 B, free
  6171947008 B, reserve 2 GiB, cap 4 GiB, return cap 64 MiB, OK.
- Manifest sha256 9ede911608384d13b2fe736fb547a2135c61b611586342e2f948166c9a16a476:
  stage native, execution_state UNUSED, run_id stage608-native-a39a,
  stage_inputs {}, required_checks 14, source_export_sha256
  d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62 (same common
  export as the a39a checks preflight e5a8dbf9 / receipt 176ac198).
- On-disk sha256: run608.sh e2ed7e13…, stage608.py a558db9a… (both identical
  to the a39a checks export), native598.tar d73e4e35…, rolldown608-source.tar.gz
  203aa483… (identical to the a46c/1bed native pins), source598.tar e79a0e45…,
  successor598.tar e44987e3… (a39a freeze).
- `python3 -I -B stage608.py verify-inputs` exit 0; `__pycache__` removed.
  No .env, .db, key or pem files. Native has no stage predecessors.

Launch (FIRST step of a fresh worker, only after independent review of this
preflight and `offload deadline` >= 2655 s):

```sh
set -eu
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-native-substep-a39a
sha256sum export-manifest.json run608.sh stage608.py native598.tar rolldown608-source.tar.gz
python3 -I -B stage608.py verify-inputs
offload deadline
set +e
offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh > ../native-substep-a39a-offload.log 2>&1
status608=$?
printf '%s\n' "$status608" > ../native-substep-a39a-offload.rc
exit "$status608"
```

Afterwards `storage608.py result --stage native --result <abs result608-native>`
before acceptance. Acceptance and failure rules unchanged from the a46c native
preflight (expected addon 0b6607e7 reproduces); on timeout or failure do not
rerun unchanged. Then runtime, then unified-0 per
job608-after-substep-budget-continuation.md.
