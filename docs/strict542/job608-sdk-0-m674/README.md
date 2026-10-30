# job608 sdk-0 m674 at 674840b6 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-sdk-0-m674 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  7714f4b6680f983d697b914c600c862b0ef6e75142953a1a8d23a2acc4b9534a, source_commit 674840b6,
  stage_inputs = native m674 (5a412599), middle m674 (dc75babf). Preflight b180cbfd (no stray __pycache__),
  independent APPROVE eeac5eab.
- Fresh gates at launch (launch.txt): health up, no competing run, verify-inputs 0, sh -n 0,
  storage608 check --root P --stage sdk-0 0, 3174s left (>= 2655).
- Launch (same caps as sdk-0 tsccwdf6a4): offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-sdk-0
  -- timeout -k 15s 2400s sh run608.sh. Background Bash timeout 2800s; offload client rc 0 (sdk-0-offload.rc).
- Result: exit-code.txt 0, STEP608 sdk-0-build-done +448s, sdk-0-pass; 0 error/fail/cancel lines in build.log.
  Result 1771001 bytes, under return cap. Receipt f51049011a7114b6e636d60e3e7cfd516258fcb95317bbc81b572e0e58f9fdd7.
- Mode check: `find result608-sdk-0 -perm /022` = 0 entries. Checkpoint listing (`tar -tvzf`, not extracted):
  379 entries = 374 files + 5 dirs, 0 symlinks, 0 group/other-writable; sorted name set identical to the sdk-0
  tsccwdf6a4 checkpoint (md5 of sorted names 36a85ffb... both).
  checkpoint.tar.gz 307e76bf703def5f082c6f624044301b83057ec2b23a8f6b38431e7a02d8d209 (kept in P only, not committed).
  result-files.sha256 lists every returned file; offload log gzip -n.
- Next: independent acceptance, then sdk-1 m674 in a fresh worker (one launch per worker). 595 MUST NOT APPLY.
  No install/seal/root/unit/sudo/service changes.
