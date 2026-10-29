# job608 checks at label source 49d3fe33: SPENT FAILURE, source correction

- 12:34Z launch by the prior worker never reached offload (empty log, no
  runs.log entry, no rc). Its empty log is preserved privately as
  checks-label49d31-offload.preempty-12-34.log. Fresh verify-inputs, sh -n and
  storage608.py check (stage checks) exited 0 (verify/storage re-run right
  after launch, not before; recorded honestly).
- 12:37Z ONE reviewed checks offload (1200s/14g/4CPU) at stage-checks-label49d31:
  remote rc=1 after 278s (runs.log 12:41:38Z). Every suite passed except
  docs/strict542/usage-window-types608.test.mjs: tsc 7.1.0-dev.20260920.1 refused
  with TS5112 because the full export has a root tsconfig.json and the test
  passes explicit files. The earlier GREEN export (82cc92b8) had no root
  tsconfig, so it could not see this. No result608-checks returned.
  Log: checks-offload.log.gz, rc: checks-offload.rc. Stage is SPENT, no replay.
- Correction: the test now spawns tsc with cwd at its temp directory (no
  tsconfig discovery). Flags, inputs and assertions are unchanged; no
  --ignoreConfig flag is introduced.
- Focused offload (240s/2g/1CPU, export with the real root tsconfig.json from
  source598.tar): old test RED (rc 1, TS5112), new test GREEN (rc 0).
  inputs.sha256, tsc-version.txt, red/green rc and logs here.

Next: independent review of this correction, NEW checks stage/manifest at the
corrected commit, ONE checks run, acceptance; native successor only as first
heavy step of a later fresh worker. 595 MUST NOT APPLY.
