# Independent acceptance: job608 sdk-1 tsccwdf6a4 actual run

Reviewer: independent. I did not produce this evidence. Scope: evidence commit `f28a50ab`
(`job608-sdk-1-tsccwdf6a4/`). P = /srv/encrypted/dev-move-98/agentq-source608-20261028-private.
Result directory P/stage-sdk-1-tsccwdf6a4/result608-sdk-1. All checks were read-only. No
offload was launched, nothing under /srv was modified, and the checkpoint was read through
tarfile/`tar -t` only, never extracted.

## Checks

- PASS: preflight. `job608-sdk0-1-tsccwdf6a4-preflight.md` pins the sdk-1 manifest
  `1474cff7...61f0` and says the next stage may launch in the same worker after an accepted
  run if >=2655s are left. Its independent review (647d59af) ends `VERDICT: APPROVE`, and sdk-0
  acceptance (abd8eff8) ends `VERDICT: ACCEPT`. The README records 2694s left (>=2655). I
  cannot independently re-observe the worker clock, so that figure is a claim.
- PASS: manifest. The SHA256 of `P/stage-sdk-1-tsccwdf6a4/export-manifest.json` is
  `1474cff7f4da3873e348d8662f5e85a6a4f918cba405292ee532a020c5e461f0`, which equals the pin and
  the receipt manifest_sha256. The manifest stage is `sdk-1`. The staged `stage608.py` is
  `cmp`-identical to the committed `docs/strict542/stage608.py`.
- PASS: return codes. The private `P/sdk-1-tsccwdf6a4-offload.rc`, the committed
  `sdk-1-offload.rc`, and both copies of `exit-code.txt` (private and committed) all
  contain `0`.
- PASS: offload log. The decompressed committed `sdk-1-offload.log.gz` is `cmp`-identical to
  the private log. Its entries are the BEFORE/AFTER archive release snapshots,
  sdk-1-stage-native-start +10s, sdk-1-restore-build-done +23s, sdk-1-build-start
  (budget 2254s) +26s, `STEP608 sdk-1-build-done +137s` and `STEP608 sdk-1-pass`.
- PASS: result file hashes. The private result contains exactly five regular files.
  `sha256sum -c result-files.sha256` reports OK for all five.
- PASS: committed copies. exit-code.txt, sdk-1/stage-receipt.json and
  strict542-checks/pnpm-path.txt are `cmp`-identical to the private originals. build.log and
  checkpoint stay private, bound by result-files.sha256 and the receipt.
- PASS: stage receipt. SHA256 `e57265f3879f60f18331c9270f3635c7d5b085579e6a6f75fb64a75ecc6b19ae`.
  The receipt has kind `JOB608_STAGE_RECEIPT`, stage `sdk-1`, exit_code 0 and run_id
  `stage608-sdk-1-tsccwdf6a4`. It binds source_commit `f6a4de2ebc6924d16fe559f9858bf8c50dce1eba`
  and source_export_sha256 `e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145`,
  which equal the manifest. Its outputs are sdk-1/build.log `ab5dfafc...8f89` and
  sdk-1/checkpoint.tar.gz `f31068ea...9640`, and both equal the actual file SHA256.
- PASS: stage inputs. The receipt lists 7 stage_inputs: middle build.log `9d1fdaf9`,
  checkpoint `32ea0475` and stage-receipt `9eb3083c`, plus native libtests-receipt `2f81179f`,
  receipt `4a651254`, rolldown binding `0b6607e7` and stage-receipt `10474857`. Each equals
  both the staged `stage608-inputs` copy and the accepted
  P/stage-middle-tsccwdf6a4/result608-middle or P/stage-native-tsccwdf6a4/result608-native
  original.
- PASS (scrutinised): checkpoint. It is 31785 bytes against 1760089 for sdk-0. `tar -tzvf`
  exits 0 with 8 entries. None is absolute or contains `..`. All are under
  `sdk/openclaw-dts-plugin-sdk-2`, which is exactly stage608.py `checkpoint_path('sdk-1')`
  (`'sdk/openclaw-dts-plugin-sdk-'+str(1+1)`). The entries are artifact-record.json,
  receipt.json, `data/compiler-inputs/openclaw-dts-plugin-sdk-2.json`
  (`{"roots":[],"inputs":[]}`), an empty `data/dist/`, and the sidecar
  `sdk/openclaw-dts-plugin-sdk-2.build608.json`. The inner receipt has schema
  `strict542-declaration-group608-v1`, status `COMPILED_GROUP_NOT_PUBLISHED`, group
  `openclaw-dts-plugin-sdk-2`, source f6a4de2e and export e81e07d2. It has `required` = 0, and
  the record has 0 inputs and 1 output, the compiler-inputs file.
  Why an empty group is correct: in source f6a4de2e, `tsdown.config.ts` builds
  `pluginSdkPartitions = [public entries, non-public entries]`. The comment there says
  "Outside private QA the private SDK partition has no emit roots, so the declaration plugin
  performs no compiler work for it." Non-public entries are only selected when
  `OPENCLAW_BUILD_PRIVATE_QA=1`, and neither run608.sh, stage608.py nor build.log mentions
  PRIVATE_QA. Group index 2 (`openclaw-dts-plugin-sdk-2`) is that private partition. The
  sdk-0 checkpoint (`plugin-sdk-1`, 158 required, 371 outputs) carries all the public SDK
  declarations. An empty sdk-2 is therefore expected, not a lost output. The +137s build
  (mostly the 48s pnpm install, then `tsdown-build invocation 1/1 finished in 2.7s`) fits
  that.
- PASS: build log. 235 lines. `grep -ciE 'error|fail|cancel'` returns 0. It ends with
  `[tsdown-plugin-sdk] openclaw-dts-plugin-sdk-2: cache miss (disabled)`, a TS7
  experimental-API WARN, `[tsdown-build] invocation 1/1 finished in 2.7s` and
  `[build-all] phase timings: no phases ran`.
- PASS: storage. `python3 -I -B docs/strict542/storage608.py result --stage sdk-1 --result
  P/stage-sdk-1-tsccwdf6a4/result608-sdk-1` exits 0, with logical_return_bytes 42148 against
  a cap of 33554432.
- PASS: scope. `git show --stat f28a50ab` touches only 7 files under
  `docs/strict542/job608-sdk-1-tsccwdf6a4/`.

## Notes

- Downstream: the tail stage restores this checkpoint. The checkpoint is valid by
  extract_checkpoint's rules (root + sidecar present), but tail must tolerate an empty
  `data/dist/` for plugin-sdk-2. That belongs to tail preflight, not to this acceptance.
- The 2694s-left gate figure is taken from the README. The offload log does not echo it.

VERDICT: ACCEPT
