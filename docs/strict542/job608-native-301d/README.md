# job608 native 301d at exact 301d7456 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-native-301d (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest b61f89b59122ba32fbfbc192918c4af94987ab3e8e23c1c15779519c9ff815b0,
  source_commit = runner_commit = 301d7456, no input_lineage. Preflight 7c55092a, independent APPROVE a86f43a3.
- Fresh gates at launch 2026-10-30T05:48:56Z: health up, no competing run, no result/log/rc, storage608 check native 0, ~3100s left.
- Launch (m674 caps): offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh
- offload rc 0, inner exit-code.txt 0; result 48652047 B (< 64 MiB return cap).
- rolldown-binding.linux-x64-gnu.node sha256 0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042,
  byte-identical to native m674/tsccwdf6a4 (deterministic across commits).
- Mode check: `find result608-native -perm /022` = 0 entries.
- Committed: offload log/rc, all non-binary result files, result-files.sha256 for every file. Binary stays only in P.
- Next (fresh worker): independent acceptance of THIS run, then compiler-301d (--input P/stage-native-301d/result608-native,
  base/caps from compiler m674). 595 MUST NOT APPLY. No install/seal/root/unit/sudo/service changes.
