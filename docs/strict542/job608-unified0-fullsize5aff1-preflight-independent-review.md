# Independent unified-0 fullsize5aff1 preflight

Reviewer: Rook /root/runtime_acceptance, separate from preparation/execution.
Reviewed exact preflight/handoff commit 903321e339cafbd21576416971242efb3d6fca08
and the actual private UNUSED export after runtime acceptance da0e733d.
**VERDICT: APPROVE exact SOURCE-ONLY PREFLIGHT, conditional on fresh live
admission in the next fresh worker. 595 MUST NOT APPLY.**

Independently verified:

- Export stage-unified-0-fullsize5aff1 has exact manifest
  912af4bc9ff88303a0a78765a16620b415f22e39984957adcfcb172b56b56468,
  stage unified-0, execution_state UNUSED, launch_history none,
  run_id stage608-unified-0-fullsize5aff1, required_checks 14 and executable
  source/runner freeze 5aff81feb4098654ce07e7ff09e336119770be85.
  Canonical identity JSON independently recomputes common export
  230f79f5b6f95826a02a15f1c5fdd9d1fbc5a7abd60064b33e3d1776af0f086d.
- Actual runner e2ed7e1337f5d0564b56e61174d0837440655cd38f75416608bff3de82780605
  and helper a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4
  match exact frozen committed bytes and preflight pins. The maintained
  preparer remains 1e701de05d9ccdfccee532cfef8bcc93ba0fc8f9937caf86d689cfc3eda216f2.
  Source review 6dd1e199 and inventory review 6035be0c remain applicable;
  evidence-only commits do not change the executable freeze.
- Streamed successor598.tar hashes to
  cfee3626edc6738c8db6cd7f5507a5d9a254e10c50ab1ef55a7d3666f2c582f6.
  All three large common archives have the exact accepted runtime manifest
  pins and retain the same device 64512 and inodes 395540/395541/395542 as
  that accepted export. Their previously reviewed bytes were not redundantly
  rehashed. The existing secretless/synthetic-fixture qualification is retained.
- Exactly seven stage inputs match actual independently accepted NEW native
  73351f27 and runtime da0e733d producers, including their hardlink identities:
  native inodes 395959..395962; runtime inodes 395998..396000, all device 64512.
  Every staged file was freshly streamed through SHA-256. Exact native pins:
  producing receipt 435ef3f26d1045eaca54ea9e8057737a812a5e279681e2c3bdd278f30fb62515,
  compile receipt 4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e,
  libtests receipt 2f81179f5d1bf14d1519cf446935a3cd783da0e28e79a69067c85e5f873dd946,
  addon 0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042.
  Exact runtime pins:
  producing receipt d41a3c6f9b404376f24b97e98f1be30d5ebf7d7ab46174d10156b9432cd5cefb,
  checkpoint 2a882adb41e4b9338f4b25aa591c528ab457e3bc94417062b5dbb400fae3f0fb,
  build log d893e900ae20456b5010b10191ad19d17fc04fa1462f312bdf773dfbbf142baf.
  All seven equal actual manifest and preflight pins. Both native608-stages
  JSON pins also match. No historical a39a producer is consumed. Accepted
  checks 9d1dfc33, native 73351f27 and runtime da0e733d are committed ancestors.
- Complete exact 16-file export inventory consists of manifest, runner, helper,
  four archives, two native608-stages receipts and seven stage608-inputs files.
  No extra files, symlinks, special entries, __pycache__, result directory or
  unique sibling unified-0-fullsize5aff1 offload log/rc exists.
- Fresh independent `python3 -I -B stage608.py verify-inputs` and
  `sh -n run608.sh` both exit 0. Fresh storage608.py check exits 0 with
  1606281752 unique bytes, 5718089728 free bytes, 2147483648 reserve,
  4294967296 aggregate cap and 33554432 unified-0 return cap. These agree
  with current preflight figures; launch still requires fresh live checks.

The exact approved command is
`offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-0 -- timeout -k 15s 2400s sh run608.sh`,
with actual output/rc captured to the unique sibling paths in the preflight.
S1902/1905 authorizes this placement; no broker/unit/budget change follows.
Historical descriptive budget/purpose/source-review text inherited by the
immutable manifest does not override the exact current stage, pins, accepted
predecessors or reviewed preflight.

Launch only as the FIRST heavy action in a fresh worker, after this exact
review, actual accepted checks/native/runtime, fresh health up, no competing
remote run, storage 0, inputs 0 and at least 2655 seconds remaining AFTER
preflight. Prefer at least 2895 seconds including observed transfer. The current
preparing worker cannot launch it. Preserve original check, owner, privilege,
lifetime and failure gates; never replay an admitted attempt.

This is preflight approval only. After execution require actual client/result 0,
exact manifest/source/common/run/seven-input/output receipts, safe complete
unified-0 checkpoint AND binding inventories, every actual compiler status,
full build log, storage result 0 within 32 MiB and independent acceptance of
committed evidence. Only actual independently ACCEPTED and settled NEW unified-0
unlocks compiler execution. Prepared compiler manifest 668db7e1 remains UNUSED
and conditionally gated; no compiler acceptance or launch is granted here.

An admitted failure is SPENT: retain actual evidence and diagnose before a
changed attempt. Preadmission 76 preserves UNUSED only without lease/transfer/
placement; clean 75/95 and unknown settlement follow documented reconciliation.
Remaining declaration/compiler/package, final artifact/action/privilege/whole
seal/actual automatic-review and genuine ordered HQ595 gates remain open.
No offload, heavy test/build, installed/root/service/provider/queue mutation,
commit or push was performed by this review.
