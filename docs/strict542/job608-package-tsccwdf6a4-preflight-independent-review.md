# Independent preflight review: job608 package tsccwdf6a4

Reviewed commit 96ac4746: `job608-package-tsccwdf6a4-preflight.md`, `job608-package-tsccwdf6a4-export-manifest.json`,
`job608-superseded-stage-quarantine-20261029.txt` and `job608-after-tail-tsccwdf6a4-continuation.md`. Review date 2026-10-29.
The review was read-only: nothing was launched, extracted, built, moved or installed, and no sudo was used.
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private, S=P/stage-package-tsccwdf6a4.

## Check 1: manifest pin, committed copy and identity
- PASS. sha256 of S/export-manifest.json is 9064b9ea579d366f5d04978030a2a95a5fc1b3eb43f8758386bcb303a3ff9a38. That equals the doc pin and the continuation pin, and `cmp` against the committed copy returns 0.
- PASS. stage=package, execution_state=UNUSED, launch_history=none, source_commit=runner_commit=f6a4de2ebc6924d16fe559f9858bf8c50dce1eba, source_export_sha256=e81e07d2…, run_id=stage608-package-tsccwdf6a4, stage_helper_sha256=a558db9a…, runner_sha256=715e53bd….

## Check 2: stage inputs equal the accepted results
STAGES in stage608.py: `'package': ['native','checks','compiler','tail']`. Manifest stage_inputs has 12 files. On-disk S/stage608-inputs holds exactly those 12 files, and each sha256 matches.
- PASS native: libtests-receipt 2f81179f, receipt 4a651254, rolldown-binding 0b6607e7, stage-receipt 10474857. These equal job608-native-tsccwdf6a4/result-files.sha256 and the live result608-native (acceptance recorded in 769857fd/57742314).
- PASS checks: installed.json 2f5411ec, tests.log 156c53ed, stage-receipt 57393630. These equal job608-checks-tsccwdf6a4/result-files.sha256 and the live result (evidence 92aeda26, acceptance d9a3822e).
- PASS compiler: tests.log c8302788, stage-receipt e5b96beb. These equal job608-compiler-tsccwdf6a4/result-files.sha256 and the live result (acceptance dd34e5e4).
- PASS tail: build.log 7272c306, checkpoint b5b8f9ff, stage-receipt 8df9caa8. These equal job608-tail-tsccwdf6a4/result-files.sha256 and the live result (evidence 836b3d66, cap fix 8f4fb3b3, ACCEPT 6fdaddd5).

## Check 3: live gates and absent outputs
- PASS. `cd S && python3 -I -B stage608.py verify-inputs` rc=0, and `sh -n run608.sh` rc=0.
- PASS. S/stage608.py is cmp-identical to docs/strict542/stage608.py (a558db9a). S/run608.sh is cmp-identical to docs/strict542/run-stage608.sh (715e53bd).
- PASS. S/result608-package, P/package-tsccwdf6a4-offload.log and P/package-tsccwdf6a4-offload.rc are all absent (ENOENT).
- PASS. `python3 -I -B docs/strict542/storage608.py check --root P --stage package` rc=0: used 1405142008, free 4986339328, reserve 2147483648, return cap 2147483648, max store 4294967296.

## Check 4: superseded-stage quarantine
- PASS. The list has 26 entries and none contains tsccwdf6a4. All 26 exist under /srv/encrypted/dev-move-98/agentq-source608-superseded-20261029/, which holds exactly 26 entries. None remains in P.
- PASS. P and the quarantine dir are on the same device (st_dev 64512), so the move was a rename: no copy and no deletion, and moving the dirs back reverses it. No symlink in P/base or any P/stage-*-tsccwdf6a4 (depth 2) points outside P or to the quarantine. No *tsccwdf6a4/export-manifest.json names any quarantined dir.
- PASS (judgement). Is this non-weakening? No constant changed: CAPS, MAX_STORE, FREE_RESERVE and the 16MiB/128MiB allowances are untouched. The storage608 forecast scope is "new private source files only; historical files preserved", so the superseded non-tsccwdf6a4 stages were outside the budget the 4GiB aggregate cap was sized for. Their evidence was already committed. The physical safety gate is the volume free reserve. It is computed on the same filesystem, so it still counts the moved bytes. 4986339328 >= 2GiB reserve + 2GiB cap + 16MiB holds with about 670MB margin, and after a full 2GiB return the volume would still keep the 2GiB reserve. The move is recoverable and does not weaken any gate.

## Check 5: what package does, and whether it fits
- The run608.sh package branch does the following in order: stage608 stage-native, restore-build (extracts only the tail checkpoint, the one BUILD_STAGE among its inputs), and merge-logs (checks + compiler logs). It then writes strict542-checks/evidence.json, resolves pnpm 12.5.1, and runs `env -i … sh docs/strict542/build598.sh checkpoint608`. build598.sh does a frozen `pnpm install`, then `build-checkpoint608-owned.mjs complete`, then `pnpm --filter openclaw --prod deploy result598-build/runtime`. It writes evidence.json and package-receipt.json and finishes with `application598.py tree` → tree.json. The EXIT trap moves strict542-checks and result598-build into result608-package. The stage receipt is written last.
- PASS (plausible). Timing: tail did install + restore + join in 237s. Package adds a prod deploy and a tree hash but no new compile, so it should take well under 2400s. Peak memory should be below the 9.77GB full compile, and 14g/4CPU is the same envelope as the accepted stages.
- PASS (plausible, unmeasured). Return size: the result is a prod-only deploy tree plus logs and JSON. The export itself is about 900MB, and a prod node_modules is normally several hundred MB, so it should fit 2048MiB. No measured size of a previous package deploy exists in the repo.

## Check 6: launch command
- PASS. `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-package -- timeout -k 15s 2400s sh run608.sh > ../package-tsccwdf6a4-offload.log 2>&1; printf '%s\n' "$?" > ../package-tsccwdf6a4-offload.rc`. It is foreground, launched once, with the log redirected and rc captured, the same shape as tail/sdk-0/sdk-1. It also requires >=2655s left and all live gates rechecked.

## Recorded risks (non-blocking)
- R1: The package builder has no inner `2280 - elapsed` budget, unlike the build stages. Only the outer 2400s timeout applies. On a timeout, the builder-fail log tail may not print, and the sh EXIT trap may not move result598-build. The failure would still be loud (rc 124/137), not silent.
- R2: The size of the runtime deploy has never been measured. If it exceeded 2048MiB, `storage608 result --stage package` must refuse it and it must not be accepted. Never raise the cap after the fact without a separate review.
- R3: OUTPUTS has no 'package' entry, so stage-receipt.json `outputs` is {}. Acceptance must pin result598-build/{evidence.json,package-receipt.json,tree.json,build.log,deploy.log} through result-files.sha256 and tree.json, not through the receipt.
- R4: The quarantine is outside P. Keep it until final acceptance, and restore it with `mv -n` if any superseded evidence is needed again. Do not delete it without a separate decision.

VERDICT: APPROVE
