# Independent interrupted combined compaction outcome review608

VERDICT: APPROVE the interrupted-outcome evidence only. Reviewed exact commit
68f7dd3bb661f171569575464ee3f4fee56a7fb3 against base d2111e6f. No material evidence error found.
This is NOT combined diagnostic, native compilation, deterministic rebuild,
resource-fit, package or application success. Export combined1 is SPENT and must
never be relaunched; exit75 prohibits another attempt in the current worker.

## Exact run and evidence

The outcome and launch record bind foreground session31288, frozen source
6d9c429b4886d26c83888f1570f977ce63e215a7, slot
`tmp-export608-native-compact-combined1-c18fb246`, and manifest SHA256
`efa4b30f839a3b00739169f3beadd06e7989552208e592f4f5440c9bc8246968`.
Independently hashed the committed manifest and checked its source and accepted
receipt pins. The launch records03:32:43.101938Z with worker expiry04:31:27Z,
which exceeds the required51 minutes remaining. No fresh launch was performed.

Rehashed all eight outcome-bound evidence files and compared their bytes with
commit68f7dd3b and the local originals in
`/home/deploy/agentq/tmp/compaction-combined1-live`, plus the exact broker log
`/home/deploy/agentq/tmp/compaction-combined1-run608.log`. All match:

| Evidence suffix after `job608-compaction-combined-` | SHA256 |
| --- | --- |
| broker.txt | c77df336749001e93bce04d61002307f16cefad6096aac81fc1e9f1c18bf4a8a |
| checks.json | 1dbc17ed1b93d5225d3b2a63585866148f49f3a7d6ab63a672be8a7062b9c7c6 |
| native-build.txt | 0193fd13c00e12f37c776743638721bbed10a148b8d1642e8fd0af2281c7fd69 |
| native-negative.txt | 0d22b30e323e79e3266d2f6a5af221775a84b79c3130561d5d98b96fd1f45440 |
| native-receipt.json | 20821f5b4634d9a126d7b25c4cb250b7cd8954881e4ad49f26487170635e7709 |
| native-tests.txt | f6a74e06f0e0a05f7166514a13becd96897d87f2c260eeb0ec232680ba267ff8 |
| settlement.json | 2104caa311759ae8e1e8b0225f69a208846914f61220d12576702fb228b73103 |
| tests.txt | 86c20131abb7de2828b0c50e006ee7afd10f6690bf72e2298ac53e36caa11415 |

Checks evidence has exit_code0, the exact frozen source, and the exact test-log
hash. The retained log proves Node groups101+34 and Python groups
15+18+13+19+11+3+5+2+6:227 scoped checks, all passing. This does not claim the
required complete240-check diagnostic. The build log proves7 positive lifetime
tests and2 ecmascript libtests passing, including the exact named real
`compact_clone_reclaims_abandoned_arena_and_preserves_scan_identity` regression.
Ecmascript release compilation records9m51s. The separate retention-negative
mutation records4 passing and exactly3 expected failing checks: early reader
union, repeated-module final use, and unused release before first render.
These expected failures are not failed positive implementation assertions.

## Receipt identity and interruption

The incomplete compile receipt is byte-identical to its preserved original.
Its12 shared source/toolchain fields and named compaction regression match both
independently accepted compaction stage receipts:

- Compile SHA256 `4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e`.
- Libtests SHA256 `2f81179f5d1bf14d1519cf446935a3cd783da0e28e79a69067c85e5f873dd946`.

Those are also the manifest's exact two receipt inputs. Independently hashed
all four owner-input files in the maintained tree and frozen source6d9c429b;
all match the receipt. All six prepared-source hashes match both accepted
receipts, reusing the prior independent recomputation recorded in the accepted
source/skeleton review. The combined receipt differs from accepted compile
only in `complete:false` and the absent `addon_sha256`. The accepted addon pin
`0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042`
cannot supply the missing combined rebuild.

The broker log explicitly reports `job lease expired or revoked`,
`remote_lease_denied`, no local execution, and reconciliation required. The
outcome records broker exit75 after1427.565s; those precise foreground transport
measurements are recorded facts, not separately recoverable from this broker
text. The local offload runs.log has no completed combined1 entry; it does not
provide success evidence. The retained build ends during addon compilation,
with no finished addon compilation or complete receipt. The consumer requires
source rebuild completion, exact accepted receipt bytes and addon digest before
publication; that boundary was not reached. No positive implementation assertion
failure is observed. The exact lease-revocation trigger remains unestablished.

The settlement JSON equals the outcome's settlement object and its local
original: observed04:05:42.236539Z,426 lease records, zero live leases, zero
managed containers, runner lock available, mutation_performed:false. It also
explicitly records all_records_revoked:false and all_records_expiry_zero:false.
This is a historical read-only settlement observation; it does not assert that
every retained record was revoked or authorize retained-slot reuse without fresh
reconciliation.

## Remaining gates and review limits

No addon was emitted in the preserved artifacts. Native byte equality, typed
inventory, parity/trace/lazy/minifier fixtures, AI/config census and the full
typed frozen package are unproved by this attempt.595 remains gated. Only a
fresh exact secretless source-only export, independently reviewed for a later
qualifying admitted foreground worker, may be considered; never upload the
prior addon/cache, retry the spent export, or bypass the default2GiB1CPU and
outer2700s+15s bounds. All existing package, artifact/action, privilege-policy,
seal, automatic queue, baseline, natural-gap and fresh-owner gates remain.

Declined to judge: the exact revocation cause; current remote/controller/slot
state beyond the retained snapshot; future export execution or resource fit;
complete package and protected application steps. These are outside this
historical evidence review and have no acceptance here. Prior handoff
job608-resume-after-compaction.md was read as the pre-run requirements; its
unused-combined1 wording needs the parent's separate current-handoff update.

Review used read-only Git/source/log/hash inspection and count arithmetic.
No tests, builds, offload, runtime/service/seal/config changes or outbound
messages were performed. The recording commit adds only this review file.
