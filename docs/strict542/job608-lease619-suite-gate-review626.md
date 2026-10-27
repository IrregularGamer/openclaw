# Review626: independent source review of608 lease619 suite completeness gate

Source: /home/deploy/agentq/tmp/source552, branch strict542-source552,
exact commit c58e8d229cc15bfafa9ebe744618390ffe76388c (executable change
29b4f5e0), diff c7096dd5..c58e8d22 (8 files, docs/strict542 only).

VERDICT: APPROVE (evidence-validation gate only)

Checked:
- All16 pins in lease619-suite-inputs.json match ops-work 78d0afd and HEAD
  byte-for-byte (sha256 via git show); approved619 inputs untouched.
- AST inventory equals the real unittest loader IDs for the run_suites.sh
  layout: baseline78, candidate90, no duplicates, no _FailedTest.
- Committed focused logs re-ran locally (17-test module only, stubbed IO):
  identical modulo timing/paths; candidate17 OK, baseline4 FAIL/5 ERROR.
  parse_log accepts both real logs; baseline records equal
  lease619-baseline-regressions.json exactly (9 records, 7 test IDs).
- Fail-closed: rc!=0/1 (timeout124/signal), missing/duplicate/unexpected
  test, skip/xfail/unexpected success, Ran-count or OK/FAILED mismatch,
  status vs diagnostics disagreement, candidate-only or unrecorded baseline
  difference, any candidate error other than the23 fixed-root ERRORs.
- Validator is read-only (no subprocess/writes). No skip/waiver added.
- test_lease619_suite_gate.py: 13 PASS (Python 3.14.4).

Limitations:
- The23 fixed-root errors are pinned by count/reason and baseline
  equality, not by test ID (IDs were never recorded by619).
- Tests printing between "..." and status would make the gate refuse
  (fail-closed; would need reconciliation, never pin edits).
- Full78/90 suites remain UNRUN (live sealed17338c48 refuses admission).
- Not proof of HQ owner, application, authentic receipt or execution;
  does not replace the automatic608 queue review.
