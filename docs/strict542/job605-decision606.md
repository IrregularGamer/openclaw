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

Historical command already consumed by the single Decision606 run with default2g/1CPU.
Do not run again under this decision:

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

## Actual settled outcome and exact continuation boundary

The single authorized run exited1 after189 passing relevant checks and a
successful pinned frozen dependency install. The unchanged floor refused before
config census/any compiler/config15. See job605-decision606-outcome.json and the
actual logs and tests named there, plus job605-decision606-independent-review.md. No diagnostic result or
runtime artifact exists. The remote parent's post-settlement read-only snapshot
confirms high=max2147483648, cpu.max100000/100000, swap0, pids512. Its2150412288
peak and counters are cumulative; they are NOT a measured run/config15 peak.
The failed invocation did not record its effective limit, so no exact value or
OOM/timeout is invented. This outcome does not meet606's condition for requesting
a larger budget. No second admitted run or unchanged retry was performed.

The owning reader scripts/lib/process-memory.mts returns capacityBytes from
the controller ceilings, but limitBytes also subtracts competing charged usage
after crediting inactive_file and its own RSS. Installation cache/slab pressure
is a possible explanation only; it was not measured at refusal. Source successor
ba38e2b7 preserves the exact floor and predicates and includes capacityBytes,
limitBytes, unresolved, usageKnown and floorBytes in a failed-admission message.
Its14 lightweight policy checks pass. The189-test remote result remains exact
918bcd11 evidence, not an execution of this later diagnostic-message successor.
Do not silently change limitBytes to capacityBytes, credit active_file/slab,
reclaim cgroups/host caches, relax the floor or infer compiler feasibility.

595 has no application-ready artifact from605. Continue the ordered future HQ
procedure in job598-HQ-HANDOFF.md only after an actual complete supported build,
package/tree receipt, action and next seal exist and exact independent reviews
and the actual automatic queue approval cover them. Its old automatic598 review
references must be reconciled to the actual queue review identity of the final
prepared implementation; never manufacture APPROVE598 or rewrite a review proof.
The existing source and privilege-design approvals do not cover absent bytes.

Retain that handoff's original-seal/all-guards validation, exact old/new inventory,
exclusive backups and partial-application poison/rollback/reseal rules. Retain
its genuine finite foreground nonqueue HQ natural-gap requirement and the
mandatory fresh post-restart owner binding AND accepted-run acknowledgements;
old510/515 identities and queue ops labels cannot supply them. The external-wait
source3c18a58 remains uninstalled and cannot bootstrap its own initial gap. Only
an actually available existing timed slot after genuine finite HQ acknowledgement
can be used once; no reservation, detached continuation, repeated docs retry,
direct DB/status/counter edit, stop/resume bypass or new scheduler request exists.
575/588 stays by reference604ffc9/package1b22c4d/evidenced1304c7/review592,553
retains sole SAME510 continuation and497 retains all original release gates.
Approval1529 remains ONLY INTERNAL_REPORT_URL/API_BASE_URL.
