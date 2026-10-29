# Job 608 unified-4 tsccwdf6a4: independent re-acceptance (ACCEPT)

Independent re-review dated 2026-10-29. It follows the prior review `b901b0ba`
(`job608-unified-4-tsccwdf6a4-independent-acceptance.md`, CHANGES REQUESTED because
evidence commit `89623de8` left out the gitignored `build.log`). The fix under review is
commit `5e70391f2e44ba9692f6f48c66d840eaf1bdd14f`. P denotes
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private`. The reviewer did not
produce this evidence. Only read-only commands were run (git show/diff/ls-files,
sha256sum, cmp, od, and the non-writing `storage608.py check`/`result` subcommands).

## Blocking finding resolution

- `git show --name-status 5e70391f` and `git diff --name-status b901b0ba 5e70391f` both list
  exactly one change: `A docs/strict542/job608-unified-4-tsccwdf6a4/result608-unified-4/unified-4/build.log`
  (241 insertions). No other file changed. `git diff 89623de8 5e70391f` under the evidence
  directory shows only that same file.
- The committed blob's SHA256 is `dc2337e8c7fb6e67d33bab1cfd21794b01d4fc9bfba5bda4d3d0b34f38b51fff`.
  It has 241 lines and 9308 bytes and is `cmp`-identical to
  `P/stage-unified-4-tsccwdf6a4/result608-unified-4/unified-4/build.log`.
- The blocking finding is resolved.

## Result inventory (`result-files.sha256`)

- From inside `P/stage-unified-4-tsccwdf6a4/result608-unified-4`, `sha256sum -c` passes for all
  five listed files. `find` shows exactly those five files.
- The evidence commit now tracks four result copies: `exit-code.txt`,
  `strict542-checks/pnpm-path.txt`, `unified-4/build.log` and `unified-4/stage-receipt.json`.
  Each HEAD blob is `cmp`-identical to its private original. `sha256sum -c` passes for those four
  from the committed result directory. The fifth file, `unified-4/checkpoint.tar.gz`
  (`03da89d6...7731b3`), is private by design and not committed, as in the prior review and for
  unified-3. Its private hash matches.

## Other checks re-verified

- Private `P/unified-4-tsccwdf6a4-offload.rc` and committed `unified-4-offload.rc` both contain
  bytes `0\n` and are `cmp`-identical. The committed `exit-code.txt` matches its listed hash.
- The decompressed committed `unified-4-offload.log.gz` and the private outer log both have SHA256
  `e027e7adcbfb39e87b9c21073ebfdaa77edf7f51d35d4ea7de21fcab14f025c3`.
- `P/stage-unified-4-tsccwdf6a4/export-manifest.json` has SHA256
  `e406475889b8e83d6fe2f369a41a5adf1d1f69f94933933d1d808cb0f353fc4f`.
- The receipt's SHA256 is `0d6c99fec370e44b2a0d4e2f7c4a5f0f9cc3488d1fa3b16b3835a515f2cb208c`.
  It records kind `JOB608_STAGE_RECEIPT`, stage `unified-4`, exit_code 0, run_id
  `stage608-unified-4-tsccwdf6a4` and manifest_sha256 `e4064758...4fc4f`.
- `storage608.py check --root P --stage unified-4` exits 0 (free 5357785088 bytes, above the
  2147483648 reserve). `storage608.py result --stage unified-4` exits 0 with 1220394 logical
  return bytes, below the 33554432 cap.
- The deeper checks in the prior review (archive inventory, sidecar/binding digests, stage inputs,
  build-log content) were not repeated. They depend on files whose hashes are re-confirmed
  unchanged above, so they still hold.

## Scope and limits

This re-review covers unified-4 only. It ran no build, offload, extraction, or state mutation.
Its only change is this document and its Git publication. Do not relaunch unified-4; the stage
is SPENT. No installation or release authority; 595 MUST NOT APPLY.

VERDICT: ACCEPT
