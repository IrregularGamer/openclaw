# job608 runtime tsccwdf6a4 at f6a4de2e — actual run evidence (595 MUST NOT APPLY)

- Stage P/stage-runtime-tsccwdf6a4, manifest d0d4d630af82f520dbe2609ac7f8ad4018d72ccffe24ba1e4bbd5bdc21e2fbf7,
  preflight review 396aa580, launched once at 2026-10-29T14:22:36Z with
  `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-runtime -- timeout -k 15s 2400s sh run608.sh`.
- offload rc 0; STEP608 runtime-build-done +729s, runtime-pass; result exit-code.txt 0.
- stage-receipt.json sha256 3e284e2c...; outputs runtime/build.log 242dfc93..., runtime/checkpoint.tar.gz
  9e028d031b3b06d8fbbae8c4817e53ee06896e8e05097fa261363af73bdbd9c5 (88 MB, not committed; stays in
  P/stage-runtime-tsccwdf6a4/result608-runtime, read-only by procedure). stage_inputs = the 4 accepted native pins
  (binding 0b6607e7).
- result-files.sha256 lists every result file. The stage is SPENT: never relaunch.
- Pending: independent acceptance, then unified-0 preparation (inputs result608-native + result608-runtime).
