# Independent corrected native consumer input review, 2026-10-26

APPROVE ONE corrected source-only consumer from
`/home/deploy/agentq/tmp/export608-native-consumer-unitfast`, subject to ALL
conditions below. This is a separate input/execution decision from acceptance
of the previous exit1 outcome in job608-consumer-recovery-outcome-review.md.
It approves no passing diagnostic, package, application, privilege or seal.

Exact source is `0041793a1dfb63fc6594b3c954754717f143b17d`. Correction
`c1bf240d6c9f429c72adeb5ab750e3a158ce06e9` selects the owning unit-fast
Vitest shard, retaining empty-selection refusal, one worker and no file
parallelism. Follow-up0041793a adds the six source-reviewed package-policy
tests and the corresponding evidence label. It changes no compiler recipe,
native source/toolchain/receipt, floor, budget, parity expectation or config15
diagnostic. The prior failure was the concrete wrong-shard selection, not a
failed native compile, failed parity or failed config15 measurement.

I independently verified the fresh export's exact eight-file regular/no-link
inventory, small file hashes and complete successor archive. The successor
is byte-identical to `git archive` of every manifest-listed path at the exact
owning commit; all173 regular member bytes were additionally compared with
git. The runner equals owning `docs/strict542/run-native608.sh`; shell syntax
passes. No runner, compiler, package manager, tests or offload executed for
this review, and no large base archive was reread.

| Input | SHA-256 |
| --- | --- |
| export-manifest.json | `a09747e3c64033c41f86e40f0dc0e42b26b4fe5926dfbc33d4fe4ad63d05e494` |
| successor598.tar | `91ffa313a0b74326c9cad77ac65ceae25d8f03a4b7f02f2a24182dd4bb4c7a8c` |
| run608.sh | `39d26e327d26479f60d52cd9d4ef36529805032e14e7432f30e3f52c625e8ae0` |
| source598.tar | `e79a0e45a4eaea4afe325ca94ba201d5ae43d09d8c15dc07d0695c87ba743de3` |
| native598.tar | `d73e4e35720ffcb71856ce8168e75fa3b4fd49251fd78c811e1abded8b2701de` |
| rolldown608-source.tar.gz | `203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac` |
| native608-stages/compile/receipt.json | `e210de64481feece6ae64ee192c0e14626cc112f2ef4c47c7fac526f7fc7faad` |
| native608-stages/libtests/receipt.json | `54e7461ac5c2f2b7fb3b91408b77b7811728c7432ef9e0ca574e496fb28a7bf1` |

The manifest equals docs/strict542/job608-native-consumer-unitfast-export.json.
Source/native/Rolldown archives retain the previously verified device/inode/
size identities:1583918/689664000,1583919/921600,308931/5962781 bytes.
The runner still checks raw archive hashes before extraction. Exactly two
original receipt JSON files are uploaded; no addon, dependency/toolchain binary
or cargo output/cache is an input. The addon must be rebuilt under this lease
and again equal the complete pinned receipt and addon hash. Returned addon
bytes from the previous run remain output only and are not reused as input.

Execution is conditional on the targeted sourcec1bf240d inventory run first
settling successfully and producing reviewed evidence for ALL209 scoped
checks plus exactly three passing typed-inventory tests. The active run is not
assumed to have passed. The exact export manifest and this review must also
be committed before execution, with ordinary broker admission/settlement.

Run only in a FRESH worker with at least55minutes of verified remaining
lifetime, unchanged2GiB/1CPU budget and all original floors:

    offload run --artifacts result598 -- timeout -k 15s 3000s sh run608.sh

The smaller outer deadline bounds the whole consumer even though its existing
inner compile timeout remains5400s. Keep the foreground tool session alive
through transfer, execution, result collection and settlement. Do not launch
in the current worker expiring11:50UTC. Any refusal, timeout, transport loss,
rebuild mismatch, empty selection or test failure requires preserved evidence
and reconciliation; no automatic additional retry is approved.

Only actual completion can establish real stock/patched parity, both
lazy-barrel modes and config15 outcome. Even a passing diagnostic supplies no
full typed production package/tree, artifact-bound action/review, next-seal,
privilege handoff, application, fresh HQ owner/run acknowledgement or release
authority. All original downstream gates remain mandatory.

## Targeted inventory prerequisite satisfied

Independent returned-artifact verification against evidence733af87b completed:
sourcec1bf240d's actual evidence exits0 and binds the returned tests.log and
Vitest JSON. Node groups101,24 and Python groups15,18,13,19,11,2,6 sum to209
passing scoped tests. Vitest reports success with exactly three total/passed,
zero failed, and the result names the intended
/work/source/test/scripts/build-all-bounded608.test.ts with three assertions.
All three actual returned files equal their committed documentation copies.
Thus the targeted inventory prerequisite of review11b14be3 is SATISFIED:
212 tests passed in total. This establishes no native parity/config15/package.

Verified SHA-256 values: evidence.json
`e998816ee07a3f2217a9bf68ada2918c60f6386729749de1ffe487e48842f05d`;
vitest.json
`14b05ae3aca615c9b6358adf51eff311169eda173f3ed14d5290144b6870257f`;
tests.log
`b1be0804d6afd49b3319353a7afb3a79665eb2dbd00fa42550cc3ba4e5e5ab28`;
committed offload log
`eea62fef9a3bd89c63385c591bf2d0e7a52e3efeaef8b1163090b41dd2ccedd8`;
outcome.json
`356c81939f652225ff5bf3c84acd007915507e6d9e176d0446782f2856cf8608`.

Every other execution condition remains: the corrected consumer may run once
only in a FRESH normally admitted worker with at least55minutes remaining,
using the exact approved source/export and3000s/15s command above. No new
consumer may start in the current worker expiring11:50UTC. No artifact-bound
action, application, privilege, seal or release gate is satisfied by this update.
