# Job608: installed tooling check timeout is pre-existing at 1 CPU (proposal, needs independent review)

Status: PROPOSAL ONLY. No check is waived by this file. The package runner is unchanged.

## Facts
- package3 (export a8041db9, source 55a1dd59, offload 4g/1CPU): installed tooling shard
  191/192 pass. Only failure: test/scripts/write-unified-entry-dts.test.ts
  "reuses unaffected canonical groups while rebuilding runtime after input edits",
  vitest 120000 ms timeout. Log: job608-package3-offload.log.gz.
- dtsprobe1 (runner job608-dtsprobe1-runner.sh, same digest-verified archives, one offload,
  4g/1CPU) ran ONLY that test twice:
  - base c790ba44 (no 608 overlay): exit 1, timeout. Phases: initial-build 69.8s,
    unchanged-build 18.1s, edited-build killed (143) at the deadline.
  - successor 55a1dd59: exit 1, timeout. Phases: initial-build 61.0s, unchanged 17.3s,
    edited 20.7s (exit 0), then cold-writer killed at the deadline.
  Log: job608-dtsprobe1-offload.log.gz.
- The only 608 change to the code under test (scripts/lib/tsdown-declaration-writer.mts) is
  gated on OPENCLAW_608_BOUNDED_PACKAGE, which this test never sets. The successor got
  further than base in the same budget.

## Conclusion
The timeout comes from the upstream test's 120s budget vs the admitted 1 CPU. It is not
a regression from 608. Every assertion that ran passed in both variants.

## Requested decision (independent reviewer, not the author)
Choose one, then record it in a committed review:
1. Accept this single test as baseline-equivalent at 1 CPU. The runner may then treat it
   as satisfied only via base-parity proof (base also times out with the same phase
   profile), with every other installed check still required. OR
2. Require a source split of that test into bounded cases that each fit 120s at 1 CPU,
   without removing any assertion.
Never lower the floor, raise the CPU/memory budget, or delete the test.
