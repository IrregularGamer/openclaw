# Independent corrected isolation timeout and normal cleanup review

Reviewer: Rook `/root/build_analysis`, 2026-10-25 UTC.
Actual exported source: `6d7ecc59f7c60f64cfdd35066a57b19c5d3e7e2c`.
Reviewed exact evidence: `2d6c25f8` and `b084357b`.
Verdict: **APPROVE ACTUAL EVIDENCE ONLY**. This is a failed finite diagnostic,
not accepted build, empirical feasibility, artifact or application approval.

Independently verified all eight hashes in the committed outcome manifest.
Stored probe log, receipt, tests and test evidence are byte-identical to actual
recovered `runs/598/isolated-corrected-final` files. Stored offload log matches
`runs/598/isolated-probe-reconciled-run.log`. The separate corrected-run.log is
the earlier191-byte scanner refusal and is not this successful admission log.
Stored thread sample/detail and
post-run metadata match their actual small `runs/598` counterparts. Test-log
hash and source binding match the actual test evidence. Source/native archive
proof relies on prior exact independent review; no large archive was rehashed.
The export manifest source matches6d7ecc59 and its runner digest matches that
exact committed runner, including reviewed fixed disposable-store cleanup.

Exactly184 checks passed: Node101+9, Python15+18+13+19+9, both Node fail0 and
five Python OK summaries. The actual receipt records17 admitted results: AI
and main configs0 through14 status0, then main-config15 status null with
timedOut:true and SIGKILL. Config15 is the original intact unified runtime
graph. The owner logged868110ms remaining shared deadline, SIGTERM then SIGKILL,
and observed process-group state dead. Actual recovered exit code is1. Later
configs16 through56 were not admitted; there is no full runtime/artifact success.

The native thread sample records2GiB memory,1CPU quota, cpuset0-3 and18 total
compiler threads, including six active Rolldown workers. Intermediate resource
samples show native-heavy RSS and comparatively low V8 heap. These support the
specific native scheduling mismatch discussed in the independently reviewed
pool successor; they do not establish its future performance or prove exclusive
causation of the timeout. Neither intermediate memory.events nor a final explicit
timeout kill supports an OOM claim. The earlier nested-config resolution defect
is corrected: package configs now actually compile, but unified runtime still
times out under the unchanged finite budget.

Actual post-run metadata records existing runner lock available, zero managed
containers and absent source/native-source/.pnpm-store. The exact slot retains
only the known five inputs and result598. This is evidence that normal EXIT
cleanup, including the reviewed store removal, completed. It is not a fresh
application/native-owner quiet predicate or permission to dispose new artifacts.
The reviewer did not rerun remote observations or launch any compiler/cleanup.

The active-run settlement condition from source review74da218e is now evidenced.
Its exact native-pool successor36940dd8 remains byte-unchanged in executable
diagnostic/runner/owner paths through b084357b. One later normally admitted
fixed-native-pool experiment may proceed from a verified fresh committed
secretless export, with preserved actual prior outcomes, the same slot and all
ordinary scanners, leases,2GiB/1CPU limits and900s deadline. Any new uncertainty
requires reconciliation; no unchanged diagnostic retry, heap/deadline increase,
graph omission, guard exception or empirical success is approved.

Complete build/profile/declaration/postbuild/package and deterministic artifact
proof, independent action/privilege/seal review, automatic queue review and all
job595 installation and genuine fresh HQ owner/run acknowledgements remain open.
