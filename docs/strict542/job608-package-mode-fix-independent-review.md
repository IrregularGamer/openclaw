# Independent review: job608 package mode refusal (d5eff2b7) and run-stage608 umask fix (674840b6)

Reviewer did not author either commit. Read-only on /srv (tar -tv/-tvz listings only, nothing extracted), no offload, no pull.
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private.

## 1. Root cause — PASS
- `tar -tvf P/stage-package-tsccwdf6a4/source598.tar | grep CHANGELOG.md`: `-rw-rw-r-- root/root 16715 ... CHANGELOG.md`
  (plus 6 nested CHANGELOG.md, all 0664). Mode histogram of source598.tar: 50506 `-rw-rw-r--`, 244 `-rwxrwxr-x`,
  2073 `drwxrwxr-x`, 2 symlinks; no 0644/0755 entries at all, consistent with git archive tar.umask default 0002
  (repo has no tar.umask override).
- GNU tar 1.35 behaviour reproduced locally (non-root, a 0664 entry): `umask 002; tar -xf` -> 664; `umask 022; tar -xf`
  -> 644; `umask 022; tar --same-permissions -xf` -> 664. Root defaults to --same-permissions, so the old runner
  (plain `tar -xf`, remote superuser) produced a group-writable tree regardless of umask.
- Accepted tail checkpoint `P/stage-tail-tsccwdf6a4/result608-tail/tail/checkpoint.tar.gz` (tar -tvzf only):
  1003 `-rw-rw-r--` and 68 `drwxrwxr-x` entries (alongside 14896 `-rw-r--r--`/1000 `drwxr-xr-x` build-created ones),
  matching the README counts.
- stage608.extract_checkpoint (stage608.py:65-69) does `extractall(filter='data')` then explicitly
  `chmod(entry.mode&0o777)`, re-adding the group-write bits the data filter stripped; it only rejects 0o7000.
- Conclusion: rerunning package from the accepted tsccwdf6a4 stages would deterministically restore 0664/0775 files
  and be refused again by application598 tree. It can never pass.

## 2. No check weakened — PASS
- `git show --stat d5eff2b7`: only job608-package-tsccwdf6a4/{README.md,package-offload.log.gz,package-offload.rc}.
- `git show --stat 674840b6`: only run-stage608.sh (+umask 022, 3x `tar --no-same-permissions -xf`, comment) and
  test_stage608.py (+17 lines).
- `git diff f6a4de2e..674840b6 --stat` over application598.py, stage608.py, build598.sh, prepare-stage608-export.py:
  empty. storage608.py differs in that range only via 8f4fb3b3 (tail return cap 128->192MiB), unrelated to either
  commit and not a mode/identity check.
- No chmod, no post-hoc mode fixing, no identity/receipt/manifest editing. The modes are corrected at their origin.

## 3. Completeness of the staged path — PASS (non-blocking notes)
`umask 022` is set in run608.sh before `mkdir source native-source`, so it is inherited by every later process
(stage608.py, npm exec/pnpm install, `env -i` builders, build598.sh, pnpm deploy; env -i does not reset umask).
Remaining extraction/copy sites on the staged path:
- source/successor/native tars: fixed.
- build-native608.py:46 rolldown608-source.tar.gz: `extractall(filter='data')` strips group/other write; only
  the addon leaves it, via shutil.copyfile in stage_native (new file, umask-governed, mode not copied). OK.
- build-native608.py:91 wheel (zipfile.extractall): modes not applied, umask-governed. OK.
- stage608.extract_checkpoint: restores exact archived modes, so it is clean only if checkpoints are rebuilt under
  the fix (see 5). Old checkpoints must not be reused.
- native608-stages copytree happens locally at export time and carries only receipts, not runtime files. OK.
- pnpm store/deploy copies: created under umask 022; source files they copy are now 0644/0755. OK.
No remaining gap found that puts 0664/0775 into result598-build/runtime.
Non-blocking: (a) legacy runners run-package608.sh, run-bounded608.sh, run-native608.sh, run-native608-stage.sh,
run-installed-split608.sh, run-inventory608.sh, run-isolated598.sh, run-workers608.sh, job608-dtsprobe1-runner.sh
still use plain `tar -xf`; not on the staged path, but must not be revived without the same fix.
(b) Defense in depth: extract_checkpoint could reject entries with `mode & 0o022` so a stale checkpoint fails at
restore instead of after the full deploy. Not required for correctness.

## 4. Test quality — PASS
`python3 -m unittest discover -s docs/strict542 -p test_stage608.py`: Ran 17 tests, OK (uid 1000).
The new test (a) statically asserts `umask 022` immediately precedes `mkdir source native-source` and that all
exactly three following `tar` lines start with `tar --no-same-permissions -xf`; (b) extracts a synthetic tar
(0775 dir, 0664 file, 0775 exec) under `umask 002` then `umask 022` and expects 755/644/755.
What it proves: removing the umask line or the flag fails (a); removing the umask also fails (b) as non-root.
What it does not prove: as non-root, part (b) passes even without `--no-same-permissions` (non-root tar applies
umask anyway), so the flag is enforced only by the static check; its runtime effect is proven only when run as
root (commit message claims a root run; my local repro above confirms --same-permissions keeps 664 under umask 022).

## 5. Consequence — CONFIRMED (PASS)
prepare-stage608-export.py:71-76: source_export_sha256 = sha256 of {base_source_archive_sha256, source_commit,
successor_archive_sha256}; the successor archive includes every path changed since the base commit, so it now
includes the new run-stage608.sh. A new runner commit changes source_commit and the successor digest, hence
source_export_sha256. stage608.verify_inputs (stage608.py:115-120) requires every producing-stage receipt's
source_commit and source_export_sha256 to equal the manifest's, so accepted tsccwdf6a4 receipts are rejected.
Independently of identity, those checkpoints carry 0664 modes (item 1). All producing stages (native, checks,
compiler, runtime, unified-0..5, middle, sdk-0/1, tail) must be rerun from fresh exports at the new commit.

VERDICT: APPROVE
