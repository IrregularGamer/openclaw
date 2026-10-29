# Job 608 unified-1 tsccwdf6a4: independent acceptance

Independent review dated 2026-10-29. Scope: the actual unified-1 run only, frozen source
`f6a4de2ebc6924d16fe559f9858bf8c50dce1eba`, common export
`e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145`.
Evidence commit `62535f54`; launch `5fae23a7`; independent batch preflight `40bd39fa`
(`docs/strict542/job608-unified1-5-tsccwdf6a4-preflight.json`). P denotes
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private`. The reviewer did not
produce this evidence.

## Verified

- Private `P/unified-1-tsccwdf6a4-offload.rc`, committed `unified-1-offload.rc`, and result
  `exit-code.txt` (bytes `0\n`) all contain `0`. The decompressed committed outer log is
  byte-identical to the private outer log (SHA256 `f313a479...6daa`, 7 lines). It records
  native-start +11s, restore-build-done +19s, build-start +20s with 2260s budget,
  build-done +440s, and `unified-1-pass`. The launch record's single offload command
  matches the README.
- The private result contains exactly the five files named by `result-files.sha256`;
  `sha256sum -c` run inside `P/stage-unified-1-tsccwdf6a4/result608-unified-1` passes
  for all five. Total returned bytes: 1252537. The four committed result copies pass
  the same check from the committed result directory and are `cmp`-identical to the
  private originals. The 1241860-byte checkpoint
  (`e1525252...b145270`) remains private. Evidence files are unchanged since `62535f54`.
- `P/stage-unified-1-tsccwdf6a4/export-manifest.json` SHA256 is exactly
  `41793290b24ca68cd61e2bf3027e14951a44efd2e84d0be8677d1a104146b75b`.
- Receipt SHA256 is `c43e9f974425f7abf5d54b7740ef7344789c4118699ac44322145af85f984db1`.
  Kind `JOB608_STAGE_RECEIPT`, stage `unified-1`, exit_code 0, run_id
  `stage608-unified-1-tsccwdf6a4`, manifest_sha256 `41793290...b75b`. These equal the
  preflight `stages[0]` (stage, run_id, manifest_sha256, directory; its
  predecessor_manifest_sha256 `3a1b42d1...708a` is the accepted unified-0 manifest).
  Source and common export equal the frozen values above, as used for unified-0.
- Receipt stage_inputs equal the preflight `common.stage_inputs` and the manifest's
  exact seven pins; these are the same seven hashes accepted for unified-0 (native
  `57742314`, runtime `5824b14b`). Streaming hashes of each staged file under
  `stage608-inputs/` match. The manifest's base source, compiler upstream, native
  export, successor archive, runner and stage-helper hashes and commits all equal the
  preflight `common`; staged `run608.sh`, `stage608.py` and `successor598.tar` hash to
  those values.
- Receipt output hashes match the actual build log
  `031bf42d689ca99f2740e944cdae8f367e228161fdcf74cc23f6ca6cf5cd5f27`
  and checkpoint
  `e1525252c3c6574809e942599b465d4bb1baa69c2fe4984ac70761b689145270`.
- The complete 244-line build log ends with the tsdown invocation
  `1/1 finished in 308.5s`, followed by `phase timings: no phases ran`, which is
  consistent with the frozen owner path for unified groups (empty ordinary label list;
  declaration group produced during preparation), as for unified-0.
- No actual error TS, ERR!, failed, cancel, exit-code, fatal, timeout, OOM, killed, or
  signal failure lines. The only warning-related lines are the
  package-manager-warning script name and the experimental TypeScript API notice;
  `signal-utils` and `@lit-labs/signals` are package names, not signal failures.
- Frozen `scripts/lib/tsdown-config-groups.mts` gives non-SDK groups
  `[openclaw-dts-base, openclaw-dts-extensions-1..5]`, so unified-1 owns
  `openclaw-dts-extensions-1`. Read-only in-memory archive inspection (no extraction)
  finds 29 entries: 10 directories and 19 regular files, all beneath
  `unified/openclaw-dts-extensions-1` or its `unified/openclaw-dts-extensions-1.build608.json`
  sidecar. No links, special entries, duplicate paths, absolute or `..` paths, or
  setuid/setgid/sticky bits.
- The sidecar (schema `strict542-build-group-binding608-v1`) and group receipt agree
  (sidecar.receipt equals receipt.json), carry `COMPILED_GROUP_NOT_PUBLISHED`, kind
  `unified`, group `openclaw-dts-extensions-1`, and bind the frozen source/common export
  and accepted native compile/libtests/addon hashes. The sidecar identity is equal to
  the accepted unified-0 sidecar identity. The recomputed complete group inventory
  digest is `9a606817ff8caaeefb47ac9cb14d9d473f7fbaddca904a687fbfb0c78331635d`, equal to
  the binding. Predecessor digest `25ffcb65...8770` matches the receipt read directly
  from the accepted runtime checkpoint archive, and equals unified-0's predecessor.
  The artifact record equals receipt.record; all 16 of its output hashes match the 16
  files under `data/` (no unlisted files), including
  `compiler-inputs/openclaw-dts-extensions-1.json` and the required extension `.d.ts`
  outputs.
- `python3 -I -B docs/strict542/storage608.py check --root P --stage unified-1` exits 0
  (it did not refuse the spent stage; output reports return_cap_bytes 33554432, free
  above reserve). `storage608.py result --result
  P/stage-unified-1-tsccwdf6a4/result608-unified-1 --stage unified-1` exits 0,
  returning 1252537 logical bytes below the 33554432-byte return cap.

## Scope and limits

The manifest's `execution_state: UNUSED` remains immutable prelaunch metadata;
the actual run evidence establishes that this stage is SPENT and must not replay.
This accepts unified-1 only. Stage unified-2 and its files were not touched or reviewed.
No build, test, offload, extraction, installed-state, root, service, or queue mutation
was run by this review; only this requested review document and its Git publication
change.

No installation or release authority; 595 MUST NOT APPLY.

VERDICT: ACCEPT unified-1 tsccwdf6a4 at f6a4de2e. No acceptance findings;
rc 0, exact five-file inventory, receipt/preflight/manifest bindings, successful
openclaw-dts-extensions-1 group production, owned checkpoint and storage return
verified. 595 MUST NOT APPLY.
