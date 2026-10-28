# job608 unified-0 (1bed) offload outcome — TIMEOUT, evidence only

- Launched 2026-10-28T20:51Z as the first step of a fresh worker, exactly as approved (preflight 2d38d7ed, independent APPROVE ac7f4dd3, Decision646):
  `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-unified-0 -- timeout -k 15s 2400s sh run608.sh`
- Result: rc=124 (inner `timeout 2400s` fired). Local log 2124 B, sha256 prefix 6e143fd6df805ca6.
- The only markers are `BEFORE_ARCHIVE_RELEASE608` / `AFTER_ARCHIVE_RELEASE608` (cgroup memory.current ~0.93 GB, anon ~9.8 MB, pgscan/pgsteal 0, so no memory pressure at release).
  There is no `STEP608 unified-0-pass`, and the build-failure tail was never printed because the outer timeout killed the whole shell.
- No artifacts came back (a failed offload returns none), so there is no unified-0 receipt.
- Interpretation: the same run608.sh path passed for runtime (726b81a2) in ~26 min. So the unified-0 work after archive release (stage-native, restore-build, pnpm 12.5.1 exec, unified-0 build) needs more than 2400 s on 1 CPU. That matches the earlier CPU-bound config-15 finding, not memory.
- Gates, floors and budgets are unchanged. Nothing was installed or sealed. 595 MUST NOT APPLY.

## Next (source-only, own worker)
1. Add per-substep STEP608 timestamps (stage-native / restore-build / pnpm / build start) in run608.sh, and make the build's own timeout shorter than the outer one so build.log tail and a partial receipt are returned on timeout.
2. Split unified-0 into smaller reviewed units (e.g. unified-0a/0b by config subset) that each fit in 2400 s at 1 CPU, without weakening checks. Then preflight, independent review and launch as the FIRST step of a fresh worker.
