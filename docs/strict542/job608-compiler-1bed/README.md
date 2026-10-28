# job608 compiler stage receipt (frozen 1bed)

Source-preparation evidence only. **595 MUST NOT APPLY.** No install authority.

- One admitted run from the UNUSED export `stage-compiler-1bed` (preflight e52d4c4f, independent APPROVE 6e38694f): `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-compiler -- timeout -k 15s 2400s sh run608.sh`. Launched 20:10:43Z, rc 0 by 20:15:47Z (~5 min, far under the 2400 s inner limit). Final step line: `STEP608 compiler-checks-pass`.
- Stage receipt sha256 3f91e8be…: manifest 5c39447c…, run_id stage608-compiler-1bed, source 1bed4d1b, export 5d7e9d57…, exit 0, stage_inputs equal to the accepted native outputs (e8198c1d/4a651254/2f81179f/0b6607e7).
- Output compiler/tests.log 88c06532… (committed here, byte-identical to the return): 5 node:test files, 10 tests, 10 pass, 0 fail, 0 cancelled; lockfile supply-chain policy check passed.
- Return guard: `storage608.py result --stage compiler` reports 26767 logical bytes, under the 16 MiB cap. Raw compiler-offload.log sha256 c217df73… (gzip copy here).
- The compiler output is a `package` input only (STAGES). The runtime stage (preflight 612c97be, APPROVE 2db30e9b) was launched once at 20:15:55Z from `stage-runtime-1bed`.
