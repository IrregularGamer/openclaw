# job608 independent review: native preflight m674 at 674840b6

Reviewer: independent (read-only; no offload/build/service run). Date 2026-10-29.
Checklist: job608-native-tsccwdf6a4-independent-review.md, rules of
job608-after-package-moderefusal-continuation.md, applied to P/stage-native-m674
(P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private). C = 674840b669c43af54a62e30b4028f219f4a428c9.

## 1. Stage hashes (all match manifest fields)
- export-manifest.json 738684f384b11cd40db2f3daa21d8f1460fb4f15b7e7673e371d80c52ef2dbf5 (expected, match)
- run608.sh b04abd4d6d08f2352bd04e5ecc4e3e56d9f6c67223c175a03e98fa44cc0b7816 (= runner_sha256)
- stage608.py a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4 (= stage_helper_sha256; unchanged vs tsccwdf6a4)
- successor598.tar 9374675e9d48f846cfe8a428cb1b32bbc188e41c021bf653224084f0f6190296 (= successor_archive_sha256; 19128320 B)
- source598.tar e79a0e45a4eaea4afe325ca94ba201d5ae43d09d8c15dc07d0695c87ba743de3 (= base_source_archive_sha256)
- native598.tar d73e4e35720ffcb71856ce8168e75fa3b4fd49251fd78c811e1abded8b2701de (= native_export_sha256)
- rolldown608-source.tar.gz 203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac (= compiler_upstream_archive_sha256)
- source598/native598/rolldown hashes equal P/stage-native-tsccwdf6a4 (same native inputs; hard links, nlink 44).

## 2. Gates
- `python3 -I -B stage608.py verify-inputs` exit 0; `sh -n run608.sh` exit 0.
- storage608.py check --stage native not run here; stays a fresh live gate at launch.

## 3. Manifest
- execution_state UNUSED, launch_history "none (fresh finite export)", run_id stage608-native-m674,
  stage native, source_commit = runner_commit = C, stage_inputs {} (empty),
  source_export_sha256 e1a6de35..., successor_paths 1070.
- native_stage_outputs: exactly compile/receipt.json (4a651254...) + libtests/receipt.json (2f81179f...).

## 4. Commit diff f6a4de2e..674840b6
- Code changes only: run-stage608.sh (+umask 022, tar --no-same-permissions x3, comment),
  test_stage608.py (+17), storage608.py/test_storage608.py (tail return cap 128->192MiB, 8f4fb3b3,
  already noted in job608-package-mode-fix-independent-review.md; native cap 64MiB unchanged; not a
  runner input). Everything else is docs/strict542 evidence. No change to scripts/, src/,
  stage608.py, prepare-native-consumer608.py, prepare-stage608-export.py.
- run608.sh byte-equals `git show 674840b6:docs/strict542/run-stage608.sh` (runner_source_path);
  stage608.py byte-equals `git show 674840b6:docs/strict542/stage608.py`.
- diff vs tsccwdf6a4 run608.sh: only the umask/--no-same-permissions hunk.

## 5. native608-stages
- `diff -r` vs P/stage-native-tsccwdf6a4/native608-stages: identical.

## 6. Successor archive
- Streamed `git archive 674840b6 -- <1070 successor_paths> | sha256sum` =
  9374675e9d48f846cfe8a428cb1b32bbc188e41c021bf653224084f0f6190296, 19128320 B (matches tar and manifest).

## 7. Absent
- P/stage-native-m674/result608-native, P/native-m674-offload.log, P/native-m674-offload.rc: absent.

## 8. Launch command
- `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh`
  (caps unchanged from tsccwdf6a4).

## VERDICT
VERDICT: APPROVE the native m674 launch preflight (manifest 738684f3, C=674840b6), CONDITIONAL on
fresh live gates at launch (health up, no competing run, verify-inputs 0, storage608.py check --stage
native 0, no result/log/rc, remaining >= 2655s). ONE run only, no unchanged replay after admission.
Not acceptance; acceptance needs the run's own result.
