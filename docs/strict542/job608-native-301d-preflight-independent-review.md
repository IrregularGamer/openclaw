# job608 independent review: native preflight 301d at 301d7456

Verdict: APPROVE

Reviewer: independent (read-only; no offload/build/service run). Date 2026-10-30.
Reviewed: docs/strict542/job608-native-301d-preflight.json (7c55092a) against P/stage-native-301d
(P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private). C = 301d7456bf5b0c4179b27d0db97eac7b07143f4a.
Checklist: job608-native-m674-preflight-independent-review.md.

## 1. Stage hashes (all match the preflight json)
- export-manifest.json b61f89b5... (= manifest_sha256)
- run608.sh b04abd4d... (= runner_sha256; same as m674)
- stage608.py 1d2bf411... (= stage_helper_sha256)
- successor598.tar e2ed663e... (= successor_archive_sha256)
- source598.tar e79a0e45..., native598.tar d73e4e35..., rolldown608-source.tar.gz 203aa483... (= m674 values)

## 2. Gates
- `python3 -I -B stage608.py verify-inputs` exit 0; no __pycache__ created. `sh -n run608.sh` exit 0.
- storage608 check not re-run here; stays a fresh live gate at launch.

## 3. Manifest
- execution_state UNUSED, launch_history "none (fresh finite export)", run_id stage608-native-301d, stage native,
  source_commit = runner_commit = C, stage_inputs {}, input_lineage absent, successor_paths 1252.
- native_stage_outputs identical to m674: compile/receipt.json 4a651254..., libtests/receipt.json 2f81179f...

## 4. Byte equality
- run608.sh == `git show 301d7456:docs/strict542/run-stage608.sh`; stage608.py == `git show 301d7456:docs/strict542/stage608.py`.

## 5. Code diff 674840b6..301d7456 (excluding docs/strict542/job608-*)
- run-stage608.sh unchanged. stage608.py: only Decision662 lineage (LINEAGE_* constants, check_lineage,
  lineage branch in verify_inputs that is inert when input_lineage is absent, receipt copies input_lineage only
  when present). No change to native producer/archive/restore logic.
- prepare-stage608-export.py: opt-in --lineage-ancestor, package-only; not used for this export.
- build598.sh (+frozen-package608.py materialize after pnpm deploy runtime) and frozen-package608.py: package/build
  path only, not native. Tests only otherwise.

## 6. native608-stages
- `diff -r` P/stage-native-301d/native608-stages vs P/stage-native-m674/native608-stages: identical.

## 7. Launch / caps / no prior run
- Launch argv equals m674 README: offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-native --
  timeout -k 15s 2400s sh run608.sh.
- No P/native-301d-offload.log/.rc and no result608-native in the stage dir.
