# job608 unified-5 m674 at 674840b6 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-unified-5-m674 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  0a57d40c4c41e84f473af238b429001041df3fef1a9647d2077f4340c896e590, source_commit 674840b6,
  stage_inputs = native m674 (accepted 5a412599) + runtime m674 (accepted 388d36b8).
  Preflight 68ea86a5 (stray import __pycache__ moved with `mv -n` to P/trash-608/unified-5-m674-pycache;
  verify-inputs with python3 -I -B = 0), independent APPROVE a699cf94.
- Fresh gates at launch (see launch.txt): health up, no competing run, verify-inputs 0, sh -n 0,
  storage608 check --root P --stage unified-5 0, ~3250s left (>= 2655).
- Launch (same caps as unified-4 m674): offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-5
  -- timeout -k 15s 2400s sh run608.sh. Background Bash with timeout 2800s; offload client rc captured: 0 (unified-5-offload.rc).
- Result: exit-code.txt 0, STEP608 unified-5-build-done +423s, unified-5-pass.
- Mode check: `find result608-unified-5 -perm /022` = 0 entries; checkpoint listing (`tar -tvzf`, not extracted)
  25 entries, 0 group/other-writable. checkpoint.tar.gz
  737515b739b8ac872a6ef1b9ef0a1fca1f1ae6166dbcdbcae3da1862344cc6a1 (kept in P only, not committed; build.log likewise).
  Same name set as the tsccwdf6a4 unified-5r1 checkpoint (P/stage-unified-5r1-tsccwdf6a4).
  result-files.sha256 lists every returned file.
- Next: independent acceptance, then middle m674 in a fresh worker (one launch per worker). 595 MUST NOT APPLY.
  No install/seal/root/unit/sudo/service changes.
