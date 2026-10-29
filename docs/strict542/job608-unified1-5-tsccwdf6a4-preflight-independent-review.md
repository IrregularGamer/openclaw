# Independent unified1..5 tsccwdf6a4 batch preflight

Reviewed exact preparation `37784051` and all five actual UNUSED exports on
2026-10-29, after independent current compiler acceptance `dd34e5e4`.

VERDICT: APPROVE CONDITIONAL SOURCE-ONLY BATCH PREFLIGHT. No findings.
595 MUST NOT APPLY. This review accepts no future group result.

P is `/srv/encrypted/dev-move-98/agentq-source608-20261028-private`. Actual
`P/stage-unified-N-tsccwdf6a4/export-manifest.json` SHA256 values equal the exact
committed JSON preflight pins:

| N | Manifest SHA256 |
| --- | --- |
| 1 | `41793290b24ca68cd61e2bf3027e14951a44efd2e84d0be8677d1a104146b75b` |
| 2 | `1fe4787f887d7f7733a0de75cc4cc56540b6f5eb9ad5ad35ec110b07fdcc96c4` |
| 3 | `4a43a68bc9df54b83547d20b04c8b345f6e54c1ec735c853d49cebada38054f0` |
| 4 | `e406475889b8e83d6fe2f369a41a5adf1d1f69f94933933d1d808cb0f353fc4f` |
| 5 | `a63306a5afdfd7330d23c1cd27bbeea62edbfb9bacce261246668208fc1f81e4` |

Each manifest selects its own stage `unified-N` and run_id
`stage608-unified-N-tsccwdf6a4`, execution_state UNUSED, no launch history.
Each has exactly 16 regular files, no symlink or result; its exact sibling
`unified-N-tsccwdf6a4-offload.log` and `.rc` are absent. Compared with the accepted
unified-0 manifest, only stage, run_id, predecessor manifest and predecessor
attempt fields differ. Every predecessor points to actual accepted unified-0
manifest `3a1b42d1b104c977b258a82b82fedd85a02e15c7d2fdaaff754caad4e455708a`.

All five source/runner commits are
`f6a4de2ebc6924d16fe559f9858bf8c50dce1eba`, common export
`e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145`.
Each runner and helper hashes to manifest pins `715e53bd...cd6a` and
`a558db9a...0de4` and is byte-identical to both accepted unified-0 and the exact
frozen Git blob. Each successor archive was independently streamed and hashes to
`88fc8d3f1934c00d65e75324b79d8745f743a6fe426aaa98ecd50d38bef69ac9`.
The large source/native/compiler archives retain accepted device/inodes
64512/395540, 64512/395541 and 64512/395542 and unchanged digest pins; these
previously accepted large bytes were not redundantly rehashed.

Each exact input set has the same seven accepted native/runtime pins as unified-0:
native addon `0b6607e7...e042`, compile `4a651254...ed9e`, libtests `2f81179f...d946`,
producer `10474857...6d3`; runtime build `242dfc93...b5cb`, checkpoint
`9e028d03...d9c5`, producer `3e284e2c...bb04`. Every staged input is the same
accepted immutable inode; each distinct input inode was streamed once and all
five consumers compared against it. Both producer receipts have the expected
kind/stage/exit0/source/common identity and exact pinned outputs. Both
native608-stages receipts and the compile receipt's addon binding match.
Across all checks, 38 distinct small/input/successor inodes totaling 203298065
bytes were streamed, with bounded hash memory.

Preparation records five `verify-inputs` exit0 results. This independent review
reproduced exact required-set, pin and producer-receipt validation for every
stage using the shared-inode hash cache, avoiding five redundant input reads.
Fresh independent `sh -n` exits 0 for every runner. Fresh storage608.py checks
exit 0 for all five stages: unique bytes1960790400, free5362884608,
reserve2147483648, aggregate cap4294967296, return cap33554432 per group.
These observations do not replace live checks immediately before each launch.

Frozen group/config owners map unified1..5 exactly to
`openclaw-dts-extensions-1` through `openclaw-dts-extensions-5`. They remain
separate canonical group productions consuming native/runtime, with required
owned checkpoint roots and `.build608.json` sidecars. The unchanged runner
retains its isolated environment, 2280s elapsed-adjusted build budget,
native/compiler/snapshot/declaration identity gates, archive/receipt hashes,
and ordinary cancellation/settlement rules. No group is joined or published
by this batch preflight; middle is the later join owner.

Require accepted current checks `d9a3822e`, native `57742314`, runtime `5824b14b`,
unified-0 `ffc14e61`, compiler `dd34e5e4`, and this exact batch approval. The
preflight's PENDING compiler wording is preparation-time metadata; actual
acceptance now satisfies that procedural gate. Execute sequentially 1 through5,
one group per admitted finite run, FIRST heavy action in a fresh worker. Before
each run recheck exact manifest/UNUSED/no result/log/rc, health up, no competing
run, root filesystem >=1GB free, storage0, `verify-inputs`0, shell syntax0 and
at least 2655 worker seconds remaining AFTER preflight. Do not launch in the
current short worker or reduce the command/gates to fit it.

From the exact `P/stage-unified-N-tsccwdf6a4` directory, for that manifest's N only:

`offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-N -- timeout -k 15s 2400s sh run608.sh`

Capture exact sibling log/rc as specified in `37784051`. One launch spends that
stage. Before advancing require actual client/result0, success marker, complete
receipt/source/common/run/manifest/input/output bindings, owned checkpoint and
sidecar/inventory, storage-return0, committed complete actual evidence and a
separate independent acceptance for the producing group. Never replay a spent
stage. Preserve failed or unknown results and reconcile settlement through the
ordinary owner; no status/counter/DB edits or weakened admission floors.

All six unified groups, including accepted0, must pass and be independently
accepted before middle preparation/review/run. SDK, tail, package and final
artifact old/new/build-receipt/action/privilege/whole-seal/reseal/automatic-review/
exact genuine nonqueue HQ595 gates remain open. This review grants no install,
application, sealing or deployment authority. Only this requested review document
and its Git publication change; no heavy test/build/offload, installed/root/
service/queue/provider/config mutation or group launch occurred.

595 MUST NOT APPLY.
