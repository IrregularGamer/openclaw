# job608 unified-0 a39a: independent failure-evidence review

SOURCE/EVIDENCE ONLY; **595 MUST NOT APPLY.** Reviewed exact commit
`11c1673e1067bca8c65b56c755241a11b834bd34`, all five added evidence files,
and the actual private sibling client log/rc and attempted export. Reviewer:
Rook `/root/review_compiler_preflight`, 2026-10-29 UTC.

Independent checks:

- Every evidence file is byte-identical to its exact committed version.
  `offload.log.gz` SHA256 is
  `86efb4d53cdd16fa3ced3795ee6f70e358397775b982d0cbd8af659901326c4e`.
  Its expansion is exactly the actual private
  `unified-0-substep-a39a-offload.log`: 8442 bytes, SHA256
  `4bde47a05b9c9f721469bb8c34e5f9bf87fce0957b62a02f13abb9343b710e9f`.
- Actual private `unified-0-substep-a39a-offload.rc` and committed `offload.rc`
  both contain exactly `124\n`. The raw log separately records
  `STEP608 unified-0-build-start budget=2258s +22s` and
  `STEP608 unified-0-build-fail 124 +2280s`.
- The committed manifest is byte-identical to the actual attempted export's
  manifest, SHA256
  `900edc324f8e2068521a9d4fc19b0c80d0fbca91cfa01ba5c618d2528fb0b4fd`.
  Run stage608-unified-0-a39a, source
  `a39ad5ee95609193502850d0dbb87b5dcbb5e3e3`, common export
  `d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62`
  agree with outcome.json and the independently approved launch preflight.
- No result608-unified-0 directory exists in the actual attempted export.
  No stage-success/build-done or native API phase marker occurs in the complete
  raw client log. It reaches openclaw-dts-base with caches disabled after the
  frozen install and then shows liveness messages. This establishes the failed
  finite attempt, not its precise native operation or cause.

The prelaunch manifest is immutable and still says UNUSED. Actual outcome is
correctly recorded separately as **SPENT_FAILURE_DO_NOT_REPLAY**. No returned
checkpoint, successful stage receipt, package or artifact can be promoted from
this evidence. The compiler export's prerequisite was not satisfied; its ready
preflight does not authorize a launch following this failure. Earlier accepted
checks/native/runtime evidence retains its own scope and supplies no unified-0
success. Current checker eviction, duplicate semantic work, pressure and the
precise native phase remain unproven.

The README and outcome correctly direct a new independently reviewed finite API
observation at a39a, rather than replay of the spent export, unchanged historical
1bed diagnostic or nonexistent further config-subset split. Preserve every
original diagnostic, source/input seal, cancellation/settlement and publication
boundary. No runtime settlement or live health check was performed in this
read-only evidence review; those remain separate prerequisites for future work.

Exact evidence/helper-range `git diff --check` passes. No tests, diagnostic,
offload, export change, runtime/root/service/config/unit/seal/provider operation
ran. This is an independent review of failure-record accuracy, not automatic
queue review, source/package/action approval or successful build acceptance.

**VERDICT: APPROVE FAILURE EVIDENCE ONLY.** The unified-0 attempt failed124,
is spent and must never be replayed unchanged. All final package, artifact,
action, privilege, seal, automatic-review and genuine HQ handoff gates remain.
