# job608 independent review: runtime preflight tsccwdf6a4 at f6a4de2e

Reviewer: independent (read-only; no offload/build/service run). Date 2026-10-29.
Template: job608-native-tsccwdf6a4-independent-review.md, applied to
P/stage-runtime-tsccwdf6a4 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private).

## 1. Stage hashes / identity
- export-manifest.json d0d4d630af82f520dbe2609ac7f8ad4018d72ccffe24ba1e4bbd5bdc21e2fbf7 (expected, match)
- run608.sh 715e53bd...cd6a (= runner_sha256), stage608.py a558db9a...0de4 (= stage_helper_sha256);
  both cmp-identical to P/stage-native-tsccwdf6a4 copies.
- source598.tar / native598.tar / rolldown608-source.tar.gz: same inodes as native stage
  (395540 / 395541 / 395542). successor598.tar cmp-identical to native stage copy (17991680 B).

## 2. Gates
- `python3 -I -B stage608.py verify-inputs` exit 0; `sh -n run608.sh` exit 0.

## 3. Manifest
- execution_state UNUSED, stage runtime, run_id stage608-runtime-tsccwdf6a4,
  source_commit = runner_commit = f6a4de2ebc6924d16fe559f9858bf8c50dce1eba,
  source_export_sha256 e81e07d2770ad597... (= native stage manifest).
- JSON diff vs native stage manifest, changed keys only: predecessor_manifest_sha256,
  predecessor_package_attempt, run_id, stage, stage_inputs (all expected).
- predecessor_manifest_sha256 b51a34e9... = accepted native stage manifest sha.
- Cosmetic: `purpose` unchanged, still reads "...build stage native..."; not used by
  run608.sh/stage608.py. Non-blocking.

## 4. stage_inputs
- Pins exactly: native/stage-receipt.json 1047485796fe..., native/receipt.json 4a651254152b...,
  native/libtests-receipt.json 2f81179f5d1b..., native/rolldown-binding.linux-x64-gnu.node
  0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042 (= accepted binding, 57742314).
- Each pin equals sha256 of the file in stage608-inputs/; all four are the same inode as
  P/stage-native-tsccwdf6a4/result608-native/native/* (hard links).

## 5. run608.sh runtime branch (lines 124-148)
- stage-native + restore-build via stage608.py, npm exec pnpm@12.5.1 version-pinned resolve
  (established reviewed pattern), identities from manifest, fixed 2280 s inner budget, env -i
  build via docs/strict542/run-build-stage608.sh, archive-build. No sudo/systemctl/install/
  credential/provider/network-auth actions; no curl/wget/ssh/token use anywhere in run608.sh.

## 6. Absent (unused stage)
- result608-runtime, ../runtime-tsccwdf6a4-offload.log, ../runtime-tsccwdf6a4-offload.rc: absent.

## Verdict: APPROVE
All checks pass; launch as planned (`offload run --timeout 2460 --mem 14g --cpus 4
--artifacts result608-runtime -- timeout -k 15s 2400s sh run608.sh`), same form as accepted
native/unified launches. Only note: stale `purpose` text (cosmetic, non-blocking).
