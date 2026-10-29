# Job608 middle tsccwdf6a4 preflight — 595 MUST NOT APPLY

NEW UNUSED export P/stage-middle-tsccwdf6a4, prepared 2026-10-29T18:0xZ by unchanged
prepare-stage608-export.py (sha256 1e701de0…, == f6a4de2e) under ulimit -v 512MiB, rc0:
`--base P/stage-unified-0-tsccwdf6a4 --commit f6a4de2e --stage middle` with inputs
native/runtime/unified-0..4 from their stage-*-tsccwdf6a4/result608-* and unified-5 from
P/stage-unified-5r1-tsccwdf6a4/result608-unified-5 (accepted c7e554ab; spent
stage-unified-5-tsccwdf6a4 has no result and is not used).
Manifest cc7651f8749dd402cf4839810dc1b3b61e90d7c5e1650b9417183f30157600ca (copy:
job608-middle-tsccwdf6a4-export-manifest.json); source_export e81e07d2 (same freeze).
Fresh: verify-inputs0, sh-n0, storage608 check --stage middle 0, df free 8.4GB.
Unchanged runner keeps the fixed 2280s inner build budget and all gates.

Launch ONCE (same finite caps as unified groups), after independent preflight approval:
```sh
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-middle-tsccwdf6a4
offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-middle -- timeout -k 15s 2400s sh run608.sh > ../middle-tsccwdf6a4-offload.log 2>&1
printf '%s\n' "$?" > ../middle-tsccwdf6a4-offload.rc
```
Requires >=2655s left after preflight; never detached; one launch spends the stage.
