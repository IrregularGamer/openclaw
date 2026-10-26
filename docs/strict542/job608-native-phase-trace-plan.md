# Fixed native phase-localization continuation608

Spec: job608 changes round2, exact spent post-metadata outcome86cb85df and its
independent outcome review. Job608 is incomplete;595 must not apply.

The ONE eba2def8 export settled rc1/2062s at2026-10-26T23:06:04Z. All235 checks
passed and the rebuilt17df2061 addon/complete receipt matched compile4 byte for
byte. AI+main0..14 succeeded. Main15 was SIGKILL after112472.703534ms, not a
timeout; main16..56/workers did not run. Last buildEnd sample: RSS1821642752,
V8heap18604160,cgroup2141941760 bytes. Its sampled OOM counters remain zero;
exact killer and native subphase remain unknown. The final interval used1.201548s
user and4.409903s system CPU. These observations do not identify a failing phase.

Pinned bundle/bundle.rs invokes buildEnd after scan normalization, before link
and generation. Both prior AST lifetime corrections act in generation. Moving
another release blindly cannot show whether link ever reaches generation.
Existing rolldown_tracing supports RD_LOG target filters in this release and
stdout ENTER/CLOSE events. Readable/json modes omit those spans, while Chrome
requires another feature. Use the existing release tracer without native source,
receipt, toolchain or compiler-semantic changes.

- [x] Add RED inherited RD_LOG/RD_LOG_OUTPUT refusal and fixed config15-only
  environment policy tests. Both fail for missing behavior. Implement the narrow
  policy and propagation assertion; all12 focused policy tests GREEN.
- [x] Add a real synthetic-input native fixture proving this addon emits link
  and generation target spans plus ENTER/CLOSE through the fixed stdout mode.
  It remains UNRUN until the next admitted full export. It is not test evidence.
- [ ] Independent exact source/export review, then ONE fresh qualifying >=51min
  foreground worker: same full runner, all238 affected checks (135Node90Python,
  3typed10real), rebuilt compile4 equality, existing8parity variants, both native
  and stock lazy/minifier cases, AI+all57main configs/all4workers. Only config15
  receives fixed RD_LOG filters and RD_LOG_OUTPUT=stdout. Preserve raw probe.log
  and release-phase-trace.log. Keep 900s compiler/2700s outer deadlines,
  1625784320-byte floor,2GiB1CPU,zero new swap and real cancellation/settlement.
- [ ] Independently review actual settled output. Trace overhead may change
  timing; do not compare it as an uninstrumented performance measurement. Locate
  the last entered/closed phase from raw spans, not the buildEnd telemetry hook.
  Missing/unsupported tracing, refusal, timeout or partial output is not success.
- [ ] Use that evidence for any next memory correction in its existing source
  owner, RED/GREEN and independent review; no unchanged retry or floor waiver.
  Only independently accepted complete success permits the existing full typed
  frozen-package promotion plan. Artifact/action/privilege/seal/automatic-queue
  reviews and exact HQ natural-gap/post-restart-owner gates remain mandatory.

No additional standalone native stage is needed: all4 native owner hashes are
unchanged, so accepted compile4+libtests3 receipts remain the exact inputs. The
new export still rebuilds the addon from committed secretless source in its own
lease; never upload addon/cache/toolchain/dependencies or runtime/auth material.

Validation limits: the extra local isolated-config598 test could not load the
unchanged scripts/lib/isolated-config.mjs absent from this partial maintained
checkout (ERR_MODULE_NOT_FOUND). Retain job608-native-phase-focused.txt as that
harness result; do not count it as an assertion failure or a passed test. The
unchanged source arrives from the pinned base in the next full offload export.
New fixture/policy syntax checks pass;12 policy tests pass. Full tests are not
claimed for this source until that admitted run. No local gateway build/tests,
installed/sealed/root/unit/sudoers/service/config/provider or queue mutation.
