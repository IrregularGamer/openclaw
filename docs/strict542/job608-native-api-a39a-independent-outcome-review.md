# job608 a39a API/resource diagnostic: independent outcome review

**VERDICT: APPROVE EXACT DIAGNOSTIC EVIDENCE ONLY. 595 MUST NOT APPLY.**

Reviewer: Rook `/root/review_api_outcome`, 2026-10-29 UTC. Reviewed exact
`aca9dd98e9aa642b4d9c518ce8376b9d3181a787` and actual returned export
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-api-phase-a39a-diag1`.
Unrelated newer source edits are outside this review. No material finding.

Independent verification:

- Exact manifest SHA256 is
  `0cba05c7a70e1f4fd1c66f4f840f326616ce6bf23568200cf4005d5a3826d3b6`.
  Frozen source remains `a39ad5ee95609193502850d0dbb87b5dcbb5e3e3`;
  canonical common identity independently recomputes as
  `d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62`.
  All seven preflight module/manifest/runner pins match actual bytes. The four
  external diagnostic modules match committed `a970c798` bytes; none is promoted
  into frozen product source. All four source archives were independently
  streamed and match their manifest digests. All seven native/runtime input
  digests match; fresh `python3 -I -B stage608.py verify-inputs` exits0.
- The complete actual eight-file evidence inventory matches outcome JSON and
  exact committed raw bytes. The six files under returned `native-api608`
  total293855 B; sibling client log/rc add1911 B. Fresh `storage608.py result`
  exits0 against the unchanged33554432 B cap. No checkpoint, successful stage
  receipt, package, or artifact promotion exists in the returned tree.
- Actual client status file is0. Actual inner exit file and diagnostic
  command_exit are124; collection_exit is0 and cancelled_signal is null.
  These mean successful diagnostic collection of a timed-out command, never
  successful compilation. Receipt identity/run_id match the exact preflight.
- All112 resource samples parse, with zero sampling_error records. CPU/memory
  summary fields independently recompute exactly. Observed wall interval is
  1107.953720 s; aggregate CPU usage grows855.796739 s, comprising278.618625 s
  user and577.178114 s system. Throttled time grows356.816317 s across4209
  throttled periods. Peak memory is4287950848 B; maximum sampled current is
  4287168512 B, near the4 GiB cap. Memory high/max/OOM/OOM-kill deltas are all0.
  CPU and memory pressure counters both grow substantially. These aggregate
  measurements include setup and collection; they do not identify a particular
  native function's CPU cost or establish either pure CPU or memory causation.
- All nine raw phase records equal outcome JSON: parse returns in2.505437 s,
  snapshot creation in98.998217 s, config diagnostics in0.023579 s and program
  diagnostics in0.236494 s. First global diagnostics starts and has no returned
  event before the900 s whole-compiler bound. No later syntactic/bind/semantic,
  emit or close event occurs. The900 s bound includes preceding compiler work;
  it is not900 s spent solely inside global diagnostics.
- Pinned collector60742b3e waits its child, then checks/kills surviving live
  process-group members before its final sample and diagnostic publication.
  Actual owner log independently reports parentSignal SIGTERM, cleanup
  parent-signal, child SIGKILL, observedProcessState dead,
  observationScope process-group, finalStatus143. Final resource sample contains
  only the outer wrapper and collector, with no inner runner/compiler/native
  process. This supports settlement of the observed timeout; null external
  cancelled_signal is consistent with the inner compiler timeout.

The pinned upstream `session.go` digest39321b51 was independently rechecked.
Its actual handleGetGlobalDiagnostics forces GetSemanticDiagnostics before
returning lazy global diagnostics. Consequently the observed first-global
delay cannot be fixed by moving a later explicit semantic query adjacent to
it. This observation does not establish checker-cache expiry, an optimization,
or a finalized native CPU profile. Such a profile remains a separately reviewed
finite diagnostic, with no authority from this review.

The preflight's SPENT banner correctly prohibits replay; historical UNUSED
manifest/body text remains historical. The exact HQ handoff diff changes only
current diagnostic status and preserves original final gates. Frozen source,
inventory, successful stage chain/build/package, artifact/action/privilege/seal
reviews and automatic queue review remain required. Genuine foreground
nonqueue HQ ownership, a natural settled gap, fresh post-restart owner binding
and accepted-run acknowledgements, backup/rollback/reseal rules are not waived.
575/588/592 remain by reference;553 alone owns SAME510 continuation.

Exact-commit whitespace check passes. No build, full suite, offload, export
mutation, live provider call, installed/sealed/root/unit/sudo/service/budget or
scheduler action ran for this read-only evidence review. Approval does not
accept a package, installer application, future diagnostic or production action.
