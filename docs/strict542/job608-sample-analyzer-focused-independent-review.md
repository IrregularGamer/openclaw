# Independent review: sample analyzer and focused admission composition

VERDICT: APPROVE the sample-only analyzer at 691b7845 and the narrowly scoped
focused-test preflight ca447412. The baseline diagnostic was still running when
reviewed; no final build outcome or acceptance is asserted. This reviewer did
not launch an offload or build. **SOURCE ONLY. 595 MUST NOT APPLY.**

## Analyzer and observed evidence

Read `analyze-unified608-samples.py` and compared its output with the actual
printed ps rows in the ongoing frozen-1bed diagnostic. Snapshot SHA256
`325433363c86d3b265dc3d1433a3922388ff54c131a9890fd54e91d8717f1c68`,
19147 bytes, has nine samples and no completion marker. Its CPU-time format,
RSS KiB conversion, fixed command-prefix role recognition and raw hash match
the observed format. The 2MiB read bound is appropriate for finite log analysis.

At the common first/last observations (elapsed 241 -> 1083 seconds), raw rows
and analyzer agree:

- Native TypeScript PID330: CPU 1 -> 568 seconds, delta567 seconds.
- Declaration Node PID307: CPU12 ->55 seconds, delta43 seconds.
- Checkpoint Node PID245: CPU43 ->46 seconds, delta3 seconds.
- Native TypeScript largest sampled RSS: 3231993856 bytes.

This establishes active native CPU work dominating the observed CPU increments
among these printed roles. It establishes no exact API query, native ownership,
complete process inventory, instantaneous or unique memory use, cgroup pressure,
OOM history, success, timeout or complete cause of elapsed wall time. Repeated
log tails are not extra process samples. Process PID/role matching and monotonic
CPU/age checks detect some discontinuities, not kernel start identity; the
analyzer correctly makes that limit explicit. Its final `end` is observer
command status, not a successful stage receipt or artifact acceptance.

The 3c0901de correction, included in candidate95, removes duplicated Node
filesystem admission work while preserving caller/snapshot policy. The native
process evidence does not prove that callback correction fixes the full-stage
timeout. Nor does the correction's small test establish native compiler speed.
After the real baseline outcome, a timeout/failure must lead to a source-level
decision informed by these samples. Another unchanged heavy native run or a
larger wall allowance is not justified by this analyzer or focused test. Any
further heavy run needs a concrete reviewed source correction or bounded,
question-specific diagnostic, plus its existing source/identity/resource gates.

## Optional focused remote check

Independently verified the export at
`/home/deploy/agentq/tmp/export608-admission95-focused.n_rr23g0`: exactly the five
preflight source files plus `focused-source-manifest.json`, no symlinks or prior
result directory. The five files total35759 bytes, match every preflight SHA256,
and are byte-identical to commit95e62f8b6c7af341b2dfc21163627aa8a533649d.
The sole metadata file matches the preflight fields excluding command/launch_gate,
SHA256 `62f8ce637fce562f34d4c3de1bcd314976b80a2b0a6d8f7851952dfd131fc5bd`.
The declared archive hash was not independently rehashed; the actual extracted
source bytes were verified instead.

The exact ca447412 command uses offload180 seconds,2g,1CPU, inner test120 seconds
with15-second kill grace. Its shell parses with `sh -n`, saves the actual test
or timeout status, prints tests.log, writes that saved status and exits with it.
The 45-second remaining outer allowance is suitable for these small artifacts;
offload's worker deadline separately requires375 seconds. Failed offload returns
no artifacts, so printed synthetic test output is the failure evidence.

The test drives seven explicit composition cases through the real emitter,
filesystem and boundary code. The native API/compiler, snapshot/seal and related
toolchain modules are test doubles. This can support composition/policy only,
not compiler correctness, seal correctness, full-suite/package/application
acceptance or the baseline timeout fix.

Launch authority remains conditional: only after the ongoing diagnostic actually
returns and settles, no overlap, current deadline admission, unchanged exact
source pins and clean export. No additional long run is required by this review.
