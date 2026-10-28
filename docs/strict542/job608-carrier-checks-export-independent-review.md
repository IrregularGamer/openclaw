# Independent carrier-source checks-only export preflight608

**VERDICT: APPROVE EXACT CHECKS-ONLY PREFLIGHT.** No material finding for one
normally admitted checks-only attempt. Reviewer: Rook `/root/carrier_review`,
2026-10-28 UTC. This is not a successful test outcome, native/build/package
approval, full source-inventory acceptance or installation authority.

Exact export:
`/home/deploy/agentq/tmp/export608-stage-checks-carrier-next`.
Manifest SHA256:
`20111ce5f68e7764e7176a670df6e9097deafa51d02291810bf65dd41c8c7c2d`.
Frozen source: `1bed4d1bb53eff145f724cc6a448dc73b3609015`.
Common source/export identity:
`5d7e9d57fb660e2b54f5595e81ddf332027e21b303937c2cd6bc7f718f311263`.
Existing independent carrier source review is committed at `1b63fa7a`.
This document does not change the freeze or export.

Fresh bounded local read-only proof passed:

- Actual manifest digest matches the exact requested pin. Canonical JSON of
  base archive digest, frozen source and successor archive digest recomputes
  the recorded common identity. Stage is `checks`, runner commit equals the
  freeze, and `stage_inputs` is exactly empty. No local predecessor input or
  `result608-*` directory exists. `UNUSED` and absent results are a preparation
  snapshot, not independent proof of remote launch history.
- Actual runner and helper are private regular files and byte-identical to
  their exact frozen Git source paths. Both manifest pins match: runner
  `eac266cfaab7efef7c92ed94c53a0a55e75303b8ee4810bc15f21f243a76b8ee`,
  helper `a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4`.
  `sh -n run608.sh` and `python3 -I stage608.py verify-inputs` pass in the
  actual export directory without launching the runner.
- Streamed the 13,414,400-byte successor tar and a fresh
  `git archive <freeze> -- <all621 successor_paths>` to SHA256. Both equal
  `ea5b2c39506f527fe0e72743ffeb301f4b0e9d36e62f287b78d57b6795c89360`.
  Separately validated all621 regular members, 12,918,362 payload bytes:
  duplicate-free safe paths, exact frozen Git blob identities and executable
  mode representation. The path list is sorted and unique. The90 paths omitted
  from the complete base-to-freeze diff are all historical `docs/strict542/job608-*`
  evidence files; no executable/source path from that diff is omitted.
- Both small native receipt files match their manifest digests. No giant base,
  native or upstream archive was reread; their raw pins rely on the canonical
  preparer's reported streaming verification and the runner's mandatory
  pre-extraction rechecks. The overlay proof above is independent.
- The exact `checks` branch includes the native-owner transport, Python native
  endpoint, root-owner supervisor, application/refusal and cancellation/settlement
  suites. Source inspection confirms real fd3/IPC and escaped-descendant/
  parent-death cancellation fixtures remain selected. The branch contains no
  native-consumer rebuild, archive-build or full package-builder invocation.
  It installs frozen test dependencies and runs the four existing tooling
  test files; this is checks execution, not runtime installation.
- Parsed all12 selected Python test modules:135 declared test methods. The
  15 Node test files and four installed tooling test files are byte-identical
  to the prior reviewed frozen9fb source. The planned census is therefore
  158 Node +135 Python +198 installed =491, retaining the prior Node/installed
  census and adding the two carrier plus seven preparer cases to the prior482.
  Actual discovered/pass counts must be reconciled from the new run; no full
  suite was executed in this preflight.

The manifest's inherited purpose says `native`, and `required_checks: 14`, old
review-pending and predecessor fields describe historical stages. They do not
select runtime behavior or establish the current census. Current dispatch and
identity come from exact `stage: checks`, frozen runner/helper bytes and archive/
export pins. Do not report those inherited fields as current results.

The proposed finite command is one normal-admission run with `--mem 4g --cpus 1
--timeout 1500`, inner `timeout -k 15s 1440s sh run608.sh`, returning only
`result608-checks`. Existing deadline, lease, swap-zero, resource and settlement
gates remain mandatory. No bypass or policy change is authorized. At preflight
the local filesystem reported254,308,352 available bytes, above the proposed
16,777,216-byte return reserve. That reserve is a planning bound, not a measured
maximum for unknown logs/dependencies or remote scratch; admission and actual
run results remain the operator/controller's responsibility.

End-to-end retained checkpoint/final-package storage remains unresolved. This
checks-only preflight does not permit an expensive native/full-build/package
retry, deletion of retained artifacts or relabelling older stage evidence.
Later source/storage changes require their own reviewed source freeze and fresh
bindings; successful checks at this freeze cannot be relabelled for changed
source. Exact final artifact/action/privilege/original-and-next-seal, owner/
acknowledgement and REAL automatic queue gates remain required.

No full test/build, offload launch, remote inspection, installed/sealed/root/
unit/sudoers/runtime/service/scheduler mutation occurred in this review. The
only authored deliverable is this document. **595 MUST NOT APPLY.**
