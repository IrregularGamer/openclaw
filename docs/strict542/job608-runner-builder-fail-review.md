# job608 independent review: 04a7b8ea runner builder-fail tail + package4 export

Reviewer: independent (not the author). Read-only; no offload launched, no
installed/sealed file changed.

## Scope
- `04a7b8ea` `docs/strict542/run-stage608.sh` (package branch builder call) and
  `docs/strict542/test_stage608.py` (new regression test).
- `/home/deploy/agentq/runs/608/prepare-consumer608-export.py` `--runner-commit`.
- UNUSED export `/home/deploy/agentq/tmp/export608-stage-package-032241`
  (export-manifest.json sha256 `127108335cf6...`).

## Checks performed
- Status preserved: `cmd || { status=$?; ...; exit "$status"; }`; `$?` is read
  as the first statement in the group, so it is build598.sh's non-zero rc; the
  log tail is `|| true` guarded and the group always exits with that rc. A
  failure is never turned into success; `builder-pass` is still only reached on
  rc 0. The EXIT trap still records the same rc in exit-code.txt.
- `set -eu`: errexit is suspended only for the left side of `||` in the parent
  shell; build598.sh runs in its own `sh` with its own `set -eu`, so its
  internal checks are unaffected. `status` is assigned before use (no `-u` issue).
- cwd: runner does `cd source` (line 54) and the package branch only uses
  `(cd .. && ...)` subshells, so cwd at the builder call is `source/`; build598.sh
  creates `result598-build/build.log` relative to that same cwd. Path correct.
  If build598.sh fails before its `exec >build.log` redirection, its messages
  already go to stdout and the missing-log tail is suppressed by `2>/dev/null || true`.
- Nothing weakened: diff touches only the builder invocation line; env -i
  argument list, checks, assertions, deadlines, budgets, receipts unchanged.
- Secrets: build598.sh runs under `env -i` with only HOME, PATH and the three
  STRICT542 identity vars (commit, export digest, run id), exports only fixed
  build constants, and never echoes the environment. build.log holds
  node/pnpm versions and install/build/preflight output of committed source.
- Test: `python3 -I docs/strict542/test_stage608.py` -> 10/10 OK. Same test
  against the parent runner (`04a7b8ea^`) -> FAILED (1), so it is red before /
  green after. It extracts the actual block from the package branch and runs it
  under `set -eu` with a fake builder exiting 7: asserts rc 7, `builder-fail 7`,
  log content on stdout, and that the following line is not reached.
- Export: `run608.sh` byte-equal to `git show 04a7b8ea:docs/strict542/run-stage608.sh`;
  sha256 `d06e24a5...` equals manifest `runner_sha256`; `runner_commit`
  `04a7b8ea92d7...`; `source_commit` 6ae72a29 unchanged; `stage_inputs` cover
  native/checks/compiler receipts and outputs; `execution_state` UNUSED;
  `predecessor_manifest_sha256` equals checks-024237 manifest digest.
  `cd export && python3 -I stage608.py verify-inputs` -> rc 0.
- Diff vs `export608-stage-checks-024237/run608.sh`: only the builder-fail block.
- Old export untouched: its run608.sh equals `04a7b8ea^` runner, sha256
  `add81a4c...` matches its own manifest, mtime 02:44 (before the 03:22 export),
  different inode from the new runner. The preparer unlinks the hard link before
  writing the new runner, so the shared inode is never written through.

## Notes (non-blocking)
- The runner itself does not check `runner_sha256`; the pin relies on the
  admission/launch path checking the manifest, as before.
- The preparer reads the runner from the live source552 checkout by commit; it
  resolves the full commit with `rev-parse ^{commit}`, so the pin is exact.

## Verdict
APPROVE
