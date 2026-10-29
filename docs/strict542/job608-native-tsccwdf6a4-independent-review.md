# job608 independent review: native preflight tsccwdf6a4 at f6a4de2e

Reviewer: independent (read-only; no offload/build/service run). Date 2026-10-29.
Checklist: same as job608-checks-tsccwdf6a4-independent-review.md, applied to
P/stage-native-tsccwdf6a4 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private).

## 1. Stage hashes
- export-manifest.json b51a34e949a4322f891b34d200c7d87f58333ab854209c0e4b4c2f5703a9f9f6 (expected, match)
- run608.sh 715e53bd43979434f317807973d9712bc58d6ecbeec357561f92053b8aa3cd6a (= manifest runner_sha256)
- stage608.py a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4 (= stage_helper_sha256)
- successor598.tar 88fc8d3f1934c00d65e75324b79d8745f743a6fe426aaa98ecd50d38bef69ac9 (= successor_archive_sha256; 17991680 B)
- source598.tar e79a0e45a4eaea4afe325ca94ba201d5ae43d09d8c15dc07d0695c87ba743de3 (= base_source_archive_sha256)
- native598.tar d73e4e35720ffcb71856ce8168e75fa3b4fd49251fd78c811e1abded8b2701de (= native_export_sha256)
- rolldown608-source.tar.gz 203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac (= compiler_upstream_archive_sha256)
- source598/native598/rolldown are the same inodes as the superseded label49d31 stage (hard links).

## 2. Gates
- `python3 -I -B stage608.py verify-inputs` exit 0; `sh -n run608.sh` exit 0.
- `stage608.py check --stage native`: no such subcommand (helper prints "unknown stage608
  command", rc 2). The `check --stage native` gate belongs to docs/strict542/storage608.py
  and stays a fresh live gate at launch time; not run here.

## 3. Manifest
- execution_state UNUSED, launch_history none, run_id stage608-native-tsccwdf6a4,
  stage native, source_commit = runner_commit = f6a4de2ebc6924d16fe559f9858bf8c50dce1eba,
  stage_inputs {} (empty), source_export_sha256 e81e07d2... (same as accepted checks tsccwdf6a4).
- native_stage_outputs: exactly compile/receipt.json + libtests/receipt.json; native608-stages
  identical to the label49d31 stage (diff -r clean).

## 4. Successor archive
- Streamed `git archive f6a4de2e -- <888 successor_paths> | sha256sum` =
  88fc8d3f1934c00d65e75324b79d8745f743a6fe426aaa98ecd50d38bef69ac9, 17991680 B (single
  invocation; matches the tar and manifest, and the accepted checks stage successor).

## 5. Diff vs superseded stage-native-label49d31 (manifest 61c98062)
- Changed keys only: run_id, source_commit, runner_commit (49d3fe33 -> f6a4de2e),
  source_export_sha256 (0bb56af5 -> e81e07d2), successor_archive_sha256 (ae36bfdf -> 88fc8d3f),
  successor_paths (858 -> 888: +30, all docs/strict542 evidence/review files, 0 removed),
  predecessor_package_attempt text (49d3fe33 -> f6a4de2e). All other keys identical.
- run608.sh and stage608.py byte-identical to the label49d31 stage. 49d3fe33..f6a4de2e
  touches none of prepare-native-consumer608.py, run-stage608.sh, stage608.py, scripts/.
- Cosmetic only: source_correction_review still carries the inherited 5ec111ba text
  (unchanged from label49d31); not a launch input.

## 6. run608.sh (native branch)
- Verifies archive digests, receipts and no NAPI_RS_* env; extracts source/successor/native
  tars; runs `timeout -k 15s 2400s python3 docs/strict542/prepare-native-consumer608.py`;
  copies receipt.json, libtests-receipt.json, rolldown-binding.linux-x64-gnu.node into
  result608-native/native/; EXIT trap writes result608-native/exit-code.txt.
- Native branch has no npm/pnpm install, no sudo/systemctl/install, no credentials,
  secrets or provider calls; writes only inside the export (outputs to result608-native).

## 7. Absent
- result608-native, P/native-tsccwdf6a4-offload.log, P/native-tsccwdf6a4-offload.rc: absent.

## 8. Launch command
- Intended: `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh`
  is exactly the label49d31 native preflight `launch` (job608-native-label49d31-preflight.json).

## VERDICT
VERDICT: APPROVE the native tsccwdf6a4 launch preflight (manifest b51a34e9, f6a4de2e),
CONDITIONAL on fresh live gates at launch (health up, no competing run, verify-inputs 0,
storage608.py check --stage native 0, no result/log/rc, remaining >= 2655s, prefer 2895).
ONE run only, no unchanged replay after admission. Never launch superseded label49d31.
This is not acceptance; acceptance needs the run's own result. 595 MUST NOT APPLY.
