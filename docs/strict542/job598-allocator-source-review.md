# Independent process-local allocator diagnostic source review

Reviewer: Rook `/root/outcome_review`, 2026-10-26 UTC.
Exact reviewed source: `3ceb4c5db4bb1b9b9230f3c90f6a759ecda62c50`,
`d63c551331e1607d759a675d3194e5cbf6712f59`, through corrected
`1c27e20616bafec25837dc182121e1f2f70dfba6`.
Verdict: **APPROVE SOURCE FOR A LATER NORMALLY ADMITTED DIAGNOSTIC ONLY**.
Current source8ce run must first settle and receive actual-outcome review.

Independently compared all three committed native1 process/pressure samples
against actual runs/598/native1-resumed-{thread-sample,pressure,ancestor-pressure}.json:
byte-identical. SHA256 respectively:
- `566c179031c477e5cf8c97200c882f6865df00061e404ce2a1feb67662e3a07e`
- `5d3958c44abfc7457f928c732b70beb556298f927e2de1565e1d5672a4c83452`
- `c69cc28e54ba152ed14929723f6f0b2719991c6aeb59de99db878fe6e09d0639`

The plan accurately describes one runnable Rolldown worker,14 threads, high
anonymous THP residency, severe reclaim/refault pressure, and the existing
ancestor1.5GiB memory.high below leaf2GiB max. Its high counter is cumulative;
these samples do not prove THP alone causes timeout or show an OOM.

Independently consulted primary upstream [Rolldown binding source](https://raw.githubusercontent.com/rolldown/rolldown/v1.2.9/crates/rolldown_binding/src/lib.rs),
[Cargo features](https://raw.githubusercontent.com/rolldown/rolldown/v1.2.9/crates/rolldown_binding/Cargo.toml),
[exact lock](https://raw.githubusercontent.com/rolldown/rolldown/v1.2.9/Cargo.lock), and
[mimalloc environment documentation](https://github.com/microsoft/mimalloc#environment-options).
They support the recorded mimalloc-safe global allocator, Linux v3 features,
0.1.66/sys2 0.1.62 dependency pins and process-local MIMALLOC_ALLOW_THP=0 option.
The option avoids host/kernel/unit changes; actual RSS/feasibility remains unknown.

The original static tsdown-build import had a transitive import-time audit gap
(sanitizer imports native-typescript and TypeScript native API modules).
Corrected1c27e206 dynamically imports that entire build-owner closure after
admission and fixed environment installation. Remaining static local imports
are policy/census and process-memory readers; the latter imports only Node
builtins and the plain mountinfo path decoder. Parent config import follows the
fixed policy, child exec receives it, and each invocation asserts propagation.
Inherited allocator controls are refused case-insensitively, including matching
or empty values. No caller-selected allocator, preload or native patch is added.

Independently ran `node --test docs/strict542/serial-probe598.test.mjs docs/strict542/isolated-config598.test.mjs`:
13 pass, zero failures/cancellations/skips. Telemetry adds only read-only
memory.stat/pressure and allocator markers; no transform/resolve/output hook.
Full ordered graph selection, fixed pools1, heap calculation,900s compiler
deadline, normal4352MiB build guard, cancellation/settlement and budgets remain.

No new diagnostic was launched by this reviewer. A fresh committed secretless
export and ordinary resource/lease/scanner admission remain required after the
unchanged current run settles; no alternate slot or retries outside that path.
This is no empirical capacity, complete build/artifact, application or release
approval. Complete owning checks, deterministic final artifacts, independent
action/privilege/seal review, automatic598 review and every595 fresh genuine HQ
ownership/accepted-run acknowledgement gate remain open.
