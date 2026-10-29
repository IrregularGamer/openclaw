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
job608-package-mode-fix-independent-review.md. Do not use the fix until that review ends `VERDICT: APPROVE`.

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
