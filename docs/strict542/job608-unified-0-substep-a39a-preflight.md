# job608 unified-0 preflight at substep-budget freeze a39a (UNUSED)

SOURCE ONLY; nothing launched; **595 MUST NOT APPLY.** No package, application,
install or reseal authority. This is the measured config-15 declaration stage.

- Freeze: `a39ad5ee95609193502850d0dbb87b5dcbb5e3e3`; common source export
  `d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62`.
- Accepted predecessors: native `4f54ce46` (result c2cbb9cb, receipt a301fb35),
  runtime `9f5d4331` (result 8a4b1f56, receipt eb4488f2).
  Checks at this freeze are independently accepted in `2e19dbd1`.
- Export: `/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-unified-0-substep-a39a`.
  Prepared 2026-10-29 with the committed preparer SHA256
  `1e701de05d9ccdfccee532cfef8bcc93ba0fc8f9937caf86d689cfc3eda216f2`,
  `--base <private>/base --commit a39ad5ee... --stage unified-0`
  and `--input` each accepted native/runtime result, under `ulimit -v 524288`
  and `timeout -k 15s 480s`; preparer exit 0. No build/offload ran in preparation.
- Storage check before prep: 1318315563 unique bytes, 6006927360 free bytes,
  2147483648 reserve, 4294967296 aggregate cap, 33554432 return cap; exit 0.
- Manifest SHA256 `900edc324f8e2068521a9d4fc19b0c80d0fbca91cfa01ba5c618d2528fb0b4fd`; stage unified-0, execution_state UNUSED,
  run_id stage608-unified-0-a39a, required_checks 14. Runner e2ed7e13 and
  helper a558db9a are byte-identical to the a39a committed runner/helper and
  the accepted runtime export. The common archives/overlay retain the exact
  runtime pins: source598 e79a0e45, successor598 e44987e3, native598 d73e4e35,
  rolldown608-source.tar.gz 203aa483.
- Exactly seven hard-linked predecessor inputs, verified by
  `python3 -I -B stage608.py verify-inputs` (exit 0). No result608-unified-0,
  offload log/rc, loose .env/.db/key/pem files or __pycache__ is present.
  The common source archive's tracked synthetic/example fixtures are qualified
  in b2c98f20; no runtime state or credential is transferred.

| Input | SHA256 |
| --- | --- |
| native/libtests-receipt.json | `2f81179f5d1bf14d1519cf446935a3cd783da0e28e79a69067c85e5f873dd946` |
| native/receipt.json | `4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e` |
| native/rolldown-binding.linux-x64-gnu.node | `0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042` |
| native/stage-receipt.json | `a301fb35b8da76283393d3b8420028c75d95a50bdde34bf5429392ad0a120f93` |
| runtime/build.log | `13ed360ce36c3ff73fb3f5b83dd5ea335267909742e159e52c8078705ce8d969` |
| runtime/checkpoint.tar.gz | `85f3d1e3b92da6803c810a099c14d10286feac8475fef133cce4350054d95991` |
| runtime/stage-receipt.json | `eb4488f2e5ef31baca3580ae5542d56302d2b15c53a622b4b26abd4e9a92e81b` |

The inherited human-readable purpose still says stage native; the controlling
stage field correctly selects unified-0. No wrapper, floor, resource budget,
owner predicate, root/unit/sudo policy, cancellation or settlement gate changed.

Launch only after exact independent approval of this preflight and UNUSED
export, as the FIRST heavy step in a fresh worker with live deadline >=2655 s:

```sh
set -eu
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-unified-0-substep-a39a
sha256sum export-manifest.json run608.sh stage608.py native598.tar rolldown608-source.tar.gz
python3 -I -B stage608.py verify-inputs
offload deadline
set +e
offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-unified-0 -- timeout -k 15s 2400s sh run608.sh > ../unified-0-substep-a39a-offload.log 2>&1
status608=$?
printf '%s\n' "$status608" > ../unified-0-substep-a39a-offload.rc
exit "$status608"
```

The reviewed runner prints per-substep STEP608 markers and fixes the build's
inner deadline at stage +2280 s (15 s kill grace), leaving time for failure
progress/build.log tails before the outer timeout. Outer budget is 2460 s;
2460+195=2655 s must fit. Never start late or increase these budgets.

After actual success, run `storage608.py result --stage unified-0 --result
<private>/stage-unified-0-substep-a39a/result608-unified-0`, verify client/result0,
all receipt source/export/manifest/input/output identities and the complete
checkpoint owner inventory; commit the receipt/logs and obtain independent
acceptance. A successful runtime emission is not config-15 declaration success.
On timeout/failure, mark this attempt spent and preserve its exact local log/rc;
do not rerun unchanged. If it exceeds the fixed budget, implement/review the
planned config-subset split in owning source without dropping checks or lowering
floors. Exit76 before admission means preserve and continue in a fresh worker.
Then follow `job608-after-substep-budget-continuation.md` for every remaining
stage and all final artifact/action/privilege/seal/automatic-review/HQ gates.
