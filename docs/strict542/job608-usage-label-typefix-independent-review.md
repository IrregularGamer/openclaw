# Independent usage-window label type correction review

Reviewer: Rook `/root/unified_type_review`, independent source/failure reviewer.
Reviewed source/test commit `49d3fe3348215314582acf7be3872f403f7f6af4`, RED test
commit `9d6c4154a103362b6e037d9c09c67e759fc8099c`, and committed evidence
`82cc92b88c89cc53f58b9376cae017705439acb8` against source baseline
`5aff81feb4098654ce07e7ff09e336119770be85`.

**VERDICT: APPROVE exact SOURCE-ONLY correction and narrow regression evidence.
No blocking source finding. 595 MUST NOT APPLY.**

## Independently verified failure and correction

The actual unified-0 attempt used common export
`230f79f5b6f95826a02a15f1c5fdd9d1fbc5a7abd60064b33e3d1776af0f086d`
and manifest
`912af4bc9ff88303a0a78765a16620b415f22e39984957adcfcb172b56b56468`.
Its decompressed offload log independently hashes to
`5a9da761227212aef4ef57347497a97cc817e4bbe5871c9012135a6eb778909c`,
matching outcome.json. Actual native declaration diagnostics are TS2322 at
source byte 13195 and TS6500 at byte 1370. I mapped those exact baseline bytes
to `label: WINDOW_LABELS[key]` and required `label: string`. The child reported
status/finalStatus 1, null signals, timedOut false, process-group state dead,
and 152.5 seconds; the stage reported build-fail 1 at +279 seconds. Client exit
was 1 and no result artifacts returned. This is a source type error, with no
evidence of timeout or resource admission refusal.

The correction reads an own property into a local `label`, explicitly rejects
undefined with the existing provider_unrecognized_field reason, and uses the
narrowed string. It retains Object.hasOwn, the earlier null-window skip, every
recognized label, all numeric/reset validation, exhaustion-before-missing
precedence, and applicable-window order. No assertion, cast, widening,
non-null assertion, or inherited-property acceptance conceals the error.
Owner, route, privilege, freshness, cancellation, lifetime and provider HTTP
logic are unchanged.

The executable delta from 5aff81fe through 49d3fe33 is exactly the parser,
its existing test file, the new actual-parser typecheck test, and one checks
runner invocation. Other intervening changes are evidence/documentation.
The runner invokes the new check after the existing frozen install, appends
its output to the checks log, and exits on failure before installed checks
and stage receipt production. Its existing budget and failure policy remain
unchanged. Fresh independent `sh -n docs/strict542/run-stage608.sh` and
`git diff --check 5aff81fe 49d3fe33` both exited 0.

## Exact source and recorded regression evidence

I read the actual private RED, incomplete GREEN and complete GREEN2 exports
at the paths in outcome.json, and independently SHA-256 compared every listed
source file against both that outcome and its committed git blob. All matched.
All complete GREEN2 source files also match the current evidence HEAD.
Important exact hashes:

- RED usage-preflight.ts: `b017b54b506a4e7a1b914b9a0fce47fc4a3441122333b96c19292b6342949450`.
- Corrected usage-preflight.ts: `eb9478c8182ae95fcd16ac72202983fe45943694944a0670e5823bca983dced5`.
- Extended usage-preflight.test.mjs: `6c970f9272f48c575d2837bb1234acf00045ac348cc2f4cea9b60080ad0382c0`.
- New usage-window-types608.test.mjs: `4ea193364f7ed854bf202b9ceba207eca8980ba3508cfb15fd22a3c6369aa499`.

The complete six-file GREEN2 export additionally contains exactly the committed
selected-runtime-auth-read.ts and both gateway registration source fixtures.
The returned RED/GREEN2 inputs.sha256, install.log, typecheck.log and
typecheck.rc files match their retained repository counterparts byte for byte.
Decompressed offload-log SHA-256 values independently match outcome.json:

- RED: `dd0ec2d9e9180d1168a03538cfa8f66f8c5e8f297a74bf1346fbb5946b9be725`.
- Incomplete GREEN: `72d2c4983e2491c199b3fb7e7bb37fe7ff991bdc214bae711d43b388c3fdc2b7`.
- Complete GREEN2: `74ffd514069b194c75e276c95e5ca650d610658b792bcd19e9fbad091735e448`.

The new check extracts the actual committed window type and actual parser
section, then invokes installed TypeScript with strict and
noUncheckedIndexedAccess, ES2022, noEmit and an isolated typeRoots directory.
It asserts compiler error absence, null signal and status 0, with bounded
runtime/output, and removes its temporary files. It tests actual source bytes
instead of a second implementation; removing the parser boundaries fails.

Recorded RED has the expected actual TS2322 at extracted parser line 55:
string | undefined is not assignable to string. Compiler status was 2 and
the Node test failed with status 1; client 0 only represents the wrapper's
successful assertion of the expected failure. It is not a passing typecheck.

Recorded complete GREEN2 has client 0 and typecheck/test status 0, with 36
tests passed and zero failures, cancellations, skips or todos: 35 preflight
tests plus the actual-parser compile test. The extended tests exercise all
five labels and null-window skipping, and reject computed own keys __proto__,
constructor, toString and hasOwnProperty. Existing coverage retains malformed,
unknown, nonfinite, missing and exhausted windows, applicable/nonapplicable
exhaustion precedence, auth/owner drift, clocks/deadlines/cancellation, and
gateway registration/privilege assertions.

The incomplete GREEN has client 1 and registration-suite ENOENT because its
export omitted the two registration source fixtures. Its partial successes
are explicitly NOT acceptance; GREEN2 supplies the complete narrow proof.

## Limits and remaining gates

I inspected and hashed existing actual execution evidence; I did not rerun
tests, launch offload, or run a heavy build. I also inspected the supplemental
outcome.json metadata prepared after 82cc92b8: it adds the exact source refs,
reported offload/requested npm invocations and the compiler-version evidence
limit, without changing the source, tests, runner, result hashes or verdicts.
Those invocations request TypeScript 7.1.0-dev.20260920.1; retained install.log
files only state that two packages were added. No separate installed --version
receipt was captured, and I do not attest that installed version. The typecheck
test itself resolves actual installed node_modules/typescript/bin/tsc.

This extracted-parser check establishes the narrow regression evidence. It
does not replace the full native declaration/unified build or establish the
whole gateway import graph, compiler, package, final artifact/action/privilege,
whole seal, actual automatic-review, application or ordered HQ595 gates.
The changed checks-runner invocation has been source/syntax reviewed; no new
complete checks-stage execution is claimed here.

The failed source5aff81fe unified-0 attempt remains SPENT_FAILURE_NO_REPLAY.
Historical accepted checks/native/runtime receipts remain evidence for their
original exact source/export identities and must not be relabelled for this
correction. Prepared compiler manifest 668db7e1 remains UNUSED and cannot
execute on the failed unified-0 predecessor. Fresh changed source exports,
source-inventory and exact preflight reviews, all required actual stage
results, settlement and independent acceptance remain necessary before
successors are authorized. This review grants no launch or application
authority. **595 MUST NOT APPLY.**

Only this requested review document was written. No commit, push, root,
service, provider, queue or installed-state mutation was performed.
