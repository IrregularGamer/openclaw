# Job608 continuation after package mode refusal — 595 MUST NOT APPLY

Supersedes the NEXT pointer of job608-after-tail-tsccwdf6a4-continuation.md. All earlier gates, caps and
reviews still apply unless stated here.

## What happened
Package tsccwdf6a4 (manifest 9064b9ea) ran once and is SPENT: rc2, application598 tree refused
`CHANGELOG.md` as group-writable (evidence d5eff2b7). Root cause: git-archive 0664/0775 modes were kept
by tar on the remote, so the source tree, every accepted tsccwdf6a4 checkpoint (tail holds 1003 0664 files)
and the deployed runtime are group-writable. The check is correct and stays unchanged.

Source-only fix 674840b6: run-stage608.sh extracts source/successor/native with `umask 022` and
`tar --no-same-permissions` (test_stage608 17/17, also as root). Independent review:
job608-package-mode-fix-independent-review.md: independent APPROVE 017cd166 (root-mode flag also exercised by running test_stage608 as root, 17/17). Fix commit C = 674840b6.

## Consequence
The runner comes from the export commit, so source_export_sha256 changes and stage608.verify_inputs refuses every
tsccwdf6a4 receipt. All accepted tsccwdf6a4 stages are SUPERSEDED as package inputs (their evidence stays).
Never replay them, never hand-edit receipts/manifests, never chmod a result to pass.

## NEXT (fresh workers, one launch each, FIRST heavy action, >=2655s left)
Rerun the full DAG at the reviewed fix commit C (674840b6 or the reviewed successor), in dependency order:
native -> checks, compiler, runtime -> unified-0..5 -> middle -> sdk-0, sdk-1 -> tail -> package.
For each stage: prepare-stage608-export.py --base P/stage-unified-0-tsccwdf6a4 --commit C --stage S
--input <accepted results of the new run only> --dest P/stage-S-<new tag>; storage608 check (quarantine
superseded tsccwdf6a4 stages with `mv -n` as before if room is short; never raise a cap), verify-inputs0, sh -n0,
manifest pin, independent preflight APPROVE, ONE offload with the same per-stage --mem/--cpus/--timeout as
its tsccwdf6a4 launch doc, evidence commit, independent acceptance. Before acceptance of each build stage,
additionally list its checkpoint (`tar -tvzf`, never extract) and require zero group/other-writable entries.
After package: final artifact receipt + old/new hash inventory, action/privilege/seal/reseal reviews,
automatic queue review, genuine ordered HQ595 handoff. 587 fd3/socket transport replaces 586 sudo; never add
the 586 rule. Do not `git pull` source552 in a worker. 595 MUST NOT APPLY.

## Progress (tag m674, C = 674840b6)
- native m674: rc0 (evidence 53bda0a0), addon 0b6607e7 (identical to tsccwdf6a4), 0 group/other-writable,
  preflight APPROVE 6049ed36, independent ACCEPT 5a412599. Accepted input: P/stage-native-m674/result608-native.
- checks m674: rc0 (evidence df554bc5; offload runs.log rc=0 811s, client rc file not captured because the wrapping
  bash was killed to dodge the harness 600s background limit, disclosed), 14/14 checks, 0 group/other-writable,
  stage_inputs {} (STAGES['checks']=[]: do NOT pass --input for checks), preflight APPROVE 2e9a908c,
  independent ACCEPT 52c178f7. Accepted input: P/stage-checks-m674/result608-checks.
- compiler m674: rc0 (evidence 17c0ea58; foreground, offload.rc 0, 245s), tests pass 0 fail, 0 group/other-writable,
  preflight APPROVE 8566c2b9, independent ACCEPT 61e3dd9e. Accepted input: P/stage-compiler-m674/result608-compiler.
- runtime m674: rc0 (evidence ee84e508; background Bash 2800s, offload.rc 0, build +726s, runtime-pass),
  checkpoint 6178cfd9 8959 entries 0 group/other-writable, preflight APPROVE 4b777a33, independent ACCEPT 388d36b8.
  Accepted input: P/stage-runtime-m674/result608-runtime.
- unified-0 m674: rc0 (evidence 93a37171; background Bash 2800s, offload.rc 0, build +430s, unified-0-pass),
  checkpoint b22eb141 9 entries 0 group/other-writable, preflight APPROVE 639aa75c, independent ACCEPT f30faed4.
  Accepted input: P/stage-unified-0-m674/result608-unified-0.
- unified-1 m674: rc0 (evidence 514da3ba; background Bash 2800s, offload.rc 0, build +443s, unified-1-pass),
  checkpoint 4208af9f 29 entries 0 group/other-writable, preflight 14e9d421 APPROVE 12e8caac, independent ACCEPT c13d0b6a.
  Accepted input: P/stage-unified-1-m674/result608-unified-1.
- unified-2 m674: rc0 (evidence b737aff1; background Bash 2800s, offload.rc 0, build +425s, unified-2-pass),
  checkpoint de6fd118 36 entries (same name set as tsccwdf6a4) 0 group/other-writable, preflight c8aef54b APPROVE c10b2716,
  independent ACCEPT 36fcdcbe. Accepted input: P/stage-unified-2-m674/result608-unified-2. prepare-stage608-export.py left an
  unmanifested stage608 __pycache__ in the export (import side effect); trash it before gates and rerun verify-inputs.
- unified-3 m674: rc0 (evidence 988c5eb7; background Bash 2800s, offload.rc 0, build +445s, unified-3-pass),
  checkpoint b5b3a5b1 30 entries 0 writable, independent ACCEPT 400a1eac. Accepted input: P/stage-unified-3-m674/result608-unified-3.
  `trash` was not on PATH in this worker and gio cannot trash on /srv/encrypted: move the import __pycache__ with
  `mv -n` to P/trash-608/<stage>-pycache and rerun verify-inputs with `python3 -I -B`.
- unified-4 m674: rc0 (evidence 3471cde6; background Bash 2800s, offload.rc 0, build +419s, unified-4-pass),
  checkpoint bebc68d0 32 entries (same name set as tsccwdf6a4) 0 writable, preflight 783031cf APPROVE f48fb963,
  independent ACCEPT 0302c32f. Accepted input: P/stage-unified-4-m674/result608-unified-4.
- unified-5 m674: rc0 (evidence bc6f1ce2/70290de4; background Bash 2800s, offload.rc 0, build +423s, unified-5-pass),
  checkpoint 737515b7 25 entries (same name set as tsccwdf6a4 unified-5r1) 0 writable, preflight 68ea86a5 APPROVE a699cf94,
  independent ACCEPT 1c9da566. Accepted input: P/stage-unified-5-m674/result608-unified-5.
- NEXT fresh worker, FIRST heavy action: middle m674 (prepare, gates, independent preflight, ONE launch) with
  `--base P/stage-unified-0-tsccwdf6a4 --commit 674840b6 --stage middle --input P/stage-native-m674/result608-native
  --input P/stage-runtime-m674/result608-runtime --input P/stage-unified-N-m674/result608-unified-N (N=0..5)`
  (STAGES['middle'] = native, runtime, unified-0..5), --dest P/stage-middle-m674, same caps as middle tsccwdf6a4
  (--timeout 2460 --mem 14g --cpus 4, timeout -k 15s 2400s; never raise), all gates above,
  one launch per worker; then sdk-0, sdk-1, tail, package. verify-inputs: `cd stage && python3 -I -B stage608.py verify-inputs`;
  storage: `python3 -I -B docs/strict542/storage608.py check --root P --stage middle`.
  Worker harness: give the Bash call running `offload run` a timeout >= offload --timeout + 300s (ms), or run it in
  the foreground with timeout 600000 only if --timeout <= 420; the background default kills at 600s.
  storage608.py needs `check --root P --stage S`. Gates+launch in one background Bash took ~5 min before admission.
  prepare-stage608-export.py took ~3-4 min here; start it immediately so the >=2655s gate still holds at launch.
