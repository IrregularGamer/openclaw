# Job 608 unified-2 tsccwdf6a4: independent acceptance

Independent review dated 2026-10-29. Scope: the actual unified-2 run only, frozen source
`f6a4de2ebc6924d16fe559f9858bf8c50dce1eba`, common export
`e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145`.
Evidence commit `b6d2c1b0`; launch `7b3ca6df`; independent batch preflight `40bd39fa`
(`docs/strict542/job608-unified1-5-tsccwdf6a4-preflight.json`, `stages[1]`); accepted
unified-1 `8d229ccb`. P denotes
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private`. The reviewer did not
produce this evidence.

## Verified

- Private `P/unified-2-tsccwdf6a4-offload.rc`, committed `unified-2-offload.rc`, and result
  `exit-code.txt` (private and committed) all contain bytes `0\n`. The decompressed
  committed outer log is byte-identical to the private outer log (SHA256 `50fa2fe3...e8f3`,
  7 lines). It records native-start +11s, restore-build-done +19s, build-start +21s with
  2259s budget, build-done +430s, and `unified-2-pass`. The launch record's single offload
  command (`--timeout 2460 --mem 14g --cpus 4`, inner `timeout -k 15s 2400s`) equals the
  preflight launch parameters and the README.
- The private result contains exactly the five files named by `result-files.sha256`;
  `sha256sum -c` run inside `P/stage-unified-2-tsccwdf6a4/result608-unified-2` passes
  for all five. Total returned bytes: 1226040. The four committed result copies pass
  the same check from the committed result directory and are `cmp`-identical to the
  private originals. The 1215090-byte checkpoint
  (`c8202cf8...bafda6`) remains private. Evidence files are unchanged since `b6d2c1b0`.
- `P/stage-unified-2-tsccwdf6a4/export-manifest.json` SHA256 is exactly
  `1fe4787f887d7f7733a0de75cc4cc56540b6f5eb9ad5ad35ec110b07fdcc96c4`.
- Receipt SHA256 is `52b1c90e4bc7a9f8363d1e22ff3c276f4ae5cfb40b5aec781877d638126096d3`.
  Kind `JOB608_STAGE_RECEIPT`, stage `unified-2`, exit_code 0, run_id
  `stage608-unified-2-tsccwdf6a4`, manifest_sha256 `1fe4787f...96c4`. These equal the
  preflight `stages[1]` (stage, run_id, manifest_sha256, directory; its
  predecessor_manifest_sha256 `3a1b42d1...708a` is the accepted unified-0 manifest, as for
  unified-1). Source and common export equal the frozen values above.
- Receipt stage_inputs equal the preflight `common.stage_inputs` and the manifest's
  exact seven pins (same seven hashes accepted for unified-0/unified-1; native
  `57742314`, runtime `5824b14b`). Streaming hashes of each staged file under
  `stage608-inputs/` match. The manifest's base source, compiler upstream, native
  export, successor archive, runner and stage-helper hashes and commits all equal the
  preflight `common`; staged `run608.sh`, `stage608.py` and `successor598.tar` hash to
  those values.
- Receipt output hashes match the actual build log
  `d6d37d984a407d8b4e6e4049a767c6bf8b07e87d7324a3e210ee048f9fd33578`
  and checkpoint
  `c8202cf8c1e9ba38baf7aba36706364c047435d964d711b58be925c270bafda6`.
- The complete 245-line build log shows `openclaw-dts-extensions-2: cache miss (disabled)`
  and ends with the tsdown invocation `1/1 finished in 293.1s`, followed by
  `phase timings: no phases ran`, consistent with the frozen owner path for unified
  groups, as for unified-0/unified-1.
- No actual error TS, ERR!, failed, cancel, exit-code, fatal, timeout, OOM, killed, or
  signal failure lines. The only warning-related lines are the
  package-manager-warning script name and the experimental TypeScript API notice;
  `signal-utils` and `@lit-labs/signals` are package names, not signal failures.
- Frozen `scripts/lib/tsdown-config-groups.mts` gives non-SDK groups
  `[openclaw-dts-base, openclaw-dts-extensions-1..5]`, so unified-2 owns
  `openclaw-dts-extensions-2`. Read-only in-memory archive inspection (no extraction)
  finds 36 entries: 12 directories and 24 regular files, all beneath
  `unified/openclaw-dts-extensions-2` or its `unified/openclaw-dts-extensions-2.build608.json`
  sidecar. No links, special entries, duplicate paths, absolute or `..` paths, or
  setuid/setgid/sticky bits.
- The sidecar (schema `strict542-build-group-binding608-v1`) and group receipt agree
  (sidecar.receipt equals receipt.json), carry `COMPILED_GROUP_NOT_PUBLISHED`, kind
  `unified`, group `openclaw-dts-extensions-2`, and bind the frozen source/common export
  and accepted native compile/libtests/addon hashes. The sidecar identity is equal to
  the accepted unified-1 sidecar identity. The recomputed complete group inventory
  digest (frozen `workspaceInventory608` + `digest608` algorithm, 34 entries) is
  `cc80066b1b1a0b9e2a63daf070ed7c4d935e0eb0e68912daa03e11a362f26bdd`, equal to the
  binding. Predecessor digest `25ffcb65...8770` equals the digest of the runtime receipt
  read directly from the staged accepted runtime checkpoint archive, and equals the
  predecessor in the accepted unified-1 checkpoint binding (frozen `buildStage608` makes
  every unified group's predecessor `runtime`, not the previous unified group).
  The artifact record equals receipt.record; all 21 of its output hashes match the 21
  files under `data/` (no unlisted files), including
  `compiler-inputs/openclaw-dts-extensions-2.json` and all nine required extension
  `.d.ts` outputs (anthropic, github, litellm, minimax, openai, reef, xai).
- `python3 -I -B docs/strict542/storage608.py check --root P --stage unified-2` exits 0
  (return_cap_bytes 33554432, free above reserve). `storage608.py result --stage
  unified-2 --result P/stage-unified-2-tsccwdf6a4/result608-unified-2` exits 0,
  returning 1226040 logical bytes below the 33554432-byte return cap.

## Ordering

Unified-2 was launched (`7b3ca6df`) before unified-1 acceptance was recorded; unified-1
was then independently accepted at `8d229ccb`. This does not affect validity: both are
independently preflighted sibling exports of the same accepted unified-0/runtime
predecessor (`stages[0]` and `stages[1]` share predecessor manifest `3a1b42d1...708a`),
unified-2 consumes no unified-1 output, and its checkpoint binds runtime, not unified-1.
The launch record made unified-2 acceptance conditional on unified-1 acceptance, and that
condition is now met.

## Findings (non-blocking)

- The evidence README states the tsdown invocation `finished in 274.7s`; the actual
  committed and private build log records `293.1s`. Documentation inaccuracy only; the
  hashed build log is authoritative and no binding depends on the README figure.

## Scope and limits

The manifest's `execution_state: UNUSED` remains immutable prelaunch metadata;
the actual run evidence establishes that this stage is SPENT and must not replay.
This accepts unified-2 only. Stage unified-3 and its files (run in progress) were not
touched or reviewed. No build, test, offload, extraction, installed-state, root, service,
or queue mutation was run by this review; only this requested review document and its
Git publication change.

No installation or release authority; 595 MUST NOT APPLY.

VERDICT: ACCEPT unified-2 tsccwdf6a4 at f6a4de2e. No blocking findings;
rc 0, exact five-file inventory, receipt/preflight/manifest bindings, successful
openclaw-dts-extensions-2 group production, owned checkpoint and storage return
verified. 595 MUST NOT APPLY.
