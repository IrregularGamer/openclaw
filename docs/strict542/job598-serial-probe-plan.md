# Strict542 serial build probe implementation plan

Goal: measure the unchanged complete runtime config inventory with one Rolldown build at a time, in a disposable admitted 2GiB export. This is diagnostic preparation, never a releasable artifact.

Architecture: reuse upstream invocation, memory accounting, output scanner and process-tree cancellation. Fixed arguments preserve every original runtime config and the unified singleton graph. The normal build and4352MB guard stay unchanged. No heap override is allowed. Probe output cannot satisfy application598 build evidence.

- [x] Test refusal of unknown/oversized kernel capacity, caller heap/concurrency controls and existing output.
- [x] Add small policy plus finite probe entry; no runtime, installer or native changes.
- [ ] Independent exact source review before one admitted execution from committed secretless export.
- [ ] Preserve actual outcome and independent evidence review. Only actual success can justify a later owning build-plan correction; no artifact/action approval follows from a runtime-only probe.

Primary supporting contract: https://tsdown.dev/reference/cli documents --concurrency1. Exact pinned0.23.0 support also appears in upstream wrapper tests. Serial scheduling changes overlap only; unbundle or entry partitioning would change module identity and is excluded.

Source review:73162fb2 independently approves exact c790ba44 for one diagnostic only. The unchanged full4352MB guard remains mandatory. Compiler time is900s shared across both invocations plus existing bounded cleanup grace. No declaration/package/postbuild/artifact evidence is supplied by this probe.
