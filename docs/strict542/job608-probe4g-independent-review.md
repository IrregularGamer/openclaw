# Independent review of the diagnostic4GiB source correction

2026-10-27. VERDICT: APPROVE SOURCE ONLY for the exact correction.

Reviewed 4cb57dc06e8689743aa76c576b7ff83792e325ac through
2021131975e1373c10e4bb23b77ca1aa3ae6bc3b independently of its author.
The diff contains five files: the diagnostic policy/test, rationale and RED/GREEN
logs. The only executable policy change is admitProbe's upper capacity ceiling
from2147483648 to4294967296 bytes, with the corresponding refusal message.

The change corrects a real owning-source contradiction. Frozen source
6d9c429b4886d26c83888f1570f977ce63e215a7 calls admitProbe unconditionally in
isolated-probe598.mts before native selection, compiler/config imports or receipt
creation. Its old2GiB maximum necessarily refuses an observed4GiB capacity.
readProcessMemoryCapacity deliberately separates effective ceiling capacityBytes
from usage-adjusted remaining limitBytes; a smaller remaining budget does not
make the4GiB ceiling pass. The new maximum matches the already-authorized
Decision618/S Telegram1825 per-run resource ceiling and does not change broker,
kernel, cgroup or installed policy.

Independently verified unchanged behavior:

- Capacity must remain known, positive and finite; remaining memory must remain
  positive, finite and no greater than capacity. More than4GiB still refuses.
- admitUnifiedGraphCapacity still refuses at/below1625784320 bytes. The caller
  still invokes that floor check before admitProbe. Existing-output refusal and
  inherited compiler, graph-selection, native addon, allocator, preload and
  tracing-control refusals are unchanged.
- Fixed oneCPU native pools, allocator policy, config15-only tracing, exact
  original configuration selection, worker splitting/minification, native
  source/receipt/addon identity checks and success scanners are untouched.
  No compiler heap override, changed graph, singleton split or check waiver is
  added. Canonical memory accounting,900s probe deadline and existing outer
  runner deadline/cancellation/settlement ownership remain unchanged.
- Normal full/package4352MiB admission and the unpromoted typed boundedPackage
  route are unchanged. This diagnostic correction does not promote package code.

Fresh focused verification, with no heavy local suite:

- node --test docs/strict542/serial-probe598.test.mjs:13PASS,0FAIL,
  0skipped (458ms). The new positive test exercises a4GiB ceiling with both
  full4GiB and1800MiB remaining budgets; oversized4GiB+1 refuses.
- Independently loaded the old committed policy into an in-memory data URL and
  ran the new test source against it without editing source files:12PASS/1FAIL,
  with only the new4GiB case failing on the old2GiB refusal. This corroborates
  the committed RED/GREEN evidence. The unchanged floor and controls tests pass.

No source flaw requiring changes was found in this narrow correction. The
admission function remains a source-side workload check, not proof of execution
placement, lease ownership, complete output or successful resource use.

The active byte-identical combined3 export remains uncorrected and must be
preserved and reconciled through its supported bounded completion/settlement
path. This review neither mutates that export nor authorizes an unsupported
interrupt, SSH kill or relaunch. It gives no successful diagnostic evidence.
A future fresh combined4 export needs its own exact source/archive/runner/input
review and normally admitted4GiB/1CPU foreground execution with the required
remaining runtime; no launch is authorized by this document alone. No binary,
dependency or cache input may replace the source rebuild and paired native
receipt/addon equality checks. Complete independently accepted diagnostic
success remains mandatory before package promotion. Typed build/package,
artifact/source/action/privilege/seal reviews, automatic608 APPROVE and all595
fresh-owner/post-restart/accepted-run application gates remain required.
