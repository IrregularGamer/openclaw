# Independent inventory-only execution review, 2026-10-26

APPROVE ONE normally admitted scoped/inventory-only offload of exact source
`c1bf240d6c9f429c72adeb5ab750e3a158ce06e9` from the fresh secretless export
`/home/deploy/agentq/tmp/export608-inventory`, subject to the finite worker
window below. No native rebuild, parity, config15, production build/package,
application, action, privilege, seal or release run is approved here.

The primary reports that the prior source157b93a8 consumer completed its native
rebuild with the exact pinned addon equality and frozen dependency installation,
then failed because the tooling Vitest shard selected no tests. That is a
failure, not parity/config15 or package evidence. This targeted run validates
the owning test selection and current scoped source; it does not repeat the
native compilation or manufacture the unfinished consumer outcome.

The source correction is specific: basec790's
`test/vitest/vitest.scoped-config.ts:217-222` excludes unit-fast members by
default; `vitest.unit-fast.config.ts` owns their inclusion. `run-native608.sh:84`
now selects that owner while retaining `--passWithNoTests=false`. This review
does not authorize executing that full consumer runner.

`run-inventory608.sh:32-40` runs the existing scoped gateway/native/IPC/
cancellation/application/policy checks, including all six package-guard tests.
Its only dependency operation is the unchanged frozen pnpm12.5.1 install.
`:42-50` selects the exact typed inventory file using the owning unit-fast
configuration, one worker, no file parallelism and empty-selection refusal.
The JSON gate requires success, three total tests, three passed and zero failed
before emitting `SCOPED_TESTS_ONLY_NOT_BUILD_OR_APPLICATION`. The selected file
has exactly three tests: complete canonical phase/order preservation, retained
4352MB admission refusal at2GiB, and typed-output skip refusal. It does not
execute those compiler phases.

Runner cleanup is confined to its own extracted `source`, `native-source` and
disposable `.pnpm-store`; artifacts remain in `result608-inventory`. Archives
are digest-verified before extraction and released only after consumption.
The finite outer command also bounds dependency installation. No source or
runtime mutation was performed by this reviewer; only shell syntax and static
source/export checks ran, not this runner or its tests.

Exact export verification completed independently:

| Input | SHA-256 |
| --- | --- |
| export-manifest.json | `29746963a9726f6ead478baeb3ab77dfa846dc1a183814af091bb9cc55521a62` |
| successor598.tar | `0a3a886fa775167deaecd47a05b016799faf240c137a360351b526acde8a73b1` |
| run608.sh | `7003f547f2c66044bba2de8867bfac7888455cd99d79511c96097609308a9be1` |
| source598.tar, retained basec790 | `e79a0e45a4eaea4afe325ca94ba201d5ae43d09d8c15dc07d0695c87ba743de3` |
| native598.tar, retained external source | `d73e4e35720ffcb71856ce8168e75fa3b4fd49251fd78c811e1abded8b2701de` |
| test/scripts/build-all-bounded608.test.ts | `a6dd0fff1e278a52937777a703a6d601e395c2bddeb13a6519aefe2d4fa084ae` |

The manifest equals `docs/strict542/job608-inventory-export.json`. The successor
tar is byte-identical to `git archive` of its complete listed source paths;
all164 regular member bytes were separately compared with the owning commit.
The runner equals owning source. The export contains exactly its five expected
regular, non-symlink files. Large base/native archives retain the previously
verified same-device/inode/size identities (1583918/689664000 bytes and
1583919/921600 bytes respectively); they were not reread. Their raw digest
checks remain mandatory in the remote runner before extraction. `sh -n` of
both changed runners passed.

Use only the existing admitted 2GiB/1CPU broker path:

    offload run --artifacts result608-inventory -- timeout -k 15s 480s sh run608.sh

The primary must commit the exact export manifest first and confirm ordinary
settlement/admission. At review verification time11:39:58UTC, the primary's
worker expiry is11:50UTC. Admit only while enough worker lifetime remains for
the full480s deadline,15s kill grace, transfer and result/settlement handling;
otherwise defer. Keep the foreground session alive through settlement. A
refusal, timeout, transport loss, missing result or failed test requires
preserved evidence/reconciliation and grants no automatic further retry.
This is source/input approval for that one run, not a passing test receipt.
