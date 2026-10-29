# job608 independent review: unified-0 preflight tsccwdf6a4 at f6a4de2e

Reviewer: independent (read-only; no offload/build/service run). Date 2026-10-29.
Templates: job608-runtime-tsccwdf6a4-independent-review.md, job608-unified0-fullsize5aff1-preflight-independent-review.md,
applied to UNUSED P/stage-unified-0-tsccwdf6a4 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private).

## 1. Stage hashes / identity
- export-manifest.json 3a1b42d1b104c977b258a82b82fedd85a02e15c7d2fdaaff754caad4e455708a (expected, match)
- run608.sh 715e53bd...cd6a (= runner_sha256), stage608.py a558db9a...0de4 (= stage_helper_sha256);
  both cmp-identical to P/stage-runtime-tsccwdf6a4 copies. successor598.tar cmp-identical (17991680 B; own inode 396143).
- source598.tar / native598.tar / rolldown608-source.tar.gz: same inodes as runtime stage (395540 / 395541 / 395542).

## 2. Gates
- `python3 -I -B stage608.py verify-inputs` exit 0; `sh -n run608.sh` exit 0.

## 3. Manifest
- execution_state UNUSED, stage unified-0, run_id stage608-unified-0-tsccwdf6a4,
  source_commit = runner_commit = f6a4de2ebc6924d16fe559f9858bf8c50dce1eba, source_export_sha256 e81e07d2770ad597...
- JSON diff vs runtime stage manifest: only stage, run_id, stage_inputs, predecessor_manifest_sha256
  (b51a34e9... -> d0d4d630..., = sha256 of runtime stage manifest), predecessor_package_attempt
  (-> "stage608-runtime-tsccwdf6a4 (superseded by source f6a4de2e)"). No other field changed.

## 4. stage_inputs (STAGES['unified-0'] = native, runtime)
Pin = sha256 of stage608-inputs file = same inode as accepted result file:
- native/libtests-receipt.json 2f81179f... (396079), native/receipt.json 4a651254... (396080),
  native/rolldown-binding.linux-x64-gnu.node 0b6607e7... (396081), native/stage-receipt.json 10474857... (396082)
  -> P/stage-native-tsccwdf6a4/result608-native/native/* (accepted 57742314).
- runtime/stage-receipt.json 3e284e2c... (396134), runtime/checkpoint.tar.gz 9e028d03... (396133),
  runtime/build.log 242dfc93... (396132) -> P/stage-runtime-tsccwdf6a4/result608-runtime/runtime/* (accepted 5824b14b).
- Set = {n/stage-receipt.json} + OUTPUTS[native] + OUTPUTS[runtime] exactly; 7 pins, no extras.

## 5. run608.sh unified branch (`runtime|unified-[0-5]|middle|sdk-[0-1]|tail`)
- stage-native + restore-build via stage608.py, pnpm@12.5.1 path resolve via npm exec, identities from manifest,
  fixed inner budget 2280s minus elapsed, `env -i` build, archive-build, receipt. No sudo/systemctl/system install/
  credentials/network auth. (pnpm install --frozen-lockfile appears only in checks/compiler branches.)

## 6. Absent (unused)
- P/stage-unified-0-tsccwdf6a4/result608-unified-0, P/unified-0-tsccwdf6a4-offload.log, .rc: all absent.

## 7. Storage
- `storage608.py check --root P --stage unified-0` exit 0:
  {"current_unique_bytes": 1851660141, "free_bytes": 5472342016, "free_reserve_bytes": 2147483648,
   "max_store_bytes": 4294967296, "return_cap_bytes": 33554432, "stage": "unified-0"}

## Planned launch (next fresh worker, FIRST heavy step, needs >=2655s left)
`cd P/stage-unified-0-tsccwdf6a4; offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-0 -- timeout -k 15s 2400s sh run608.sh > ../unified-0-tsccwdf6a4-offload.log 2>&1; printf '%s\n' "$?" > ../unified-0-tsccwdf6a4-offload.rc`

## Verdict: APPROVE
No discrepancies. Note only: stage-root __pycache__/ exists (as in runtime stage; from stage608.py runs); harmless.
