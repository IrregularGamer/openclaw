# Independent prelaunch review: unified-0 fresh observer

VERDICT: APPROVE the exact source-only diagnostic design at 3f10895ee3d135c8b3f50345bbf358902596a57c,
subject to the final fresh-export checks below. No launch was performed by this
reviewer. No install, acceptance, application or reseal authority. **595 MUST NOT APPLY.**

## Exact scope and evidence

- Frozen build source: 1bed4d1bb53eff145f724cc6a448dc73b3609015. Reviewed
  run-stage608.sh, run-build-stage608.sh, stage608.py, preparer, and owning build
  checkpoint/declaration source at that commit. Observer is outside the source
  archive and does not alter receipt identities or accepted inputs.
- Observer SHA256: `73d17f3c1e0892cd3366986d28e69b86e8f4fb9da4e5b91f9a8510b61a20c186`.
  Frozen runner SHA256: `eac266cfaab7efef7c92ed94c53a0a55e75303b8ee4810bc15f21f243a76b8ee`.
- Exact launch: from NEW `stage-unified-0-diag-fresh608`,
  `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-unified-0 -- sh observe-unified608.sh`.
  Require the current worker deadline check to admit it (at least 2655 seconds
  remain when offload checks). No local fallback or change to admission/floors.
- `sh -n` passes. Temporary stub tests changed only sampler sleep 120 -> 1 second
  and inner wall 2300 -> 2 seconds. Success, explicit failure and timeout returned
  0, 7 and 124 in 1.39, 1.35 and 2.04 seconds respectively; each emitted one
  sample, the synthetic log tail and its actual final status. Each process group
  had zero surviving live processes after return. Evidence is under
  `/var/tmp/review608-observer-8pa4od5v/`. No real build was run.

## Findings

1. Reconciliation is sufficient for one new diagnostic. I independently read
   the 180-byte retained `unified-0-diag-offload.log`: transfer guard refused
   `source/.npmrc`, then reported `remote_environment_blocked`. That attempt did
   not execute the observer or compiler. There is no retained client status file;
   no status is invented. The local original export has no source/ directory.
   The retained refusal is committed as `job608-unified-0-diag-refusal.log`,
   SHA256 `d98b62996e1f3144a579d8a5de2b6014868dadffa9f28f9cc10fe835f8f610b7`.
   offload derives its remote slug from the absolute export path; a NEW path
   changes that slug. Its rsync uses --delete with exclusion/per-directory
   .gitignore filtering, so preserved stale generated remote files are plausible,
   not proven. No filter or guard bypass is proposed. The historical launch note
   now prominently identifies its unsupported discarded-copy claim and command
   as superseded intent.
2. The observer keeps failure visible. The unchanged runner has an EXIT cleanup,
   but its whole process tree can be terminated by the inner 2300-second timeout.
   The observer survives that timeout, stops and waits its sampler (which itself
   kills and waits its owned sleep), prints the last 80 build-log lines and the
   actual status, then exits with that status. The 15-second kill grace still
   leaves 145 seconds inside the outer 2460-second bound. Every 120 seconds the
   sampler emits process CPU-time/RSS and up to 20 synthetic build-log lines.
   Missing early build.log is expected and does not change the status.
3. No nonzero result is acceptable stage output. offload pulls requested
   artifacts only after rc=0. An observed timeout remains diagnostic evidence;
   neither a partial output nor an observer log substitutes for the unchanged
   stage receipt. Successful output still requires independent exact acceptance.

## Source analysis for the next decision

`unified-0` selects exactly `openclaw-dts-base` and has no ordinary build-all
phase labels. It restores and validates the runtime predecessor, then compiles
the declaration group inside awaited `prepareBuildCheckpoint608`, before the
ordinary phase loop and its phase timings. The runtime `tsdown-unified` duration
of 6m33s measures runtime JS, not this DTS group; that duration cannot establish
how fast unified-0 should finish.

The build-all bounded deadline is passed to `runStep` in the phase loop. This
declaration produce path directly awaits `executeTsdownBuildPlan(group.plan, 1)`;
the reviewed outer observer timeout is therefore the explicit wall bound for
the diagnostic. After samples identify the consumer, any correction or split
should live at the existing canonical declaration/build owner and preserve
native ownership, identity, membership, private output inventories, cancellation
and settlement, and complete final joins. Repeating unchanged with more budget
would not resolve that source-level question.

## Final export checks required before launch

Confirm NEW destination, UNUSED unified-0 manifest, exact source/export pins,
byte-identical frozen runner/helper and observer, accepted native/runtime input
digests, verify-inputs rc0, and absence of source/ or prior results. Preparation
must use the committed streaming-hash preparer without overlapping an upload.
This design review does not claim those pending export checks have run.
