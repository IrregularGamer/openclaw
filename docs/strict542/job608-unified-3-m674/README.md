# job608 unified-3 m674 at 674840b6 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-unified-3-m674 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  de4ec8896e749ea0361a4f623c3867db8239c417f5a3334c80f35a46c973f1f6, source_commit 674840b6,
  stage_inputs = native m674 (accepted 5a412599) + runtime m674 (accepted 388d36b8).
  Preflight e1d27a31 (stray import __pycache__ moved with `mv -n` to P/trash-608 since trash is not on PATH;
  verify-inputs rerun with python3 -I -B = 0), independent APPROVE 1d3f2b9b.
- Fresh gates at launch (see launch.txt): health up, no competing run (load 0.33), verify-inputs 0, sh -n 0,
  storage608 check --root P --stage unified-3 0 (free 4691165184), 3292s left (>= 2655).
- Launch (same caps as tsccwdf6a4): offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-3
  -- timeout -k 15s 2400s sh run608.sh. Background Bash with timeout 2800s; offload client rc captured: 0 (unified-3-offload.rc).
- Result: exit-code.txt 0, STEP608 unified-3-build-done +445s, unified-3-pass.
- Mode check: `find result608-unified-3 -perm /022` = 0 entries; checkpoint listing (`tar -tvzf`, not extracted)
  30 entries (same name set as tsccwdf6a4 unified-3), 0 group/other-writable. checkpoint.tar.gz
  b5b3a5b1d59c9dd45553985e308f095917c7a5913923e9c4e6cbcccf90422617 (kept in P only, not committed; build.log likewise).
  result-files.sha256 lists every returned file.
- Next: independent acceptance, then unified-4 m674 in a fresh worker (one launch per worker) with
  --input native m674 + runtime m674 results. 595 MUST NOT APPLY. No install/seal/root/unit/sudo/service changes.
