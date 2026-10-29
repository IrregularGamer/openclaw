# Job 608 unified-3 tsccwdf6a4: independent acceptance

Independent review dated 2026-10-29. Scope: the actual unified-3 run only, frozen source
`f6a4de2ebc6924d16fe559f9858bf8c50dce1eba`, common export
`e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145`.
Evidence commit `54a012d5`; launch `b6d2c1b0`; independent batch preflight `40bd39fa`
(`docs/strict542/job608-unified1-5-tsccwdf6a4-preflight.json`, `stages[2]`); accepted
unified-1 `8d229ccb`, accepted unified-2 `16819bd2`. P denotes
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private`. The reviewer did not
produce this evidence.

## Verified

- Private `P/unified-3-tsccwdf6a4-offload.rc`, committed `unified-3-offload.rc`, and result
  `exit-code.txt` (private and committed) all contain bytes `0\n`. The decompressed
  committed outer log is byte-identical to the private outer log (SHA256 `ec50b805...1b58`,
  7 lines). It records native-start +11s, restore-build-done +19s, build-start +23s with
  2257s budget, build-done +433s, and `unified-3-pass`. The launch record's single offload
  command (`--timeout 2460 --mem 14g --cpus 4`, inner `timeout -k 15s 2400s`) equals the
  preflight launch parameters and the README.
- The private result contains exactly the five files named by `result-files.sha256`;
  `sha256sum -c` run inside `P/stage-unified-3-tsccwdf6a4/result608-unified-3`
  passes for all five. Total returned bytes: 1243806. The four committed result copies
  pass the same check from the committed result directory and are `cmp`-identical to the
  private originals. The 1232752-byte checkpoint
  (`0ebfb963...62432b`) remains private. Evidence files are unchanged since `54a012d5`.
- `P/stage-unified-3-tsccwdf6a4/export-manifest.json` SHA256 is exactly
  `4a43a68bc9df54b83547d20b04c8b345f6e54c1ec735c853d49cebada38054f0`.
- Receipt SHA256 is `c80d60282536ff312f99a03622dc1e4128332a0a832a2fc99718220f32e7c09f`.
  Kind `JOB608_STAGE_RECEIPT`, stage `unified-3`, exit_code 0, run_id
  `stage608-unified-3-tsccwdf6a4`, manifest_sha256 `4a43a68b...054f0`. These equal the
  preflight `stages[2]` (stage, run_id, manifest_sha256, directory; its
  predecessor_manifest_sha256 `3a1b42d1...708a` is the accepted unified-0 manifest, as for
  unified-1/unified-2). Source and common export equal the frozen values above.
- Receipt stage_inputs equal the preflight `common.stage_inputs` and the manifest's
  exact seven pins (same seven hashes accepted for unified-0/1/2; native
  `57742314`, runtime `5824b14b`). Streaming hashes of each staged file under
  `stage608-inputs/` match. The manifest's base source, compiler upstream, native
  export, successor archive, runner and stage-helper hashes and commits all equal the
  preflight `common`; staged `run608.sh`, `stage608.py` and `successor598.tar` hash to
  those values.
- Receipt output hashes match the actual build log
  `f330586a32244be82abfa96c33c1d1ab1e09e7ce94d34d199afdfaa6eb21947f`
  and checkpoint
  `0ebfb963f97bc16c52b93a7b75f7b6823c03af9404b1faea6e5ce2858562432b`.
- The complete 244-line build log shows `openclaw-dts-extensions-3: cache miss (disabled)`
  and ends with the tsdown invocation `1/1 finished in 294.2s`, followed by
  `phase timings: no phases ran`, consistent with the frozen owner path for unified
  groups, as for unified-0/1/2.
- No actual error TS, ERR!, failed, cancel, exit-code, fatal, timeout, OOM, killed, or
  signal failure lines. The only warning-related lines are the
  package-manager-warning script name and the experimental TypeScript API notice;
  `signal-utils` and `@lit-labs/signals` are package names, not signal failures.
- README figures checked against the logs and files: build-done +433s, tsdown 294.2s,
  1243806 returned bytes, receipt and checkpoint SHA256 all match. (The same evidence
  commit also corrects the unified-2 README tsdown figure to 293.1s, resolving the
  non-blocking finding from `16819bd2`; no unified-2 hashed file changed.)
- Frozen `scripts/lib/tsdown-config-groups.mts` gives non-SDK groups
  `[openclaw-dts-base, openclaw-dts-extensions-1..5]`, so unified-3 owns
  `openclaw-dts-extensions-3`. Read-only in-memory archive inspection (no extraction)
  finds 30 entries: 12 directories and 18 regular files, all beneath
  `unified/openclaw-dts-extensions-3` or its `unified/openclaw-dts-extensions-3.build608.json`
  sidecar. No links, special entries, duplicate paths, absolute or `..` paths, or
  setuid/setgid/sticky bits.
- The sidecar (schema `strict542-build-group-binding608-v1`) and group receipt agree
  (sidecar.receipt equals receipt.json), carry `COMPILED_GROUP_NOT_PUBLISHED`, kind
  `unified`, group `openclaw-dts-extensions-3`, and bind the frozen source/common export
  and accepted native compile/libtests/addon hashes. The sidecar identity is equal to
  the accepted unified-1 and unified-2 sidecar identities. The recomputed complete group
  inventory digest (frozen `workspaceInventory608` + `digest608` algorithm, 28 entries) is
  `cc0194374d7da5993daf59850775f92b9fc0a58648c5b332e97a29c2ea5ce7fc`, equal to the
  binding. Predecessor digest `25ffcb65...8770` equals the digest of the runtime receipt
  read directly from the staged accepted runtime checkpoint archive, and equals the
  predecessor in the accepted unified-1 and unified-2 checkpoint bindings (frozen
  `buildStage608` makes every unified group's predecessor `runtime`, not the previous
  unified group). The artifact record equals receipt.record; all 15 of its output hashes
  match the 15 files under `data/` (no unlisted files), including
  `compiler-inputs/openclaw-dts-extensions-3.json` and all eight required extension
  `.d.ts` outputs (browser, crabbox, github-copilot, lmstudio x2, openrouter, sglang,
  together).
- `python3 -I -B docs/strict542/storage608.py check --root P --stage unified-3` exits 0
  (return_cap_bytes 33554432, free above reserve). `storage608.py result --stage
  unified-3 --result P/stage-unified-3-tsccwdf6a4/result608-unified-3` exits 0,
  returning 1243806 logical bytes below the 33554432-byte return cap.

## Ordering

Unified-3 was launched (`b6d2c1b0`) before unified-2 acceptance was recorded; unified-2
was then independently accepted at `16819bd2`. This does not affect validity: unified-1,
unified-2 and unified-3 are independently preflighted sibling exports of the same
accepted unified-0/runtime predecessor (`stages[0..2]` share predecessor manifest
`3a1b42d1...708a`), unified-3 consumes no unified-1/unified-2 output, and its checkpoint
binds runtime. The launch record made unified-3 acceptance conditional on unified-2
acceptance, and that condition is now met.

## Findings (non-blocking)

None.

## Scope and limits

The manifest's `execution_state: UNUSED` remains immutable prelaunch metadata;
the actual run evidence establishes that this stage is SPENT and must not replay.
This accepts unified-3 only. Stage unified-4 and later were not touched or reviewed.
No build, test, offload, extraction, installed-state, root, service, or queue mutation
was run by this review; only this requested review document and its Git publication
change.

No installation or release authority; 595 MUST NOT APPLY.

VERDICT: ACCEPT unified-3 tsccwdf6a4 at f6a4de2e. No blocking findings;
rc 0, exact five-file inventory, receipt/preflight/manifest bindings, successful
openclaw-dts-extensions-3 group production, owned checkpoint and storage return
verified. 595 MUST NOT APPLY.
