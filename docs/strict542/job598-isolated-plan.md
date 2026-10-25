# Job598 isolated compiler investigation plan

Goal: test fresh per-configuration compiler lifetimes under the SAME admitted 2GiB/1CPU and shared900s deadline. This is diagnostic source preparation, not accepted build evidence.

Evidence: d874f143 independently reviewed the actual timeout. Runtime-only resolution passes every main config to one child, even at concurrency1. Prior configurations may retain compiler/native memory; the actual failing phase is unknown. Fresh-process isolation tests that hypothesis without splitting the shared Gateway/SDK graph. Existing upstream config export and tsdown CLI config support are reused, with no dependency or compilation-policy changes.

Implementation (Rook uses writing-plans, TDD and inline execution):
- [ ] Test strict complete ordered config census/selection, unchanged config identity, invalid index and changed census refusal.
- [ ] Add maintained scripts/lib selection helper; diagnostic config wrapper selects one WHOLE original config and adds bounded telemetry only. Keep all entries, dependencies, plugins, hooks, options and graph boundaries.
- [ ] Add finite isolated diagnostic, AI first then every original main config in original order, each in a new child through the existing scanner/cancellation owner. Preserve no-clean and original900s shared deadline; stop on first refusal.
- [ ] Independent exact source review before a single admitted committed secretless export run, including all180 relevant checks plus new selector tests.
- [ ] Preserve actual per-config census, begin/end/RSS/heap/cgroup telemetry and result evidence; independent review. No unchanged retry. Any success still requires complete owning build/profile correction, declarations/postbuild/package/tree/action/seal and automatic598 review.

Normal4352MiB full-build preflight, native predicates, supervisor, installer and all595 gates stay unchanged. No heap/deadline override, omitted config, new entry partition, singleton duplication, caller-selected root command, live operation or local gateway build is allowed. Parent-loaded config metadata adds overhead; the probe cannot establish capacity until the actual run. Cgroup telemetry is best effort diagnostic evidence, never admission or success authority.


Native pool successor design: actual runner thread sample observed6 runnable
rolldown-worker threads in an admitted1CPU container, cpuset0-3. Pinned Rolldown
1.2.9 source init() defaults its custom Tokio runtime to physicalCPU*3/2,
independent of quota: https://raw.githubusercontent.com/rolldown/rolldown/v1.2.9/crates/rolldown_binding/src/lib.rs
(lines111-133). Existing scripts/lib/vitest-isolated.mts already owns explicit
native-pool settings. The fixed diagnostic policy now generates workers1,
blocking1, Rayon1 and Tokio1 AFTER refusing inherited controls. Every compiler
plan and the parent config evaluator use those exact fixed values, recorded in
plan markers/receipt. This is scheduling/resource correction, not heap or deadline
override, tree-shake/config omission, dependency patch or empirical speed proof.
The active6d7ecc59 run remains immutable and must finish/settle normally before
any fresh corrected experiment. Independent exact successor review is required.
