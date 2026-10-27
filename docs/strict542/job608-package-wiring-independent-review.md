# Job635: independent job608 package wiring source review

VERDICT: CHANGES

Reviewed 2026-10-27 by Rook. SOURCE ONLY: no installation, application,
production deployment, package offload replay, or automatic parent608 review.

## Exact scope

Base `aaf84b93` (review633), followed by exactly `cdad2e7e`, `24ae6bfc`,
`a6a460c9`, `e4d80ecb`, `b8ee3f4e`, `dc3bba88`, `20552650`.
Target `205526509eb922430cbce488df6d1a329b49e9a3`; the maintained branch
already contains later work. Findings below concern the pinned target and
retained package1 export, not approval of those later commits.

## Required changes

1. **Installed tests cannot run in the selected shard.** At target
   `docs/strict542/run-package608.sh:66`, all four `test/scripts` suites are
   selected through `test/vitest/vitest.unit-fast.config.ts`. Its discovery
   rejects these files: the exact target classifier finds `filesystem-state`
   in all four, plus mock/dynamic-import reasons in two. None is forced into
   unit-fast. With `--passWithNoTests=false`, this exits nonzero before native
   rebuild, checks receipt, or package build. Select the owning tooling shard
   and preserve the nonempty-selection/failure gate. Later `55a1dd59` already
   makes this source correction; it is outside this review range and does not
   retroactively validate package1. `703502c1` separately surfaces failure logs.

2. **Retained package1 is missing required native receipt inputs.**
   `/home/deploy/agentq/tmp/export608-package1` currently contains only the
   manifest, runner and four archives. There is no
   `native608-stages/compile/receipt.json` or
   `native608-stages/libtests/receipt.json`. The manifest pins both, and
   `prepare-native-consumer608.py` requires them at the export root before
   rebuilding. The runner never stages them. Even after fixing item 1, this
   retained export cannot reach the real-native checks. A fresh job608-owned
   export must include exactly those source-stage JSON receipts, verify their
   pinned hashes, and transfer no addon/toolchain/cache/auth material. Do not
   replay the spent package1 export. This observation concerns the retained
   directory; it does not establish what a historical remote slot contained.

## Native route and retained safeguards

`resolveNativeBoundedTsdownPlan608` refuses both heap override environment
keys and `resolvedMaxOldSpaceMb`; heap sizing still uses canonical observed
memory budgeting and normalization. Parent admission rejects inherited
`NODE_OPTIONS` and native/compiler controls. Required native receipts, source
owner hashes and addon bytes are revalidated by
`trustedNativeCompilerEnvironment608` at parent preparation, child startup,
planner entry and declaration compilation. The derived native environment is
established before transitive config/native imports; caches remain disabled.

The graph floor remains **1625784320 bytes**. The dedicated route permits
observed capacity up to the already authorized 4 GiB, refuses unresolved,
nonfinite, inverted, or floor-level limits, and rechecks capacity per config.
Ordinary full/package planner admission is unchanged, including its fatal
4352 MiB full-graph heap requirement. The canonical package phase inventory
and complete typed output requirement remain intact. Cancellation checks,
live-Gateway output fencing, process-tree settlement, 2700000 ms parent
absolute deadline and 900000 ms compiler-stage deadline remain present.

## Runner, packaging and authority

All four archives are hashed before extraction. Scoped tests, installed tests,
source-native byte-equal rebuild and real native parity/lazy/minifier tests
are ordered before `strict542-checks/evidence.json`; nonzero status prevents
that receipt. Item 1 makes the gate fail closed, rather than forge success.
The final build receipt additionally binds test-log hash, source identity,
source/target locks, deployment log, package receipt and native receipt/addon
hashes. `pnpm deploy` here creates a private portable directory; it does not
install or activate a running service.

The builder receives `env -i` with only HOME, tool PATH and three fixed manifest
identities. pnpm 12.5.1 is checked before and after resolving its physical
shim, and again by the builder. Both installs use `--frozen-lockfile`;
frozen-package preflight retains original lock/workspace/npmrc pins and
rejects npm/pnpm configuration inheritance and legacy fallback evidence.
No host environment/auth/secret transfer is introduced by this diff. HOME is
the remote builder home, not an uploaded home directory.

`releaseDisposableStore("..")` owns only export-root `.pnpm-store`, requires
real source/node_modules/store directories and clone-or-copy/isolated policy,
and refuses escaping installed links before deletion. EXIT cleanup is scoped
to the disposable export. Native rebuild has `timeout -k 15s 2400s`; compiler
and package build have the finite internal deadlines above. Installs, tests
and packaging still require the admitted foreground worker/outer execution
limit; these shell scripts do not themselves supply a total-run timeout.
Keep a finite outer deadline for any corrected job608 launch.

## Export identity verification

Manifest SHA256:
`417ecc62e54c2999f6d004d7aa534c533e2ae556085b6792fe57f52849a790c6`.
Its committed copy at `ce6548f4:docs/strict542/job608-package1-export.json`
has the same digest. Rehashed all four retained archives: every digest matches
its manifest field. `run608.sh` equals target `run-package608.sh` byte for byte,
SHA256 `453eacecedcb36c3cc3d3e1c6816a057708fa94bcbaa831a72099f5274b773b6`.
All **385** successor regular files equal their target Git blobs and exactly
match `successor_paths`; no special successor archive members exist. All
changed executable/code/test paths since base `c790ba44` are overlaid.
The 83 omitted changed paths are historical review/evidence documents under
`docs/strict542`, not executable source: this is a selected source overlay,
not a claim to contain every historical document in the target Git tree.

`source_export_sha256` is an acceptable composite identity, not a raw tar hash:
SHA256 of UTF-8 canonical JSON, sorted keys and separators `(',', ':')`, with
exactly `base_source_archive_sha256`, `source_commit`,
`successor_archive_sha256`. Recomputed value:
`acb4672002313ccff0bc6b7cedcff0265b86df651da935f78a7c59782e72ca67`.
The separately pinned runner, compiler archive and native archive identities
must remain alongside it. Matching composite/archive identities do not imply
all required external receipt files are present (item 2).

## Verification performed

Pinned lightweight snapshot from `git show 20552650:<path>`; no dependencies
installed. `TMPDIR=/home/deploy/agentq/runs/635 timeout -k 5s 60s node --test`
with `native-compiler608.test.mjs`, `bounded-package608.test.mjs` and
`disposable-inputs608.test.mjs`: **15 passed, 0 failed**, about 1.5 seconds.
Both pinned shell files pass separate `sh -n` checks. Executed the exact
unit-fast disqualifying patterns against the four target test blobs and
verified their absence from the forced-inclusion list. Archive/overlay and
composite checks were read-only and streamed; no package run was started.
Installed Vitest, native rebuild and full package execution were intentionally
not repeated: job608 owns those stages. Later package outcomes or baseline
exceptions are not approved here. This verdict grants no application authority.
