# Job608 combined frozen source review

**VERDICT: APPROVE SOURCE ONLY** for exact frozen build source
`2b543da30204b358d4b58a8fb52b060f405f3789`.

Independent reviewer: Rook `/root/review_export_helper`, 2026-10-28. No new
material source issue was found. This review binds the complete source by
combining the prior exact review of
`591158cfe4a569c9e857780e9cc185cb4590b9b7` in
`job608-final-source-review.md` with the fifteen executable/test paths changed
between that source and the frozen commit, listed below. Evidence-only changes
are not executable approvals or proof of successful production stages.

## Prior source and correction chain

Read the prior591 review and independently compared its entire 22-path source
SHA256 table against frozen2b Git blobs. Nineteen paths are byte-identical;
only `build598.sh`, `stage608.py`, and `run-stage608.sh` differ and are reviewed
here with the new checkpoint owner and declaration writer integration. Thus the
previously reviewed selected-runtime reader, native-owner transport/server,
finite root supervisor, usage preflight, native targets, application/rollback
helpers, fixed service/drop-in, native rebuild/consumer, frozen package guard,
bounded compiler scheduler, worker phases and native lifetime source remain
bound to that earlier review. This is source identity, not installed identity.

Read `job608-declaration-checkpoint-independent-review.md` (9607b331),
`job608-f1fe77e8-independent-review.md`,
`job608-ce32086b-independent-review.md` (01c7a18e + ce32086b), and
`job608-review-e564e781.md`. The original f1fe77e8 CHANGES_REQUIRED verdict must
not stand alone as an approval: its F1 parent-link refusal and F2 DAG coverage
are corrected in frozen2b. Fresh tests exercised both. The e564e781 entry passes
its own preparer into build-all, breaking the top-level-await self-import cycle
without replacing admission or checkpoint validation; its regression passed.

## Complete canonical build and provenance

The bounded build still derives the full original canonical phase list and
refuses caller-selected steps, runtime-only policy, inherited compiler controls,
unadmitted capacity, cache restoration and an existing source checkout/dist.
Runtime, middle and tail partition that ordered list at the original unified
and SDK declaration writer boundaries. Six unified and two SDK producers select
the existing canonical groups through the original writer. They compile only
after restoring and validating their exact predecessor workspace.

Runtime/middle/tail receipts say CHECKPOINT_NOT_BUILT; group receipts/bindings
say COMPILED_GROUP_NOT_PUBLISHED. Middle requires all six unified bindings;
tail requires both SDK bindings. Source/export identity, predecessor receipt
digest, group receipt and complete inventory must agree. Recursive validation
checks the entire ordered ancestry, roots and phase results. `complete` requires
tail and the concatenated successful original phases, with every status `ran`.
A partial group, failed compiler, missing binding or incomplete predecessor
cannot satisfy it. Checkpoint publication occurs only after successful phases;
the runner emits its successful stage receipt only after the stage and archive
commands return zero.

Every checkpoint binds the common base/source/successor archive identity,
original lock/workspace/package, Node/pnpm, native compile/libtest/addon bytes,
portable full config census, deterministic environment and fresh-source inventory.
Outer stage manifests pin the exact required producing receipt, logs and output
digests; consumers reject extra/missing files, foreign source/export identities
and addon bytes differing from independently pinned native receipts.

Declaration joins recheck every canonical group, actual compiler membership,
snapshot signature, byte inventory, modes and topology before and after copying.
They retain the original declaration publication owner, required outputs,
conflicting-owner refusal, sanitization, relative closure and final input seal.
Both ordinary declaration entry points retain their existing behavior.

The final package runner must restore the validated tail and call `complete`
before unchanged frozen production deploy, package receipt, check-log evidence
and full runtime-tree inventory. All original checks remain in the checks and
compiler stages; the new checkpoint/refusal fixtures are added to checks.
No producer checkpoint or source approval supplies BUILT/application authority.

## Checkpoint transport and execution limits

Archives have fixed stage-owned roots and exact sidecar bindings. Restore rejects
absolute/traversing/duplicate entries, hardlinks, special types, privileged modes,
non-directory archive parents, escaping links and collisions, and uses Python's
`data` extraction filter. JavaScript validates receipt/source identity and full
inventory before restoring, refuses symlink ancestors, checks link containment
including a normalized target exactly `..`, and rechecks restored inventory.
Receipt hashing streams; large archive/checkpoint hashes are not whole-file reads.

Admission still requires observed capacity above the unchanged config15 floor
and at most 4 GiB; 1 CPU and zero swap remain external admitted-run requirements.
Native/compiler identity and process-tree settlement remain mandatory. The
existing compiler invocation owner relays parent signals and joins termination;
failed/cancelled compilation cannot publish a successful group receipt. The
2700000 ms build-all deadline remains on managed steps, and every stage requires
the finite admitted outer offload deadline and worker settle allowance.

Prior nonblocking observations F3-F7 remain limits of this approval: in-process
group production/join does not receive build-all's managed-child timeout or
AbortSignal directly; outer admitted deadlines and the compiler's signal/tree
owner must remain in force. Checkpoint preparation precedes the later heap
shortfall branch (the bounded native plan currently returns no heap shortfall).
Transport safety also relies on the supported interpreter's `data` filter for
indirect link normalization. Secretless committed export provenance, canonical
group-name agreement and exclusion of node_modules are required; these helpers
are not a general untrusted archive or secret scanner. Actual complete package
execution must prove that omitted install scratch is unnecessary. None of these
observations authorizes an unchanged failed heavy-stage retry or budget escape.

## Independent checks and limits

The tested files and their implementation dependencies were confirmed unchanged
between the working checkout and frozen2b before these commands:

- `TMPDIR=/var/tmp timeout 30s node --test docs/strict542/build-checkpoint608.test.mjs docs/strict542/declaration-checkpoint608.test.mjs docs/strict542/native-declaration-checkpoint608.test.mjs docs/strict542/native-compiler608.test.mjs`
  passed 20/20, zero failed/cancelled/skipped (14.300 seconds).
- `TMPDIR=/var/tmp PYTHONDONTWRITEBYTECODE=1 timeout 30s python3 -m unittest discover -s docs/strict542 -p test_stage608.py -v`
  passed 14/14 (0.392 seconds).
- Shell syntax checks passed for `build598.sh`, `run-stage608.sh` and
  `run-build-stage608.sh`; `git diff --check 591158cf 2b543da3` passed.

These cover partition/ancestry, incomplete/foreign/tampered source and outputs,
mode/link transport, native pin/control refusal, fixture cancellation and the
TLA regression. The actual declaration writer and native admission owner are
exercised, but compiler/snapshot/publication boundaries are partly injected;
this is not production native declaration or complete package execution proof.
Node emitted its existing experimental stripTypeScriptTypes fixture warning.
No heavy build, full suite, dependency install, export preparation, offload,
installed/root/service/unit/seal or producer mutation ran in this review.

The later local hardlink preparation helper is separately reviewed at
`1a8b422d6e43897d5b8036585218e1585226b515` in
`job608-hardlink-helper-independent-review.md`. It does not change this frozen
build pin; the old preparer blobs below are source inventory, not authorization
to use their superseded local copying procedure.

## Gates before595 application

The complete exact-source production package, runtime tree, build/check/test
receipts and full staged provenance remain required. Prior591 or intermediate
source results cannot be relabelled as frozen2b proof. This review approves no
artifact, action, privilege policy, seal, application, service or scheduler step.
Before595 applies, independently review the exact final artifact/tree, action
and helper/backup/rollback identities, current privilege policy and exact
original/additive next seal, bind those reviews to this source and final bytes,
and obtain the real automatic queue reviews required by the existing workflow.
The ordered HQ handoff still requires genuine finite foreground nonqueue
ownership, a natural settled admission gap, unchanged guards, original seal and
native predicates, separately reviewed service actions, and fresh post-restart
owner binding AND accepted-run acknowledgements. No gate is waived here.

## Exact changed-source identities at frozen2b

| Path | SHA256 |
| --- | --- |
| `docs/strict542/build-checkpoint608.test.mjs` | `50ef4d64ec2ad25e9fdb91f2e4aa1c09ae69d0169a640de6744d161cf5aab800` |
| `docs/strict542/build598.sh` | `c8a4ae84a453da897544639eafcd2532302eb639e5cfe3dda409e208fdd49789` |
| `docs/strict542/declaration-checkpoint608.test.mjs` | `3716eeb232c46545dd08b0e2f3bbbcd451970e6648853d9a8a05500b76f6a443` |
| `docs/strict542/native-declaration-checkpoint608.test.mjs` | `686af52165a6a51d35260c56ee5f6e8be1d1cf4d51a25cb71afe164ea167a225` |
| `docs/strict542/prepare-finite608-export.py` | `161067f7291a78a98dd4e9f253f843bb3a823b4b667a7f483c2dee58346d395a` |
| `docs/strict542/prepare-stage608-export.py` | `ffe2b9f3d58809bf2e308ff1d42d88c0d7a5db8dcb30005358fc713555bf34f6` |
| `docs/strict542/run-build-stage608.sh` | `95cf54e01e33303691f0d0303a3e075f7f13de8fe77b386bedc1f325f53ad589` |
| `docs/strict542/run-stage608.sh` | `a77673ff2774592a03e48da07711637fd508fec0ef4b26dd363d46ff25542e8e` |
| `docs/strict542/stage608.py` | `c162c5a15c9fc1392c5fbec06f543127f176031a162d99aaf4ea3b6b2c2a5d52` |
| `docs/strict542/test_stage608.py` | `6a7a164902939538d75639dd79ef46fe11e2f8127cfbf8f3a7cba4f99ff821e1` |
| `scripts/build-all.mts` | `4b923e4627999e6b6978444d2d8bfc76c3c6fa640de41136afa55345637754b7` |
| `scripts/build-checkpoint608.mts` | `c69ffb9400f5521090450bbbb3fe090fe5c75462d5f20886a15b5c4331000790` |
| `scripts/lib/bounded-build-checkpoint608.mjs` | `ee87431017449c2abdf9bcea1915606a2b02cb574efbdd1747653d11fec29286` |
| `scripts/lib/declaration-checkpoint608.mjs` | `981645225a3ce4cddd627860c13e196941f03e7a543390dd9ab5ed5ab2e6ed8a` |
| `scripts/lib/tsdown-declaration-writer.mts` | `9f33711c418315bcf237bc9f8edaf17c810198ebc8d270d3a16547d1341807ef` |
