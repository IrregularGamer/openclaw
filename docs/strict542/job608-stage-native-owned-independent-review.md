# Independent corrected-freeze native outcome review608

**VERDICT: APPROVE ACTUAL NATIVE-STAGE EVIDENCE ONLY.** No material finding.
Reviewer: Rook `/root/review_current_inventory`, 2026-10-28 UTC.
Exact reviewed commit `6336e306fea0c8283dc2f29156f02b7e71180fb8`, compared with
`dfb8ea82ee7a3381e73d583815500b1f5cde2bf6`. All nine changed evidence files
are committed-byte-identical to the working files. Verification JSON SHA256:
`747317616ed356b126263716121017b1b9f115d6a95e4128e75f3d1b2f6b957e`.

Independently streamed SHA256 over ALL TEN returned regular files beneath
`tmp/export608-stage-native-owned-next/result608-native`; the exact file set,
all digests and duplicate receipt/addon bytes match verification.json. There
are no additional file or symlink entries. Both 24,303,312-byte addon copies
hash to `0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042`.
The freshly rebuilt compile receipt is byte-identical to its independent
manifest input, SHA256
`4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e`.
The carried libtests receipt is byte-identical to its independent manifest
input, SHA256
`2f81179f5d1bf14d1519cf446935a3cd783da0e28e79a69067c85e5f873dd946`.
Every receipt owner_inputs hash independently matches its frozen Git source;
shared source/toolchain/patched-source/policy fields agree.

The committed manifest equals the retained launch manifest, SHA256
`708a52c26402db1b4b030c0a0a64a91911fb6dd15d9798ade2e12b091c2f9e2e`.
The actual native stage receipt has SHA256
`f40df3a579bd600c154b14ad9d9ac863b5ab26381f8615aa54d0829c0ea05069`.
Its source, common export, run ID, manifest, empty stage-input set and all three
output digests agree exactly with the actual export and verification JSON:
source `5f7d810b7f254e4f06dbf7761b557ba90bf1a2b0`, common export
`76b4b47a0e5c3e0a157f75ff1b76d60753c8acdbf5f76bc495668dd985d70f64`, run
`stage608-native-next`, native stage and exit0. Actual result exit-code.txt and
`runs/608/stage-native-owned-offload.rc` both contain0. The raw offload log ends
with STEP608 native-rebuild-pass. The zero rc is separately recorded producer
terminal evidence, not a claim that this log contains a terminal rc line.

All four committed gzip files match their compressed digests. Expanded bytes,
SHA256 and lengths match the corresponding actual returned or raw offload files:
compaction10,053 bytes, offload2,119, rebuild26,495 and retention-negative1,897.
I inspected the real logs: the fresh run passes seven lifetime tests and two
rolldown_ecmascript tests, including the named compaction regression. The retained
AST negative control deliberately fails three of the same lifetime assertions
while four pass. This is the expected detection of old retain-through-codegen
behavior; it is not an unresolved implementation failure. The actual compile
owner requires its nonzero exit and named failing assertions, then records
retention_negative_detected=true. The fresh release addon build completes, and
both compaction_tests_exit and lifetime_tests_exit are0.

Important scope distinction confirmed against prepare-native-consumer608.py
and build-native608.py: this native stage rebuilds the compile artifact from
source and compares exact compile-receipt/addon bytes. It validates the separately
accepted native libtests receipt and copies that exact receipt after matching
the rebuild. It does NOT rerun the full historical rolldown native library suite
in this stage. The carried native_lib_tests_exit0 field remains its earlier
reviewed, source/toolchain-identical receipt evidence. No new claim of112 fresh
library tests, gateway checks, IPC refusal/cancellation tests, declaration
compiler success or completed package is supported by this outcome.

Fresh bounded checks above and `git diff --check dfb8ea82 6336e306` passed.
No heavy test/build, offload launch, source archive rehash, export edit,
root/runtime/config/service/scheduler/seal operation or provider call ran in this
review. No independent live remote metadata/CPU profile or full raw-archive
secret scan was performed. The earlier exact source/preflight review still owns
those limits. This evidence establishes the successful current native stage and
deterministic native artifact match, not whole-gateway reproducibility.

Current checks/compiler/runtime/unified0..5/middle/sdk0..1/tail/package stages and
full required realistic IPC/refusal/cancellation evidence remain required.
Exact final artifact/tree/action/source/privilege/original-and-next-seal reviews,
authentic automatic queue review, backups/rollback, and finite foreground
NONQUEUE HQ natural-gap execution remain outstanding. Native peer PID/start/
cgroup/MainPID predicates and cancellation/settlement stay unchanged. Fresh
post-restart genuine owner binding AND accepted-run acknowledgements remain
mandatory. Old frozen2b receipts cannot be relabelled. The corrected ordered HQ
handoff and575/588/592 by-reference,553 sole SAME510 and497 scheduler gates remain
intact. **595 MUST NOT APPLY from this native-stage review.**
