# Unified-0 diagnostic reconciliation608

SOURCE ONLY. 595 MUST NOT APPLY.

The launch recorded at 21:46:55Z did not reach compilation. Actual retained
`unified-0-diag-offload.log` is 180 bytes and contains exactly a transfer-guard
refusal for `source/.npmrc` and `remote_environment_blocked`. No client .rc file
was retained; do not invent its status. The launch note is intent, not a result.
No sampler samples or new build receipt exist from that attempt.

Read-only inspection found no local source/ in stage-unified-0-1bed. The failed
2400s run reused that remote slug. offload uses rsync --delete with per-directory
.gitignore filters, so generated remote files can survive the failed command's
interrupted cleanup. A NEW export path/remote slug is the supported fresh-export
reconciliation; no transfer filter, forbidden filename or safety policy changes.
The cause is a hypothesis until the new transfer actually passes.

Prepare NEW stage-unified-0-diag-fresh608 using the committed frozen1bed preparer,
base and accepted native/runtime inputs, exact source/export/runner/helper pins,
and verify-inputs. Source stays1bed and common export5d7e9d57. Add only the
committed observe-unified608.sh outside source, record its SHA256. Independent
prelaunch review is required. Run once from that export with admitted4g/1CPU:

    offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-unified-0 -- sh observe-unified608.sh

The observer gives the unchanged build2300s inside2460s, emits CPU/process and
synthetic build-log tails every120s, kills and waits its own sampler sleep, and
prints the actual status and final log tail even when the build times out.
An actual timeout is diagnostic evidence only. No partial receipt may stand in
for build success. Any possible successful output needs exact independent
acceptance before reuse. Keep original owner/identity/admission/floors/checks,
cancellation/settlement, source inventories and final package/HQ gates intact.

Next use the actual phase evidence to correct or split the existing build owner.
No unchanged allocator retry, default-budget retry, runtime auth/provider call,
local build, installed/sealed/root/unit/sudoers/service/config change is allowed.
