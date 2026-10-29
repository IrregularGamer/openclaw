# job608 checks-stage preflight at singleThreaded freeze a46cd576 (UNUSED)

SOURCE ONLY; nothing launched; 595 MUST NOT APPLY. No application, install,
package or reseal authority.

- Freeze: a46cd5765702f3b019d5a433b82d19ac57821a8d (contains emitter 7cbbb99c,
  independent APPROVE source-only in job608-native-singlethreaded-independent-review.md).
- Export: `/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-checks-singlethreaded-a46c`
  prepared with committed `prepare-stage608-export.py --base <private>/base
  --commit a46cd576... --stage checks`.
- storage608.py check --stage checks: free 6382252032 B, reserve 2 GiB, cap 4 GiB, OK.
- Manifest sha256 5f6e09743454e75b306f0b4e937c5fbf321dc52898ce95321299cd1ec28013e4;
  runner eb662d8191b7abeb5474e61546e1a97811e4bdb621aa6687e36982bc76644b01 and
  helper a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4
  (both unchanged from candidate95). State UNUSED, stage checks,
  stage_inputs {}, run_id stage608-checks-a46c, required_checks 14,
  source_export_sha256 88279fe17ba6263f5e982c8bb7bad16a13e8f5ad8cf367eebb1921caded20d9e.
- `python3 -I -B stage608.py verify-inputs` exit 0. Export contains no .env,
  .db, key, result or cache files.

Launch (FIRST step of a fresh worker, only after independent review of this
preflight and `offload deadline` showing >= 2655 s):

```sh
set -eu
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-checks-singlethreaded-a46c
sha256sum export-manifest.json run608.sh stage608.py
python3 -I -B stage608.py verify-inputs
offload deadline
set +e
offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-checks -- timeout -k 15s 2400s sh run608.sh > ../checks-singlethreaded-a46c-offload.log 2>&1
status608=$?
printf '%s\n' "$status608" > ../checks-singlethreaded-a46c-offload.rc
exit "$status608"
```

Acceptance rules are unchanged from the candidate95 checks section of
job608-after-native-admission-continuation.md. After checks: native, runtime,
unified-0 (measured config-15) per job608-after-singlethreaded-continuation.md.
