# job608 finite API observer resource sampling: independent source review

SOURCE ONLY; **595 MUST NOT APPLY.** Reviewed exact
`a970c798ce41e91df07f8cb720ffe27e07342f3f` against `4f6cf9c9`: four paths,
all byte-identical to the committed versions. Reviewer: Rook
`/root/review_compiler_preflight`, 2026-10-29 UTC. This adds to the separate
limited a39a three-pin rebind review; it does not broaden that approval into a
product-source, package, application-action or automatic queue review.

Diagnostic helper SHA256 is
`60742b3ec7e6d66b48ef37cce97c5833d8dd73f0c9465441b6a44946098a5e55`.
The sole new external module pin is diagnose-unified608.py SHA256
`e9054f13c3b94e0813c825d3318e3da5e14beb40a37947be0cfd7ae6b22d7aa8`.
That module is byte-identical to frozen a39a source. I inspected its complete
top-level behavior and sample() function: import defines constants/functions;
the historical profiler and main entry remain behind the main guard and are
not executed by resource_sampler(). validate() checks the module pin before
main imports it and passes only its maintained read-only sample function.

sample() reads process pid/name/state/parent/CPU/RSS/wait from fixed /proc stat
and wchan files, plus cpu.stat, memory.current, memory.peak, memory.events,
memory.pressure and cpu.pressure under the fixed cgroup root. It does not read
command arguments, environment or source contents. Process-exit races are
handled by the existing sampler; required cgroup-read failures become explicit
sampling errors rather than invented measurements.

collect() retains its actual (child_rc, cancelled) return contract, exact child
command/timeout/process group, forwarding, kill grace and settlement sequence.
It creates samples.jsonl exclusively, samples approximately every10 s while
the child is live, and takes a final sample after settlement. Callback exceptions
record only the exception type label, never its arbitrary message. File/JSON
errors remain failures. Sampling adds no profiler, service, child, semantic
option, source edit, budget override or receipt/publication authority.

main retains the actual command_exit separately. Missing/empty or explicitly
failed resource evidence cannot receive collection_exit0: empty samples count
as one error; sample error records are counted; an otherwise collectable0/124
becomes collection_exit7. Existing command/cancellation failures remain failures.
Diagnostic JSON records sample/error totals and still declares
accepted_checkpoint false and application_authority false. A final sample is
post-settlement state and must not be interpreted as active compiler usage.
Actual phase progression and counter deltas must be read together before making
CPU, memory or checker-cache claims.

Inspected the actual tests and committed logs. RED records14 tests with the two
new sample_fn cases failing against the prior collector. GREEN records15 tests
passing, including preserved actual rc, explicit error/no-message leakage and
main refusing empty/error samples while retaining actual command_exit124.
These fixtures test collection/refusal behavior; they do not prove remote
sampler availability or current compiler performance. I did not rerun them.
Fresh in-memory syntax compilation of helper, sampler module and tests succeeds;
exact commit diff whitespace check passes. No import, sample, test, diagnostic,
export, offload or runtime/root/config/unit/service/seal/provider action ran.

A NEW exact UNUSED diagnostic export still needs independent preflight with all
four external module pins, unchanged frozen runner/helper/archive identity and
accepted current native/runtime inputs. Launch only FIRST in a fresh worker
after live health/storage, no other offload, settlement and sufficient deadline;
outer1740 s plus195 s reserve does not fit the current worker. Actual diagnostic
result0 is not build success: require actual inner status, complete phase and
resource evidence, nonempty samples, zero sampling errors and independent
outcome review. No result, package, action, installed target or seal is accepted.

**VERDICT: APPROVE DIAGNOSTIC RESOURCE-SAMPLING SOURCE ONLY.** No material
finding. Exact export preflight and all final acceptance/installation gates
remain required.
