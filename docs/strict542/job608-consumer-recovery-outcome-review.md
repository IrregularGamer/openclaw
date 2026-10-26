# Independent admitted consumer outcome review, 2026-10-26

APPROVE the accuracy of the preserved outcome/evidence from source
`157b93a8f0db0d1fe61c71cb7fdfd635c81a6c76`, admitted under review
`f81194b0648766f0f8ab04153b4122e7c620b4bc`, and committed in evidence
`1384ca5e`. This is evidence acceptance only, not a passing consumer, build,
package, action, application, privilege, seal, scheduler release or deployment
approval. The consumer's actual exit code is1.

I independently verified all six file hashes named by the outcome, its scoped
check log binding, the rebuilt receipt against the separately pinned compile
receipt, and the actual returned output-only addon bytes. No runtime mutation,
package manager execution, tests, compiler or offload ran for this review.
No large source archive was reread.

The scoped log records Node groups101 and24 passed, zero failed, plus Python
groups15,18,13,19,11,2, each OK. These sum to203 actual passing scoped tests.
That total does not include the subsequently added six package-policy tests
or the separate earlier110-test native library stage.

The native compile log records release completion in23m49s. Its complete
receipt equals `job608-native-compile-receipt.json` exactly, including pinned
owner/patch/toolchain/cargo/lifetime fields. The actual returned addon is
24,295,760 bytes and hashes to
`f8b7634b1ccf713ec593f2a802373e16bffc92f1a63edd82704232c4960adcc6`,
matching both receipts. It remains output only at
`/home/deploy/agentq/runs/608/native-consumer-recovery-results/result598/result598-native/rolldown-binding.linux-x64-gnu.node`.
This establishes this native rebuild's byte equality; it does not establish
complete application/package reproducibility or authorize binary upload.

The probe log records frozen dependency install completion with pnpm12.5.1
in2m13.6s, followed by Vitest's `No test files found, exiting with code1` for
`test/scripts/build-all-bounded608.test.ts`. The test file appears in both
the include and exclude lists. This matches the reviewed tooling-shard
selection defect. `run-native608.sh` at source157b93a8 uses `set -e` before
that command and orders native parity, both lazy-barrel modes and config15
after it. Therefore those later phases did not run. There is no real parity,
config15 measurement or full-build/package result from this consumer.

| Preserved evidence | SHA-256 |
| --- | --- |
| job608-consumer-recovery-outcome.json | `18ee9bb4b564e9914b8c3e41e1da7614f3edaefc668c028d296c517a222165e4` |
| job608-consumer-recovery-native-receipt.json | `e210de64481feece6ae64ee192c0e14626cc112f2ef4c47c7fac526f7fc7faad` |
| job608-consumer-recovery-native-compile.txt | `dd259bdf02e53048aa55062fce2a8329d4555b0bf244c8de752458581d3fd0b8` |
| job608-consumer-recovery-checks.json | `3602599f34ff807543bfcf3d75549b5ac57f052246e5916f5fd567dcf4302827` |
| job608-consumer-recovery-checks.txt | `fe74bb6132a3e163823589ab44ee2e1b5b40fd7f16cd9ddc3949a1b719f27346` |
| job608-consumer-recovery-probe.txt | `5bbad745a4cceceea5884d206ae09d2afe6ce1dc05327c6b1c0810148d2e36ab` |
| job608-consumer-recovery-offload.txt | `6bfd100aecd0df6db93f098cceb53354db829a7416431fcd1ba91a53fa0d7bb6` |

Correction `c1bf240d6c9f429c72adeb5ab750e3a158ce06e9` selects the owning
unit-fast shard while retaining empty-selection refusal. Its separate targeted
inventory run covers the current209 scoped checks and three inventory tests
only if its eventual exact result proves them; that result is not presumed
here. It does not replace real native parity/config15 or production packaging.
Follow-up `0041793a1dfb63fc6594b3c954754717f143b17d` adds the six reviewed
package-policy tests and matching evidence label to a future native consumer;
it grants no unexecuted outcome.

At independent verification time11:44:24UTC, the current worker expires at
11:50UTC. The observed23m49s native rebuild alone cannot fit that remainder,
even before installation, parity, config15, transfer and settlement. Do not
launch another corrected native consumer in this worker. It requires a fresh
normally admitted worker with sufficient finite lifetime, a fresh secretless
source-only export, exact committed manifest/runner/receipt pins and a new
independent execution decision. No future export is approved by this outcome
review. Preserve every original2GiB/1CPU limit, floor and application gate.
