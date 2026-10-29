# job608 independent review: checks preflight at singleThreaded freeze a46cd576

**VERDICT: APPROVE**

Reviewed: `job608-checks-singlethreaded-a46c-preflight.md` (commit 841ba12b) against
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-checks-singlethreaded-a46c`.
Read-only review by an independent reviewer that did not prepare the export. Nothing was
launched; no offload, build, preparer or export-writing command was run; the export was not modified.

This review grants no install, package, application or reseal authority. 595 MUST NOT APPLY.

## Findings

1. Hashes match the doc: export-manifest.json 5f6e0974...28013e4, run608.sh eb662d81...76644b01,
   stage608.py a558db9a...27c0de4. Manifest runner_sha256 / stage_helper_sha256 agree.
2. run608.sh is byte-identical to `git show a46cd576:docs/strict542/run-stage608.sh`, and
   stage608.py to `git show a46cd576:docs/strict542/stage608.py` (cmp, no differences).
3. Manifest fields: execution_state UNUSED, stage checks, stage_inputs {}, run_id
   stage608-checks-a46c, required_checks 14 (equal to admission95-next), source_commit and
   runner_commit both a46cd5765702f3b019d5a433b82d19ac57821a8d, source_export_sha256
   88279fe1...caded20d9e. Recomputed source_export_sha256 from the canonical identity
   (base_source_archive_sha256, source_commit, successor_archive_sha256) per
   prepare-stage608-export.py: matches.
4. Key set identical to ../stage-checks-admission95-next/export-manifest.json. Recursive diff
   yields exactly 7 differing values, all identity fields: source_commit, runner_commit,
   run_id, source_export_sha256, successor_archive_sha256, successor_paths,
   predecessor_package_attempt. required_checks, required_check_inventory, budget, base
   hashes, native receipts and all other fields are unchanged.
5. successor_paths: 710 vs 669; the 41 added paths equal exactly the files added in
   `git diff 95e62f8b a46cd576` (the 4 modified files were already listed); none removed.
   `git archive a46cd576 -- <successor_paths>` reproduces successor598.tar sha256
   dcc959c7...6bb303515, matching the manifest.
6. Base archives: source598.tar (inode 395540, not hashed), native598.tar (395541) and
   rolldown608-source.tar.gz (395542) are the same inodes as ../base. The two
   native608-stages receipt.json files are separate copies, byte-identical to ../base.
7. No .env, .db, key, .pem, result, __pycache__ or .pyc entries in the export.
8. Launch command is bounded: offload --timeout 2460 --mem 4g --cpus 1, inner
   `timeout -k 15s 2400s`, preceded by sha256sum, verify-inputs and `offload deadline`
   (requires >= 2655 s). The doc requires it to be the FIRST step of a fresh worker, only
   after this review. The target log/rc paths (../checks-singlethreaded-a46c-offload.{log,rc})
   do not exist yet, so there is no collision.
9. Non-blocking: manifest `purpose` says "stage native", inherited unchanged from
   admission95-next (prepare script only rewrites purpose for stage native). Neither run608.sh
   nor stage608.py reads `purpose`; stage selection uses `stage` = checks. Cosmetic only.

## Limits

- Did not run `stage608.py verify-inputs` or `storage608.py check`; the doc's exit-0 and
  free-space claims are taken as reported. Did not hash source598.tar (inode comparison only).
- Did not re-review run608.sh / stage608.py logic or the emitter itself; relied on the
  byte-identity to a46cd576 and the prior source-only APPROVE.
- Acceptance of any outcome still follows the candidate95 checks rules and needs its own review.
