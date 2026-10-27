# Independent review of actual619 prerequisite reconciliation

2026-10-27. VERDICT: APPROVE (exact source and comparison evidence only).

Reviewed diff from e6a43a31281e3fb27df3a9fc90f6585f5e18dcc9 through
74447eacb0c95f72ec20433305b941fd17b15af7, including executable source commit
a6096c36c26f24580d2da62e4d92ebfb6be1c8f9 and the preserved full logs.
Review performed independently of the reconciliation implementer.

Evidence checked directly:

- All16 suite/source/runner pins match both approved619 commit
  78d0afd5a5f4b6304f80c18aa61f7a75c343b3c3 and actual execution commit
  5bfe1aa92fc8c83486372d74c9259ac44777cce7, using git object bytes, and match the returned export at
  /home/deploy/agentq/tmp/export.bDNF. Original619 inputs are unchanged.
- The AST inventories and parsed complete logs contain exactly78 baseline and
  90 candidate tests, with terminal rc1, complete matching unittest summaries,
  no omitted/duplicate/unknown tests, skips or timeouts. Baseline has4FAIL and
  28ERROR; candidate has23ERROR. These full suites do not pass.
- Counter(candidate diagnostics) equals the23 exact pinned tuples. All23 also
  occur on baseline. Counter(baseline) minus Counter(candidate) equals the
  original nine focused regression tuples exactly (4FAIL/5ERROR, seven test
  IDs including subtests). No candidate-only diagnostic exists.
- The23 shared diagnostics are19 PermissionError fixed-root errors and4
  AttributeError missing-requeue_history errors, over14 distinct test IDs.
  The four AttributeErrors are a frozen fixture mismatch: run_suites.sh copies
  current inc-261023-03/test_integration.py over baseline/agentq.py; the tests
  call requeue_history at lines122/134, while the frozen agentq.py has no such
  function. Current inc-261023-03/agentq.py defines it at768. Both variants use
  identical frozen dispatcher bytes. The19 other errors arise when temporary
  Controller roots reach maintenance.Preservation's fixed-root predicate.
- Committed full logs match the actual returned logs byte-for-byte. SHA256:
  baseline93432f9b508283ca3c2b7cb2cfc877b618ff2090104acc7e6765125e3e7245aa;
  candidate670b5392057ee1a8f291db642c8ddffdd60c7dbc22e7b20ed30b7161842e226c.
  Shared diagnostic pin SHA256 is
  e346a2dc3ce0e728a9ccd21808f6f863994b21bbcdc37646df53164deb99352e.
- Actual /home/deploy/agentq/runs/622/HQ-RECEIPT.md records foreground HQ
  application at12:53Z and the successful admitted job632 comparison from the
  export root; the earlier incomplete upload is explicitly discarded.
  Read-only checks of the live control.py and validation.json installed_hashes
  entry both yield db4d290323a4e0d90ff597ed920da32dc610660813d1ac0c8a5798ae7d7bc3ce.
  The seal file itself hashed to
  5301d131e85af4a637344464f0d52f0b3b801c0fe8ede75f7fe1a9a6c12d0e64
  at review time. This verifies the current hash entry, not a new full seal audit.

Fresh bounded verification:

- TMPDIR=/var/tmp python3 -B -m unittest discover -s docs/strict542
  -p test_lease619_suite_gate.py -v:14 PASS (0.111s).
  The candidate-new-failure test explicitly expects "unexpected failures".
- The read-only gate on the actual returned export/logs exits0 and emits the
  same receipt as job608-lease619-full-receipt.json:78/90 tests,19 fixed-root
  errors,4 dispatcher fixture errors,9 baseline-only diagnostics,0
  candidate-only regressions. The prior gate was observed refusing the
  inaccurate generic23-fixed-root assumption on these same actual logs.

The correction is valid evidence reconciliation for the original619
no-candidate-regression condition. Exact Counter equality pins test ID,
FAIL/ERROR, subtest text and terminal exception; it strengthens diagnostic
identity over the previous generic count/reason check and does not permit
arbitrary shared failures. Existing inventory/completion/source/focused
regression checks remain. No new production check waiver or passing-suite
claim is justified or introduced. The unrelated fixture mismatch remains
documented; this review does not claim its blocked assertions were tested.

The actual619 prerequisite is satisfied for the single already-authorized
preserved combined3 4GiB/1CPU launch, subject to the existing exact unused-export
hash checks and normal registered offload admission. No second launch, local
heavy test, service/provider/configuration/root/seal mutation or595 application
is authorized by this review. Complete combined3 diagnostics, canonical typed
package and runtime receipt, exact inventory and independent
source/action/privilege/seal reviews, automatic608 APPROVE and existing595
application gates all remain required. This reviewer ran only small parser
checks and read-only source/artifact/hash inspection; no full suite was rerun.
