# Job608 continuation after Option B input lineage 301d7456 — 595 MUST NOT APPLY

Supersedes the NEXT pointer of job608-after-package-m674c-binding-continuation.md. All earlier gates, caps, reviews apply.

## Done (worker ending 05:52Z, 2026-10-30)
- Decision662 Option B implemented source-only in 301d7456: `prepare-stage608-export.py --lineage-ancestor A`
  (package only; A must be a strict ancestor via `git merge-base --is-ancestor`; every A..C path must be in
  stage608.LINEAGE_ALLOWED_PATHS or `docs/strict542/job608-*` evidence; only native/compiler/tail may use it; checks
  never). Record `input_lineage` in the manifest and in the stage receipt; stage608.verify_inputs enforces it remotely.
  Default (no flag) exact same-commit binding unchanged. 31 local tests OK. Independent APPROVE 7beaf342.
- Reviewer process caveat (binding for every lineage preflight): state that the recorded changed paths touch no
  producer-side logic (frozen-package608.py preflight, stage608.py archive_build/stage_native/restore). For
  674840b6..301d7456: frozen-package608.py only adds materialize; stage608.py only adds lineage checks.
- checks rerun at 301d7456 (it runs the changed tests): P/stage-checks-301d, manifest 1a5d47a7, export 99add7e1,
  preflight 0edf2b6c, independent APPROVE 80a15857/0cb20a15, ONE launch. Result: see evidence job608-checks-301d/.

## NEXT (fresh worker; one launch per worker)
1. If checks 301d not yet accepted: independent acceptance (14 checks, 0 group/other-writable, nlink 1). If rc!=0,
   diagnose from evidence; never relaunch unchanged.
2. Prepare: `prepare-stage608-export.py --base P/stage-unified-0-tsccwdf6a4 --commit 301d7456 --stage package
   --lineage-ancestor 674840b6 --input P/stage-native-m674/result608-native --input P/stage-compiler-m674/result608-compiler --input P/stage-tail-m674/result608-tail
   --input P/stage-checks-301d/result608-checks --dest P/stage-package-301d`. Inputs = the same accepted m674 result
   dirs the m674c attempt used (see job608-after-package-m674b-hardlink-continuation.md). Remove the __pycache__
   prepare's import writes inside dest before gates. Gates: verify-inputs 0, sh -n 0, storage608 check package,
   free reserve. If storage refuses: per Decision662 pin manifests then delete own spent stage-package-m674,
   stage-package-m674b; never lower the reserve.
3. Preflight json (include input_lineage + caveat statement), independent preflight review, ONE package launch
   14g/4CPU/2460s (needs >=2655s left), evidence, independent acceptance.
4. Then final artifact receipt + old/new hash inventory, action/privilege/seal/reseal reviews, automatic queue review,
   ordered HQ595 handoff (fresh post-restart owner binding + accepted-run acks; 587 fd3 socket transport replaces 586
   sudo, never add the 586 rule).

## checks 301d result
rc 0 (evidence job608-checks-301d/ 8d368786), independent ACCEPT 788c76fc. NEXT starts at step 2 (prepare package 301d).

## package 301d (worker 05:20-06:20Z, 2026-10-30)
- Prepared P/stage-package-301d (manifest 025654bd, runner b04abd4d, helper 1d2bf411; lineage 674840b6). Storage
  first refused (12 MB short): pinned + deleted spent stage-package-m674/m674b (hardlinked, ~19 MB freed) and
  trash-608/stage-package-m674c-refused-prepare (19.8 MB); reserve unchanged. Gates 0; preflight 77350895,
  independent APPROVE 1fe9cdbc. ONE launch ~05:33Z (14g/4CPU/2460s); log/rc P/package-301d-offload.{log,rc}.
- NEXT: if rc file exists, record evidence (copy result608-package receipt + sha listing + modes) and get independent
  acceptance; if rc missing/worker killed, treat as completion_unknown: reconcile via `offload status`/runs.log,
  never relaunch unchanged on the same slug. Then step 4 above.

## package 301d RESULT (supersedes NEXT above)
ONE launch rc 1: `checkpoint source/native/toolchain identity mismatch` (gateway inner checkpoint identity is exact
commit+export; tail-m674 chain is bound to 674840b6/e1a6de35). Evidence + diagnosis: job608-package-301d/README.md (1b75fa38).
Option B lineage cannot bridge it without forging identity; do not relax validateBuildReceipt608.

## NEXT (fresh workers, one launch each)
Rebuild the identity chain at exact 301d7456 (same-commit, no --lineage-ancestor), in m674 order with m674 caps/argv:
native -> compiler -> sdk-0 -> sdk-1 -> unified-0..5 -> runtime -> middle -> tail; reuse checks-301d (ACCEPT 788c76fc,
exact 301d7456); then package (no lineage). Prepare pattern per stage: `prepare-stage608-export.py --base <same base the
m674 stage used> --commit 301d7456 --stage <s> [--input <accepted 301d predecessor results>] --dest P/stage-<s>-301d`
(take base/inputs from job608-<s>-m674-preflight.json; slugs <s>-301d). Each: gates, preflight json, independent
review, ONE launch, evidence, independent acceptance. Before each prepare, if storage refuses, pin manifests then delete
only own spent *-m674 stages superseded by an accepted *-301d result; never lower the reserve. Then step 4 (receipt,
hash inventory, action/privilege/seal reviews, queue review, ordered HQ595 handoff).

## native 301d (worker 05:40-06:40Z, 2026-10-30)
- Prepared P/stage-native-301d (manifest b61f89b5, exact 301d7456, no lineage, stage_inputs {}); gates 0
  (verify-inputs, sh -n, storage608 check native, pycache 0). Preflight 7c55092a, independent APPROVE a86f43a3.
- ONE launch 2026-10-30T05:48:56Z (14g/4CPU/2460s, ~3100s left); log/rc P/native-301d-offload.{log,rc}.
- NEXT: if rc exists, record evidence (job608-native-301d/: log.gz, rc, non-binary results, result-files.sha256,
  mode listing) + independent acceptance; if rc missing, completion_unknown: reconcile via offload status/runs.log,
  never relaunch unchanged on the same slug. Then compiler-301d (inputs: native-301d result), per NEXT above.
- RESULT: rc 0, addon 0b6607e7 (identical), 0 group/other-writable; evidence 7e81d22c, independent ACCEPT 66fc5a20.
  Accepted input: P/stage-native-301d/result608-native.
- NEXT (fresh worker): compiler-301d: prepare --base P/stage-unified-0-tsccwdf6a4 --commit 301d7456 --stage compiler
  --input P/stage-native-301d/result608-native --dest P/stage-compiler-301d (caps from job608-compiler-m674-preflight.json),
  gates, preflight, independent review, ONE launch, evidence, acceptance. Then sdk-0, sdk-1, unified-0..5, runtime, middle, tail, package.
- Worker note: never `git pull` source552 in a worker (it hangs); commit+push only.

## compiler 301d (worker 06:40-07:40Z, 2026-10-30)
- Prepared P/stage-compiler-301d (manifest d0af6061, exact 301d7456, no lineage, input native-301d result); gates 0. Preflight 04230866, independent APPROVE 493fe1ad.
- ONE launch 2026-10-30T06:47:51Z (14g/4CPU/600s); log/rc P/compiler-301d-offload.{log,rc}. If rc missing: completion_unknown, reconcile, never relaunch unchanged.
- compiler RESULT: rc 0 (STEP608 compiler-checks-pass; node tests 10/10 pass, same as m674), 0 group/other-writable;
  evidence 5326f131, independent ACCEPT 20e153c0. Accepted input: P/stage-compiler-301d/result608-compiler (package only).

## CORRECTED stage order (supersedes the order listed above; from the m674 preflight --input lists)
runtime(native) -> unified-0..5(native+runtime) -> middle(native+runtime+unified-0..5) -> sdk-0, sdk-1(native+middle)
-> tail(native+middle+sdk-0+sdk-1) -> package(native+checks-301d+compiler-301d+tail; no lineage). sdk cannot precede middle.

## runtime 301d PREPARED (not launched)
P/stage-runtime-301d manifest 7677269f, input native-301d, gates 0; preflight 4dd6fc6a, independent APPROVE 65462a6c.
NEXT (FIRST step of a fresh worker, needs >=2655s): re-run verify-inputs + storage608 check runtime + sha256 of
export-manifest.json (must still be 7677269f) then ONE launch with the preflight argv (14g/4CPU/2460s, inner 2400s),
log/rc P/runtime-301d-offload.{log,rc}; evidence + independent acceptance. Then unified-0..5 (caps from each
job608-unified-N-m674-preflight.json, inputs native-301d + runtime-301d), middle, sdk-0/1, tail, package, step 4.

## runtime 301d resume 2026-10-30T11:24:08Z (Rook)
Revalidated prepared manifest 7677269f, runner b04abd4d, helper 1d2bf411; verify-inputs/sh -n 0; no pycache. Storage check runtime 0 (4210499584 bytes free); offload up with no competing run. 3468s remained before worker deadline, exceeding 2655s. Preflight 4dd6fc6a and independent APPROVE 65462a6c unchanged. Launching the ONE reviewed runtime command; no installed/root/seal/service changes. Capture P/runtime-301d-offload.{log,rc}; next evidence and independent acceptance, then fresh-worker unified-0-301d.
