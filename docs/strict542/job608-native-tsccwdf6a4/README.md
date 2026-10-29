# job608 native tsccwdf6a4 at f6a4de2e — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-native-tsccwdf6a4, manifest b51a34e949a4322f891b34d200c7d87f58333ab854209c0e4b4c2f5703a9f9f6,
  preflight independently APPROVED 54587210. Fresh gates at launch 13:3xZ: health up, no competing run,
  verify-inputs 0, storage608.py check --root P --stage native 0 (unique 1678259202 B, free 5645930496 B).
- Launch: offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh
- offload rc 0, inner exit-code.txt 0, STEP608 native-rebuild-pass; result 48652053 B (< 64 MiB return cap); finished 14:08Z.
- rolldown-binding.linux-x64-gnu.node sha256 0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042 (native/ and result598-native/ copies byte-identical);
  receipt addon_sha256 prefix 0b6607e73d6f. Compaction tests ok (0 failed).
- Committed: offload log/rc, all non-binary result files, result-files.sha256 for every file. The 24 MB binding
  stays only in P (hash above); not committed.
- Next (fresh worker): independent acceptance of THIS run, then runtime stage at f6a4de2e through unchanged gates.
  595 MUST NOT APPLY. No install/seal/root/unit/sudo/service changes.
