# Complete bounded package build (source preparation)

The explicit `boundedPackage` profile belongs to `scripts/build-all.mts`. It has
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

This profile is only for fresh secretless disposable exports admitted to the
existing offload broker's hard 2 GiB RAM, zero swap and one CPU lease. Before any
build output mutation, it rejects inherited compiler controls, `.git`, previous
`dist`/`dist-runtime`, unresolved memory capacity, capacity above 2 GiB or effective
limit at/below the unchanged 1625784320-byte config15 reclaim-thrash floor. It
rechecks capacity before each whole compiler config. Native pools are fixed to
one and mimalloc THP is disabled before compiler imports. These are process
controls; no cgroup, unit, sudo policy or installed file changes.

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

After those reviews, use only a fresh committed `git archive` export through
`offload run`, with its ordinary 2 GiB/one CPU limits. Install frozen dependencies
through the existing reviewed export/bootstrap procedure. Run the policy tests
and the real `test/scripts/build-all-bounded608.test.ts` inventory tests remotely,
then invoke:

```
node --import ./scripts/tsx.mjs scripts/build-all.mts boundedPackage
```

The package/receipt owner must then execute every existing package validation,
native pin validation, supervisor IPC/refusal/cancellation check and deterministic
artifact packaging step. Successful compiler scheduling alone is not a package,
installation, action/privilege/seal review or application authority. No live
provider, credential transfer, gateway restart or deployment occurs here.
