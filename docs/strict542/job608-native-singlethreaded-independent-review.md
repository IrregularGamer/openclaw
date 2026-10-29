# Job608 independent source review: singleThreaded native emitter candidate

Reviewed commits: `a97beadd` (fixture/test/doc) and `7cbbb99c` (emitter), parent `a9a2b761`.
Reviewer did not author the change. Review is source-only.

## Checks

1. **Placement and validity: PASS.** `7cbbb99c` adds `singleThreaded: true` as the last key of the final
   virtual `compilerOptions` object, after `...compilerOptions` (caller spread) and after
   `noEmitOnError: false` / `noCheck: false`, so a caller cannot override it. Upstream snapshot
   (`runs/608/upstream-snapshot-owner/`, gitHead f29aeb9f) was checked with grep:
   - `declscompiler.go:233` declares `singleThreaded` as a boolean with no command-line-only flag.
   - `compileroptions.go:158` has `SingleThreaded Tristate json:"singleThreaded"`.
   - `program.go:553-554` has `SingleThreaded()` default to `Options().SingleThreaded`.
   - `program.go:558/659/702/706/1839` pass that value to `NewWorkGroup` and the checker pool.
   - `workgroup.go:20-22` selects `singleThreadedWorkGroup`.
   - `project.go` has no `SingleThreaded` override.
   - `session.go:4593` is `handleGetGlobalDiagnostics`.
   All 7 SHA256 values in the candidate doc match the snapshot files.
   Caveat: tsconfig acceptance of the option by the real native binary is inferred from source,
   not executed. The fixture mocks the API.
2. **No weakening: PASS.** The emitter diff is +3 lines (one option plus a comment), with no
   deletions. The fixture diff only routes the existing stubs (`parseConfigFile`, `createSnapshot`,
   `close`, `seal`, diagnostics) through observable hooks. It removes no assertion. Unchanged:
   root set, diagnostics (`includeSemantic`), source membership, input seal, cancellation/`assertValid`,
   close, emission, memory floor and budget.
3. **Tests meaningful: PASS.** On candidate HEAD, `node --test docs/strict542/native-admission608.test.mjs`
   gives 9 pass and 0 fail. With the a9a2b761 emitter temporarily swapped in (then restored), it gives
   7 pass and 2 fail: `scheduling-default` and `scheduling-override`. That matches the committed RED log.
   The override case passes `singleThreaded:false, noCheck:true, noEmitOnError:true` and asserts that
   the final config still forces `true`/`false`/`false`. The cases also assert explicit and ambient roots,
   the full snapshot request, semantic diagnostics, and the order snapshot -> diagnostics -> membership -> close -> seal.
4. **Emitter SHA256: PASS.** `git show a9a2b761:...emitter.mts | sha256sum` =
   `2f8a05d0b713daf4d60d4e0359efe677b8f2710b05b1fd594e401adf1a3a2431`.
   `git show 7cbbb99c:...emitter.mts | sha256sum` =
   `330ebfd5240be7449c7c374ef7a57a6446dead50117e22ed2d81100934d3d547`. Both match the doc.

## Verdict

**APPROVE source-only.**

This is not build, package, install or application acceptance. It establishes no native output
parity or performance. All downstream gates in the candidate doc remain. Job595 must not apply.
