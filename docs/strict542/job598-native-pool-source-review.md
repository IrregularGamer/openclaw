# Independent fixed native-pool diagnostic source review

Reviewer: Rook `/root/build_analysis`, 2026-10-25 UTC.
Exact reviewed range: `38882ebd` through
`36940dd8c1dda70ee2328d2f3ed9b7da523c53ff`, including
`3a4aaf3d8a504a28dca907d67ee194d3335ad1b1`.

Verdict: **APPROVE SOURCE for one later admitted diagnostic**, conditional on
normal settlement and independent outcome review of the currently active
`6d7ecc59` run. Do not interrupt, replace or concurrently rerun that run. This
approval establishes neither empirical feasibility nor a normal-build admission
exception, accepted artifact or installation authority. A successful current run
does not itself justify repeating an already satisfied proof obligation.

Independently inspected actual small thread samples: admitted container CPU
quota1CPU, memory2GiB, visible cpuset0-3,18 compiler threads and six named Rolldown
workers active in the sampled workload. RSS is approximately1.4GiB; separate V8
samples remain low. These observations establish oversubscribed native workers,
not exclusive causation of all elapsed time, a peak-memory bound, or failure of
the still-active run.

Independently checked exact pinned Rolldown1.2.9
[primary initialization source](https://raw.githubusercontent.com/rolldown/rolldown/v1.2.9/crates/rolldown_binding/src/lib.rs):
lines111-133 accept explicit worker/blocking limits, default blocking concurrency
to4 and custom worker concurrency from physical CPU count. This custom runtime
is not fixed by TOKIO_WORKER_THREADS alone. The existing maintained
scripts/lib/vitest-isolated.mts already sets these native pool controls explicitly.
The evidence justifies testing a fixed single-CPU native policy while retaining
the exact full compiler graphs and existing memory/deadline constraints.

The existing diagnostic policy owner now creates an immutable four-key pool
constant: ROLLDOWN_WORKER_THREADS1, ROLLDOWN_MAX_BLOCKING_THREADS1,
RAYON_NUM_THREADS1 and TOKIO_WORKER_THREADS1. The environment helper returns a
copy, preserving caller input. The probe first applies existing admission plus
new inherited ROLLDOWN_/TOKIO_/RAYON_RS_NUM_CPUS refusals, including empty values,
then generates its fixed environment. No caller-selected thread count is added.
Parent metadata evaluation receives the same fixed policy before dynamic config
import; AI and every selected whole-config child inherit it. Each actual spawn
plan asserts propagation through the existing invocation owner's returned env.
Receipt/plan markers and child telemetry record effective controls and observed
thread counts. These are diagnostic facts, not success authority.

The diff preserves config census, entries, shared singleton graph, root config
placement, option values, dependency pins, output roots, runtime-only selection,
900s shared deadline and existing heap computation. Existing scanners, process
groups, cancellation/settlement, export runner and reconciliation implementation
are unchanged. Normal4352MiB admission remains intact; nothing affects installed
code, supervisors, units, sudoers, native owner predicates or runtime credentials.

Independently ran the two lightweight Node test files: all11 tests passed, zero
failures. No compiler or heavy/local suite was run by this reviewer. Before the
approved later attempt, retain the current run's actual settled outcome, verify
the committed fresh secretless successor export and normal2GiB/1CPU admission,
and independently review any necessary workspace reconciliation. Later evidence
must establish actual pool/thread behavior and full ordered config outcome;
unchanged retries or empirical performance claims are not authorized here.

All complete-build/profile/declaration/postbuild/package, deterministic artifact,
independent action/privilege/seal, automatic queue and job595 genuine HQ owner
binding/application requirements remain open.
