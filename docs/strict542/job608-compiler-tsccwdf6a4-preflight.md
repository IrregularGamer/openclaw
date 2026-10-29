# Job608 compiler tsccwdf6a4 conditional preflight — 595 MUST NOT APPLY

Prepared by unchanged prepare-stage608-export.py at frozen f6a4de2ebc6924d16fe559f9858bf8c50dce1eba.
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private.
Export P/stage-compiler-tsccwdf6a4 is UNUSED; no result or sibling compiler log/rc.

- Manifest SHA256 39dbe8f21e6e6e5cb7d250900607fb88b7ddaf96192461a6fe15db62df6bf3e8.
- Source/runner f6a4de2ebc6924d16fe559f9858bf8c50dce1eba.
- Common export e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145.
- Successor archive 88fc8d3f1934c00d65e75324b79d8745f743a6fe426aaa98ecd50d38bef69ac9.
- Runner 715e53bd43979434f317807973d9712bc58d6ecbeec357561f92053b8aa3cd6a; helper a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4.
- Predecessor is unified-0 manifest 3a1b42d1b104c977b258a82b82fedd85a02e15c7d2fdaaff754caad4e455708a.
- Required stage inputs: native only, exactly four pins below, from independently
  accepted native57742314. Unified-0 success is an additional procedural gate.

```json
{
  "native/libtests-receipt.json": "2f81179f5d1bf14d1519cf446935a3cd783da0e28e79a69067c85e5f873dd946",
  "native/receipt.json": "4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e",
  "native/rolldown-binding.linux-x64-gnu.node": "0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042",
  "native/stage-receipt.json": "1047485796fe27d9f653a734dcebd1828caaa455eaa1ee64d625b024c35ed6d3"
}
```

## Independent review and live launch gates
Require actual accepted current checks d9a3822e, native57742314, runtime5824b14b
and unified-0 (actual client/result0 evidence c362cd3a + complete build log d597e6eb,
independent acceptance PENDING). Historical unified results cannot satisfy this.
Require independent exact preflight approval, fresh health up, no competing run,
root / >=1GB, storage check0, verify-inputs0, sh -n0, absent result/log/rc, and
>=975s remaining AFTER preflight (600+195 settle+180 observed transfer).
If time insufficient, launch FIRST in a fresh worker through all same gates.

The unchanged compiler branch retains all five actual Node invocations and original
stock/native minifier/worker/lazy-barrel parity, refusal and cancellation checks.
No testcase/check, owner predicate, memory floor, budget or settlement rule changes.
Finite launch (only AFTER all gates; cwd P/stage-compiler-tsccwdf6a4):

```sh
offload run --timeout 600 --mem 14g --cpus 4 --artifacts result608-compiler -- timeout -k 15s 540s sh run608.sh > ../compiler-tsccwdf6a4-offload.log 2>&1
printf '%s\n' "$?" > ../compiler-tsccwdf6a4-offload.rc
```

One launch spends the stage. Actual client/result0, all five complete Node summaries,
zero failures/cancellations/skips/todos, exact receipt/input/output/source/common
identities, full result inventory, storage-return0, committed evidence and independent
acceptance are required. Preserve unknown settlement/failure evidence without replay.
This is preparation only. No installed/sealed/root/unit/sudo/service changes,
live providers, runtime config, credentials, or installation authority.
