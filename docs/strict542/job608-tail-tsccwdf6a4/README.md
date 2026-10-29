# Job608 tail tsccwdf6a4 — actual evidence (595 MUST NOT APPLY)

Frozen source f6a4de2ebc6924d16fe559f9858bf8c50dce1eba; common export e81e07d2.
Stage P/stage-tail-tsccwdf6a4, manifest add772f5f0e861bf1a28f8ecdf1d616aea4a505af745579e192bc9e17fe3bbdb
(preflight 40043eb9, independent APPROVE 4a45d64c). Inputs: accepted native, middle (9eb3083c),
sdk-0 (08530815), sdk-1 (e57265f3). P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private.
Fresh-worker FIRST heavy action. Live gates: health up, no competing run, root free 8439132160,
storage608 check --stage tail 0, verify-inputs0, sh -n0, exact manifest pin, result/log/rc absent,
~3450s left (>=2655).

ONE admitted foreground offload (SPENT):
`offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-tail -- timeout -k 15s 2400s sh run608.sh`.
Client rc0, result exit0; STEP608 tail-build-done +237s, tail-pass. The only error/fail/cancel
match in build.log is the asset filename `update-failure-report-*.js` (not a failure).
Receipt SHA256 8df9caa882488b0356d70f1b39f1939ee8695fd6177ec8b995a55e9e453cae61 (exit0, source
f6a4de2e, export e81e07d2, manifest add772f5). checkpoint.tar.gz b5b8f9ff…86aa (161524783 bytes)
stays private; never extracted into installed state. Hashes: result-files.sha256.

## FINITE RETURN CAP GATE FAILED under the frozen storage608 (NOT YET ACCEPTED)
`storage608.py result --stage tail` at the frozen plan: `finite stage return cap exceeded`
(logical return 161610911 > tail cap 134217728 = 128MiB). The checkpoint really is the full tail dist
(dist/worker ~108MB, control-ui ~91MB, package-update-activation-recovery.mjs ~66MB, extensions ~51MB
uncompressed), so the 128MiB planning cap was undersized and the gate was not misread.
The proposed fix is the next commit: a source-only storage608 correction, tail cap to 192MiB.
The aggregate forecast stays within 4GiB: 696548381 + 256MiB + 2848MiB + 128MiB = 4085546013 <= 4294967296.
Under the corrected cap the existing result passes (161610911 <= 201326592, rc0). Acceptance of
this result requires an independent review of BOTH the cap correction and this evidence; it must not
be accepted without that review.
