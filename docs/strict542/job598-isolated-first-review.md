# Independent first isolation outcome and corrected source review

Reviewer: Rook `/root/build_analysis`, 2026-10-25 UTC.
Actual source export: `fe56d16f85a45edc667eb8649ce345a3279b34e5`.
Evidence commits: `476634e7` and `56fec406c9feeebb7c71fc0da92ff749342627e8`.
Exact corrected source reviewed: `56fec406c9feeebb7c71fc0da92ff749342627e8`.

Verdict: **APPROVE ACTUAL EVIDENCE and CORRECTED SOURCE for one admitted
corrected diagnostic only**. No build/artifact/application authority follows.

Independently parsed exactly184 passing checks: Node101+9, Python15+18+13+19+9;
both Node summaries have fail0 and all five Python summaries are OK. Stored
tests, test evidence, probe log and probe receipt are byte-identical to actual
recovered `runs/598/isolated-final` files. Independently compared the offload log
with `runs/598/isolated-probe-run.log`: identical. SHA256 values:

- tests: `6780aacb1787c7041907d1bfc441c9ac207cb4743b0bda5dd5aa94381f810ea7`
- test evidence: `2e1493e3c2497f133410e1ec84af58e6ad743cf08d18d8183f1f90d9331ef114`
- probe log: `4c7be283f3ac307dd7a1f96303d9b4fdbf09579844f2784939423afc74773314`
- probe receipt: `d596afa0cac1b95bc72a3adc2215fcc70807591e88ac52a4f73bf1c0e06a355f`

Test evidence binds sourcefe56d16f and the matching test-log hash. The committed
export manifest has that same source and runner digest
`d7edf5f7d4ec60451719c832a29b0b28b94fd1ecb4a65151bb469099a364f878`,
independently matched to the reviewed runner bytes. Base/native archive hashes
are unchanged from the previously independently reviewed export; this review
relies on that prior exact archive evidence. Fresh independent large-archive
rehashing did not complete under local IO contention and is not claimed here.
Actual successor payload parity must continue to be verified when exporting the
corrected committed source; the old manifest does not represent that successor.

The actual receipt contains57 main configurations. AI finished status0 in3318ms;
main-config0 finished status1 in1632ms, with timedOut false. The log reports
UNRESOLVED_ENTRY for agent-core entry paths, then owning-wrapper observation
`dead` with process-group scope. Final recovered exit code is1. This is a short
entry-resolution defect, not evidence of resource exhaustion, full graph
compilation, successful isolation, or2GiB feasibility. Kernel samples are
intermediate diagnostic observations and cannot prove a full-build peak.

The earlier independent source review incorrectly assumed config cwd remained
the source root. I missed tsdown's config-directory resolution behavior; the
actual compiler entry point disproved that assumption. This correction belongs
in this receipt alongside that superseded claim, rather than waiving the failure.

Reviewed exact minimal executable diff: move the diagnostic config from
`docs/strict542/isolated-config598.mts` to root
`tsdown.isolated598.config.ts`, update its two imports, and select that root path
from the probe. The wrapper now shares the original tsdown.config.ts directory,
preserving default-root semantics without a root override or changes to entries,
options, output roots, graph boundaries, census, budget, scanners or cancellation.
No stale executable reference to the removed config remains. Historical logs
properly retain its former path. Other changes preserve the observed outcome and
update the existing HQ handoff; no normal heap admission or runtime policy changed.

Independently reran the nine lightweight selector/refusal tests: all passed.
The real entry-resolution failure supplies a concrete implementation correction,
so one corrected fresh committed secretless admitted offload run is justified.
This is not an unchanged diagnostic retry. Its full relevant checks and actual
per-config outcome still require independent evidence review. All original
full-build/artifact/action/privilege/seal/automatic queue review and job595 gates,
including fresh genuine post-restart HQ ownership acknowledgements, remain open.
