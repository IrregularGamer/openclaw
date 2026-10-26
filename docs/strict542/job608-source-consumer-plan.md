# Source-only native consumer, source 157b93a8

This supersedes only the binary-input consumer paragraph of
job608-native-split-plan.md. Native compile and libtests stage recipes, pinned
sources/toolchain, 2GiB/1CPU hard lease and their finite 5400s deadlines remain
unchanged. This is diagnostic preparation, not package/application authority.

The interrupted libtests attempt is preserved in
job608-native-libtests-interrupted-* and reconciled in
job608-native-libtests-recovery-review.md. Only a complete, successful recovered
stage receipt permits the next stage. The original remote slot remains untouched.

The consumer export consists of the existing digest-pinned source598.tar and
native598.tar, the pinned Rolldown source archive, git archive of the exact
successor_paths in its manifest, run-native608.sh as run608.sh, and exactly two
manifest-pinned JSON files under native608-stages/{compile,libtests}/receipt.json.
No addon, cargo target, toolchain, dependency tree, credential or runtime config
is uploaded. prepare-native-consumer608.py refuses any extra binary input,
redirected input, absent/unfinished test receipt or disagreeing source/toolchain.

Commit the final exact manifest and receipt evidence before execution. Run once
from that fresh export with the existing broker:

    offload run --artifacts result598 -- sh run608.sh

The runner performs all scoped gateway, external-native, supervisor real IPC,
cancellation/settlement, disk-preparation and policy tests, including the new
exact-original-seal-link and source-only consumer refusal cases. It rebuilds
the addon from source under the current lease and requires its complete receipt
and addon bytes to equal the previously pinned compile artifact. The existing
nativeCompiler608 owner then validates BOTH complete compile/libtests receipts
and the actual addon before import. This checks native rebuild reproducibility;
it does not establish full application reproducibility.

After frozen dependency installation and ordinary disposable store release,
the runner includes the formerly unrun installed Vitest typed-profile census
check (one worker, no file parallelism, empty selection refuses), real
stock/patched eight-variant bundler output/behavior parity, both lazy-barrel
fixture modes, then the finite complete-config runtime diagnostic. Canonical
4352MiB full-package admission and the diagnostic1625784320-byte floor remain.
No failure, SIGKILL, missing settlement or receipt is a successful build.

The exact current baseline was read-only verified in
job608-current-baseline-validation.json: all56 original seal entries, seven
guard bytes/complete metadata records, boot and six absent targets match the
historical baseline without refreshing it. The original seal includes the
preexisting devstack symlink. Installed control.py validation_ok hashes through
it; the preparation previously refused it unconditionally. c32bea1e now permits
only that fixed original link string and resolved non-link target, with its
original sealed content hash; all other links, redirection, changed content or
replacement by a regular file refuse. The regression was red before correction
and green afterward. No installed validation predicate, seal or file changed.

Current successor corrections require exact independent source review before
application. No source/action/privilege/seal/automatic approval for an absent
full package is claimed. Full typed build, frozen production package, real
tree/action/next-seal receipts and independent reviews remain mandatory after
diagnostic success; use job608-to595.md's ordered natural-gap procedure.
