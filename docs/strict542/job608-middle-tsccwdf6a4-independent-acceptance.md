# Independent acceptance: job608 middle tsccwdf6a4 actual run

Reviewer: independent. I did not produce this evidence. Scope: evidence commit `f6a6802d`
(`job608-middle-tsccwdf6a4/`). P = /srv/encrypted/dev-move-98/agentq-source608-20261028-private.
Result directory P/stage-middle-tsccwdf6a4/result608-middle. All checks were read-only. No
offload was launched and nothing under /srv was modified. The checklist follows the unified-5r1
acceptance.

## Checks

- PASS: return codes. The committed `middle-offload.rc`, the private
  `P/middle-tsccwdf6a4-offload.rc`, and result `exit-code.txt` (private and committed) all
  contain `0`.
- PASS: offload log. The decompressed committed `middle-offload.log.gz` is `cmp`-identical to
  the private `P/middle-tsccwdf6a4-offload.log`. It records middle-stage-native-start +11s,
  middle-restore-build-done +20s, middle-build-start (budget 2256s) +24s,
  `STEP608 middle-build-done +309s` and `STEP608 middle-pass`. A case-insensitive grep for
  refus, exit75, offload_status and error finds nothing.
- PASS: result file hashes. The private result contains exactly five regular files and no
  other non-directory entries. `sha256sum -c result-files.sha256`, run inside the private
  result directory, reports OK for all five: exit-code.txt, middle/build.log,
  middle/checkpoint.tar.gz, middle/stage-receipt.json and strict542-checks/pnpm-path.txt.
- PASS: committed copies. All four committed small files are `cmp`-identical to the private
  originals: exit-code.txt, middle/build.log, middle/stage-receipt.json and
  strict542-checks/pnpm-path.txt. `git ls-files` lists all four. The 115935311-byte
  checkpoint stays private.
- PASS: stage receipt. Its SHA256 is `9eb3083c62bbb5ecf715a375ec00f344b4d21c70fc291bd695ee92be5937d2cf`.
  It contains kind `JOB608_STAGE_RECEIPT`, stage `middle`, exit_code 0 and run_id
  `stage608-middle-tsccwdf6a4`. It binds source_commit `f6a4de2ebc6924d16fe559f9858bf8c50dce1eba`
  and source_export_sha256 `e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145`.
  Both equal the corresponding fields of `P/stage-middle-tsccwdf6a4/export-manifest.json`.
  Its outputs are exactly the two entries that stage608.py `OUTPUTS['middle']` requires:
  `middle/build.log` = `9d1fdaf9...e301` and `middle/checkpoint.tar.gz` = `32ea0475...6e220`.
  Both equal the actual SHA256 of the private files. It has 24 stage_inputs: native,
  runtime and unified-0..5, with unified-5 at `0dc9bea0...9e34`, the accepted 5r1 receipt.
- PASS: manifest. `P/stage-middle-tsccwdf6a4/export-manifest.json` SHA256 is unchanged at
  `cc7651f8749dd402cf4839810dc1b3b61e90d7c5e1650b9417183f30157600ca`. That equals the receipt
  manifest_sha256 and the committed `job608-middle-tsccwdf6a4-export-manifest.json`. The
  committed `stage608.py` is `cmp`-identical to the staged copy.
- PASS: checkpoint listing. `tar -tzf` exits 0 and lists 15533 entries. No entry is an
  absolute path or contains a `..` component. Every entry falls under `middle/` (0 outside):
  middle/data/dist (11558), dist-runtime (3441), packages (508), extensions (23), and
  middle/receipt.json. stage608.py `checkpoint_path('middle')` returns `middle`, and
  `extract_checkpoint` accepts only `middle` and `middle/...` for this stage. The archive
  therefore satisfies middle-stage ownership. Inner middle/receipt.json has schema
  `strict542-build-checkpoint608-v1`, status `CHECKPOINT_NOT_BUILT` (the expected status for
  runtime/middle/tail checkpoints, the same as the accepted runtime checkpoint) and stage
  `middle`. Its identity binds source f6a4de2e and export e81e07d2. All 7 phases have status
  `ran`, and the runtime ancestor is recorded.
- PASS: storage check. `python3 -I -B docs/strict542/storage608.py result --stage middle
  --result <private result>` exits 0 with logical_return_bytes 115949588, under the
  134217728-byte cap.
- PASS: build log. It has 263 lines, and `grep -ciE 'error|fail|cancel'` returns 0. It ends
  with `phase timings: total 2m 33.2s` across seven phases.
- PASS: README claims. rc0, +309s, the receipt, build.log and checkpoint hashes, the
  115935311-byte checkpoint, 115949588 bytes under the cap, and the manifest all match what I
  observed.

## Scope and limits

No build, offload, extraction, installed-state change or queue mutation was run. The only
change is this document. Stage middle-tsccwdf6a4 is SPENT and must never be replayed. No
install or release authority. 595 MUST NOT APPLY.

VERDICT: ACCEPT
