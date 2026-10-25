# Independent fixed-pool placement-refusal and retained-export review

Reviewer: Rook `/root/build_analysis`, 2026-10-25 UTC.
Exact reviewed evidence: `a31958c4eacb5d6182c75995e74c31684ab5f30b`.
Verdict: **APPROVE REFUSAL AND RESUME EVIDENCE ONLY**. No new test/compiler,
feasibility, complete build/artifact, application or release approval follows.

Independently compared the committed refusal with actual
`runs/598/isolated-probe-native1-run.log`: byte-identical. Its SHA256 is
`22161e9e85b5020a1461901544be9df2586cd01252cfa62636f2c0c783b0075b`,
matching the committed outcome. The actual JSON records placement_blocked,
local_execution:false and retry_requires_reconciliation:true; recorded exit75
is consistent with that refusal. The evidence correctly states no transfer,
tests or compiler started on this attempt.

Independently inspected the installed local offload owner's cmd_run ordering:
normal remote admission precedes the healthy/relative-cwd placement check,
which returns placement_blocked before push_tree and the remote run call. Thus
this exact refusal supplies no new remote186-check or compilation evidence.
It also does not identify which placement condition failed. Later cached
health cannot establish the cause or retroactively prove admission. No retry,
bypass, local compiler or new slot was launched by this reviewer.

The committed native1 export manifest matches the actual retained
`tmp/export598-config-isolation/export-manifest.json`. It binds source
`8ce523c01d7299d516dfd3bf05882b9a75567370`, basec790ba44 and the unchanged
previously reviewed base/native archive digests. This review relies on prior
exact large-archive evidence; it does not claim fresh base/native rehashing.

Independently hashed the retained small successor archive:
`697e339cf97a9917a1e330147a177d22422612be48d293ec1ce3b8a62092c92e`.
All57 regular-file paths match the manifest and every payload matches its exact
committed source8ce523c0 bytes. The only other archive members are four ordinary
parent directories; no unexpected link/device member exists. This includes the
reviewed36940dd8 fixed-pool implementation, not merely the old base archive.
The retained runner SHA256 is
`4ddaa154badc56d2c8f1fc62def549fa52e9e8e7e7383000cb5793dc95a4c037`;
its bytes match both manifest and source8ce523c0 run-isolated598.sh exactly.

The supported resume remains one normally admitted command from that retained
same-slot export, after placement reconciliation and ordinary lease/scanner/
resource checks: `offload run --artifacts result598 -- sh run598.sh`.
No direct retry loop, new slot, deadline/heap increase, installed policy change
or local fallback is approved. Preserve actual refusal and prior settled outcome
receipts; unknown future workspace/admission state requires reconciliation.

The prior184 remote checks apply to6d7ecc59. The11 local policy tests and exact
independent source review74da218e certify source preparation only. A later
admitted186-check run, actual fixed-pool behavior and complete config outcome
remain unproven. Complete owning build/profile/declaration/postbuild/package,
deterministic artifact, independent action/privilege/seal review, automatic598
queue review and every595 application and fresh genuine HQ ownership gate remain
open. The recorded soft dependencies and narrow release approval do not waive
those requirements or grant installation authority.
