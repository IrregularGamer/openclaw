# job608 sdk-1 m674 at 674840b6 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-sdk-1-m674 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  23f06cb093235b4fe9141cd114be54ec350a9f0b49e7d8e0766cd8c439763759, source_commit 674840b6,
  stage_inputs = native m674 (5a412599), middle m674 (dc75babf). Preflight 6eb72338 (no stray __pycache__),
  independent APPROVE 735c912a.
- Fresh gates at launch (launch.txt): health up, no competing run, verify-inputs 0, sh -n 0,
  storage608 check --root P --stage sdk-1 0, 3143s left (>= 2655).
- Launch (same caps as sdk-1 tsccwdf6a4): offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-sdk-1
  -- timeout -k 15s 2400s sh run608.sh. Background Bash timeout 2800s; offload client rc 0 (sdk-1-offload.rc).
- Result: exit-code.txt 0, STEP608 sdk-1-build-done +136s (tsccwdf6a4: +137s), sdk-1-pass (offload log); 0 error/fail/cancel lines in build.log.
  build.log tail "tsdown-build invocation 1/1 finished in 2.3s" / "phase timings: no phases ran" (same as tsccwdf6a4).
  Result 42043 bytes, under return cap. Receipt c4911678dfefc01d9920f23b0e08dae5df15b9c6fc2aa5ffa494905a6e0dc368.
- Mode check: `find result608-sdk-1 -perm /022` = 0 entries. Checkpoint listing (`tar -tvzf`, not extracted):
  8 entries = 4 files + 4 dirs, 0 symlinks, 0 group/other-writable; sorted name set identical to the sdk-1
  tsccwdf6a4 checkpoint (diff empty).
  checkpoint.tar.gz 8a0f1f2eb6e0797f802c40fe9e32317b92accd7dac2650f557adf967bb10e4e1 (kept in P only, not committed).
  result-files.sha256 lists every returned file; offload log gzip -n.
- Next: independent acceptance, then tail m674 in a fresh worker (one launch per worker). 595 MUST NOT APPLY.
  No install/seal/root/unit/sudo/service changes.
