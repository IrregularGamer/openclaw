# Job608 continuation after native tsccwdf6a4 — 595 MUST NOT APPLY

Supersedes the "NEXT FRESH WORKER" section of job608-after-checks-tsccwdf6a4-continuation.md.

- native tsccwdf6a4 (manifest b51a34e9, preflight review 54587210) ran ONCE: rc0, native-rebuild-pass.
  Stage is SPENT: never relaunch it. Evidence docs/strict542/job608-native-tsccwdf6a4/.
- Native run independently ACCEPTED 57742314 (step (1) below is DONE).
- NEXT fresh worker: (2) prepare runtime stage at f6a4de2e consuming the accepted native binding hash, independent
  preflight review, then ONE runtime offload as first heavy step. Then unified0 (pass + acceptance before
  compiler), compiler, unified1..5, middle, sdk0/1, tail, package; final artifact/action/privilege/seal/automatic
  reviews and job608-final-HQ-HANDOFF.md bound to the actual package.
- Do not `git pull` in workers. No install/seal/root/unit/sudo/service changes.
