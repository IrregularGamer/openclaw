# Job608 package tsccwdf6a4 — actual evidence: REFUSED by the tree mode gate (595 MUST NOT APPLY)

Stage P/stage-package-tsccwdf6a4, manifest 9064b9ea579d366f5d04978030a2a95a5fc1b3eb43f8758386bcb303a3ff9a38
(preflight independent APPROVE 1cc5bf20). P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private.
Fresh-worker FIRST heavy action, 2026-10-29 ~19:47Z. Live gates all passed: health up, remote load 0.2,
no competing run, / 7.9G free, storage608 check --root P --stage package 0 (1405142008 used),
verify-inputs0, sh -n0, exact manifest pin, result/log/rc absent, ~3530s left.

ONE admitted foreground offload (SPENT, never replay):
`offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-package -- timeout -k 15s 2400s sh run608.sh`.
Client rc2 (package-offload.rc; private log sha256 a6e1a0e8…ec42, committed gzip copy). STEP608 builder-start,
frozen install, build-checkpoint608 complete (restored accepted checkpoints), `pnpm --filter openclaw --prod
deploy` succeeded (FROZEN_DEPLOY_INPUTS_VERIFIED…), then the unchanged application598.py tree inventory refused:

    REFUSED: special or writable-by-group/other mode: CHANGELOG.md

then STEP608 builder-fail 2. No result608-package was returned, so there is no receipt and nothing to accept.

## Root cause (source defect, not an environment fault)
- `git archive` writes entries 0664/0775 by default (tar.umask 0002). source598.tar lists CHANGELOG.md as
  `-rw-rw-r--`. run-stage608.sh extracts it with plain `tar -xf` on the remote, where tar keeps archive modes
  (same-permissions as the superuser), so the whole working source tree is group-writable.
- pnpm deploy copies package files with their modes, so CHANGELOG.md (the first entry in sorted order) is 0664 in runtime.
- The same 0664 modes were propagated into every accepted build checkpoint: the accepted tail checkpoint
  (8df9caa8) holds 1003 `-rw-rw-r--` files and 68 `drwxrwxr-x` directories (dist-runtime/extensions/*,
  dist/control-ui/{provider-icons,file-icons,fonts}, …), and stage608.extract_checkpoint deliberately restores
  exact modes. Rerunning package from the accepted stages would therefore always refuse.
- The refusing check is correct (application artifacts must not be group/other-writable) and is NOT weakened.
  A post-hoc chmod of the runtime would hide where the modes come from, so the fix is at the origin: the
  staged runner creates the source tree under umask 022 without preserving archive write bits. That changes
  the runner commit and therefore source_export_sha256, so all producing stages (native, checks, compiler,
  unified-*, middle, sdk-*, tail) must be rerun from fresh exports under the corrected commit. Accepted
  tsccwdf6a4 stages stay recorded evidence but are superseded as package inputs.
