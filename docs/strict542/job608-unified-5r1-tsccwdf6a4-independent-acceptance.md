# Independent acceptance: job608 unified-5r1 tsccwdf6a4 actual run

Reviewer: independent. I did not produce this evidence. Scope: evidence commit `78e9a6f7`
(`job608-unified-5r1-tsccwdf6a4/`), launch record `4191978f`
(`job608-unified5r1-tsccwdf6a4-continuation.md`) and preflight APPROVE `ca83930e`.
P = /srv/encrypted/dev-move-98/agentq-source608-20261028-private. Result directory
P/stage-unified-5r1-tsccwdf6a4/result608-unified-5. All checks were read-only. The checklist
follows the unified-4 acceptance and re-acceptance.

## Verified

- Private `P/unified-5r1-tsccwdf6a4-offload.rc`, committed `unified-5r1-offload.rc`, and
  result `exit-code.txt` (private and committed) all contain bytes `0\n`.
- The decompressed committed `unified-5r1-offload.log.gz` is `cmp`-identical to the private
  outer log. SHA256 `c378a45dd9b05dc28dbff62bdb6811239bd606adf3385c4be19edf71502d89b1`
  matches on both sides. The log records native-start +11s, restore-build-done +19s,
  build-start (budget 2258s) +22s, build-done +440s and `unified-5-pass`, and has no
  `offload_status` line. The launch record's single command (`--timeout 2460 --mem 14g
  --cpus 4`, inner `timeout -k 15s 2400s`) matches the README.
- The private result contains exactly the five files listed in `result-files.sha256`.
  `sha256sum -c` passes for all five, for 1226413 bytes in total. All four committed copies
  are `cmp`-identical to the private originals: exit-code.txt, pnpm-path.txt,
  stage-receipt.json, and build.log. `git ls-files` lists build.log, so the gap found in the
  unified-4 review does not recur. The 1215797-byte checkpoint (`2b480ad8...7ae8`) stays
  private.
- The receipt SHA256 is `0dc9bea0...9e34`. It has the same structure as the unified-4
  receipt: kind `JOB608_STAGE_RECEIPT`, stage `unified-5`, exit_code 0, run_id
  `stage608-unified-5-tsccwdf6a4`. It binds source_commit
  `f6a4de2ebc6924d16fe559f9858bf8c50dce1eba` and source_export_sha256 `e81e07d2...8145`.
  manifest_sha256 is `a63306a5...81e4`. Its output hashes match the actual build.log
  (`4a2e0945...3200`) and checkpoint. Its seven stage_inputs equal the preflight
  `common.stage_inputs`, which are the same pins as the unified-4 receipt.
- `P/stage-unified-5r1-tsccwdf6a4/export-manifest.json` has SHA256 exactly `a63306a5...81e4`.
  That equals preflight `job608-unified1-5-tsccwdf6a4-preflight.json` `stages[4]`
  (stage, run_id and manifest_sha256 all match). The only difference is `stages[4].directory`:
  it names the spent unified-5 path, while this run used the hardlinked 5r1 copy. The launch
  record documents that copy, and preflight `ca83930e` approved it (`diff -r` identical).
  This is not a defect.
- build.log has 240 lines. It shows `openclaw-dts-extensions-5: cache miss (disabled)` and
  ends with `[tsdown-build] invocation 1/1 finished in 287.7s` and `phase timings: no phases
  ran`. A case-insensitive grep for error, fail, cancel, ERR!, fatal, timeout, OOM and killed
  finds nothing.
- `python3 -I -B docs/strict542/storage608.py result --stage unified-5 --result <dir>`
  exits 0 and returns 1226413 logical bytes, under the 33554432-byte cap.
- The README claims are true: rc0, +440s, 287.7s, 1226413 bytes, the receipt, checkpoint and
  log SHA256s, the manifest equal to stages[4], and four committed files with build.log
  force-added. Ordering also holds: the run's files are timestamped 17:51, after preflight
  `ca83930e` at 17:41, and evidence `78e9a6f7` was committed at 17:52.

## Scope and limits

This review did not inspect the checkpoint's internal entries. The unified-4 acceptance
did that, but this task did not ask for it, and the receipt output hash binds the checkpoint.
No build, offload, extraction, installed-state change or queue mutation was run. The only
change is this document. Stage 5r1 is SPENT and must never be replayed. No install or release
authority. 595 MUST NOT APPLY.

VERDICT: ACCEPT
