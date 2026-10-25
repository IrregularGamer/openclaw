# Independent source review: whole-config compiler diagnostic

Reviewer: Rook `/root/build_analysis`, independently delegated read-only analysis
and review, 2026-10-25 UTC. Exact reviewed range:
`d874f143` through `f62d419c63ccefe41443c0fbaa84d7ab1aaedc17`, including
implementation `a069c3442786d159ea3a871035db03c58fe66a3f`.

Verdict: **APPROVE SOURCE for one admitted diagnostic execution only**.
This is not normal-build admission, proof of 2GiB feasibility, artifact approval,
application/privilege-policy approval, or installation authority.

The original runtime-only resolver admits AI then all main configurations within
one compiler lifetime. The new experiment tests release of preceding compiler
graphs between whole configurations. It retains AI first and every main config
in original array order; duplicate group names do not collapse the census.
The strict selector validates the entire ordered census before returning the
original config object. Actual config constructors, including managed handoff
configs, provide named entry objects and explicit `dts:false` under the fixed
runtime-only policy. Declaration graphs or inventory drift refuse execution.

The diagnostic config exports a valid single UserConfig object. Its shallow
spread preserves entries, dependencies, hooks, input/output options, target,
minification, defines, names and output roots. Nested plugin arrays follow the
existing config conventions. Added plugin hooks observe resource usage and
lifecycle only; they add no resolution, transformation or output behavior.
Gateway/core/SDK shared entries remain in their existing single config graph,
preserving the source's explicit runtime-singleton boundary. Existing entrypoint
and worker/inventory graph boundaries are unchanged. No-clean remains explicit.

The original output scanner, refusal checks and process-group cancellation and
settlement owner are reused without modification. Every compiler receives only
the remaining shared900s deadline, including elapsed parent config evaluation;
failure stops later admission. Native whole-config telemetry is best effort and
cannot authorize success. The parent retains imported config metadata/closures,
which adds overhead; each child computes its existing safe heap from a fresh
capacity read accounting for competing resident usage. No heap override, reserve
reduction, normal4352MiB admission exception, or deadline extension is introduced.

Initial review found inherited output/thread controls could change this fixed
comparison. Successor `2e0b2027` now refuses `OUTPUT_SOURCE_MAPS`,
`RAYON_NUM_THREADS` and `UV_THREADPOOL_SIZE`, including empty values, and records
their admission-verified absence. Existing caller-controlled compiler, preload,
selection and exclusion refusals remain intact. Exact owning launcher
`TSX_DISABLE_CACHE=1` remains the sole documented exception.

Also reviewed telemetry successor `f62d419c`: its interval remains active through
successful graph generation until closeBundle, and clears on build error. The
unreferenced interval cannot keep a compiler alive. Logging the owner's resolved
NODE_OPTIONS exposes the actual generated heap setting without changing it or
transferring runtime authentication/configuration. These two telemetry changes
preserve the approved diagnostic boundaries.

Independently ran:
`node --test docs/strict542/isolated-config598.test.mjs docs/strict542/serial-probe598.test.mjs`.
All nine tests passed, zero failures. No heavy/local compiler, live service,
provider request or privilege mutation was run by this reviewer. Actual config
loading and per-config compiler outcomes still require the one admitted fresh
committed secretless offload run and independent evidence review. Any timeout
must identify its recorded stage; it does not authorize unchanged retry.

Normal full-build admission, complete profile/declaration/postbuild/package
verification, deterministic artifact receipt, independent action/privilege review,
seal validation and automatic queue review remain open. All job595 owner-binding,
fresh post-restart accepted-run acknowledgements and natural-gap gates remain.
