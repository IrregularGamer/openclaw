# Job 608 unified-0 tsccwdf6a4: independent acceptance

Independent review dated 2026-10-29. Scope: the actual unified-0 run only, frozen source
`f6a4de2ebc6924d16fe559f9858bf8c50dce1eba`, common export
`e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145`.
Evidence commits: `c362cd3a` and build-log correction `d597e6eb`; launch `577ba15e`,
independent preflight `ad22814a`. P denotes
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private`.

## Verified

- Private `unified-0-tsccwdf6a4-offload.rc`, committed `unified-0-offload.rc`, and result
  `exit-code.txt` all contain `0`. Decompressed committed outer log is byte-identical
  to the private outer log. It records native-start +11s, restore-build-done +19s,
  build-start +20s with 2260s budget, build-done +422s, and `unified-0-pass`.
- The private result contains exactly the five files named by `result-files.sha256`;
  every SHA256 matches. Total returned bytes: 647069. All four committed result
  copies, including the build log added by `d597e6eb`, are byte-identical to the
  private originals. The 636339-byte checkpoint remains private.
- Receipt SHA256 is `1ac0a79838bd11407b95f46f1a4f239f7d2e41873118c918acb102a4ea9c1563`.
  Its kind is `JOB608_STAGE_RECEIPT`, stage `unified-0`, exit_code 0, and run_id
  `stage608-unified-0-tsccwdf6a4`. Source and common export match the frozen values
  above; manifest_sha256 matches the actual export manifest:
  `3a1b42d1b104c977b258a82b82fedd85a02e15c7d2fdaaff754caad4e455708a`.
- Receipt stage_inputs equal the manifest's exact seven pins. Streaming hashes of
  each staged file and the corresponding accepted native/runtime result file
  match: native binding `0b6607e7...e042`, compile receipt `4a651254...ed9e`,
  libtests receipt `2f81179f...d946`, native stage receipt `10474857...6d3`, runtime
  build log `242dfc93...b5cb`, runtime checkpoint `9e028d03...d9c5`, and runtime stage
  receipt `3e284e2c...bb04`. These retain acceptance `57742314` / `5824b14b`.
- Receipt output hashes match the actual build log
  `6df1a0c3e23baa3c2c517c1975c35fd9d261cb06098a45fa291b5b4074f02855`
  and checkpoint
  `1583290f01734085ea0a5f64ab08eac32855b43116df426103da4080b7740897`.
- The complete 240-line build log ends with the successful tsdown invocation
  `1/1 finished in 274.7s`, followed by `phase timings: no phases ran`. Frozen
  `scripts/lib/bounded-build-checkpoint608.mjs` selects an empty ordinary label
  list for unified groups; frozen `scripts/build-checkpoint608.mts` produces the
  declaration group during preparation before that loop. The timing line is
  consistent with this owner path and the produced checkpoint.
- There are no actual error TS, ERR!, failed, exit-code, fatal, timeout, OOM,
  killed, or signal failure lines. The three warning-related lines are a slow
  tarball download warning, the package-manager-warning script name, and the
  experimental TypeScript API notice. Package names `signal-utils` and
  `@lit-labs/signals` are not signal failures.
- Read-only archive inspection finds exactly nine entries: four directories and
  five regular files, all beneath `unified/openclaw-dts-base` or its required
  `unified/openclaw-dts-base.build608.json` sidecar. There are no links, redirects,
  duplicate paths, special entries, or privileged mode bits.
- The sidecar and group receipt agree, carry `COMPILED_GROUP_NOT_PUBLISHED`, name
  `openclaw-dts-base`, and bind the frozen source/common export and accepted native
  hashes. The recomputed complete group inventory digest is
  `96f0396740bf8f1026b2a0f53a1f9afd197b01f37009b6b1ea5f6c23b520ca13`.
  Its predecessor digest `25ffcb65...8770` matches the receipt read directly from
  the accepted runtime checkpoint archive, without extraction.
  The artifact record equals the receipt record; its two output hashes match
  `compiler-inputs/openclaw-dts-base.json` and required `dist/index.d.ts`.
- `python3 -I -B docs/strict542/storage608.py result --result
  P/stage-unified-0-tsccwdf6a4/result608-unified-0 --stage unified-0` exits 0,
  returning 647069 logical bytes below the 33554432-byte return cap.

## Scope and limits

The manifest's `execution_state: UNUSED` remains immutable prelaunch metadata;
the actual run evidence establishes that this stage is SPENT and must not replay.
This accepts unified-0 only. It grants no installation, sealing, package,
application, privilege, service, or automatic queue approval. No build, test,
offload, extraction, installed-state, root, service, or queue mutation was run by
this review; only this requested review document and its Git publication change.

595 MUST NOT APPLY.

VERDICT: ACCEPT unified-0 tsccwdf6a4 at f6a4de2e. No acceptance findings;
rc 0, exact five-file inventory, receipt bindings, successful group production,
owned checkpoint and storage return verified. 595 MUST NOT APPLY.
