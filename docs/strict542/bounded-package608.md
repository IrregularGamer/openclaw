# Complete bounded package build (source preparation)

The unpromoted source candidate `boundedPackage` profile belongs to `scripts/build-all.mts`. It has
exactly the canonical `package` profile's ordered phases, including clean, all
package declarations, both canonical unified declaration writers, SDK export and
CLI import checks, bundled and external plugin assets, UI, postbuild, metadata
and stamps. It disables artifact caches. The normal `full` and `package` profiles
retain the measured 4352 MiB admission guard without alteration.

Only AI/package/unified compiler scheduling changes: each complete original
configuration runs in a fresh compiler process with concurrency one. The unified
singleton graph remains one configuration, with the original entry map, output
paths, plugins, dependencies and lazy-barrel policy. The typed config census binds
selection; mismatch, missing typed package configs or runtime configs requesting
declarations refuses. Canonical declaration writers still own partitioning,
staging, compiler-input receipts, input-change verification and publication.

This candidate is limited to fresh secretless disposable exports admitted to the
existing offload broker's hard 2 GiB RAM, zero swap and one CPU lease. Before any
build output mutation, it rejects inherited compiler controls, `.git`, previous
`dist`/`dist-runtime`, unresolved memory capacity, capacity above 2 GiB or effective
limit at/below the unchanged 1625784320-byte config15 reclaim-thrash floor. It
rechecks capacity before each whole compiler config. Native pools are fixed to
one and mimalloc THP is disabled before compiler imports. These are process
controls; no cgroup, unit, sudo policy or installed file changes.

Both the build owner and direct unified compiler driver retain canonical full-graph
4352 MiB admission before any cleanup. Consequently this candidate refuses a
2 GiB full build before output mutation. The changed-source lazy-barrel diagnostic
reached linking but received SIGKILL after buildEnd at the2GiB ceiling (rendering is an unconfirmed source-analysis hypothesis); whole-config scheduling does
not establish that this memory requirement can safely be lowered. A reviewed
source correction that bounds post-link memory and successful complete measured
validation remain prerequisites to any change in that admission.

The build owner has one absolute 45-minute build deadline; each compiler group
has an absolute 15-minute deadline. Existing managed-child and tsdown owners
forward cancellation, settle process groups and scan unresolved imports and
ineffective dynamic imports. Any timeout, compiler/scanner refusal or unsettled
child fails the build and cannot create accepted package evidence.

Do not run this profile before the changed-source whole-config diagnostic has
completed successfully and an independent reviewer has accepted that receipt and
the exact bounded profile source. The profile is an alternative explicitly scoped
schedule, not evidence that the normal full-build memory guard is unnecessary.
The diagnostic must not be relabeled a full typed build.

There is currently no supported successful full build under the admitted 2 GiB
budget. Do not execute another unchanged diagnostic or attempt this profile's
full build; it intentionally refuses before cleanup. Preserve this source
schedule for exact review after a post-link memory correction. No build/package
receipt exists for this candidate.

Once the memory correction and complete build are independently reviewed, the
package/receipt owner must execute every existing package validation,
native pin validation, supervisor IPC/refusal/cancellation check and deterministic
artifact packaging step. Successful compiler scheduling alone is not a package,
installation, action/privilege/seal review or application authority. No live
provider, credential transfer, gateway restart or deployment occurs here.
