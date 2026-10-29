# Independent runtime fullsize5aff1 preflight

Reviewer: Rook /root/native_runtime_review, separate from preparation/execution.
Reviewed exact preflight/handoff commit90b0eb48, clarity update75f0441d and actual
private UNUSED export.
**VERDICT: APPROVE exact SOURCE-ONLY PREFLIGHT, subject to live admission.
595 MUST NOT APPLY.** No runtime has been launched or accepted by this review.

Verified independently:

- Export stage-runtime-fullsize5aff1 has exact manifest
  46f4f743157f10fa3b64b4256b179c5256b79f51632e17afb8c519b4311995ac;
  stage runtime, UNUSED, launch_history none, run_id stage608-runtime-fullsize5aff1,
  required_checks14, source/runner freeze5aff81feb4098654ce07e7ff09e336119770be85.
  Canonical identity JSON recomputes common export
  230f79f5b6f95826a02a15f1c5fdd9d1fbc5a7abd60064b33e3d1776af0f086d.
- Runner e2ed7e1337f5d0564b56e61174d0837440655cd38f75416608bff3de82780605
  and helper a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4
  match manifest and exact frozen committed bytes. Maintained preparer remains
  1e701de05d9ccdfccee532cfef8bcc93ba0fc8f9937caf86d689cfc3eda216f2.
- Streamed successor hash matches cfee3626edc6738c8db6cd7f5507a5d9a254e10c50ab1ef55a7d3666f2c582f6.
  Three common archives retain the accepted native export's same device/inodes
  395540/395541/395542 and exact preflight pins. Those previously reviewed large
  bytes were not redundantly rehashed. Existing synthetic-fixture/secretless
  carrier qualification remains applicable.
- Exactly four staged native inputs match accepted NEW native73351f27:
  producing receipt435ef3f26d1045eaca54ea9e8057737a812a5e279681e2c3bdd278f30fb62515,
  compile4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e,
  libtests2f81179f5d1bf14d1519cf446935a3cd783da0e28e79a69067c85e5f873dd946,
  addon0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042.
  Their bytes and device/inodes395959..395962 match the actual new producing
  result; link count3 includes the separately prepared compiler export.
  Both native608-stages JSON pins also match. No a39a producer is consumed.
- Exact13-file export inventory, no symlinks, __pycache__, runtime result or
  exact sibling runtime-fullsize5aff1 offload log/rc. Fresh independent
  `python3 -I -B stage608.py verify-inputs` exits0.
- Fresh independent storage check exits0:1502228311unique bytes,
  5822214144free,2147483648reserve,4294967296aggregate cap,
  134217728runtime return cap. Earlier preflight storage figures correctly
  describe preparation time; recheck live gates immediately before launch.

Approved command is exactly outer `offload run --timeout 2460 --mem 14g
--cpus 4 --artifacts result608-runtime -- timeout -k 15s 2400s sh run608.sh`,
with actual rc captured to the unique sibling rc file and output to the unique
log. S1902/1905 authorizes this placement. No broker/unit/budget change follows.
The unchanged runner bounds its build to2280s from stage start, with15s kill
grace and failure log tails; original checks, owners and lifetimes remain.

Launch ONLY as FIRST heavy action in a fresh worker after actual accepted
checks/native, this exact review, fresh healthup/storage0/inputs0, no competing
remote run and at least2655s remaining AFTER preflight; prefer2895s for observed
transfer. This worker cannot launch it. Historical free-text budget/producer
wording in the inherited manifest does not replace exact current preflight.
Clarity update75f0441d correctly distinguishes the accepted native result from
remaining runtime/package gates and labels superseded a39a/HQ headers historical.

Afterward require actual client/result0, complete exact manifest/source/common/
run/input/output receipt, safe complete runtime checkpoint inventory, all actual
compiler record statuses and full build log, result-storage0 and independent
acceptance before NEW unified-0 consumes native+runtime. Compiler execution
additionally requires actual independently accepted and settled NEW unified-0.
All remaining declaration/compiler/package, exact artifact/action/privilege/
whole-seal/automatic-review and genuine HQ595 gates remain open. An admitted
failure spends this attempt; preserve actual evidence and diagnose before a
changed attempt. Preadmission76 preserves UNUSED only without lease/transfer/
placement; ordinary clean75/95 and unknown-settlement reconciliation apply.
No replay, gate bypass, local heavy test/build, live provider or installed/root/
service/queue-state mutation was performed or authorized.
