# Job608 unified-3 tsccwdf6a4 launch — 595 MUST NOT APPLY

Same fresh worker after unified-2 actual rc0 (evidence in this commit) and
unified-1 independent ACCEPT8d229ccb. Frozen source f6a4de2e / export e81e07d2.
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private.
Exact stage P/stage-unified-3-tsccwdf6a4, export-manifest.json SHA256
4a43a68bc9df54b83547d20b04c8b345f6e54c1ec735c853d49cebada38054f0 (= preflight stages[2]).
Fresh verify-inputs0, sh-n0; result608-unified-3 and sibling log/rc absent.
Storage check0: unique1963273574, free5360328704, reserve2147483648, cap33554432.
Root free1394339840 (>1GB). Health up, no competing run. Deadline before
launch2807s (>=2655s required).

ONE foreground launch initiated ~2026-10-29T16:28Z:
`offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-3 -- timeout -k 15s 2400s sh run608.sh`.
Log P/unified-3-tsccwdf6a4-offload.log; rc in sibling .rc. Stage SPENT; never relaunch.
Unified-3 acceptance is conditional on unified-2 independent acceptance.
No installed/sealed/root/unit/sudo/service changes. 595 MUST NOT APPLY.
