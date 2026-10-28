# Independent corrected-freeze runtime evidence review608

**VERDICT: APPROVE ACTUAL RUNTIME CHECKPOINT EVIDENCE ONLY.**
No material finding within this scope. Reviewer: Rook `/root/review_runtime`,
2026-10-28 UTC, independent of the runtime producer and acceptance author.
Exact reviewed evidence commit: `92f33b70` (all eight changed files).
No earlier independent runtime review of this receipt was found.

I independently ran a read-only Python verifier from stdin against the actual
retained export `/home/deploy/agentq/tmp/export608-stage-runtime-owned-next`,
its returned `result608-runtime` files and actual `runs/608` log/rc files.
Every committed evidence blob was streamed from Git and matched its working
file. The reviewed acceptance checker uses bounded streaming hashes and checks
exact outputs; I did not execute its evidence-writing portion. My separate
verifier made no archive extraction or output changes, used `tarfile` streaming
mode `r|`, and streamed hashes with `hashlib.file_digest`. No giant `read_bytes`
or unbounded archive-content read was used. `git diff --check 92f33b70^ 92f33b70`
also passed.

Verified results:

- Actual client rc, returned exit-code.txt and committed rc each contain
  exactly `0\n`. Raw offload log ends in `STEP608 runtime-pass`; the separately
  retained rc provides the terminal client status, rather than an invented
  terminal line in that log.
- Actual, committed and verification stage receipts agree, SHA256
  `a4ef26da99c7d13ad21f1ed94d36b0bb85657cf7507f943c52539f65eabb712f`.
  Kind is JOB608_STAGE_RECEIPT, stage runtime, run ID stage608-runtime-next,
  exit0. Source is `5f7d810b7f254e4f06dbf7761b557ba90bf1a2b0`, common export
  `76b4b47a0e5c3e0a157f75ff1b76d60753c8acdbf5f76bc495668dd985d70f64`.
  Retained and committed manifests match receipt manifest SHA256
  `cf8907d39394721c84a496cd9aed4d52f33f4bf335335cf91a7a03252329cd80`.
- All five returned regular files match their recorded SHA256 values and
  exact file set: checkpoint, build log, stage receipt, exit-code and pnpm-path.
  No returned symlinks exist. Total returned bytes are313,378,134. Checkpoint
  SHA256 is `656a128d9966400beb6a92d8ebccca02e1d5bba737d03f1d922bc6ce95c88459`;
  build-log SHA256 is
  `c4391af26306925211fcc940e0c6a4abd303c6b0b683aedb3cafde78f253b82a`.
- Every archive member has a unique safe relative path and the exact expected
  root/prefix. All8,956 data entries match checkpoint receipt path, kind, mode
  and content hash or link target:192 directories,8,764 files, zero links.
  No hard links, devices or unexpected members were accepted. The embedded
  receipt equals the committed checkpoint receipt, is runtime with no
  ancestors, and retains status CHECKPOINT_NOT_BUILT.
- All four actual staged native input files match manifest/receipt pins.
  Checkpoint native compile/libtests/addon identity agrees respectively with
  `4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e`,
  `2f81179f5d1bf14d1519cf446935a3cd783da0e28e79a69067c85e5f873dd946`,
  `0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042`.
  Native stage receipt pin is
  `f40df3a579bd600c154b14ad9d9ac863b5ab26381f8615aa54d0829c0ea05069`.
- Both committed gzip logs match their compressed hashes, expanded hashes,
  byte lengths and actual raw log files. The58 structured compiler events
  from ai through main-config-56 all have result status0, no signal and no
  timeout. Checkpoint phases exactly match verification JSON and all ran:
  clean:dist0.398s, plugins:assets:build18.701s, tsdown-ai67.383s,
  tsdown-packages520.613s, tsdown-unified396.681s. The raw log independently
  reports completed phases and16m43.8s total. Direct-eval dependency warnings
  are present; they are not silently described as a warning-free build.

Verification JSON itself hashes to
`e176b13d93702bcc0865eb89bc537ade20c6039532a1492224c93ded6cf362f0`.
The manifest's inherited UNUSED/preparation prose and review-pending metadata
are historical snapshot text; actual retained producer evidence above establishes
this runtime outcome. That text does not create a new source-review gate waiver.

This verifies runtime-stage evidence and its carried native identity. It does
not rerun native compilation/library tests, gateway suites or provider calls;
prove whole-gateway reproducibility; or approve the subsequent unified0 timeout,
a new diagnostic/source freeze, declaration stages or any completed package.
The prior independent native/source reviews retain their own scope. No heavy
build/test, offload, root/unit/sudoers/seal/config/service or runtime change ran.

NEW current unified0..5/middle/sdk0..1/tail/package evidence, full relevant checks
and realistic supervisor IPC refusal/cancellation evidence remain required.
Exact final artifact/source/action/privilege/original-and-next-seal reviews and
the real automatic queue review remain mandatory before application. The ordered
595 handoff must preserve backups/rollback/reseal rules, finite foreground
nonqueue HQ natural-gap ownership and fresh genuine post-restart owner binding
AND accepted-run acknowledgements; old510/515 acknowledgements cannot be reused.
No owner predicate, cancellation, settlement or budget exception is granted.
575/588/592 remain by reference;553 owns the sole SAME510 continuation and497
retains its later scheduler gates. **595 MUST NOT APPLY from this review.**
