# Job636: independent installed declaration timeout review

VERDICT: OPTION 1 — accept exactly the demonstrated baseline timeout, subject to
an explicit base-parity gate in `run-package608.sh`. No general timeout waiver.

Reviewed by Rook on 2026-10-27, independently of job608 author Pinch/Claude.
Reviewed proposal `0689a1b2`, package source `55a1dd59`, base `c790ba44`, and
wiring review635 (`3c6ad3dc`). This is a decision/source review; job608 owns
implementing the gate and the subsequent fresh package export/offload. The
current runner still fails on the timeout. This review does not mark it passing.

## Evidence and limits

`job608-package3-offload.log.gz` reports four selected tooling files, three
passing and one failing: **191 passed / 192 tests**, with the sole failure:

`test/scripts/write-unified-entry-dts.test.ts` > `write-unified-entry-dts` >
`reuses unaffected canonical groups while rebuilding runtime after input edits`

The error is `Test timed out in 120000ms.` Package3 exits 1 before native rebuild
and package completion. It is a spent run, not a package success receipt.

The single-test diagnostic uses the same base/successor archives as package3,
frozen installs, tooling config, one worker and no file parallelism. Both
installs exit 0. Base Vitest exits 1 after 138 seconds; successor exits 1 after
135 seconds. Each reports one timeout and ten intentionally unselected tests.
Those ten skips are diagnostic selection, not permission to skip installed checks.

| Completed phase | Base c790ba44 | Successor 55a1dd59 |
| --- | --- | --- |
| Initial build | 69,811 ms, status 0 | 61,046 ms, status 0 |
| Consumer typecheck | 4,567 ms, status 0 | 4,722 ms, status 0 |
| Unchanged build | 18,067 ms, status 0 | 17,304 ms, status 0 |
| Edited build | 17,898 ms, status 143 at timeout | 20,666 ms, status 0 |
| Cold writer | Not reached | 8,387 ms, status 1 during timeout |

The profiles show the same cumulative deadline limitation, not identical last
phases. Successor progressed further. Correct the proposal's suggestion that
successor cold-writer was proven killed with status 143: the retained trace says
**1**, and the enclosing Vitest error is the timeout. Neither run proves the
final cold-output equality or staging-clean assertions. Base also does not prove
the edited-build assertions. Acceptance explicitly retains that coverage gap;
it does not report these unexecuted assertions as passing.

The test, its declaration/native fixtures, declaration config groups, generator
and generator-input resolver are unchanged between
base and successor. `scripts/build-all.mts` and `scripts/tsdown-build.mts` also change to add the
bounded profile/planner; this fixture calls the ordinary full profile.
The declaration writer adds the bounded-native route;
its policy lookup is conditional on presence of `OPENCLAW_608_BOUNDED_PACKAGE`.
The test does not set that key (its fixture inherits the surrounding environment).
The writer also adds an unconditional module import and explicit environment
forwarding, so "all changes gated" is too broad. The direct base/successor
probe, rather than that shorthand, supports this narrow non-regression decision.

The diagnostic shell has `set -u`, not `set -e`, and ends with `exit 0` even
when Vitest fails. Its unguarded archive-verification command is not a sufficient
fail-closed proof by itself. Independently rehashed the retained archives and
checked their shared inode identity across the two exports, equal manifests,
and both runners against their source copies. The manifest's runner hash belongs
to package3, not to the diagnostic runner. Preserve their separate identities.
The recorded placement is the admitted 4 GiB / 1 CPU / zero-swap run; this review
changes no resource policy and does not independently replay that placement.

## Pinned proof identities (SHA256)

- Base archive: `e79a0e45a4eaea4afe325ca94ba201d5ae43d09d8c15dc07d0695c87ba743de3`
- Successor archive: `44af05d71daf4785285ba83a6199d79a7e5492067fe8bf6068e00892c9b295fa`
- Package3 runner: `0bf8dd1f98a114d0bab73ff0271be3f5c23981e9035a5084578156250ee256ef`
- Diagnostic runner: `1ef71d33013469efad5b29c4c5ca16a87e919a5a222eee872c0629c5fe73bd73`
- Compressed package3 log: `a0f6f3c956662da1e94c76a153248a2b59f8b790531622791bbaeecc131656c8`
- Compressed diagnostic log: `10cc71d1b067a6d2c267787abb9cfaa281a94b962d2eee012cbbfc296930b9ca`

## Required implementation in job608

1. Keep all four installed files selected through the tooling config, with
   `--passWithNoTests=false`, one worker, no file parallelism and the existing
   120000 ms timeout. Run the named test too; do not exclude or delete it.
2. Accept an installed result only if all 192 pass, or exactly 191 pass and the
   single failure is the exact file/full test name above with the 120000 ms
   timeout. Require complete structured Vitest results, four files, no other
   failure/error/skip/todo, and normal process settlement. Missing, malformed,
   empty or truncated results, non-timeout assertion failures, worker failures,
   signals and additional failures must refuse success. Shell exit 0 from the
   diagnostic and log substring matches alone cannot authorize acceptance.
3. For the exception, bind the independently checked base-parity proof below
   to the new export/installed result. Require completed successful initial,
   consumer and unchanged phases, with no earlier assertion failure; successor
   must reach edited-build or later. Do not require an identical killed phase:
   the reviewed base and successor already differ there. Reject a new earlier
   failure. Verify the reviewed test/fixture/declaration-path identities still
   apply; if those inputs or controls change, obtain new base-parity evidence
   or split the test rather than reuse this approval blindly. Explicitly reject
   inherited bounded-native policy for this ordinary tooling check.
4. Retain raw installed results, base-parity evidence hashes and the explicit
   accepted-timeout classification in the hashed checks evidence. Report
   "191 passed + 1 accepted baseline timeout", never "192 passed" for that
   outcome. Cover the decision gate's refusal cases with lightweight tests.
5. Every scoped, native rebuild, real-native parity/lazy/minifier, typed output,
   graph floor, frozen package and final receipt requirement remains mandatory.
   Keep the manifest's required-check inventory; do not lower floors, raise
   budgets/deadlines or remove assertions. This accepts no other baseline failure.

Option 2 is not required for this pinned successor: the unchanged upstream
multi-build test exceeds the same cumulative deadline on base, while successor
completes more work. Splitting would change shared cache/history setup and need
new runtime proof. A source split remains appropriate if parity ceases to hold.

## Wiring635 and next owner

Review635 remains CHANGES for its pinned `20552650` range. Its wrong-shard issue
is corrected later by `55a1dd59`; that does not retroactively approve package1.
A new job608 export must also include and verify both pinned native stage JSON
receipts, as review635 requires, and retain a finite outer deadline. This verdict
only resolves the installed timeout decision. It authorizes no deployment,
installation, replay of spent exports, or automatic parent608 approval.

## Verification

Read-only archive/source comparisons, compressed-log parsing, unchanged-path
Git comparisons and shell syntax checks; no dependency installation, package
offload, full suite or native build was run. This documentation-only review uses
the recorded remote results as evidence, without claiming fresh runtime passes.
