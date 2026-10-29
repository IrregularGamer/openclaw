# job608 independent review: native preflight at singleThreaded freeze a46cd576

**VERDICT: APPROVE**

Reviewed: `job608-native-singlethreaded-a46c-preflight.md` (commit d83eb771) against
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-native-singlethreaded-a46c`.
Read-only review by an independent reviewer that did not prepare the export. Nothing was
launched; no offload, run608.sh, build, preparer or export-writing command was run; the export
was not modified. Commands used: sha256sum, stat, cmp, find, `python3 -I -B stage608.py
verify-inputs`, and read-only JSON parsing of export-manifest.json files.

This review grants no install, package, application or reseal authority. 595 MUST NOT APPLY.

## Findings

1. All hashes in the doc match on-disk files: export-manifest.json 3f48b86f...3bb3bd488,
   run608.sh eb662d81...76644b01, stage608.py a558db9a...27c0de4, native598.tar
   d73e4e35...2b8701de, rolldown608-source.tar.gz 203aa483...5d258ac, source598.tar
   e79a0e45...0743de3, successor598.tar dcc959c7...6bb303515. Manifest runner_sha256,
   stage_helper_sha256, native_export_sha256, compiler_upstream_archive_sha256,
   base_source_archive_sha256 and successor_archive_sha256 agree.
2. Manifest fields: stage native, execution_state UNUSED, run_id stage608-native-a46c,
   source_commit and runner_commit a46cd5765702f3b019d5a433b82d19ac57821a8d, stage_inputs {},
   required_checks 14, source_export_sha256 88279fe1...caded20d9e. Recomputed
   source_export_sha256 from the canonical identity (base_source_archive_sha256, source_commit,
   successor_archive_sha256) per prepare-stage608-export.py: matches.
3. Pins equal the 1bed native pins: stage-native-1bed manifest has native_export_sha256
   d73e4e35... and compiler_upstream_archive_sha256 203aa483...; native598.tar,
   rolldown608-source.tar.gz and source598.tar are the same inodes (395541/395542/395540) as
   ../base. Both native608-stages receipt.json files are byte-identical (cmp) to ../base and
   match manifest native_stage_outputs (4a651254..., 2f81179f...).
4. Produced by the committed preparer: a46cd576 is an ancestor of HEAD and
   prepare-stage608-export.py, run-stage608.sh and stage608.py are unchanged between a46cd576
   and HEAD (no commits, empty diff). run608.sh / stage608.py hashes equal
   `git show a46cd576:docs/strict542/{run-stage608.sh,stage608.py}`. The manifest differs from
   the approved stage-checks-singlethreaded-a46c manifest (review cdcaaa19) in exactly two
   fields, run_id and stage, as the preparer's --stage switch produces; successor598.tar is
   byte-identical to that export's. Versus stage-native-1bed the differences are only the
   expected identity fields (source/runner commit, runner_sha256, run_id, source_export,
   successor archive/paths, predecessor_package_attempt).
5. `python3 -I -B stage608.py verify-inputs` exit 0.
6. No .env, .db, .pem, .key or id_* files in the export (find, recursive).
7. stage608.py STAGES has `'native':[]`: native has no stage predecessors, so the checks
   result is not an input and launch is independent of the checks outcome.
8. Launch command matches the reviewed pattern (1bed native preflight and checks a46c
   preflight): sha256sum + verify-inputs + `offload deadline` (>= 2655 s) first, then
   `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-native -- timeout -k 15s
   2400s sh run608.sh`, log/rc to ../native-singlethreaded-a46c-offload.{log,rc} (not present
   yet, no collision). FIRST step of a fresh worker; storage608.py result check before
   acceptance; no unchanged rerun on failure/timeout.

## Notes (non-blocking)

- Manifest `purpose` keeps the generic "fixed finite canonical build stage native" text (the
  preparer's native purpose replace is a no-op on this base); identical to the 1bed native and
  checks a46c manifests, cosmetic only.
- `source_correction_review` still reads "5ec111ba ... independent review pending" inherited
  from base; unchanged from the approved precedents.
