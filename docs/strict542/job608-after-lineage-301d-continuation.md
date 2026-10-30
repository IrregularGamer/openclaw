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
