# Job608 sdk-0 tsccwdf6a4 — actual evidence (595 MUST NOT APPLY)

Frozen source f6a4de2ebc6924d16fe559f9858bf8c50dce1eba; common export
e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145.
Stage P/stage-sdk-0-tsccwdf6a4, manifest
933ed22177cbb1121faeed9922d28bbd493b945c6bb6d806dd35e43dabd5891f (preflight 856fe90d,
independent APPROVE 647d59af). Inputs: accepted native and middle (receipt 9eb3083c).
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private.
Fresh live gates (fresh worker, first heavy action): health up, no competing run,
root free 8451547136, storage608 check --stage sdk-0 0, verify-inputs0, sh -n0,
exact manifest pin, result/log/rc absent, 3558s left.

ONE admitted foreground offload (SPENT):
`offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-sdk-0 -- timeout -k 15s 2400s sh run608.sh`.
Actual client rc0, result exit0, STEP608 build-done +465s, sdk-0-pass.
build.log has one line matching error/fail/cancel: line 21, a pnpm [WARN] for a
transient registry HTTP 502 on @types/ms-2.1.0 tarball (retry attempt 1), after which
install and build completed; no error/fail/cancel otherwise.
Storage result check0 (`storage608.py result --stage sdk-0`): logical return 1770948 bytes
< 33554432 cap.
Receipt SHA256 08530815eecb839d20085cae5ccd53fccd356eeb45b775548bd68587c0ce96b0
(exit0, source f6a4de2e, export e81e07d2, manifest 933ed221). Outputs: build.log 766e2130…c990,
checkpoint.tar.gz 09f9d2b8bc8b8d82581a7266891ec7b40ed53d3d59b20e0d57b38fbe8838c3ec
(1760089 bytes) stays in the private result directory; never extract into or alter
installed state. Full hash list result-files.sha256; offload log gzip -n.
sdk-1 NOT launched in this worker (2847s left after run, below 2655s once acceptance is done).
