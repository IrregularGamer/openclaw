# Independent declaration-owner source review608

Scope: static review of frozen source1bed4d1b, performed as the independent
source/performance lane. No compiler, build, test, offload, runtime mutation or
package publication was launched. This document is source analysis, not an
acceptance receipt or proof that the2400second timeout is fixed. All original
final source/action/privilege/seal/automatic-queue/HQ and post-restart genuine
owner/ack gates remain;595 MUST NOT APPLY.

## Concrete recommendation

The smallest supported correction is the single argument at
`scripts/lib/native-declaration-emitter.mts:94`: pass the original `assertInput`
to `createDeclarationFileSystem`, in place of `assertInput ? admit : undefined`.
Keep `before.readText`, the snapshot policy's composed `admit`, the other
explicit admissions and all filesystem implementation checks unchanged.

The evidence is an exactly duplicated policy operation. In bounded production:

1. `createDeclarationFileSystem.local` resolves the candidate, rejects lexical
   outsiders and executes its own `boundary.assert(absolute)` before invoking
   the supplied callback (`native-declaration-filesystem.mts:20-38`).
2. The supplied callback is currently emitter `admit`, which executes another
   `boundary.assert` and then the arbitrary caller `assertInput`
   (`native-declaration-emitter.mts:46-51,92-97`). Both internal boundaries use
   the same physical checkout root. The filesystem boundary has already
   normalized the path before the emitter boundary sees it.
3. The tsdown caller supplies its own `boundary.assert`
   (`tsdown-declaration-boundary.mts`, native emission call). There are therefore
   THREE physical boundary assertions before ordinary lookup work, not four.
   Other callers may supply a different policy, so that third assertion is not
   assumed or removed by this recommendation.
4. Every physical assertion performs a synchronous nearest-existing-ancestor
   search using `existsSync`, then `realpathSync.native`, with lexical and
   physical containment checks (`local-check-runtime.mts:122-134`). Negative
   module/package probes repeat that work for their missing ancestors. Native
   filesystem requests additionally cross the JS/native API transport.

Passing the raw caller callback removes only item2's repeated INTERNAL physical
assertion. Even an identity or custom `assertInput` still runs on every admitted
callback, after the filesystem's independent physical containment assertion.
With no caller policy, the argument remains undefined and the existing
unbounded mode is identical. No filesystem result, path admission or symlink
target is cached. Each new callback still resolves and physically checks the
current path. `realpath` retains its additional assertion of the returned real
path; directory enumeration still checks each symbolic link.

`readFile` continues to use `before.readText`, not a raw filesystem read. The
snapshot still calls the composed `admit` in `inputPath`, captures bytes and
hash plus before/after identity metadata, and seals against a fresh snapshot.
Successful-read membership, configured ambient roots, tool/config identity,
resolution namespace, ctime/inode/dev fences, producer exceptions, diagnostics,
in-memory-only emission, API closure and publication do not change. Repeated
checks are not an atomic symlink race defense in the present code; the retained
per-operation checks and before/after seal continue to own that policy.

This correction reduces three physical assertions to two for the canonical
plugin's lookup callbacks. A captured `readFile` still has two additional
assertions in the snapshot read path, and `realpath` retains its own additional
check. This is a concrete overhead reduction, not a claimed total speedup or a
proven explanation for all2400seconds. Do not replace the filesystem's own
assertion with trust in an arbitrary callback, remove the caller callback,
introduce cross-callback admission caches or replace pinned snapshot reads.

## Owner and split constraints

`writeTsdownDeclarations` owns group preparation, private stage, canonical
selection, before/after membership seal and eventual complete publication.
The bounded produce mode executes one selected group, joins its compiler tree,
reads compiler membership, seals inputs, and then writes its checkpoint.
Checkpoint join revalidates identity/topology/bytes/membership before final
publication. Those controls are outside the proposed argument change.

The base partition already has only `index` as its emit root. Native compilation
uses `dts.entry` roots plus configured ambient declarations, not the full runtime
entry map (`native-declaration-emitter.mts:114-123`). `src/index.ts` imports CLI
bootstrap/library code, including dynamic imports that TypeScript must resolve
for checking. Its transitive program can remain large with one root. More
canonical root partitions cannot divide this single native program while
preserving the same all-diagnostics owner.

The full `unifiedDistEntries` map still becomes Rolldown inputs for every
declaration partition (`tsdown.config.ts`, declaration config construction).
The native plugin creates aliases for all inputs, but emits declaration chunks
only for selected roots; emit-only transforms replace JS modules with empty
exports. Restricting Rolldown inputs to each partition's selected entries is a
separate plausible optimization AFTER native compilation completes. It needs
output naming/cross-entry-resolution and membership equivalence evidence; the
source alone does not establish it as the native timeout fix. Do not combine it
with the one-argument change for the first measured comparison.

A possible larger phase split is sealed native declaration production followed
by declaration bundling. Existing group checkpoints are after both phases; they
cannot recover a timed-out native phase. A new native-phase checkpoint would
need exact roots/options/config/tool identity, full successful-read and source
membership, serialized declaration/source-map bytes, joined API ownership and
fresh revalidation at consumption. It must never publish a partial diagnostic
or emit result. No such split is approved or implemented by this review.

## Required focused regression evidence

Add small filesystem-facing regressions without needing a repository build:

* Supply an identity `assertInput` and reject an in-checkout symlink to an
  outside file/directory. This proves physical containment is independent of
  callback guarantees. Probe readFile/fileExists/directoryExists/realpath and
  enumeration, then assert the original boundary error is reported by
  `assertValid` rather than escaping an RPC callback.
* Supply a custom policy that denies an otherwise local path. Repeated admitted
  lookups must still invoke it; a deferred rejection must fail validation.
* Between two lookups, retarget a local symlink from inside to outside, and
  create a previously absent path under an escaping symlink. The second lookup
  must revalidate and reject; no retained positive or negative admission may
  mask it. Keep lexical outside-to-inside aliases absent.
* Preserve a supplied pinned readText result and successful-read membership;
  virtual config reads must remain virtual and not become source membership.

Relevant existing admitted compiler suites are
`test/scripts/native-declaration-boundary.test.ts` (semantic rejection, optional
SDK imports/manifest probes, aliases, outside symlink back inside, nested config
semantics, config mutation), `test/scripts/compiler-input-snapshot.test.ts`
(clock fences, byte/config/topology mutation, indirect symlink retarget,
producer exceptions), and `test/scripts/tsdown-declaration-resolution.test.ts`
(ambient membership/unrelated root exclusion, sibling output mutations and
external-install escapes). Run affected cases under the existing resource
owner, not ad hoc locally. Source paths with sparse skip-worktree flags were
read from the frozen commit with git show.

The fresh admitted diagnostic should identify whether time is spent in initial
snapshot/config parsing, async parseConfig, createSnapshot/program loading,
specific diagnostic queries, emission, sealing or bundling. Compare callback
count and synchronous boundary time before/after the argument change. If native
semantic checking dominates, this optimization can be correct yet insufficient.
Do not lower diagnostics, noCheck, ambient/source membership, cancellation,
publication or memory/deadline gates to manufacture a pass.
