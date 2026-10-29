# job608 native-stage preflight at singleThreaded freeze a46cd576 (UNUSED)

SOURCE ONLY; nothing launched; 595 MUST NOT APPLY. No application, install,
package or reseal authority.

- Freeze: a46cd5765702f3b019d5a433b82d19ac57821a8d (contains emitter 7cbbb99c,
  independent APPROVE in job608-native-singlethreaded-independent-review.md).
- Export: `/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-native-singlethreaded-a46c`
  prepared 2026-10-29T00:2xZ with committed `prepare-stage608-export.py --base <private>/base
  --commit a46cd576... --stage native` under ulimit -v 512MiB, rc 0.
- storage608.py check --stage native before prep: unique 956522354 B, free
  6367862784 B, reserve 2 GiB, cap 4 GiB, return cap 64 MiB, OK.
- Manifest sha256 3f48b86fe51a6db134081f27026ae84a52633e3113446f09b7469d6bbb3bd488:
  stage native, execution_state UNUSED, run_id stage608-native-a46c,
  stage_inputs {}, required_checks 14, source_export_sha256
  88279fe17ba6263f5e982c8bb7bad16a13e8f5ad8cf367eebb1921caded20d9e (same common
  export as the a46c checks preflight 841ba12b).
- On-disk sha256: run608.sh eb662d81…, stage608.py a558db9a… (both unchanged),
  native598.tar d73e4e35…, rolldown608-source.tar.gz 203aa483… (both identical
  to the 1bed native pins), source598.tar e79a0e45…, successor598.tar dcc959c7….
- `python3 -I -B stage608.py verify-inputs` exit 0. No .env, .db or key files.
  Native has no stage predecessors (stage608.py STAGES): the checks receipt is
  not an input, so this may launch independently of the checks result, but
  only after independent review of this preflight.

Launch (FIRST step of a fresh worker, `offload deadline` >= 2655 s):

```sh
set -eu
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-native-singlethreaded-a46c
sha256sum export-manifest.json run608.sh stage608.py native598.tar rolldown608-source.tar.gz
python3 -I -B stage608.py verify-inputs
offload deadline
set +e
offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh > ../native-singlethreaded-a46c-offload.log 2>&1
status608=$?
printf '%s\n' "$status608" > ../native-singlethreaded-a46c-offload.rc
exit "$status608"
```

Afterwards `storage608.py result --stage native --result <abs result608-native>`
before acceptance. Acceptance and failure rules unchanged from the 1bed native
preflight; on timeout or failure do not rerun unchanged.
