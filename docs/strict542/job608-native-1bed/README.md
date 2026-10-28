# job608 native stage receipt (frozen 1bed)

Source-preparation evidence only. **595 MUST NOT APPLY.** No install authority.

- One admitted run from the UNUSED export `stage-native-1bed` (preflight a287d878, independent APPROVE 4ce25cff): `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh`. Launched 19:26:40Z, rc 0 at 20:01:21Z (~2081 s, under the 2400 s inner limit). Final step line: `STEP608 native-rebuild-pass`.
- Stage receipt: manifest 31330bc3…, run_id stage608-native-1bed, source 1bed4d1b, export 5d7e9d57…, exit 0.
- Outputs: receipt.json 4a651254… and libtests-receipt.json 2f81179f…, both equal to the pinned manifest `native_stage_outputs`. Addon rolldown-binding.linux-x64-gnu.node 0b6607e7… (48 MB). It stays only in the private staging return `stage-native-1bed/result608-native` and is not committed.
- Return guard: `storage608.py result --stage native` reports 48652047 logical bytes, under the 64 MiB cap.
- Raw native-offload.log sha256 9d4cd0ca…, native-rebuild.log da088b35… (gzip copy here).
- Next: the compiler and runtime stages each take `result608-native` as a stage input (`prepare-stage608-export.py --input`). Each needs its own preflight and review, then one admitted run in a worker with enough time left.
