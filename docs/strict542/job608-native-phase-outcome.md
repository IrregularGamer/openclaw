# Spent native phase-trace diagnostic outcome608 (NOT success, NOT package evidence)

Launch: 0810d234 record, export manifest 5291b147 (independently approved 91cae5b5).
Settled: offload broker `run remote rc=1 2354s` at 2026-10-26T23:58:40Z. This export is SPENT; never relaunch it.

Observed in the retained local stream (job608-native-phase-offload.txt; offload copied no
result598 artifacts after rc1, so raw probe.log/release-phase-trace.log are NOT available here):
- The initial policy suites ran and passed, including the 12 phase-policy tests.
- Main configs progressed through index 45 (`phase":"closed"`), so config15 completed this time,
  including the fixed RD_LOG release tracing. Its span output is not retained locally, so the
  earlier config15 SIGKILL is not localized. Trace overhead and timing are not comparable.
- Config46 (main-config-46) was SIGKILLed (`timedOut:false`, process-group dead) with sampled
  RSS ~2011.9e6 bytes (V8 heap ~15.8e6), i.e. native memory at the 2 GiB lease limit.
  Configs 47..56 and all four workers did not run. AI/package/typed-frozen stages: not reached.

Conclusions:
- The failure point moved from config15 to config46. The memory pressure is in native
  (rolldown) allocation per isolated config, not in the JS heap and not specific to config15.
- No unchanged retry. The next step is a source correction in the existing isolated-config owner
  (e.g. each isolated config gets its own bounded process with RSS released between configs, or
  config46 is split), with RED/GREEN and independent review, then ONE new admitted export on a
  fresh >=51 min worker. Do not lower the floor or raise the 2 GiB/1 CPU budget.
- 595 must not apply. Package, artifact/action/privilege/seal/automatic-queue reviews and HQ
  post-restart owner/natural-gap gates remain open.
