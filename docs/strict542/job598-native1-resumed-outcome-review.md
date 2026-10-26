# Independent fixed-pool timeout, settlement and successor-input review

Reviewer: Rook `/root/outcome_review`, 2026-10-26 UTC.
Exact evidence: `0590c77d197be6841d66242527da5525f96696f9`.
Verdict: **APPROVE ACTUAL OUTCOME AND NORMAL CLEANUP EVIDENCE ONLY**.

Independently compared committed offload stdout, probe log/receipt, test log/
receipt and post-run snapshot to actual runs/598/isolated-probe-native1-resumed-run.log,
native1-resumed-final and native1-resumed-post-run.json. All six files are
byte-identical and every SHA256 matches the committed outcome. The seventh
bound file, resumed export manifest, matches its outcome hash and the previously
reviewed exact8ce export manifest byte-for-byte. Prior94275bea independently
reviewed actual186 passing tests and retained successor/runner input parity.

Actual receipt contains16 completed compiler results: AI plus main-config0..14,
all status0, no timeout, warning marker or unresolved-import failure. Config15
has timedOut:true, signal SIGTERM and elapsed869757.063ms. Actual log starts it
with869459ms remaining, then records timeout869459ms and observedProcessState:dead,
observationScope:process-group. Actual diagnostic exit-code.txt is1. Thus native
pools1 propagated but did not complete the unified runtime graph; no complete
compiler/build/artifact success follows. Receipt remains explicitly diagnostic.

The actual post-run inventory reports zero managed running containers and
source/native-source/.pnpm-store all absent. Only original export inputs and
result598 remain in the managed slot. This is evidence of normal runner trap
cleanup and observed settlement, not a claim that the reviewer inspected live
remote process state independently of the preserved read-only snapshot. The
reviewer launched no compiler, service, cleanup operation or offload command.

Separately independently inspected the unsubmitted source-only allocator
successor runs/598/allocator-successor.tar and allocator-export-manifest.json.
Manifest source is `6305e30c888a019d64b9e6a38b35848637ece034`; archive SHA256 is
`b599e23a32ae96f7cd3ab5356d6e24cf8ffb06fd8f1afb148e70bb767872be57`.
All69 regular-file paths match both manifest and gitdiff basec790ba44→6305e30c;
every payload byte matches exact6305 committed source. Remaining members are
ordinary parent directories. Base/native/runner pins match the unchanged
reviewed retained inputs. This verification made no active-export changes.

Conditional next step: after preserving this settled outcome and ordinary
placement/lease/scanner/resource reconciliation, replace only the now-idle same
slot's small successor archive and manifest with these verified6305 inputs and
submit ONE normally admitted diagnostic using the unchanged reviewed runner.
Source6305 includes independently reviewed allocator policy1c27e206; no unchanged
8ce repeat, concurrent slot, bypass, larger deadline/heap or policy/unit change.
Future admission refusal or unknown completion requires ordinary reconciliation.
No empirical allocator-capacity claim is made before its actual finite outcome.

Complete owning build/profile/UI/postbuild/package checks, deterministic artifact
receipt, independent action/privilege/original-seal review, automatic598 queue
review and all595 application and fresh genuine post-restart nonqueue HQ owner/
accepted-run acknowledgement gates remain. This grants no installation, release
or scheduler-request authority and preserves the narrow existing release scope.
