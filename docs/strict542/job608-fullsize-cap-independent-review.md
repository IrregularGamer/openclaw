# Independent source-policy correction and failure review

Reviewer: Rook /root/fullsize_preflight_review, separate from implementation.
Exact fix5aff81feb4098654ce07e7ff09e336119770be85 against6cc4416b.
VERDICT: APPROVE SOURCE ONLY. This is the S1902/1905 fixed-cap correction,
not an artifact/action/privilege/seal/application/automatic queue approval.

Independently inspected actual unified0-fullsize1a39a log4433B:
c2e43cbe89f88d4e9ccb2545f83868cf5921ce383ec668fd9682d43d7ea85794.
Actual client rc1; native-start+10s, restore+18s, buildstart+21s, fail1+88s.
The old boundedPackage capacityBytes>4GiB guard refused before compilation.
No builddone/pass/result/receipt/checkpoint. ACCEPT FAILURE ONLY; attempt spent.
Earlier preflight missed this app-level rejection; its source-lineage reasoning
remains valid, but that larger-lease command could not pass admission.

Exact production diff removes ONLY the obsolete upper rejection plus stale
wording/comment. readProcessMemoryCapacity still resolves effective observed
kernel cgroup/high/host authority. Unresolved/nonfinite/nonpositive capacity,
nonfinite limit, limit>capacity, and limit<=1625784320 all still refuse.
Every inherited compiler/environment control refusal remains. No scheduler,
worker count, native predicate, config/semantic check, timeout, privilege,
cancellation or settlement behavior changes. The broker remains the owner of
live90%MemTotal/CPU lease admission. A replacement app numeric cap is unnecessary
and would conflict with S1902/1905. No budget or installed code was changed.

Committed RED isolates the old rejection; independent fresh
node --test docs/strict542/bounded-package608.test.mjs passed7/7 with zero
failed/cancelled/skipped/todo, and git diff --check passed. Tests explicitly
accept4GiB+1/8GiB/14GiB but retain floor/unknown/limit/env refusals.
New executable freeze5aff81fe/common requires freshchecks/native/runtime and
all later affected stages. Historical a39a receipts are never relabelled.

Checks wrapper amendment approved in principle: offload1200s/inner1140s at14g/
4CPU retains ALL original suites/case limits. Only stricter external termination
changes. Requires NEW exact export/pins and independent preflight review,
health/storage/inputs and>=1395s worker plus transfer allowance before launch.
Native original2460s needs a fresh worker if2460+195 cannot fit. Never accept
partial/failed output or use a shorter wrapper to waive a test.
