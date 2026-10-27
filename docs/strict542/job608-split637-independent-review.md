# Job608 Decision637: independent finite history source review

VERDICT: APPROVE SOURCE AND RUNNERS, subject to separate exact fresh-export
verification before admitted execution. No runtime or package pass is asserted.

Reviewed independently by Rook's read-only review lane on 2026-10-27. Exact
successor `8815676d1615f4d9cc45f8ab25c82bbdf17dba34`, including split
`1acaceda`, ordinary-environment refusal `0edce246`, and affected runner
`8815676d`. Base `cd568282` contains reviews635/636. Decision637 supersedes
only review636's timeout acceptance; this successor implements no exception.

## Assertion and lifetime preservation

The cumulative history becomes four sequential cases with explicit 120000 ms
deadlines: initial build and consumer compatibility, unchanged regeneration,
isolated canonical input edit, and cold writer equality/staging cleanliness.
The diff preserves all 31 original `expect` calls and `expectStagingClean(root)`.
The only added expectation is a predecessor stage gate, executed once per case.
No assertion is skipped, excluded, made conditional, or converted to success.

One `createFixtureLifetime` owns the same temporary filesystem through all four
cases. The original fixture inputs, native fixture, preserved files, cache
records and hashes, and initial literal function declaration survive unchanged
between cases. The edited mixed-generation hash becomes the cold comparison's
input. Stage advancement occurs only after each complete successful body; a
failed predecessor causes successors to fail before consuming partial history.

Each case still owns its commands through `command.lifetime.run`, the original
test abort signal and managed child-process settlement. The suite lifetime also
tracks the complete body. Per-case cleanup joins its commands; `afterAll`
drains the retained bodies before removing shared files. The existing fixture,
compiler/cache owners and managed process implementation are unchanged.

## Runner gates

`run-package608.sh` retains the owning tooling shard, one worker, disabled file
parallelism, `--passWithNoTests=false`, failure-log reporting and shell nonzero
failure propagation. JSON installed results are retained in addition to logs.
Both runners reject inherited `OPENCLAW_608_BOUNDED_PACKAGE` and `NAPI_RS_*`
controls before ordinary tooling execution. No timeout waiver is present.

Both runners verify the four archive digests and stage receipt digests before
expensive work, and require the two regular receipt-file paths. The package's
later `prepare-native-consumer608.py` retains its stricter exact input inventory,
no-symlink, complete compile/libtest, matching source/toolchain/policy and
byte-equal native rebuild requirements. No binary or toolchain input is added.

`run-installed-split608.sh` runs the complete affected owner file rather than a
name-selected subset. Success requires Vitest exit zero, structured success,
14 passing tests, zero failures/pending/todo, one result file and four canonical
history cases. Missing/malformed JSON or an unexpected count fails closed.
Its receipt binds the source/export/run identity and raw result/log hashes and
explicitly limits scope to this affected file. Cleanup removes only disposable
source/store copies, retaining the result files.

All package-native parity, IPC refusal/cancellation, typed output, frozen
package and final artifact checks remain mandatory. Graph floors, 1 CPU,
authorized maximum 4 GiB, zero swap, cancellation and compiler/parent deadlines
are unchanged. A finite admitted outer deadline remains required. This review
does not authorize a package launch that cannot fit its execution window.

## Exact file identities and performed checks

SHA256 at the pinned successor:

- `test/scripts/write-unified-entry-dts.test.ts`:
  `03bab8f79ec16b6da3a9a96f6e735b4ee6e019e0856798ea3e20f6fee5b041df`
- `docs/strict542/run-package608.sh`:
  `6f7b431c131cf76a734af3971084d39aac589df970ac8424a01f597e0625fe9a`
- `docs/strict542/run-installed-split608.sh`:
  `0a0196496e48321f310fd5ca21ef0192f634c9816cb79ba730665907dd636ecc`

Read the exact Git diff and owning declaration, command and fixture-lifetime
implementations. Compared original and split assertion inventories (31 retained,
one new stage-gate expression). Both pinned shell runners pass `sh -n`.
No dependency install, installed Vitest, heavy test, native compilation, package
offload, root/unit/seal/sudoers action, provider call or live mutation was run by
this review lane. Fresh export review, affected runtime verification, the full
package receipt and independent action/privilege/seal plus automatic parent608
reviews remain separate required gates before the 595 handoff can be executable.

## Exact fresh installed637 export approval

APPROVE the fresh `export608-installed637` inputs for the affected-only admitted
run, using a finite 1500 s outer timeout plus 15 s termination grace, 4 GiB
maximum, 1 CPU and zero swap. This is not a full-package or application approval.

The reviewed manifest SHA256 is
`cdcd078ec71eec2ce922c04c70090a7d9c752b56f55749f381c04a340fec2469`,
source `8815676d1615f4d9cc45f8ab25c82bbdf17dba34`, run
`job608-installed637-8815676d`. Recomputed composite source identity:
`7643bdb7c558f27ff23350ccef2f6e5ddb5a936c897b5809a55e51829894438c`.

Independently streamed and matched all input SHA256 values:

- Base source: `e79a0e45a4eaea4afe325ca94ba201d5ae43d09d8c15dc07d0695c87ba743de3`
- Successor: `f484fe20027e070db38d456700e1552298e6bfe4065618f73adaf9883a407dc5`
- Native source: `d73e4e35720ffcb71856ce8168e75fa3b4fd49251fd78c811e1abded8b2701de`
- Compiler source: `203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac`
- Runner: `0a0196496e48321f310fd5ca21ef0192f634c9816cb79ba730665907dd636ecc`
- Compile JSON: `4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e`
- Libtests JSON: `2f81179f5d1bf14d1519cf446935a3cd783da0e28e79a69067c85e5f873dd946`

The runner bytes equal the pinned affected runner Git blob. All 399 regular
successor archive members equal their pinned Git blobs and exactly match
`successor_paths`; the archive has no symlink/special/duplicate members. All
changed executable/code/test paths from base are overlaid. The 83 omitted changed
paths are historical review/evidence documents under `docs/strict542`.

The export has exactly eight regular input files: manifest, runner, four source
archives and both staged JSON receipts. No filesystem symlink or special input
exists. Both receipt digests match the separately reviewed native-stage pins;
there is no addon, toolchain, dependency tree, auth, runtime configuration or
cache transfer. These receipt-only additions satisfy review635's export finding.
This verification read files and Git blobs only; execution remains the lead
worker's separately admitted step. No spent export is replayed by this approval.
