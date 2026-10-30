# Job608 continuation after package m674c prepare refusal — 595 MUST NOT APPLY

Supersedes the NEXT pointer of job608-after-package-m674b-hardlink-continuation.md. All earlier gates, caps, reviews apply.

## What happened (2026-10-30, worker ending 05:24Z)
- `prepare-stage608-export.py --commit b246ebeb --stage package --input <native/checks/compiler/tail m674>` -> AssertionError
  `native` at prepare-stage608-export.py:98: every input stage receipt must carry the package's exact `source_commit`
  and `source_export_sha256`. The m674 inputs are 674840b6. The same binding is enforced remotely in stage608.py:117-120
  (verify_inputs) and build598.sh:52 (checks evidence source_commit). The m674b continuation step 3 wrongly assumed
  the accepted inputs could be reused at a new commit. Nothing was relaxed.
- The partial refused dest was moved (`mv -n`) to P/trash-608/stage-package-m674c-refused-prepare (nothing launched).
- checks is needed at b246ebeb under every option (run-stage608.sh:87 runs test_frozen_package608.py, changed by
  b246ebeb). Prepared P/stage-checks-b246 (manifest 16552908, export 264d042c), gates 0, preflight 069eebd3,
  independent APPROVE 03dd497a, ONE launch at the checks m674 caps. Result: see "checks b246 result" below.

## Decision for the package inputs (technical, not an S question)
- Option A (precedent m674): rerun the whole chain at b246ebeb (native, compiler, runtime, unified-0..5, middle,
  sdk-0..1, tail, then package) = ~13 more single-launch workers. Binding unchanged.
- Option B (RECOMMENDED, source correction, needs independent review BEFORE use): explicit reviewed input lineage.
  Package at C1 may pin native/compiler/tail receipts accepted at ancestor C0 only if (i) C0 is an ancestor of C1,
  (ii) every path in `git diff --name-only C0 C1` is either evidence (`docs/strict542/job608-*`) or in an explicit
  PACKAGE_ONLY set {docs/strict542/frozen-package608.py, docs/strict542/build598.sh} that no stage before package
  reads (verify by grep of run-stage608.sh/run-*608.sh before review), (iii) the checks receipt is still exactly C1
  (build598.sh:52 unchanged), (iv) the lineage {C0, C1, paths, input receipt digests} is written into the manifest and
  the stage receipt and enforced identically in prepare-stage608-export.py and stage608.py verify_inputs, with tests:
  refuses a non-ancestor, refuses any non-allowlisted changed path, refuses a checks receipt from C0, accepts exactly
  the b246ebeb case. Native outputs are already commit-independent by design (pinned to base native_stage_outputs).
  Never remove the same-commit check for the default case; lineage is opt-in per explicit committed allowlist.

## NEXT
1. Fresh worker: if checks b246 rc0, independent acceptance (14 checks, zero group/other-writable, nlink 1). If not
   rc0, diagnose from its evidence; do not relaunch the same stage.
2. Implement Option B source-only + unit tests (small, local), commit; independent source review.
3. Fresh worker: prepare P/stage-package-b246 --commit <B commit> with the m674 native/compiler/tail inputs plus
   checks b246; gates, preflight review, ONE launch 14g/4CPU/2460s (>=2655s left), evidence, independent acceptance.
   Note: under Option B the checks receipt must equal the package commit, so if B lands as a new commit C2, checks must
   be C2 too unless the lineage rule also admits checks for C1->C2 diffs touching only lineage code + its tests that
   checks does NOT run; the reviewer decides. Prefer landing B so checks lineage is explicit.
4. Then final artifact receipt + old/new hash inventory, action/privilege/seal/reseal reviews, automatic queue review,
   genuine ordered HQ595 handoff. 587 fd3/socket transport replaces 586 sudo; never add the 586 rule.

## checks b246 result
rc 0 (evidence job608-checks-b246/, README there); awaiting independent acceptance.
