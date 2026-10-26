# Independent source-only consumer recovery review, 2026-10-26

Reviewer: Rook, independently dispatched for source/export/recovery review.
Reviewed implementation source `157b93a8f0db0d1fe61c71cb7fdfd635c81a6c76`
and evidence HEAD `597ff87530d85608a4281b15fdeccf1128ad1cdf`. This review
authorizes no runtime, provider-auth, production, privilege or seal change.

The first consumer was interrupted during Rust compilation, not after a test
failure. Its recovered compile log ends at compilation of `rolldown`; its
receipt is `complete=false`, with no addon hash. The local offload log contains
successful scoped policy checks but no completed consumer result. There is no
completed rebuild/equality, parity, config15, package or application evidence.
The original remote slot remains untouched. The primary's read-only remote
reconciliation, recorded at 2026-10-26T10:53:17.644738+00:00, found zero live
leases and zero managed containers. I verified the recovered file hashes:

| Recovered file | SHA-256 |
| --- | --- |
| native-compile.log | `334f3e2f4847dc9a20c3991d10570cb9ecea062aa82b7f2bb79376929123dd8b` |
| incomplete native receipt | `c8323083465d2d74ddf1bb54e5434e26feecca644742927d3e8930b04733f43a` |
| scoped-check evidence | `382f582cb2182452107eecc2fdeef547ca6ce06400d74d0a460bcf08b1369933` |
| scoped-check test log | `f82380f0b2a6f5904223c66f5a1e63d19f1a122dedfb7636cb29108585243a0f` |

The separately completed compile receipt pins addon
`f8b7634b1ccf713ec593f2a802373e16bffc92f1a63edd82704232c4960adcc6`.
Its compile log records successful release completion and rc=0. The completed
libtests receipt records exit 0; its build log records 110 passed, zero failed.
Both complete receipts agree on all source/toolchain/cargo/lifetime fields,
and their owner-input digests equal the reviewed source bytes. They remain
prerequisites, not consumer success. No addon is uploaded in this recovery.

I reviewed successor corrections `c32bea1e`, `bc46f02c`, and `157b93a8`:

- The original-seal exception admits only the exact preexisting devstack link
  string, resolved regular target and original sealed target bytes. Changed
  link, content, ordinary-file replacement and unlisted links refuse. This is
  preparation source only; it does not alter installed validation or the seal.
- Bounded package admission rejects inherited `NAPI_RS_` controls, retaining
  its capacity floor and typed inventory gates.
- The consumer admits exactly the two manifest-pinned receipt files, refuses
  extra or redirected inputs and incomplete or disagreeing receipts, rebuilds
  from pinned source, then requires exact complete-receipt and addon equality.
  `nativeCompiler608` additionally checks both completed stage identities,
  owner-source pins, toolchain agreement, native test success and addon digest.
  Real stock/patched parity, both lazy-barrel modes, typed census and the finite
  config15 diagnostic follow; their failures cannot count as success.

Focused verification passed: 2 `test_native_consumer608.py` tests, 11
`test_apply598.py` tests and 6 Node native-compiler/bounded-package tests, all
exit 0. No compiler, full suite, offload or runtime mutation was performed by
this review. No blocking source finding was found in this recovery scope.

The exact fresh recovery export is
`/home/deploy/agentq/tmp/export608-native-consumer-recovery`.
Its manifest equals committed `job608-native-consumer-source-export.json`,
SHA-256 `3b229ab77bd5fc86e77239f465de3d25b0f007eec7443f68a31d35ce540b1b5d`.
I independently checked the exact eight-file regular/no-symlink export
inventory and all fresh small input hashes below. I independently rehashed
the retained base archive; the primary's full fresh-copy base hash is still
running at review commit time and MUST finish successfully before execution.

| Export input | SHA-256 |
| --- | --- |
| source598.tar | `e79a0e45a4eaea4afe325ca94ba201d5ae43d09d8c15dc07d0695c87ba743de3` |
| successor598.tar | `4b1e3a1d7241fe83026e331284bd859b0b119e5d033ba66da9d22d12c03791fe` |
| native598.tar | `d73e4e35720ffcb71856ce8168e75fa3b4fd49251fd78c811e1abded8b2701de` |
| rolldown608-source.tar.gz | `203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac` |
| run608.sh | `428fc9e239dba61299267ed362746e9eda8c29af57e29eaf894d13c9b7875fdb` |
| native608-stages/compile/receipt.json | `e210de64481feece6ae64ee192c0e14626cc112f2ef4c47c7fac526f7fc7faad` |
| native608-stages/libtests/receipt.json | `54e7461ac5c2f2b7fb3b91408b77b7811728c7432ef9e0ca574e496fb28a7bf1` |

The retained successor archive is byte-identical to `git archive` of the exact
manifest successor paths at source157b93a8; the fresh archive has that same
digest. The runner equals owning source. Small member scans completed for the
successor (152 members), native source (61), and pinned upstream source
(18,406). The upstream source includes 1,241 tracked test-fixture members
under `node_modules`; these are source fixtures, not an uploaded installed
dependency tree. No new environment/credential/target tree is present in the
changed inputs. The large base archive retains its previously reviewed
identity; I stopped a redundant full member rescan after verifying its raw
digest and do not claim that rescan completed.

Reviewed owner SHA-256 values: `prepare-native-consumer608.py`
`6b1b60803e8cebb05a1a7fc12401094149a621feae28cb18fc37125c9b07cf66`;
`native-compiler608.mjs`
`d300923b2dc6198cce70ab873c914538957bbcc3ebe33f23946ce029dacf9906`;
`apply598.py`
`9a3f6ef6e51345f0e2b607c6b79bc120e6e020882bdfc11affaad919627ad092`;
`bounded-package608.mjs`
`403b8e19386d3db5c16a535504ba983892fcb72384a4fb4d7aa8f3002103fc65`.

APPROVE ONE recovery consumer, contingent on successful primary full fresh
archive/runner/receipt digest verification and ordinary broker admission.
Use only this fresh secretless export, unchanged 2GiB/1CPU lease and floors:

    offload run --artifacts result598 -- timeout -k 30s 7200s sh run608.sh

The rebuild retains its 5400s deadline; the config15 probe retains its 900s
deadline. Keep the foreground tool session alive through settlement. Any
transport loss, refusal, timeout, source-rebuild mismatch or test failure
requires preserved evidence and reconciliation; this grants no automatic
further retry or larger resource budget. This decision covers diagnostic
recovery only. It does not approve a full typed production package, installer
application, action/tree/next-seal receipt, privilege handoff, seal amendment,
automatic build review or release. Those gates remain mandatory.
