# Job608 runtime tsccwdf6a4 launch — 595 MUST NOT APPLY

Supersedes the NEXT section of job608-after-native-tsccwdf6a4-continuation.md.

- Prepared P/stage-runtime-tsccwdf6a4 (prepare-stage608-export.py, base stage-native-tsccwdf6a4,
  commit f6a4de2e, input accepted result608-native, binding 0b6607e7): manifest
  d0d4d630af82f520dbe2609ac7f8ad4018d72ccffe24ba1e4bbd5bdc21e2fbf7, verify-inputs 0, sh -n 0.
- Independent preflight APPROVE 396aa580 (cosmetic: inherited `purpose` text says native; not read by runner).
- Fresh gates: health up, no competing run, storage608.py check --root P --stage runtime 0,
  no result/log/rc, 3238s worker time left.
- Launched ONCE ~14:2xZ (time in P/runtime-tsccwdf6a4-launch.txt):
  `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-runtime -- timeout -k 15s 2400s sh run608.sh`
  log P/runtime-tsccwdf6a4-offload.log, rc P/runtime-tsccwdf6a4-offload.rc. The stage is now SPENT: never relaunch.

## NEXT worker
If rc file exists: commit evidence (log gz, rc, result hashes) under docs/strict542/job608-runtime-tsccwdf6a4/,
get independent acceptance, then prepare unified-0 from stage-runtime-tsccwdf6a4 with inputs result608-native +
result608-runtime, review, launch FIRST in a fresh worker. If no rc file (worker killed mid-run): preserve the log,
do not relaunch this stage; inspect `offload status`, record it, prepare a NEW stage name.
Then compiler, unified1..5, middle, sdk0/1, tail, package; final reviews and job608-final-HQ-HANDOFF.md.
No install/seal/root/unit/sudo/service changes. Do not `git pull` in workers.
