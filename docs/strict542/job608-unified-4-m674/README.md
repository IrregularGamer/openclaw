# job608 unified-4 m674 at 674840b6 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-unified-4-m674 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  e829ea958fbb546548c2afe273cab7dbd5a7698b6a875c82f5324dc144e4b469, source_commit 674840b6,
  stage_inputs = native m674 (accepted 5a412599) + runtime m674 (accepted 388d36b8).
  Preflight 783031cf (stray import __pycache__ moved with `mv -n` to P/trash-608/unified-4-m674-pycache;
  verify-inputs with python3 -I -B = 0), independent APPROVE f48fb963.
- Fresh gates at launch (see launch.txt): health up, no competing run (load 0.12), verify-inputs 0, sh -n 0,
  storage608 check --root P --stage unified-4 0, 3301s left (>= 2655).
- Launch (same caps as unified-3 m674): offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-4
  -- timeout -k 15s 2400s sh run608.sh. Background Bash with timeout 2800s; offload client rc captured: 0 (unified-4-offload.rc).
- Result: exit-code.txt 0, STEP608 unified-4-build-done +419s, unified-4-pass.
- Mode check: `find result608-unified-4 -perm /022` = 0 entries; checkpoint listing (`tar -tvzf`, not extracted)
  32 entries (same name set as tsccwdf6a4 unified-4), 0 group/other-writable. checkpoint.tar.gz
  bebc68d070034bf361c3dc39aed6c2fde5eee5590fa1a90b20835ab3179170b5 (kept in P only, not committed; build.log likewise).
  result-files.sha256 lists every returned file.
- Next: independent acceptance, then unified-5 m674 in a fresh worker (one launch per worker) with
  --input native m674 + runtime m674 results. 595 MUST NOT APPLY. No install/seal/root/unit/sudo/service changes.
