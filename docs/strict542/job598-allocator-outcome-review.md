# job598 allocator reconciled diagnostic: independent outcome review

- Reviewer: independent read-only outcome reviewer (Claude Opus 5.5 subagent; no ssh, no offload, no runs executed)
- Reviewed commit: fd08652c7ec9d614f42fb1299567562b95e402c2 (branch strict542-source552)
- Subject: job598-HQ-HANDOFF.md, section "Actual reconciled allocator diagnostic: same finite timeout (2026-10-26)"
- Verdict: **APPROVE (evidence-only)**. The handoff's description of the outcome matches the actual log and cleanup evidence.

## Verified facts

- Log runs/598/allocator-reconciled-run.log (58 lines) sha256 =
  2532f2035a028bea24e32b6e7ad82f529e43bf913cee2bc2825bfa43ae843021 (matches the handoff's 2532f203…3021).
- Allocator-policy tests: `pass 13`, `fail 0`, `cancelled 0`.
- Every diagnostic JSON record shows `allocator.MIMALLOC_ALLOW_THP="0"` and one distinct
  nativePools set: ROLLDOWN_WORKER_THREADS, ROLLDOWN_MAX_BLOCKING_THREADS, RAYON_NUM_THREADS and
  TOKIO_WORKER_THREADS all equal to "1".
- Config 14 reached `closed` with peak rss 128 MiB. Configs 0..13 have no per-phase records in
  this log, so they are not separately evidenced here. The run did continue to config 15.
- main-config-15 (pid 565) peaked at rss 1439 MiB, then: `timeout after 869346ms ... sending SIGTERM`,
  `forcing SIGKILL`, and the child result is `timedOut:true, cleanup:"timeout",
  observedProcessState:"dead", observationScope:"process-group"`. The final line is `exit=1`.
- No success claimed. The only "success" string in the log is the test name asserting that failed
  runs refuse success. The handoff explicitly claims no compiler, build, artifact, action or
  application success, and says no result598 artifacts were pulled.
- Comparison with the earlier run: the handoff records that the fixed-pool (pool=1) diagnostic for
  the same unified config 15 also timed out, after 869459ms (configs 0..14 passed, process-group
  death after SIGTERM). This run differs only by the THP-off allocator successor and ended the same
  way, about 113ms earlier. So the allocator change did not affect the config-15 stall.
- Export inputs (export598-config-isolation/export-manifest.json): run598.sh sha256 4ddaa154badc…c037
  matches runner_sha256. native598.tar d73e4e35… matches native_export_sha256. successor598.tar
  b599e23a… matches successor_archive_sha256. source598.tar (690 MB) was deliberately not rehashed
  and is taken as recorded in the manifest.
- Slot cleanup: allocator-reconciliation/immediate-idle.json reports phase LOCK_HELD_READY,
  runner_lock_available true, 0 managed running containers and no live leases. post-clean.json
  reports phase LOCK_HELD_VERIFIED_ABSENT, absent true. Both name the same slot
  (tmp-export598-config-isolation-98c59c32), so they are consistent with each other and with a
  clean teardown.

## Scope and restrictions

This review approves only the accuracy of the recorded outcome evidence. It grants **no**
compiler, build, artifact, action or application approval, and it does not authorize any further run.
The unchanged allocator source (6305e30c successor, THP-off, native pools=1) **must not be retried**.
Any further admitted diagnostic needs a new source-only change that addresses the config-15 root
cause (CPU-bound graph vs memory), plus its own independent review.
