# job608 unified-0 (1bed) diagnostic relaunch — sampler wrapper, export unchanged

Why not edit run-stage608.sh: prepare-stage608-export.py binds every stage receipt to the
source commit (`rec['source_commit']==commit`). A runner edit is a new commit and would
invalidate the accepted native 8866a036, compiler 53664cdb and runtime 7d3d1bd6 receipts
(about 3 x 40 min of reruns). So the per-substep timing lives only in the outer offload
command; the frozen 1bed export, run608.sh (sha256 eac266cf...), stage608.py, inputs and all
in-script checks/timeouts are byte-identical to preflight 2d38d7ed / APPROVE ac7f4dd3.

Re-verified locally before launch: manifest stage=unified-0, execution_state=UNUSED,
source_commit 1bed4d1b, `python3 stage608.py verify-inputs` rc0. The previous run's
remote copy was discarded by offload; the local stage dir has no result dir.

Command (from stage-unified-0-1bed, first long step of this worker, `offload deadline`
reported 3318 s longest safe):

    offload run --timeout 2980 --mem 4g --cpus 1 --artifacts result608-unified-0 -- sh -c '
      S=$(date +%s)
      ( trap '"'"'kill $s 2>/dev/null; exit 0'"'"' TERM; while :; do sleep 240 & s=$!; wait $s; echo "SAMPLE608 t=$(( $(date +%s)-S ))s"; ps -eo pid,etimes,time,rss,args --sort=-time 2>/dev/null | head -6 | cut -c1-200; done ) & P=$!
      timeout -k 15s 2920s sh run608.sh; rc=$?; kill $P 2>/dev/null; wait $P 2>/dev/null; echo "SAMPLE608 end rc=$rc t=$(( $(date +%s)-S ))s"; exit $rc'

- Budget: 4g/1CPU as before (the offload maximum admission; no floor, gate or check changed).
  Inner wall 2920 s instead of 2400 s, still inside the admitted `offload run --timeout`
  bound for this worker; it is a single diagnostic, not a new per-stage default.
- The sampler only prints the top CPU-time processes every 240 s to stdout, which comes back
  in the local offload log even when the run fails (failed runs return no artifacts).
  It answers Pinch change request 1: which substep (stage-native / restore-build / pnpm
  install / tsdown openclaw-dts-base) consumes the CPU.
- If rc=0: record the unified-0 receipt and continue unified-1..5. If rc!=0: the samples
  decide the source-level split of openclaw-dts-base, prepared as a new reviewed commit.
- 595 MUST NOT APPLY. Nothing installed or sealed.

## Independent review (agent aad13e87): CHANGES -> fixed
Runner identity (eac266cf), no secrets, and the receipt-binding claim were confirmed. Finding: `kill $P`
left the in-flight `sleep 240` orphaned holding stdout (could exceed --timeout 2980). Fixed: the sampler
traps TERM and kills its own sleep; the wrapper waits for it. Stub test (run608.sh = `sleep 3; exit 7`):
rc=7 propagated, returned in 3 s, no orphan sleep left. Launched with this fixed wrapper.
