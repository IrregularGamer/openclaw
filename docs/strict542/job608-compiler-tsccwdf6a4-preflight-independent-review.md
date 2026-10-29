# Independent compiler tsccwdf6a4 conditional preflight

Reviewed exact preparation `3c8a9c29` and private UNUSED export on 2026-10-29,
after independent acceptance of actual current unified-0 in `ffc14e61`.

VERDICT: APPROVE CONDITIONAL SOURCE-ONLY PREFLIGHT. 595 MUST NOT APPLY.

P is `/srv/encrypted/dev-move-98/agentq-source608-20261028-private`.
Actual `P/stage-compiler-tsccwdf6a4/export-manifest.json` hashes to
`39dbe8f21e6e6e5cb7d250900607fb88b7ddaf96192461a6fe15db62df6bf3e8`.
Stage compiler, run_id `stage608-compiler-tsccwdf6a4`, UNUSED, no launch history,
source/runner `f6a4de2ebc6924d16fe559f9858bf8c50dce1eba`.
Canonical sorted identity JSON recomputes common export
`e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145`.

Runner `715e53bd43979434f317807973d9712bc58d6ecbeec357561f92053b8aa3cd6a`
and helper `a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4`
match manifest pins, accepted unified-0 copies, and exact frozen Git blobs.
The three large archives retain accepted device/inodes 64512/395540,
64512/395541 and 64512/395542 and unchanged manifest hashes. They were not
redundantly rehashed. Streamed successor SHA256 matches
`88fc8d3f1934c00d65e75324b79d8745f743a6fe426aaa98ecd50d38bef69ac9`.
Compared with accepted unified-0, only stage, run_id, stage_inputs,
predecessor_manifest_sha256 and predecessor_package_attempt differ. The new
predecessor hash is the actual accepted unified-0 manifest `3a1b42d1...708a`.

Exact four native input hashes and device/inodes match accepted native `57742314`:
addon `0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042`,
compile `4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e`,
libtests `2f81179f5d1bf14d1519cf446935a3cd783da0e28e79a69067c85e5f873dd946`,
producer `1047485796fe27d9f653a734dcebd1828caaa455eaa1ee64d625b024c35ed6d3`.
Both native608-stages receipts match those accepted pins. Exact stage inventory:
13 regular files, no symlinks or result. Exact compiler sibling log/rc are absent.
Fresh independent `python3 -I -B stage608.py verify-inputs` and `sh -n run608.sh`
exit 0. Fresh independent storage check exits 0: 1870383174 unique bytes,
5453545472 free bytes, 2147483648 reserve, 4294967296 aggregate cap,
16777216 compiler return cap. Recheck live before launch.

The unchanged runner preserves all five actual test invocations: stock
worker-minify; native-codegen; stock lazy-barrel; native lazy-barrel; native
worker-minify. The three test files in the successor archive are byte-identical
to their frozen f6a4 Git blobs. Their existing minifier refusal, worker semantic,
codegen byte parity, phase-span and lazy-barrel side-effect/singleton/dynamic-export
checks remain present. No owner, cancellation, settlement or assertion was changed.
`required_checks: 14` describes installed-check metadata and does not substitute
for compiler suite membership.

The additional procedural gate is now satisfied by actual settled current
unified-0 acceptance `ffc14e61`, evidence `c362cd3a` plus `d597e6eb`; its source/common
identity is the one above. Require accepted current checks `d9a3822e`, native
`57742314`, runtime `5824b14b`, this exact preflight approval, fresh health up,
no competing remote run, root filesystem >=1GB free, storage0, inputs0, sh-n0,
and absent result/log/rc immediately before launch. Require at least 975s left
AFTER preflight: 600s timeout +195s settlement +180s observed transfer. Otherwise
launch FIRST in a fresh worker after the same gates.

The reviewed finite command, from the exact stage directory, is:

`offload run --timeout 600 --mem 14g --cpus 4 --artifacts result608-compiler -- timeout -k 15s 540s sh run608.sh`

Capture the actual sibling log and rc as specified in `3c8a9c29`. One launch
spends the stage. Require actual client/result0, all five complete Node summaries
with complete membership and zero failed/cancelled/skipped/todo, exact producing
receipt/source/common/run/manifest/input/output bindings, complete result inventory,
storage-return0, committed evidence and independent acceptance afterward. Preserve
failure or unknown-settlement evidence without replay; ordinary admission,
refusal and reconciliation rules remain in force.

No compiler launch or outcome is accepted here. Remaining unified1..5, middle,
sdk, tail, package, artifact/action/privilege/seal/automatic-review and HQ595 gates
remain open. Review executed only bounded read-only checks; no heavy test/build,
offload, installed/root/service/queue or live-provider mutation. No findings.
595 MUST NOT APPLY.
