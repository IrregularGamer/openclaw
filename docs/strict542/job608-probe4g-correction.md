# Four-GiB diagnostic source correction (source only)

The preserved combined3 export has a missed incompatible check. Decision618
changed only the launch budget to4GiB/1CPU. Frozen source6d9c429b still calls
admitProbe unconditionally, whose capacityBytes ceiling is2GiB. CapacityBytes
means the actual effective ceiling, not remaining memory. Lower remaining usage
cannot make a real4GiB ceiling pass. The independent reviewer reproduced this
refusal from frozen source before any diagnostic receipt/config import.

608 launched this preserved export after actual619 application and independent
prerequisite review. That launch was a mistake: the earlier exact launch review
and the current resumer both missed the source ceiling. The active finite run
must be preserved and independently reconciled; it cannot supply a successful
config15 receipt. Never relaunch combined3 unchanged. No unsupported client/SSH
kill was attempted: installed offload has no documented artifact-preserving
cancel action, and interrupting its unhandled streaming threads could lose
completion proof. Keep its existing2700s+15s outer bound and await settlement.

Minimal owning-source change: admitProbe now refuses capacity above4GiB rather
than2GiB, consistent with already-approved standing Decision618/S tg1825 and the
hard remote MemoryMax. The remaining limit must still be positive finite and
no larger than observed capacity. Unknown/invalid capacity, inherited controls,
existing outputs and unchanged1625784320-byte thrash floor still refuse. OneCPU,
swap0, managed cancellation/settlement,900s probe and2700s outer bounds, singleton
unified graph, native sources/receipt equality and full config census are intact.
This reconciles the approved resource ceiling, not a lowered memory floor or
an unreviewed escape. No broker/unit/cgroup/installed file changed.

TDD: new4GiB whole/reduced-remainder admission test fails against old source;
all13 focused policy tests PASS with this correction. The existing oversized
case now explicitly rejects4GiB+1. RED/GREEN raw output is preserved alongside.
Only an independent exact correction/export review can authorize a FUTURE fresh
combined export in a normally admitted foreground worker with>=51minutes.
It must include all currently affected checks, no previous addon/cache/dependency
inputs, and source-rebuild both stage receipt and addon equality. Native source
archives and accepted compile/libtest receipt bytes remain unchanged.

Package promotion is still gated on COMPLETE independently accepted diagnostic
success. Current code cannot be called a typed package/build receipt. Exact
artifact/action/privilege/seal and automatic608 review, original seal/backup/
rollback validation and595 fresh post-restart owner/accepted-run gates remain.
