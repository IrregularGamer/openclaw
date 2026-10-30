# job608 middle m674 at 674840b6 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-middle-m674 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  365d4ea6fe52d1e2f7308f15360b9cab237d6f2d7bdf7fb198b26eaca9932b0d, source_commit 674840b6,
  stage_inputs = native (5a412599), runtime (388d36b8), unified-0..5 m674 (f30faed4, c13d0b6a, 36fcdcbe,
  400a1eac, 0302c32f, 1c9da566). Preflight d5cd807b (no stray __pycache__), independent APPROVE 2dbaa156.
- Fresh gates at launch (launch.txt): health up, no competing run, verify-inputs 0, sh -n 0,
  storage608 check --root P --stage middle 0, 3227s left (>= 2655).
- Launch (same caps as middle tsccwdf6a4): offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-middle
  -- timeout -k 15s 2400s sh run608.sh. Background Bash timeout 2800s; offload client rc 0 (middle-offload.rc).
- Result: exit-code.txt 0, STEP608 middle-build-done +289s, middle-pass; 0 error/fail/cancel lines in build.log.
  Result 115949508 bytes < 134217728 return cap. Receipt 9195d45f3abe9f05e7e1e01e3976713a22c1d1a93d524c089eec5c4c50d7cd9f.
- Mode check: `find result608-middle -perm /022` = 0 entries. Checkpoint listing (`tar -tvzf`, not extracted):
  15533 entries = 13295 files + 1055 dirs + 1183 symlinks; 0 files/dirs group/other-writable. The 1183 symlinks
  list as lrwxrwxrwx (Linux symlink mode is fixed and not used for access); the type counts are identical to the
  middle tsccwdf6a4 checkpoint, so these are not introduced by the rerun. Disclosed for the acceptance reviewer; the
  package stage's apply598 check (symlink/0o022 refusals) remains unchanged and authoritative.
  checkpoint.tar.gz b80f8116637bf6d9cd12ab4b0266862b0b8dbdb8d7d6099dcdfb74add96ad4c1 (kept in P only, not committed).
  result-files.sha256 lists every returned file; offload log gzip -n.
- Next: independent acceptance, then sdk-0 m674 in a fresh worker (one launch per worker). 595 MUST NOT APPLY.
  No install/seal/root/unit/sudo/service changes.
