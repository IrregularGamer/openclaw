# job608 checks-stage preflight at substep-budget freeze a39ad5ee (UNUSED)

SOURCE ONLY; nothing launched; 595 MUST NOT APPLY. No application, install,
package or reseal authority.

- Freeze: a39ad5ee95609193502850d0dbb87b5dcbb5e3e3 (contains runner correction
  dd881aba, independent APPROVE a39ad5ee; continuation f9c66345).
- Export: `/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-checks-substep-a39a`
  prepared 2026-10-29T02:2xZ with committed `prepare-stage608-export.py`
  (sha256 1e701de0…, unchanged) `--base <private>/base --commit a39ad5ee… --stage checks`
  under ulimit -v 512MiB, rc 0. (A first call with a mistyped commit
  `a39ad5ee7` was refused by rev-parse, rc 1, nothing written.)
- storage608.py check --stage checks: free 6186987520 B, reserve 2 GiB, cap 4 GiB, OK.
- Manifest sha256 322e58a911817d9752932c07a11a807208faf3a8da0bd1043b80c75e2907e892;
  runner e2ed7e1337f5d0564b56e61174d0837440655cd38f75416608bff3de82780605
  (= `git show a39ad5ee:docs/strict542/run-stage608.sh`, the only change vs a46c
  runner eb662d81); helper a558db9a… unchanged; native598.tar d73e4e35…,
  rolldown608-source.tar.gz 203aa483…, source598.tar e79a0e45… unchanged;
  successor598.tar e44987e3… (new freeze). State UNUSED, stage checks,
  stage_inputs {}, run_id stage608-checks-a39a, required_checks 14,
  source_export_sha256 d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62.
- `python3 -I -B stage608.py verify-inputs` exit 0; `__pycache__` removed.
  Export contains no .env, .db, key or pem files.

Launch (FIRST step of a fresh worker, only after independent review of this
preflight and `offload deadline` showing >= 2655 s):

```sh
set -eu
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-checks-substep-a39a
sha256sum export-manifest.json run608.sh stage608.py
python3 -I -B stage608.py verify-inputs
offload deadline
set +e
offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-checks -- timeout -k 15s 2400s sh run608.sh > ../checks-substep-a39a-offload.log 2>&1
status608=$?
printf '%s\n' "$status608" > ../checks-substep-a39a-offload.rc
exit "$status608"
```

Afterwards `storage608.py result --stage checks --result <abs result608-checks>`.
Acceptance rules unchanged (candidate95 checks section of
job608-after-native-admission-continuation.md). On failure/timeout do not
rerun unchanged. Then native, runtime, unified-0 per
job608-after-substep-budget-continuation.md.
