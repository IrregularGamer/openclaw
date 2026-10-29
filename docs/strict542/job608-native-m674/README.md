# job608 native m674 at 674840b6 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-native-m674 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  738684f384b11cd40db2f3daa21d8f1460fb4f15b7e7673e371d80c52ef2dbf5, source_commit = runner_commit = 674840b6
  (reviewed umask/--no-same-permissions fix, APPROVE 017cd166). Preflight independent APPROVE 6049ed36.
- Fresh gates at launch 20:20:49Z: health up, no competing run, no result/log/rc, verify-inputs 0, sh -n 0,
  storage608.py check --stage native 0, 3278s left.
- Launch (same caps as tsccwdf6a4): offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh
- offload rc 0, inner exit-code.txt 0, STEP608 native-rebuild-pass; result 48651969 B (< 64 MiB return cap).
- rolldown-binding.linux-x64-gnu.node sha256 0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042,
  byte-identical to the superseded tsccwdf6a4 native build (deterministic rebuild across commits).
- Mode check: `find result608-native -perm /022` = 0 entries (no group/other-writable result files).
- Committed: offload log/rc, all non-binary result files, result-files.sha256 for every file. Binding stays only in P.
- Next (fresh worker): independent acceptance of THIS run, then checks/compiler/runtime at 674840b6 per
  job608-after-package-moderefusal-continuation.md. 595 MUST NOT APPLY. No install/seal/root/unit/sudo/service changes.
