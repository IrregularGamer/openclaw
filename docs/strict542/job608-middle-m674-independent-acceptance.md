# job608 middle m674 at 674840b6 - independent acceptance

Verdict: **ACCEPT** (SOURCE ONLY; nothing installed; #595 MUST NOT APPLY).

Reviewer: independent (read-only; no launches, installs, or modifications; checkpoint listed only, never extracted).
Evidence commit: 3e82f488 (docs/strict542/job608-middle-m674/). Preflight: docs/strict542/job608-middle-m674-preflight.json
(d5cd807b), independent APPROVE 2dbaa156 (manifest 365d4ea6fe52d1e2f7308f15360b9cab237d6f2d7bdf7fb198b26eaca9932b0d).
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private. Model: job608-unified-5-m674-independent-acceptance.md.
Rules: job608-after-package-moderefusal-continuation.md.

## 1. Receipt and hashes
- sha256(P/stage-middle-m674/export-manifest.json) = 365d4ea6... = receipt manifest_sha256 = preflight manifest_sha256.
- Receipt: kind JOB608_STAGE_RECEIPT, stage middle, run_id stage608-middle-m674, source_commit
  674840b669c43af54a62e30b4028f219f4a428c9 (= preflight), source_export_sha256 e1a6de35...4461b (same as unified-5 m674),
  exit_code 0. stage_inputs bind native (2f81179f/4a651254/0b6607e7/0bb266db), runtime (c6436d6a/6178cfd9/935e56f1) and
  unified-0..5 m674 (unified-5: 99b56226/737515b7/39ec47f7, matching the accepted unified-5 m674 outputs).
- Receipt outputs build.log e4d68407... and checkpoint.tar.gz b80f8116... equal the live files.
- `sha256sum -c result-files.sha256` run from P/stage-middle-m674: 5/5 OK. Committed exit-code.txt,
  strict542-checks/pnpm-path.txt and middle/stage-receipt.json are cmp-identical to live.

## 2. Run completion
- Committed middle-offload.rc = P/middle-m674-offload.rc = 0; live exit-code.txt = 0; committed log gz decompresses
  byte-identical to P/middle-m674-offload.log.
- STEP608 markers (offload log): middle-stage-native-start +11s, restore-build-done +19s, build-start budget=2257s +23s,
  middle-build-done +289s, middle-pass. Note: `middle-pass` is a runner marker in the offload log, not a line in
  middle/build.log (same as earlier stages); build.log (261 lines) ends with the build-all phase-timings line
  (total 2m 28.9s) and has 0 matches for error|fail|cancel (case-insensitive).
- offload runs.log: `2026-10-30T01:47:40Z run remote rc=0 561s .../stage-middle-m674`.
- launch.txt: gates vi0 shn0 storage0, manifest 365d4ea6, APPROVE 2dbaa156, ONE launch, 3227s left.

## 3. Size and modes
- result608-middle = 115949508 bytes < 134217728 return cap.
- `find result608-middle -perm /022` = 0 entries.
- `tar -tvzf middle/checkpoint.tar.gz` (list only): 13295 regular files, 1055 dirs, 1183 symlinks; 0 regular files or
  dirs with group/other write. The 1183 symlinks list as lrwxrwxrwx.
- Entry name list cmp-identical to P/stage-middle-tsccwdf6a4/result608-middle/middle/checkpoint.tar.gz; the sorted
  (name, ->, target) symlink sets are identical (md5 7fcdec1b...) in both checkpoints.

## 4. Symlink decision (key question)
The rule "zero group/other-writable entries" is satisfied. Reasons:
1. Linux symlink mode bits are always 0777 and are never used for access checks (permission to change a link is the
   parent directory's write bit; following it uses the target's mode). A link cannot be made non-0777, so the rule can
   only be meaningful for files and dirs; every parent dir here is non-writable by group/other and every target is a
   regular file in the checked set.
2. The consumer already encodes exactly this interpretation, unchanged: docs/strict542/application598.py `inventory()`
   requires `S_ISLNK(mode) or not mode & 0o7022`, and for links requires a relative target that resolves (strict) inside
   the runtime root. apply598.py `protected()` only checks the root-owned install parent chain, not the tree.
3. Targets do not escape. All 1183 links live under middle/data/dist-runtime/ and are relative
   (e.g. `middle/data/dist-runtime/extensions/a2a/api.d.ts -> ../../../dist/extensions/a2a/api.d.ts`). Resolving each
   against its directory: 0 absolute, 0 escaping, all 1183 resolve under middle/data/dist/, and 0 targets are missing
   from the archive (so application598's strict resolve will not hit a broken link).
4. The package stage's restore (stage608.py `extract_checkpoint`) allows only dir/file/symlink entries without
   setuid/setgid/sticky, rejects absolute links or any link whose normalized target is not under `middle/data/`, then
   uses `extractall(filter='data')` (which also refuses escaping links) and re-chmods only non-symlink entries. These
   links pass all of that. The package tsccwdf6a4 refusal was a 0664 regular file (CHANGELOG.md), not a symlink.
Not a weakening: group/other-writable regular files or dirs would still REFUSE; only the immutable symlink bits are
read as non-applicable, exactly as application598 already does. No source fix needed.

## 5. Scope and secrets
- 2dbaa156..3e82f488 touches only docs/strict542/job608-middle-m674/ (0 other paths): no install/seal/root/unit/sudoers change.
- Committed log gz: 0 matches for token/secret/password/private key/api key/ghp_/AKIA/bearer.
  checkpoint.tar.gz and build.log are not committed.

## Verdict
ACCEPT middle m674 (checkpoint b80f8116, receipt 9195d45f) as the middle input for the next stage at 674840b6.
