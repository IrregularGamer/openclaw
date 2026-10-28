# Independent exact native admission correction review608

Verdict: APPROVE SOURCE CORRECTION AND FOCUSED COMPOSITION EVIDENCE ONLY.
Reviewed commits afb1cbe6db2aac94a2b3ae55e4fa2183c55b8ceb and
3c0901de7c50e089e5aaa947dca8bba193886404, based on source review9db02e9e.
The actual emitter correction exists in3c0901de; afb1cbe6 contains the fixture,
test integration and evidence inventory. The earlier afb1cbe6 commit message
alone must not be taken as evidence that its emitter already changed.

The complete production source change is the filesystem callback argument in
`scripts/lib/native-declaration-emitter.mts`: raw `assertInput` replaces the
composed `admit`; explanatory comments were added. Source inspection confirms
the filesystem still performs lexical rejection and its own fresh physical
`boundary.assert` before invoking the arbitrary caller callback. The redundant
second internal physical assertion is removed. No property of the custom
callback is assumed, and no custom call is removed for a successful admission.
`before.readText` and the snapshot's composed `admit` remain unchanged, retaining
pinned byte reads and separate snapshot admission. The realpath result check,
symlink enumeration checks, deferred original error reporting, source input
membership and virtual-config behavior remain in the real filesystem module.

No source/config/tool roots, compiler diagnostic queries, emit flags, API close,
seal or produced-file exceptions change. The writer's group selection,
checkpoints, joined compiler ownership, publication, cancellation and existing
memory/deadline gates remain unchanged. This is not a declaration owner split
or an authorization to use partial compiler work.

I independently ran `node --test docs/strict542/native-admission608.test.mjs`
with Node v24.21.0:7 tests passed,0 failed,0 skipped,2848.415782ms. Before
accepting that result I confirmed that the actual working emitter, filesystem,
boundary, fixture, test and runner bytes matched exact3c0901de. The fixture uses
the REAL emitter, filesystem and boundary; module hooks supply tiny API,
snapshot, diagnostics and toolchain doubles. Each case runs in a separate child
with a15second timeout and1MiB output bound; temporary state and hooks are
cleaned up. The patch adds this test to the canonical run-stage608 checks list.
`bash -n docs/strict542/run-stage608.sh` and
`git diff --check 9db02e9e 3c0901de` passed independently.

The seven cases adequately isolate the narrow composition change:

* Two repeated fileExists calls with an identity caller policy cause two caller
  invocations and two physical boundary assertions. This proves both continued
  per-callback policy and removal of the duplicate INTERNAL assertion; it is not
  a test of the production caller's additional physical assertion.
* Identity-policy symlink escape tests cover readFile, fileExists,
  directoryExists, realpath and enumeration, with the original boundary error
  surfaced after the simulated native request returns.
* A custom denial on a physically local file is still honored and deferred.
* Positive symlink retarget and a missing lookup followed by directory-symlink
  retarget both reject on the later lookup, covering absent admission caches.
* A supplied pinned reader returns captured bytes, successful-read membership
  includes the probe, and a virtual config remains outside input membership.
* A lexical outside path pointing back inside remains absent.

The snapshot double intentionally checks only that emitter/filesystem wiring
retains the supplied reader and membership. It does not implement byte identity,
config/tool/topology capture or the real seal. The API double intentionally
checks only callback behavior, not real transport scheduling, config semantics,
source discovery, ambient roots, diagnostic correctness, cancellation or native
emission. Those limits are explicit in the fixture and correction inventory;
the focused test does not substitute for the previously identified actual
native compiler/snapshot/tsdown suites under their admitted resource owner.

All inventory SHA256 values were independently checked against git blobs:
the changed emitter is
2f8a05d0b713daf4d60d4e0359efe677b8f2710b05b1fd594e401adf1a3a2431,
and both baseline hashes plus all four new-file hashes in
`job608-native-admission-correction.json` match. The committed compressed RED
log SHA256 is
bc4818297d4c7a6086e262ce9125239f098cb8143fb046f504df8ab451ba0512;
the GREEN log SHA256 is
d3348ad388679a6b224fa6e918baef7b1c26a0be7d469d4c9a02f06cac8ad2fa.
I decompressed and read both. RED contains precisely the expected lookup
assertion failure4 versus2, with the other six cases passing; GREEN contains
seven passes. I independently reran GREEN only and did not restore or edit the
old emitter to reproduce RED.

No change-request findings were identified in this narrow correction. No full
compiler suite, offload, build, runtime mutation or publication was performed
for this review. No timeout resolution or total speedup is established. The
currently running diagnostic belongs to frozen source1bed4d1b and cannot serve
as a receipt for these changed bytes. New affected acceptance receipts and the
full required checks remain outstanding under the original owner/gates. All
original final source/action/privilege/seal/automatic-queue/HQ and post-restart
genuine owner/ack gates remain;595 MUST NOT APPLY.
