# job608 runtime stage receipt (frozen 1bed)

Source-preparation evidence only. **595 MUST NOT APPLY.** No install authority.

- One admitted run from the UNUSED export `stage-runtime-1bed` (preflight 612c97be, independent APPROVE 2db30e9b): `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-runtime -- timeout -k 15s 2400s sh run608.sh`. Launched 20:15:55Z, rc 0 by 20:41:19Z (~25 min, under the 2400 s inner limit). Final step line: `STEP608 runtime-pass`. build-all phase timings: total 16m 7.7s (tsdown-packages 8m 11.6s, tsdown-unified 6m 33.3s).
- Stage receipt sha256 726b81a2…: manifest 7deb2f4d…, run_id stage608-runtime-1bed, source 1bed4d1b, export 5d7e9d57…, exit 0, stage_inputs equal to the accepted native outputs.
- Outputs: runtime/checkpoint.tar.gz e8ae538c… (88503880 B, 8959 entries; stays only in private staging `stage-runtime-1bed/result608-runtime`, not committed) and runtime/build.log f30637b6… (gzip copy here).
- Return guard: `storage608.py result --stage runtime` reports 88569255 logical bytes, under the 128 MiB cap. A first guard call with a relative `..` path was refused (`source staging path redirect refused`), as designed; the absolute-path call passed. Raw runtime-offload.log sha256 83f45091… (gzip copy here).
- Next: unified-0..5 each take `result608-native` and `result608-runtime` as `--input` (STAGES). Each needs its own preflight and review, then one admitted run.
