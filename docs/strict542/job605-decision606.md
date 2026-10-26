# Decision606 single admitted diagnostic

Decision606 corrected the friend offload-work.slice soft limit to its existing
2147483648-byte hard limit. No larger request or offload policy change is allowed.
Retain the reviewed fail-fast floor1625784320 unchanged.

The exact committed inputs in job605-decision606-export.json reconstruct current
918bcd11 from the previously committed secretless c790ba44 export plus every
changed path (no deletions) archived from HEAD918bcd11. Base/native SHA256 values
were recomputed and match their prior reviewed receipts; runner bytes are exactly
HEAD docs/strict542/run-isolated598.sh. This is a fresh export directory, not a
checkout or a reused remote workspace. The runner validates archive hashes again
before extracting. No runtime auth/config/credentials or provider calls.

Run once through normal offload admission with default2g/1CPU:

    cd /home/deploy/agentq/tmp/export605-decision606
    offload run --artifacts result598 -- sh run598.sh

Full relevant checks precede the finite900s whole-config diagnostic. This runner
produces diagnostic evidence only, never an accepted runtime/tree/action receipt.
If config15 completes, a supported bounded owning-source full builder and actual
full build/package, deterministic receipt, independent action/privilege/seal and
automatic queue reviews remain required. If it OOMs/times out at2GiB, preserve
actual peak/outcome, stop, and ask the new >2GiB budget decision required by606.
Do not split config15, weaken checks, retry unchanged, build locally, change policy,
or claim source preparation/install completion.
