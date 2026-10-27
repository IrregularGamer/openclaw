# Independent combined4 diagnostic, post619 baseline and trusted native prerequisite review608

2026-10-27, job633. VERDICT: APPROVE all three exact prerequisite scopes only.
Not the automatic parent608 queue review. No action, privilege, seal, installation,
application or automatic608 approval exists or is implied.

Reviewed branch strict542-source552 at a166d515 (request handoff), exact outcome
commit 9a01dc9e, source preparation commits 123114cc, 6fefbf95 and dbb5f3c5.

## 1. Actual combined4 diagnostic (outcome 9a01dc9e)

- All ten artifact SHA256 entries in job608-combined4-outcome.json match the
  committed files. Receipt 09be7fd1, native receipt 4a651254, parity 56682414 and
  addon 0b6607e7 equal their actual counterparts under
  /home/deploy/agentq/runs/608/combined4-results byte-for-byte. Committed
  settlement equals runs/608/combined4-settlement.json (1368c5f6).
- All six .txt.gz files decompress to bytes whose SHA256 equals the outcome
  raw_log_identities entry and the actual source file (broker =
  combined4-actual-offload.log; probe/native-compile; compaction-tests,
  release-phase-trace, lifetime-retention-negative).
- Launch record binds frozen source d3925759, manifest 89fe92b2 (actual export
  export-manifest.json hashes 89fe92b2), export review e9dc7d11 and predecessor
  review 18dfbd0a. Actual exit-code.txt 0; outer timeout not hit.
- Receipt 09be7fd1: 58 results, labels exactly ai + main-config-0..56 in order,
  census indices 0..56. Every result status 0, signal null, timedOut false,
  error null, fatalUnresolvedImport null, hasIneffectiveDynamicImport false.
  No waiver/cancellation/scanner/deadline-override field exists; deadline 900000ms;
  capacity 4002062336/4294967296 resolved; inherited controls absent.
- Workers 46-49 each show begin/build-end/closed ISOLATED_CONFIG_DIAGNOSTIC
  phases and final status 0. d3925759 runWorkerPhases runs the bundle, then the
  fixed minifier only after a fully successful first phase, sequentially under one
  shared deadline; any failure propagates unchanged.
- 255 checks = 242 scoped (Node 101+35, Python 106 across ten unittest runs, all
  OK, evidence exit 0 at d3925759 with matching test-log hash) + 13 installed
  fixtures (vitest 3, Node 5x2 in probe.log), zero fail/cancelled/skipped.
- Native: 9 positive (7 lifetime + 2 compaction) in native-build log, compaction
  pair repeated in positive log; retention negative 4 pass/3 expected FAILED,
  retention_negative_detected true; receipt complete, exits 0. Paired libtest
  receipt in repo hashes 2f81179f. Parity has all 8 es/cjs x sourcemap x minify
  variants for addon 0b6607e7.
- Settlement: 0 managed containers, current worker lease only, runner lock
  available, slot entries only export-manifest.json/result598/run608.sh, no
  mutation. Recorded snapshot; not re-observed. Nothing was rerun or uploaded.

## 2. Post619 baseline proposal 1a0009c1 (123114cc)

Read-only sudo inspection at review time (verify script runs/633/verify_baseline633.py):
- Current seal hashes 5301d131; all 56 installed_hashes match live files.
- Backup /var/lib/agentq-safety/validation.json.bak-20261026T2153Z-continue
  hashes 7c404d1d; its 31 amendments are an exact prefix of current 37.
  Replaying the six appended old->new hashes from the backup mapping reproduces
  the current installed_hashes exactly. No other seal field differs from backup.
- Amendments 32-33 equal the prior reviewed reconciliation's new_amendments.
- Live control.py db4d2903, matching runs/622 HQ-RECEIPT (genuine 622 install).
- Seal metadata and all seven guard hashes/mode/uid/gid/mtime/ctime equal the
  proposal (no xattrs present); boot id unchanged; all six targets absent.
  Versus original 22253f35 only control.py guard (and seal) changed.
- Original 22253f35 (fceeb80e) and prior f3b3ced6 (26985d0b) unchanged since
  their commits. No further drift found; no refresh or waiver.

## 3. Trusted native environment (6fefbf95 + dbb5f3c5)

- 6fefbf95 adds the tests/docs; sparse checkout omitted the helper, which
  dbb5f3c5 adds (owner 10044854 -> c3670b0b). Review covers both together.
- trustedNativeCompilerEnvironment608 always calls nativeCompiler608 required
  mode (paired compile/libtest receipts, pin, owner sources, toolchain agreement,
  current addon hash). Parent mode refuses every NAPI_RS_ key, including empty or
  matching addon. Child mode (inherited===true only) permits solely
  NAPI_RS_NATIVE_LIBRARY_PATH equal to the freshly derived path; returns a new
  env object without mutating the caller; missing/changed bytes refuse, no stock
  fallback.
- TMPDIR=runs/633/unit-scratch node --test docs/strict542/native-compiler608.test.mjs:
  6/6 PASS.
- d3925759..a166d515 changes only this helper and its test outside job docs:
  the four native owner pins, build routes and 4352MiB guard are unchanged; no caller
  references the helper (UNWIRED). Frozen 255 checks ran d3925759's three tests;
  the three new ones ran only locally here. Full successor checks remain
  required in the future admitted package offload.

## Limits

608 may proceed with existing job608-package-promotion-plan.md. Full typed frozen
package, tree/action/next seal and final independent source/action/privilege/seal
plus automatic queue reviews remain. 595 stays gated on fresh post-restart genuine
HQ owner and accepted-run acknowledgements. 575/588 and 553 by reference only.
No root writes, installs, services, Docker, scheduler or production changes.
