# Actual619 prerequisite reconciliation, source only

2026-10-27. HQ receipt622 records actual foreground Pinch application of the
624-approved619 artifact78d0afd5a5f4b6304f80c18aa61f7a75c343b3c3 at12:53Z.
Read-only recheck: installed and seal control.py both NEW
`db4d290323a4e0d90ff597ed920da32dc610660813d1ac0c8a5798ae7d7bc3ce`.
The original619 installer/action, privilege, root and seal changes are untouched.

Job632 ran original unchanged run_suites.sh via admitted offload from committed
ops-work5bfe1aa fresh export `/home/deploy/agentq/tmp/export.bDNF`, from export root.
Its earlier omitted-directory run is discarded. Complete original returned logs
are preserved here as job608-lease619-{baseline,candidate}-full.log. All16 source
pins match; all78/90 tests complete with rc1 and no skips/timeouts/missing tests.
Baseline has4FAIL/28ERROR; candidate23ERROR. These are comparison evidence, not
passing full suites. Exact9 baseline-only diagnostics equal the existing pinned
focused regressions. No candidate-only diagnostic exists.

Correction to626's evidence assumption: the23 shared errors are19
preservation_fixed_root_required and4 AttributeError for missing requeue_history.
Original run_suites.sh overlays current inc-261023-03 test_integration.py onto
lease-cap-619/baseline/agentq.py. The former calls requeue_history at122/134;
the latter lacks it (the current inc dispatcher defines it at768). Both sides
use identical baseline dispatcher bytes. The preserved fixed-root predicate
blocks other older fixtures. No production controller check is relaxed.

The gate now requires Counter equality of every exact diagnostic tuple (test ID,
FAIL/ERROR, subtest text, exception), pinned in lease619-shared-diagnostics.json,
in addition to all original source/inventory/completion and focused-difference
checks. This replaces the inaccurate generic23 fixed-root assumption; it cannot
accept arbitrary equal failures or moved diagnostics. It does not repair/waive
the unrelated fixtures or claim their scenarios passed. The original619 review's
no-candidate-regression requirement is satisfied. Independent exact source and
outcome review is required before the single preserved combined3 launch.

The actual gate refused the old assumption (full-gate-red.txt);14 focused parser
checks now pass (reconciliation-green.txt), including timeout/incomplete/skip/
new-error refusals. Full receipt is job608-lease619-full-receipt.json, binding both
raw logs and shared diagnostic pin. No heavy tests ran locally; only parser
checks. No live service/config/credential/seal/root/unit/queue mutation occurred.

This supersedes stale no-receipt/UNRUN paragraphs in lease-cap-prerequisite,
lease619-suite-gate, resume-after-compaction and to595. After independent approval,
ONE unused combined3 launch is authorized at4GiB/1CPU under Decision618. The
full diagnostic result, canonical typed package, deterministic complete runtime
receipt, exact old/new inventory, independent source/action/privilege/seal review
and automatic608 APPROVE remain mandatory before595 application.
