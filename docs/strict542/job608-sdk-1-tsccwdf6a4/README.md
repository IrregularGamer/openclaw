# Job608 sdk-1 tsccwdf6a4 — actual evidence (595 MUST NOT APPLY)

Frozen source f6a4de2ebc6924d16fe559f9858bf8c50dce1eba; common export
e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145.
Stage P/stage-sdk-1-tsccwdf6a4, manifest
1474cff7f4da3873e348d8662f5e85a6a4f918cba405292ee532a020c5e461f0 (preflight 856fe90d,
independent APPROVE 647d59af). Inputs: accepted native and middle (receipt 9eb3083c).
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private.
Launched in the same worker after accepted sdk-0 (abd8eff8) as the preflight allows:
fresh live gates health up, no competing run, root free 8450367488, storage608 check
--stage sdk-1 0, verify-inputs0, sh -n0, exact manifest pin, result/log/rc absent,
2694s left (>=2655).

ONE admitted foreground offload (SPENT):
`offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-sdk-1 -- timeout -k 15s 2400s sh run608.sh`.
Actual client rc0, result exit0; offload log STEP608 sdk-1-build-done +137s, sdk-1-pass.
build.log has no error/fail/cancel lines.
Storage result check0 (`storage608.py result --stage sdk-1`): logical return 42148 bytes
< 33554432 cap.
Receipt SHA256 e57265f3879f60f18331c9270f3635c7d5b085579e6a6f75fb64a75ecc6b19ae
(exit0, source f6a4de2e, export e81e07d2, manifest 1474cff7). Outputs: build.log ab5dfafc…8f89,
checkpoint.tar.gz f31068ea0cb09e1a53862bcb3d1f0b50c9f21a5b32f3a37762bd4ceb5df49640
(31785 bytes) stays in the private result directory; never extract into or alter
installed state. Full hash list result-files.sha256; offload log gzip -n.
