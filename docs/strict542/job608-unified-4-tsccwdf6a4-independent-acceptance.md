# Job 608 unified-4 tsccwdf6a4: independent review (CHANGES REQUESTED)

Independent review dated 2026-10-29. Scope: the actual unified-4 run only, frozen source
`f6a4de2ebc6924d16fe559f9858bf8c50dce1eba`, common export
`e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145`.
Evidence commit `89623de8`; launch record `54a012d5`
(`docs/strict542/job608-after-unified3-tsccwdf6a4-continuation.md`); independent batch
preflight `40bd39fa` (`docs/strict542/job608-unified1-5-tsccwdf6a4-preflight.json`,
`stages[3]`); accepted unified-1 `8d229ccb`, unified-2 `16819bd2`, unified-3 `6cfa1e2d`.
P denotes `/srv/encrypted/dev-move-98/agentq-source608-20261028-private`. The reviewer
did not produce this evidence.

## Blocking finding (evidence publication only)

- Evidence commit `89623de8` does not contain the committed copy of
  `result608-unified-4/unified-4/build.log`. It adds only three result copies
  (`exit-code.txt`, `strict542-checks/pnpm-path.txt`, `unified-4/stage-receipt.json`);
  `git ls-files` confirms the build log is untracked because `.gitignore:215` (`*.log`)
  ignores it. The README states "other four files committed byte-for-byte", which is
  false for the published commit. Unified-3 (`54a012d5`) committed its build log, and its
  acceptance verified four committed copies; that check cannot pass here.
- The build log exists only as an ignored working-tree file in this clone. That file is
  `cmp`-identical to the private original (SHA256
  `dc2337e8c7fb6e67d33bab1cfd21794b01d4fc9bfba5bda4d3d0b34f38b51fff`, 241 lines, 9308
  bytes), so the fix is mechanical.
- Required change: a follow-up evidence commit that force-adds
  (`git add -f`) exactly
  `docs/strict542/job608-unified-4-tsccwdf6a4/result608-unified-4/unified-4/build.log`
  with that SHA256, changing no other hashed file. A later independent review can then
  record ACCEPT. Do not relaunch unified-4. The stage is SPENT.

## Verified (all other checks hold)

- Private `P/unified-4-tsccwdf6a4-offload.rc`, committed `unified-4-offload.rc`, and result
  `exit-code.txt` (private and committed) all contain bytes `0\n`. The decompressed
  committed outer log is byte-identical to the private outer log (SHA256 `e027e7ad...25c3`,
  7 lines). It records native-start +11s, restore-build-done +19s, build-start +21s with
  2259s budget, build-done +417s, and `unified-4-pass`. The launch record's single offload
  command (`--timeout 2460 --mem 14g --cpus 4`, inner `timeout -k 15s 2400s`) equals the
  preflight `launch` parameters and the README.
- The private result contains exactly the five files named by `result-files.sha256`;
  `sha256sum -c` run inside `P/stage-unified-4-tsccwdf6a4/result608-unified-4`
  passes for all five. Total returned bytes: 1220394. The three committed result copies
  (plus the ignored working-tree build log) pass the same check from the committed result
  directory and are `cmp`-identical to the private originals. The 1209767-byte checkpoint
  (`03da89d6...7731b3`) remains private. Evidence files are unchanged since `89623de8`.
- `P/stage-unified-4-tsccwdf6a4/export-manifest.json` SHA256 is exactly
  `e406475889b8e83d6fe2f369a41a5adf1d1f69f94933933d1d808cb0f353fc4f`.
- Receipt SHA256 is `0d6c99fec370e44b2a0d4e2f7c4a5f0f9cc3488d1fa3b16b3835a515f2cb208c`.
  Kind `JOB608_STAGE_RECEIPT`, stage `unified-4`, exit_code 0, run_id
  `stage608-unified-4-tsccwdf6a4`, manifest_sha256 `e4064758...4fc4f`. These equal the
  preflight `stages[3]` (stage, run_id, manifest_sha256, directory; its
  predecessor_manifest_sha256 `3a1b42d1...708a` is the accepted unified-0 manifest, as for
  unified-1/2/3). Source and common export equal the frozen values above.
- Receipt stage_inputs equal the preflight `common.stage_inputs` and the manifest's
  exact seven pins. These are the same seven hashes accepted for unified-0/1/2/3 (equal
  to the committed unified-3 receipt; native `57742314`, runtime `5824b14b`). Streaming
  hashes of each staged file under `stage608-inputs/` match, and the directory holds no
  unlisted files. The manifest's base source, compiler upstream, native export, successor
  archive, runner and stage-helper hashes and commits all equal the preflight `common`.
  Staged `run608.sh`, `stage608.py` and `successor598.tar` hash to those values.
- Receipt output hashes match the actual build log
  `dc2337e8c7fb6e67d33bab1cfd21794b01d4fc9bfba5bda4d3d0b34f38b51fff`
  and checkpoint
  `03da89d62ddc0a205576277d5f0707ac97c453557378da723ab65100337731b3`.
- The complete 241-line build log shows `openclaw-dts-extensions-4: cache miss (disabled)`
  and ends with the tsdown invocation `1/1 finished in 283.3s`, followed by
  `phase timings: no phases ran`. This is consistent with the frozen owner path for
  unified groups, as for unified-0/1/2/3.
- The log has no actual error TS, ERR!, failed, cancel, exit-code, fatal, timeout, OOM,
  killed, or signal failure lines. The only warning-related lines are the
  package-manager-warning script name and the experimental TypeScript API notice.
  `signal-utils` and `@lit-labs/signals` are package names, not signal failures.
- README figures checked against the logs and files: build-done +417s, tsdown 283.3s,
  1220394 returned bytes, and the receipt and checkpoint SHA256 all match. The exception
  is the "four files committed" claim above.
- Frozen `scripts/lib/tsdown-config-groups.mts` gives non-SDK groups
  `[openclaw-dts-base, openclaw-dts-extensions-1..5]`, so unified-4 owns
  `openclaw-dts-extensions-4`. Read-only in-memory archive inspection (no extraction)
  finds 32 entries: 12 directories and 20 regular files. All are beneath
  `unified/openclaw-dts-extensions-4` or are its
  `unified/openclaw-dts-extensions-4.build608.json` sidecar (plus the `unified` parent
  directory). There are no links, special entries, duplicate paths, absolute or `..`
  paths, or setuid/setgid/sticky bits.
- The sidecar (schema `strict542-build-group-binding608-v1`) and group receipt agree
  (sidecar.receipt equals receipt.json). Both carry `COMPILED_GROUP_NOT_PUBLISHED`, kind
  `unified` and group `openclaw-dts-extensions-4`, and bind the frozen source/common
  export. The sidecar identity's nativeCompile/nativeLibtests/nativeAddon hashes equal
  the staged accepted native `receipt.json`, `libtests-receipt.json` and
  `rolldown-binding.linux-x64-gnu.node`. The sidecar identity equals the accepted
  unified-3 sidecar identity (read in memory from the private unified-3 checkpoint).
- The recomputed complete group inventory digest (frozen `workspaceInventory608` +
  `digest608` algorithm, 30 entries) is
  `785f32c98aa123fd7eee70f28852b7514987dc7d59b7dbe9db1337eba1846971`, equal to the
  binding.
- Predecessor digest `25ffcb65...8770` equals the digest of the runtime receipt read
  directly from the staged accepted runtime checkpoint archive. It also equals the
  predecessor in the accepted unified-3 checkpoint binding, because frozen
  `buildStage608` makes every unified group's predecessor `runtime`.
- `artifact-record.json` equals receipt.record. Its 17 output hashes exactly match the 17
  files under `data/`, with no unlisted files. These include
  `compiler-inputs/openclaw-dts-extensions-4.json` and all eight required extension
  `.d.ts` outputs (canvas runtime-api, cua-computer, google api and runtime-api, nvidia,
  policy, talk-voice, vllm).
- `python3 -I -B docs/strict542/storage608.py check --root P --stage unified-4` exits 0
  (return_cap_bytes 33554432, free 5357789184 above the 2147483648 reserve).
  `storage608.py result --stage unified-4 --result
  P/stage-unified-4-tsccwdf6a4/result608-unified-4` exits 0, returning 1220394 logical
  bytes, below the 33554432-byte return cap. These subcommands do not write.

## Ordering

The launch record `54a012d5` was committed before the unified-3 acceptance `6cfa1e2d`.
It made unified-3 counting conditional on that acceptance, which is now recorded. The
actual unified-4 outer log and result are timestamped 17:08, after `6cfa1e2d` (16:45).
Unified-1..4 are independently preflighted sibling exports of the same accepted
unified-0/runtime predecessor (`stages[0..3]` share predecessor manifest
`3a1b42d1...708a`). Unified-4 consumes no unified-1/2/3 output, and its checkpoint binds
runtime. Ordering does not affect validity.

## Scope and limits

The manifest's `execution_state: UNUSED` is still immutable prelaunch metadata. The
actual run evidence shows that this stage is SPENT and must not replay. This reviews
unified-4 only. Stage unified-5 (currently running) and later were not touched or
reviewed. The review only read P/stage-unified-3 and P/stage-unified-4. It ran no build,
test, offload, extraction, installed-state, root, service, or queue mutation. Its only
changes are this requested review document and its Git publication.

No installation or release authority; 595 MUST NOT APPLY.

VERDICT: CHANGES REQUESTED for unified-4 tsccwdf6a4 at f6a4de2e. The actual run is
verified: rc 0, exact five-file private inventory, receipt/preflight/manifest bindings,
successful openclaw-dts-extensions-4 group production, owned checkpoint and storage
return. The one blocking defect is evidence commit 89623de8, which omits the committed
build.log copy (gitignored `*.log`). Force-add that file (SHA256 dc2337e8...1fff) and
re-review for ACCEPT. Do not relaunch. 595 MUST NOT APPLY.
