# Independent source review: job608 materialize (b246ebeb)

Scope: `git show b246ebeb` only (build598.sh +3, frozen-package608.py +31/-2, test_frozen_package608.py +17).

## Checks

1. **Refusals not weakened.** application598.py is untouched by the commit; line 92 still `require(info.st_nlink == 1, 'hardlink refused: ' + relative)`. frozen-package608 `regular()`, `preflight()` (env policy refusal + PINS) and `receipt()` are byte-identical. The CLI still refuses any argument other than the three subcommands.
2. **materialize safety.**
   - Refuses a symlinked or non-directory `result598-build/runtime` (test included).
   - `os.walk(..., followlinks=False)`: symlinked dirs are listed but never entered; symlinked/broken entries in `files` are skipped via `lstat` + `S_ISREG`. Only regular files with nlink>1 are touched.
   - Writes stay inside runtime: temp is `path.with_name('.materialize608-'+name)` in the same real directory (os.walk only yields real dirs under the checked root), opened `O_CREAT|O_EXCL|O_NOFOLLOW` 0600, then `os.replace` on the same filesystem.
   - Mode preserved via explicit `chmod(S_IMODE(original))`, so umask has no effect. Content is checked by re-reading the temp and comparing its sha256 to the bytes read, and the temp must have nlink==1 before the replace.
   - Bounded to 300000 file entries. No byte cap: each file is read whole into memory. That's fine for npm payloads (esbuild ~10 MB).
   - Edge cases (all fail closed or harmless): if a pre-existing `.materialize608-<name>` exists, `O_EXCL` fails with FileExistsError and `set -eu` aborts the build. A temp name over 255 bytes fails with ENAMETOOLONG and aborts. Temps created during the walk aren't revisited, because the `files` list was already read for that directory. A temp left by a failed run is never cleaned up, but the build has already aborted at that point, and the next run starts from a fresh deploy.
   - TOCTOU: there's a gap between the lstat/read and the replace (a file could be swapped for a symlink, or the original changed after the read). In this single-user remote build nobody else writes to the tree, so it isn't exploitable in practice. The hash check confirms the copy was written correctly. It does not prove the original was unchanged at replace time. Acceptable.
   - mtime/ownership are not preserved (the new inode belongs to the build user). Nothing downstream checks package-file mtime: application598's mtime fields cover seal/backup metadata, not package inventory.
3. **Receipt/evidence chain holds.** materialize runs after deploy and before `receipt`. `deploy.log` lives outside runtime and is never touched. If runtime `pnpm-lock.yaml` were hardlinked it would be replaced by a byte-identical private copy. `target_lock_sha256` stays the same, and receipt's `regular()` nlink check then passes on genuinely private content. BUILD_EVIDENCE asserts (source lock pin, target lock, deploy log) are unchanged.
4. **Pins and policy unchanged.** `PINS` and .npmrc/pnpm-lock.yaml are not modified. The commit adds no env-based pnpm/npm policy, and the deploy command is unchanged.
5. **Tests** (`python3 -I -B -m unittest discover -s . -p <file>` in docs/strict542): test_frozen_package608 8 OK; test_application598 19 OK; test_stage608 17 OK; test_diagnose_native_api608 20 OK.

## Findings

- No blocking issues.
- Minor/non-blocking:
  - No byte cap on per-file reads.
  - The temp-collision error is FileExistsError rather than ValueError. It still fails closed.
  - The original file is not re-hashed at replace time. This is acceptable because only one user writes to the build tree.

VERDICT: APPROVE
