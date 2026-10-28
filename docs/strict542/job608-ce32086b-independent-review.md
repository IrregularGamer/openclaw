# Independent review: job608 commits 01c7a18e + ce32086b

## Scope
- 01c7a18e: new `docs/strict542/native-declaration-checkpoint608.test.mjs`, plus a one-line change to `run-stage608.sh` that adds it to the checks stage.
- ce32086b: F1 link fix in `scripts/lib/bounded-build-checkpoint608.mjs:53`. Moves `validateChain`/`validateBinding`/`complete` from `scripts/build-checkpoint608.mts` into the lib as `validateBuildChain608`, `validateGroupBinding608` and `validateCompleteCheckpoint608`. Adds 2 tests in `build-checkpoint608.test.mjs`.
- Prior findings: `job608-f1fe77e8-independent-review.md` (F1, F2 blocking).

## Checks
| Check | Result |
|---|---|
| `node --test` build-checkpoint608, declaration-checkpoint608, native-declaration-checkpoint608, native-compiler608 | 19 tests, 19 pass, 0 fail |
| `python3 -m unittest test_stage608` | OK |
| F1 fix | PASS. The link guard now rejects a normalized target `=== '..'` as well as `../*`. The absolute-path checks (posix and win32) and the ancestor-directory check are unchanged. Test: `dist/up -> ..` and `dist/same -> .` are accepted; `up -> ..`, `dist/up2 -> ../..` and `up3 -> a/../../b` are refused. |
| Validator move compared line by line | IDENTICAL. Every `require608` predicate and message is byte-identical. The recursion and binding loop are the same. `expected(stage)` was `resolveBuildCheckpointStage608(stage,labels).labels`, which is `buildStage608(stage,labels,groups)` with the module `groups`. The lib now calls `buildStage608(receipt.stage,labels,groups)`, and the .mts passes that same `groups` object, so they are equivalent. `same` is `isDeepStrictEqual` in both places. `validateCompleteCheckpoint608` matches the removed inline `complete` block. |
| .mts call sites | Correct. The closures `validateChain`/`validateBinding` are kept as thin wrappers passing `{identity,before,outputRoots,labels,groups}` and `{kind,group,predecessor,identity}`. `complete` calls `validateCompleteCheckpoint608(predecessor,labels)`. Imports were updated. |
| F2 coverage | PASS. The valid runtime→middle→tail chain is accepted. 13 mutations are each refused with a specific message: missing unified group, extra sdk group, reordered groups, foreign predecessor digest, group source drift, receipt export drift, receipt status, missing inventory digest, `outputRoots` mismatch, runtime with ancestors, wrong predecessor stage, top-level identity drift, missing phase. `complete` is refused for null, middle and runtime predecessors, and for a short tail. |
| 01c7a18e real owner | PASS. The writer's `./native-compiler608.mjs` and `./declaration-checkpoint608.mjs` specifiers are rewritten to the real `scripts/lib` files (asserted). Only the compiler, publication, cache and IO helpers are stubbed. Refusal, tamper, absent addon, control injection, cancellation, produce/join drift and inherited addon path are all exercised. Only test and runner files changed. It is wired into `run-stage608.sh` checks. |

## Findings
| # | Severity | Location | Finding |
|---|---|---|---|
| N1 | Info | docs/strict542/build-checkpoint608.test.mjs:72 | The `phases.pop()` mutation asserts only `/./`, so it accepts any error. It is still refused, but the assertion is weak. Not blocking. |
| N2 | Info | scripts/lib/bounded-build-checkpoint608.mjs:114 | `validateCompleteCheckpoint608` dereferences `ancestors[0].ancestors[0]` without stage checks. This is unchanged from the original, and it relies on the predecessor having passed `validateBuildChain608` at restore. Behavior is preserved, not weakened. |
| - | - | - | F3–F7 from the prior review are outside the scope of these commits and remain as recorded. |

## Verdict
APPROVED. F1 and F2 are resolved. The moved validators are semantically identical. No blocking findings.
