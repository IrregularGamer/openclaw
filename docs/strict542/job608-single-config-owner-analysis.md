# job608 single-config owner analysis at frozen a39a

SOURCE ANALYSIS ONLY; **595 MUST NOT APPLY.** Analyst: Rook
`/root/review_compiler_preflight`, 2026-10-29 UTC. This records inspected source
and a conditional diagnostic plan, not approval, a source change, a performance
fix, a successful build or acceptance of any result. The coordinator reports
the current unified-0 attempt is still pending at this handoff; this lane did
not inspect or disturb its runtime. No test, diagnostic, export preparation,
offload, service, root, config, unit, seal or provider operation ran here.

Product source examined at exact freeze
`a39ad5ee95609193502850d0dbb87b5dcbb5e3e3`; common export identity
`d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62`.
References below are line numbers in that commit, except explicitly identified
upstream files. Historical config15 naming is not the selection authority.

## Unified-0 is already one complete config

- `scripts/lib/tsdown-config-groups.mts:4` lists base, two SDK and five extension
  groups; the non-SDK selection removes the two SDK groups.
- `scripts/lib/bounded-build-checkpoint608.mjs:23` (`buildStage608`) selects
  exactly the first non-SDK group for unified-0: `openclaw-dts-base`. Its sole
  predecessor is runtime. `docs/strict542/stage608.py:27` maps the stage to that
  group's archive path; it does not partition a TypeScript program.
- `tsdown.config.ts:737` (`buildUnifiedDeclarationPartitions`) selects only the
  `index` entry for base at line761. `buildCoreDistEntries` at line446 maps it
  to `src/index.ts`. The config creation at line1008 retains the full
  `unifiedDistEntries` entry map and passes only the partition's sources as
  `dts.entry`. Other entry aliases/runtime membership must remain intact.
- `scripts/lib/tsdown-declaration-boundary.mts:190` derives explicit native
  roots from `dts.entry` and calls `emitNativeDeclarations` at line214.
  `scripts/lib/native-declaration-emitter.mts:116` additionally retains every
  configured ambient declaration root. Imported transitive sources remain part
  of the program and its final input membership.

Therefore the stale suggestion to split unified-0 by config subset in
`job608-after-substep-budget-continuation.md:61` cannot subdivide this stage.
One config and one explicit emit root are already its smallest supported
canonical config unit. Removing imports, ambient roots or checks is not this
plan. There is no safe further config split established by this analysis.

## No resumable native semantic checkpoint

`compileNativeProject` owns one lifetime: create snapshot (line156), obtain the
project, collect required diagnostics (line166), emit declarations (line175),
collect every source filename (line201), close the API (line205), check complete
root membership and seal all inputs (line213). `singleThreaded:true` and
`noCheck:false` remain mandatory in the final virtual config at lines149–152.

`scripts/lib/tsdown-declaration-writer.mts:228` writes the private group
checkpoint only after its complete compiler process tree returns successfully
and input sealing succeeds. Joining at line258 validates exact source/options,
input signatures, output bytes/topology and copied membership. Publication at
line300 still joins the complete canonical batch. The declaration checkpoint
is completed output, not a serialized in-progress TypeScript checker.

Pinned upstream `tsc/internal/api/session.go:387` stores snapshots in a
session-owned `map[SnapshotID]*snapshotData`. `Close` at line4404 releases all
snapshots regardless of reference counts and closes its owned host. Protocol
`proto.go:37` defines SnapshotID as a uint64 handle; create/update/reconfigure
operate on roots/configuration/filesystem changes, not persisted checker state.
The inspected method table contains no export/import/serialize/reload semantic
snapshot operation. `tsc/internal/project/api.go:9` retains snapshots only within
the live session. Existing snapshots support reuse inside one live native
session, not resumption across separately terminated admitted runs. Keeping a
compiler alive between finite runs would require a different lifetime owner and
would not satisfy the present settlement boundary.

## Required queries and checker reuse

The native declaration plugin supplies no diagnostics override.
`compileNativeProject:38` defaults to `diagnostics = "all"`; at line166 it
requests semantic diagnostics. `scripts/lib/native-typescript-diagnostics.mts:6`
defines the exact canonical query order:

1. getConfigFileParsingDiagnostics
2. getProgramDiagnostics
3. getGlobalDiagnostics
4. getSyntacticDiagnostics
5. getBindDiagnostics
6. getSemanticDiagnostics

The async collector at line37 awaits each query sequentially. Declaration mode
omits only the sixth explicit query; global remains required in both modes.
`uniqueDiagnostics:17` retains first occurrences in canonical result order.

Upstream `session.go:4593` explicitly forces a full semantic pass before
returning lazy global diagnostics. Both that request and explicit semantic
diagnostics (`session.go:4540`) use CheckerLifetimeDiagnostics.
`project.go:550` installs an external API checker pool; consequently
`compiler/program.go:699` takes the external-pool path. `SingleThreaded` makes
its workgroup sequential; each checked file obtains the diagnostics checker
through `checkerpool.go:119`. `getDiagnosticsChecker:219` always selects index0,
creating it only if absent. Successful release at line345 retains the checker
and records lastReleased. Thus global and semantic normally reuse the same
checker; they are not inherently two cold semantic compilations.

The checker itself stores `sourceFileLinks.typeChecked`:
`tsc/internal/checker/checker.go:2238` skips completed expensive checking for
that file, and `getDiagnostics:14187` then returns stored file diagnostics.
Global and semantic still enumerate/filter diagnostics separately.

There is a specific reuse risk. `CheckerPoolOptions` and its initializer at
`checkerpool.go:22,84` set a default30 s idle timeout. `scheduleCleanupLocked:389`
uses lastReleased + IdleTimeout; `cleanupIdleCheckers:429` disposes only unheld
checkers when elapsed idle time is at least that timeout. Held work remains
protected. Syntactic and bind requests do not obtain index0, so the current
global → syntactic → bind → semantic sequence can lose its cached checker if
the intervening gap reaches the timeout. This lane did not measure that gap,
observe checker disposal, or establish duplicate cold work in the current run.

## Narrow conditional scheduling candidate

If measurement justifies it, change only the async collector's execution
schedule to config → program → global → semantic → syntactic → bind.
Store each query's returned array, then flatten in the ORIGINAL canonical
order above before existing deduplication. All six queries execute exactly
once in all mode; declaration mode retains its original five. Do not sort by
diagnostic code or otherwise change reported ordering. Preserve rejection as
failure, full roots/options/membership, emission, close, seals and publication.
No concurrency, checker-lifetime override, semantic waiver or budget change is
proposed. This removes intervening diagnostic work from the reuse gap but does
not guarantee continuity across response serialization or external scheduling
delays. It cannot make the
first cold global semantic pass fit a shorter deadline.

Minimum behavioral proof, before accepting any such change:

- Exercise the REAL async collector with fake project methods and a virtual
  clock/pool model matching index0/30 s expiry: global warms a checker; syntactic
  and bind each advance20 s; semantic records whether that generation survives.
  Old ordering produces two cold checks, adjacency one. This proves the intended
  scheduling behavior in the model, not actual native performance.
- Return distinct and duplicate diagnostics from all surfaces; require exact
  six-call membership, canonical returned order and first-occurrence deduplication.
  Verify declaration mode retains five calls and no explicit semantic request.
- Extend `docs/strict542/native-admission608.fixture.mjs` and its test driver
  with one composition case using the real collector rather than its existing
  diagnostics stub. Preserve snapshot → all queries → emission → complete
  membership → close → seal, explicit plus ambient roots, singleThreaded and
  noCheck policy. Failure closes and cannot emit or seal successful output.
- Retain actual lazy-global, declaration-transform and semantic error refusals
  in `test/scripts/native-declaration-boundary.test.ts:127`, plus native API
  observer and complete declaration/build checkpoint owner coverage. Any source
  change needs exact review, a new freeze and applicable fresh stage evidence.

## Next diagnostic if the current attempt fails

Preserve actual client log/rc, mark the attempted export SPENT and settle it;
do not replay it or assume its terminal native phase from whole-stage markers.
Reuse the EXISTING finite API observer mechanism to measure exact a39a phase
boundaries: `native-api-phases608.mjs`, `install-native-api-phases608.mjs` and
the external-launch pattern in `diagnose-native-api608.py`. Observe parse,
snapshot, every required diagnostic, emission, membership and close; compare
global completion with the actual syntactic/bind interval and semantic duration.

The current diagnostic harness is hard-pinned to OLD1bed/common5d7e/runner eac266;
its historical preflight is not a39a launch authority. Do not run it unchanged.
Prepare a NEW reviewed external diagnostic harness/export with exact
a39a/commond287/runner e2ed identity and current accepted native/runtime inputs,
using the same unchanged observer modules. Keep the frozen source untouched,
disable stage/checkpoint receipt publication, preserve actual inner and
collection statuses separately, finite deadlines, live worker reserve, resource
floors, input checks and whole-tree cancellation/settlement. Review the precise
adapted harness, pins and UNUSED export before any admitted observation. This
document prepares or launches nothing and authorizes no retry.

The observer may perturb scheduling, so even successful observation is
diagnostic evidence only. Measure first; only an evidenced owner-level change
can justify a changed build attempt. A single full global pass may itself
exceed the current finite budget; this analysis supplies no workaround for that.

## Existing finite CPU profiling route

Additional read-only inspection of the same pinned upstream revision found
`packages/typescript/src/api/async/api.ts:264,270,597–622` exposes
`api.internal.startCPUProfile(dir)` and `stopCPUProfile()`. The async client
clears its pending-batch marker before awaiting a request
(`async/client.ts:202–220,259–294`); incoming RPCs run in separate goroutines
(`tsc/internal/ipc/conn_async.go:97–106`). A later timer can therefore submit
stop while a long global request remains pending, without changing its query.
`tsc/internal/pprof/pprof.go:108–120` serializes stop and invokes
`ProfileSession.Stop:49–51`, which finalizes the CPU profile and closes its file
before returning the filename. Session close does not finalize that profile.
Any future reviewed diagnostic must obtain the successful stop receipt before
its existing outer deadline; timeout alone supplies no finalized-profile proof.
Heap profiling forces GC (`pprof.go:136`) and perturbs the measured workload.

This is an existing diagnostic mechanism, not a prepared run or launch approval.
If actual evidence isolates the first global query, adjacent global/semantic
scheduling cannot shorten its mandatory whole-program semantic pass. File-subset
diagnostic RPCs do not partition global, and splitting RPCs within one session
does not make checker state resumable across terminated runs. A CPU profile can
identify the exact checker or maintained source-type owner before proposing a
correction; no measured cause or performance fix is established here.

## Exact upstream evidence pins

Version `7.1.0-dev.20260920.1`, gitHead
`f29aeb9f825d96feea27841f3f7342dbf0df68a8`. Retained local files under
`runs/608/upstream-snapshot-owner/` were inspected and streamed-hashed:

- API session.go: `39321b51fd3f01e503e7834573f84cae55b5e1c90fef203f93e051ad25c376b1`
- API proto.go: `3bd920dcb38b8d4bebab54ff8373c722c370218c4b10746efda9899d4f47811c`
- Project api.go: `af4e204e6a79d84d65fbe6d3ba286f5955694470bee14b748ad027c3c7ce24e3`
- Project project.go: `e8c70a7d2aa2a30f5d2db17733e1379f42d803f6309a700f5c2b57b523a17d03`
- Project checkerpool.go: `3737b2244b8eb094e81ac80bd77199676512dc76327fc8cc1ed6cd2927aeaf56`
- Compiler program.go: `72f0b97bca110d5893b03c6ac8349dcdabe627c55f58f05a0dbd9b5a6da6cadb`
- Async API (`async-api.ts`, upstream `packages/typescript/src/api/async/api.ts`):
  `8103a368e0a1141c2ada59121432e7bf101c311a58bcdb88089f8a316e3b78be`
- Async client (`async-client.ts`, upstream `packages/typescript/src/api/async/client.ts`):
  `18c5e201e68a2ecdb6c1163739d638d2819b861d2ac87a0bc0ba126b2cd35a03`
- Async RPC (`ipc-conn_async.go`, upstream `tsc/internal/ipc/conn_async.go`):
  `6c6bf2a14c7dd847d208ebca0d075421ebe015bcef1606544dc77cd7cb030498`
- Profiling (`pprof.go`, upstream `tsc/internal/pprof/pprof.go`):
  `bae9085cf6c929abfcfba62b0559dfa4b437a057a8c9d8f66a48806eecffb7ec`

Exact checker.go was read directly from the pinned upstream revision and
streamed-hashed without retaining a new source file:
`f6dbbfd2d0816458155609717ebb0325e6b7751654df69a426a98d682e6cdd17`.
[Pinned checker owner](https://github.com/microsoft/TypeScript/blob/f29aeb9f825d96feea27841f3f7342dbf0df68a8/tsc/internal/checker/checker.go#L2238),
[pinned API session owner](https://github.com/microsoft/TypeScript/blob/f29aeb9f825d96feea27841f3f7342dbf0df68a8/tsc/internal/api/session.go#L4593),
[pinned checker pool owner](https://github.com/microsoft/TypeScript/blob/f29aeb9f825d96feea27841f3f7342dbf0df68a8/tsc/internal/project/checkerpool.go#L219).

This is analyst evidence, with no self-issued approval or build acceptance.
