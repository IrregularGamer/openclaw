# 608 consumer-b outcome (2026-10-26, settled rc=1), evidence only

Fresh worker (13:12Z, 1h limit). NEW never-used export
tmp/export608-native-consumer-unitfast-b, byte-identical to the reviewed export
(runner 39d26e32, successor 91ffa313, manifest a09747e3, native d73e4e35,
receipts e210de64/54e7461a all re-verified; archives hard-linked). ONE
`offload run --artifacts result598 -- timeout -k 15s 3000s sh run608.sh`
started ~13:15Z under the default 2GiB/1CPU lease. Slot accepted (no stale-slot refusal).

Result (raw log job608-consumer-b-offload.txt, sha256 3008f15b45a2db438605eea20f2a9844d209923c1b3a24761392e5a636e530cc):

- Runner policy tests: 24 pass, 0 fail (stage-receipt, addon pin, allocator,
  thread-pool, graph-floor and compiler-budget refusals all green).
- Isolated per-config diagnostics (DIAGNOSTIC_ONLY_NOT_BUILD_EVIDENCE) streamed
  for indices 38..45: all closed, peak RSS 129..361 MiB.
- Index 46 (main-config-46, tsdown.isolated598.config.ts, concurrency 1, all
  native pools 1, MIMALLOC_ALLOW_THP=0): RSS 1.32 GB running, 1.86 GB at
  build-end, 2.04 GB post-build, then SIGKILL (status null, timedOut false,
  process-group observed dead). This is the 2GiB lease memory limit, not a
  timeout. Offload exit rc=1, settled; the EXIT trap ran.
- Native byte-equality / stock-vs-patched parity / lazy-barrel / config15
  summary lines are not in the streamed stdout; the broker does not pull
  result598 on nonzero exit, so those results are NOT claimed here.

## Meaning

The single config 46 needs >2 GiB, and most of it after build-end
(1.86 GB -> 2.04 GB), i.e. in the post-build output/declaration phase, not in the
graph compile. Other configs fit easily. The next step is a source correction
in the owner that splits or bounds config 46's post-build phase (or emits it as
a separate unit), not a rerun of unchanged code and not a lowered floor/raised
lease.

## Continuation

1. Recover this exact slot's result598 through the existing jailed rsync output
   path (operator/fresh worker); never reuse it as input. This path is spent.
2. Identify config 46's entry and its post-build phase in
   tsdown.isolated598.config.ts / scripts/tsdown-bounded608.mts; implement and
   independently review the owning split/bound; then a new export + ONE run.
3. All later gates in job608-resume-after-unitfast.md stay unchanged. Nothing
   installed, sealed, restarted or released.
