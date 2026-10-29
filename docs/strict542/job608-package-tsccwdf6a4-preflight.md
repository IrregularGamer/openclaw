# Job608 package tsccwdf6a4 preflight — 595 MUST NOT APPLY

Tail accepted: evidence 836b3d66 (receipt 8df9caa8), storage608 tail cap correction 128->192MiB
8f4fb3b3, independent ACCEPT 6fdaddd5 (cap fix applied to the unchanged result, no rerun).

## Storage room (superseded staging quarantine, recoverable)
`storage608.py check --stage package` (cap 2048MiB) refused: P used 2318654419 bytes, so the
aggregate staging cap would be exceeded. 26 superseded NON-tsccwdf6a4 stage directories
(list: job608-superseded-stage-quarantine-20261029.txt; their evidence was committed earlier) were
moved with `mv -n`, on the same filesystem and without deleting anything, to
/srv/encrypted/dev-move-98/agentq-source608-superseded-20261029/. No symlink in base or any
tsccwdf6a4 stage and no tsccwdf6a4 manifest references them. Rollback: move them back.
The package room check then passed, with 1387067557 bytes used. No cap, floor or reserve was changed for this.

## Export (UNUSED)
Prepared 2026-10-29 by the unchanged prepare-stage608-export.py (sha256 1e701de0…) under ulimit -v
512MiB, rc0:
`--base P/stage-unified-0-tsccwdf6a4 --commit f6a4de2e --stage package --input .../result608-native
 --input .../result608-checks --input .../result608-compiler --input .../result608-tail
 --dest P/stage-package-tsccwdf6a4` (STAGES['package'] = native, checks, compiler, tail).
Manifest sha256 9064b9ea579d366f5d04978030a2a95a5fc1b3eb43f8758386bcb303a3ff9a38 (copy:
job608-package-tsccwdf6a4-export-manifest.json). Staged stage608.py is cmp-identical to the committed copy (a558db9a).
At preparation: verify-inputs0, sh -n0, storage608 check --stage package 0 (with the export present,
1405142008 bytes used), export 900693857 bytes. No result/log/rc exists. NOT launched (about 2150s left, below 2655s).

## Launch: fresh worker FIRST heavy action
Re-verify every live gate (health up, no competing run, df / >=1GB, storage608 check --stage package 0,
verify-inputs0, sh -n0, exact manifest pin, result608-package and P/package-tsccwdf6a4-offload.{log,rc}
absent, >=2655s left):
```sh
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-package-tsccwdf6a4
offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-package -- timeout -k 15s 2400s sh run608.sh > ../package-tsccwdf6a4-offload.log 2>&1
printf '%s\n' "$?" > ../package-tsccwdf6a4-offload.rc
```
One launch spends the stage. Afterwards: storage608 result --stage package, actual evidence commit,
independent acceptance. Then the final artifact receipt with the old/new hash inventory, the
action/privilege/seal/reseal reviews, the automatic queue review and the genuine ordered HQ595
handoff. 587 fd3/socket transport replaces 586 sudo; never add the 586 rule. Never detached.
Never replay accepted stages.
