# Independent preflight review: job608 middle tsccwdf6a4

Reviewed: preflight commit 6dc27bdc. S = /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-middle-tsccwdf6a4 (read-only; I launched nothing).

1. PASS: sha256(S/export-manifest.json) = cc7651f8749dd402cf4839810dc1b3b61e90d7c5e1650b9417183f30157600ca, and it is byte-equal (cmp) to docs/strict542/job608-middle-tsccwdf6a4-export-manifest.json. Fields: stage=middle, execution_state=UNUSED, source_commit=f6a4de2ebc6924d16fe559f9858bf8c50dce1eba, source_export_sha256=e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145.
2. PASS: S/run608.sh and S/stage608.py are byte-equal (cmp) to `git show f6a4de2e:docs/strict542/run-stage608.sh` and `stage608.py`.
3. PASS: STAGES['middle'] = native, runtime, unified-0..5. The manifest stage_inputs and S/stage608-inputs/ cover exactly those 8 stages. Every stage-receipt.json sha256 matches its accepted result: native 10474857, runtime 3e284e2c, unified-0 1ac0a798, unified-1 c43e9f97, unified-2 52b1c90e, unified-3 c80d6028, unified-4 0d6c99fe, unified-5 0dc9bea0102a4d80e4a491d1a7baecd19a71c207e273491fd308e469a53a9e34 (taken from stage-unified-5r1).
4. PASS: `python3 -I -B stage608.py verify-inputs` exits 0 and `sh -n run608.sh` exits 0. P/middle-tsccwdf6a4-offload.log, P/middle-tsccwdf6a4-offload.rc and S/result608-middle are all absent.
5. PASS: The launch command is `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-middle -- timeout -k 15s 2400s sh run608.sh`. It has fixed finite caps and no caller-selected root command, and its form matches the unified1-5 preflight.

Non-blocking notes:
- Some free-text manifest fields were carried over from earlier stages and are out of date: purpose says "stage native", and budget_authority cites friend4GiB1CPU. They are descriptive only and do not affect any digest checks or caps.
- Before launch, confirm the worker has at least 2460s left in its window (see the warning in the unified1-5 preflight).

VERDICT: APPROVE
