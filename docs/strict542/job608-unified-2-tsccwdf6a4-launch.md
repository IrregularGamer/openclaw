# Job608 unified-2 tsccwdf6a4 launch — 595 MUST NOT APPLY

Resumed clean source552 at 62535f54 on job608-fullsize-evidence (fresh worker,
deadline 2026-10-29T17:14:44Z). Frozen source f6a4de2e / export e81e07d2 unchanged.
Accepted checks d9a3822e, native57742314, runtime5824b14b, unified0ffc14e61,
compilerdd34e5e4; batch preflight APPROVE40bd39fa; continuation9ee15861.

P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private.
Exact stage P/stage-unified-2-tsccwdf6a4, export-manifest.json SHA256
1fe4787f887d7f7733a0de75cc4cc56540b6f5eb9ad5ad35ec110b07fdcc96c4 (= preflight).
Fresh verify-inputs0, sh-n0; exact result608-unified-2, sibling log/rc absent.
Storage check0: unique1962045222, free5361594368, reserve2147483648,
return cap33554432. Root free1395359744 bytes (>1GB). Health up, load0.19,
no competing remote run. Deadline before launch3529s (>2655s required).

ONE foreground launch initiated 2026-10-29T16:15Z:
`offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-2 -- timeout -k 15s 2400s sh run608.sh`.
Log P/unified-2-tsccwdf6a4-offload.log; actual rc in sibling .rc. Stage SPENT.

Ordering note: unified-1 actual evidence 62535f54 (client/result0) was complete
but its independent acceptance had not yet been recorded (prior worker hit a
usage limit). Unified-2 is an independent, already-reviewed export whose only
fresh-worker window is the FIRST heavy step (>=2655s), so it was launched first
and unified-1 independent acceptance runs concurrently. Unified-2 acceptance is
conditional on unified-1 acceptance; if unified-1 is rejected, unified-2 output
is preserved as evidence only and is not counted. Never relaunch either stage.
No installed/sealed/root/unit/sudo/service/gateway/scheduler/provider/auth/config
changes. No installation or release authority; 595 MUST NOT APPLY.
