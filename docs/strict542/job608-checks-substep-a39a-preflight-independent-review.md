# job608 independent review: checks preflight at substep-budget freeze a39ad5ee

**VERDICT: APPROVE**

Reviewed: `job608-checks-substep-a39a-preflight.md` (commit e5a8dbf9) against
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-checks-substep-a39a`.
Read-only review by an independent reviewer that did not prepare the export. Nothing was
launched; no offload, build, test, preparer or export-writing command was run. The only
command executed in the export was `python3 -I -B stage608.py verify-inputs`.

SOURCE ONLY; 595 MUST NOT APPLY. This review grants no install, package, application or
reseal authority.

## Findings

1. Recomputed sha256 matches the doc for all seven files: export-manifest.json 322e58a9...e907e892,
   run608.sh e2ed7e13...de82780605, stage608.py a558db9a...27c0de4, native598.tar d73e4e35...,
   rolldown608-source.tar.gz 203aa483..., source598.tar e79a0e45... (hashed in full this time),
   successor598.tar e44987e3...ed474. Manifest runner_sha256, stage_helper_sha256 and
   successor_archive_sha256 agree.
2. run608.sh is byte-identical to `git show a39ad5ee:docs/strict542/run-stage608.sh`, and
   stage608.py to `git show a39ad5ee:docs/strict542/stage608.py` (the path the committed
   preparer copies from); cmp, no differences. Committed preparer at a39ad5ee hashes to
   1e701de0..., as the doc states.
3. Manifest fields: execution_state UNUSED, stage checks, stage_inputs {}, run_id
   stage608-checks-a39a, required_checks 14, source_commit and runner_commit both
   a39ad5ee95609193502850d0dbb87b5dcbb5e3e3, source_export_sha256 d2875624...0ef3f62.
   Recomputed source_export_sha256 from the canonical identity (base_source_archive_sha256,
   source_commit, successor_archive_sha256) per prepare-stage608-export.py: matches.
4. `python3 -I -B stage608.py verify-inputs` exit 0; no __pycache__ or .pyc created or present.
5. No .env, .db, key, .pem, result, __pycache__ or .pyc entries in the export.
6. Launch block differs from the a46c checks preflight only in the export directory and the
   log/rc file names (diff of the fenced blocks). Bounds unchanged: offload --timeout 2460
   --mem 4g --cpus 1, inner `timeout -k 15s 2400s`, preceded by sha256sum, verify-inputs and
   `offload deadline` (>= 2655 s required). The target ../checks-substep-a39a-offload.{log,rc}
   do not exist yet, so there is no collision.
7. Non-blocking (same as a46c review): manifest `purpose` still says "stage native", inherited;
   neither run608.sh nor stage608.py reads it. Cosmetic only.

## Limits

- Did not run `storage608.py check`; the free-space claim is taken as reported.
- Did not diff the full manifest key set against the a46c export or re-derive successor_paths /
  reproduce successor598.tar via git archive.
- Did not re-review run608.sh / stage608.py logic; relied on byte-identity to a39ad5ee and its
  prior independent APPROVE.
- Acceptance of any outcome still follows the candidate95 checks rules and needs its own review.
