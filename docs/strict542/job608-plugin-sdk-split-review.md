# Job608 independent review: plugin-SDK finite split 7b72c7a7 + export installed637e

Scope: commit 7b72c7a7636bb627205411e512d4c37c71273aa8 (parent 6eeeee81) against
Decision637 (assertion-preserving bounded split), and export
/home/deploy/agentq/tmp/export608-installed637e-191743. Read-only review; no build, test or offload run.

## Source checks (test/scripts/write-plugin-sdk-entry-dts.test.ts)
- Base case body moved verbatim, in order, into four `it` cases inside
  `describe("canonical partition history")`; the whole-file diff (blank lines
  ignored) shows no removed or altered body statement. The only body change is
  `createFixture(command)` -> `createFixture(historyLifetime)` for the history root;
  the relocated fixture keeps `createFixture(command)`.
- `expect(` count 43 -> 44; the extra one is the stage guard
  (`expect(stage).toBe(expectedStage)`), so a failed predecessor fails every successor (no skip).
- State flow: case0 sets root/write/writeDeclarations/production/qa/preserved/before;
  case1 sets priorOutputs; case2 sets first/cachedDistFiles; case3 reads them after an
  explicit throw if any is missing. No variable is read before assignment, and no case refers to a local from another case.
- Timeout is `WRITER_TEST_TIMEOUT_MS` per case. `afterAll(historyLifetime.cleanup)`, `createFixtureLifetime`,
  `command.lifetime.run` + `historyLifetime.run`: same structure as the approved precedent
  1acaceda/8fbfc550 (write-unified-entry-dts). It uses no describe.sequential. Plain `it` keeps declaration order, and
  the runner passes --maxWorkers=1 --no-file-parallelism --maxConcurrency=1 and includes this file.

## Export checks
- source_commit = 7b72c7a7636bb627205411e512d4c37c71273aa8 (full).
- successor598.tar sha256 45132e9fe6296847d87c74138fcae8762db59bb7f5f56d543992f4139692a4db
  = successor_archive_sha256, and it is byte-equal to `git archive --format=tar 7b72c7a7 -- <sorted successor_paths>`.
- successor_paths (404, sorted) = 637d list + exactly docs/strict542/job608-plugin-sdk-split.md
  and test/scripts/write-plugin-sdk-entry-dts.test.ts; nothing removed.
- source_export_sha256 d321a207db486ac9be9358ce2b9283119d0ea46fb8887eb59bd8fb3d9957cb8b recomputes correctly.
- run608.sh sha256 94821dd13dc9d9d0347a1715fba579738abe900cf7ef0a72d45282333112c3f5 = runner_sha256
  = docs/strict542/run-package608.sh at 7b72c7a7.
- These files are byte-identical to the 637d export: source598.tar (e79a0e45...), native598.tar (d73e4e35...),
  rolldown608-source.tar.gz (203aa483...), native608-stages/{compile 4a651254..., libtests 2f81179f...}.
- predecessor_manifest_sha256 2c67a204... = sha256 of the 637d export-manifest.json.
- I found no .npmrc, .env*, *.pem, *.key or id_* files in successor598.tar or in the export dir.

## Findings
- Non-blocking: the inherited manifest text `required_check_inventory` names only
  write-unified-entry-dts.test.ts and has the same value as in 637d. The runner itself runs all four suite files, including this one.
- Non-blocking: case3 destructures `write` and uses it for the consumer files. No unused bindings.

VERDICT: APPROVE
