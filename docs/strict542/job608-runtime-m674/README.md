# job608 runtime m674 at 674840b6 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-runtime-m674 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  7b4724f9b7dc55ff983c66ec096aa1e8c86fd69e6c211c462c8596300e91de70, source_commit 674840b6,
  stage_inputs = native m674 (addon 0b6607e7, accepted 5a412599). Preflight independent APPROVE 4b777a33.
- Fresh gates at launch (22:48:55Z): health up, no competing run, verify-inputs 0, sh -n 0,
  storage608 check --root P --stage runtime 0 (free 4860137472), ~3150s left (>= 2655).
- Launch (same caps as tsccwdf6a4): offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-runtime
  -- timeout -k 15s 2400s sh run608.sh. Background Bash with timeout 2800s; offload client rc captured: 0 (runtime-offload.rc).
- Result: exit-code.txt 0, stage-receipt exit_code 0, STEP608 runtime-build-done +726s, runtime-pass.
- Mode check: `find result608-runtime -perm /022` = 0 entries; checkpoint listing (`tar -tvzf`, not extracted)
  8959 entries, 0 group/other-writable. checkpoint.tar.gz 6178cfd9060d8ab1080867f38b212230d0fb1faaa565167c28282efe77619a0e
  (kept in P only, not committed; 88.6 MB result). result-files.sha256 lists every returned file.
- Next: independent acceptance, then unified-0 m674 in a fresh worker with --input native+compiler+runtime m674 results
  per the stage DAG. 595 MUST NOT APPLY. No install/seal/root/unit/sudo/service changes.
