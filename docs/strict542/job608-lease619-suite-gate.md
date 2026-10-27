# Additional608 prerequisite evidence gate (source only)

The approved619 installer and all its pinned inputs remain unchanged. Its
`run_suites.sh` finishes with `comm`: its exit0 can conceal unittest failure,
timeout, missing imports or partial logs. Even empty failing-name lists can
appear equal after a killed runner. Review624 already requires inspecting
counts/timeouts in addition to that script's exit status.

`verify-lease619-suites.py` makes that evidence check executable. It reads files
only; it runs no suites, controller, service, provider or root command. It pins
all16 actual619 suite/runner/source inputs, derives the complete78/90 baseline/
candidate test inventories without importing them, requires exactly one
completed unittest summary and terminal rc, and reconciles each named result
with its full failure diagnostics. Timeout/signal, missing/duplicate test,
skip/expected failure, incomplete log, summary/exit mismatch and unknown
diagnostic refuse. No new known-error exemption is introduced.

The only candidate errors permitted are the23 pre-existing
`PermissionError: preservation_fixed_root_required` errors documented by619,
identical on baseline and candidate. The only baseline-only differences are
the exact nine focused diagnostics independently recorded here from the OLD
controller: four FAIL and five ERROR, seven test IDs including subtests.
These are the intentional regression evidence for619, not a passing full
suite. Any changed exception, inventory or count requires reconciliation and
independent review, never editing pins to make a run pass. The actual full
78/90 comparison has NOT run: old live/sealed17338c48 still refuses admission.

After genuine foreground nonqueue HQ application of the exact624-approved619
installer and the existing receipt/seal gates, run the unchanged619 suites
through admitted offload from its committed secretless export. Preserve both
full logs as artifacts. Alongside the independent outcome review, run:

```
python3 docs/strict542/verify-lease619-suites.py \
  --ops-source /path/to/exact-exported-ops-source \
  --logs /path/to/returned/lease-cap-619/out
```

Record stdout and its SHA256 alongside the export, offload/settlement and
actual HQ receipts. This evidence check is necessary, not sufficient: it
cannot authenticate execution placement, confer approval, attest ownership,
prove application or replace original seal validation. The external outcome
review must check those separate actual receipts. The original installer,
live broker, seal, approved619 artifact and its review are untouched.

Validation on2026-10-27:13 synthetic refusal tests PASS (0.045s). The real
focused17-test619 module ran against each pinned controller with transport and
private IO stubbed by its existing tests: candidate17PASS; baseline intentional
4FAIL/5ERROR. The new parser accepts the actual complete logs, including real
subtest formatting. No full control suite ran locally or remotely this worker.
Logs are `job608-lease619-{baseline,candidate}-focused.txt`. The old/new
controller and all16 input hashes are `lease619-suite-inputs.json`; exact
baseline differences are `lease619-baseline-regressions.json`.

Independent review626 APPROVED exact source commit
`c58e8d229cc15bfafa9ebe744618390ffe76388c` (executable change29b4f5e0).
The verbatim review is [preserved here](job608-lease619-suite-gate-review626.md)
from ops-work commit1b6b081. It accepts the gate and focused evidence only;
the full78/90 suites remain UNRUN. It does
not alter approved619 or approve applying it from a queue worker.608 remains
incomplete until actual622/HQ-RECEIPT.md, NEW installed/sealeddb4d2903, the
admitted full comparisons, the sole preserved4GiB combined build, typed full
package, exact source/action/privilege/seal reviews and automatic608 APPROVE.
The ordered595 handoff and original510/515 fresh post-restart owner/accepted-run
gates remain in job608-lease-cap-prerequisite.md and job598-HQ-HANDOFF.md.
