# Independent preflight review: job608 sdk-0/sdk-1 tsccwdf6a4

Reviewed `docs/strict542/job608-sdk0-1-tsccwdf6a4-preflight.md` at commit 856fe90d. Review date 2026-10-29.
The review was read-only: nothing was launched and no stage dir was changed.
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private, S=P/stage-sdk-N-tsccwdf6a4.

## Check 1: manifest pin, committed copy and identity
- sdk-0 PASS. The sha256 of S/export-manifest.json is 933ed22177cbb1121faeed9922d28bbd493b945c6bb6d806dd35e43dabd5891f. That matches the doc pin. `cmp` shows the file byte-equals job608-sdk-0-tsccwdf6a4-export-manifest.json. Fields: stage=sdk-0, execution_state=UNUSED, source_commit=f6a4de2ebc6924d16fe559f9858bf8c50dce1eba, source_export_sha256=e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145.
- sdk-1 PASS. The sha256 is 1474cff7f4da3873e348d8662f5e85a6a4f918cba405292ee532a020c5e461f0. That matches the doc pin. The file byte-equals job608-sdk-1-tsccwdf6a4-export-manifest.json. Fields: stage=sdk-1, execution_state=UNUSED, with the same source_commit and source_export_sha256 as sdk-0.

## Check 2: runner and stage608.py byte-equal f6a4de2e
- sdk-0 PASS. `cmp` returns 0 for S/run608.sh against `git show f6a4de2e:docs/strict542/run-stage608.sh`. It also returns 0 for S/stage608.py against `git show f6a4de2e:docs/strict542/stage608.py`.
- sdk-1 PASS. Both `cmp` checks return 0.

## Check 3: stage inputs
STAGES in f6a4de2e stage608.py: `'sdk-' + str(i): ['native', 'middle']` for i in 0 and 1.
- sdk-0 PASS. S/stage608-inputs holds exactly `middle` and `native`. Manifest stage_inputs lists 7 files: middle/{build.log, checkpoint.tar.gz, stage-receipt.json} and native/{libtests-receipt.json, receipt.json, rolldown-binding.linux-x64-gnu.node, stage-receipt.json}. Every file's on-disk sha256 equals its manifest value. native/stage-receipt.json (1047485796fe…) byte-equals P/stage-native-tsccwdf6a4/result608-native/native/stage-receipt.json. middle/stage-receipt.json has sha256 9eb3083c62bbb5ecf715a375ec00f344b4d21c70fc291bd695ee92be5937d2cf. That equals P/stage-middle-tsccwdf6a4/result608-middle/middle/stage-receipt.json and the receipt that job608-middle-tsccwdf6a4-independent-acceptance.md accepts (line 27, VERDICT: ACCEPT).
- sdk-1 PASS. It has the same input set, and its 7 hashes are identical to sdk-0's. The native receipt is byte-equal and the middle receipt is 9eb3083c….

## Check 4: verify-inputs, sh -n and absent outputs
- sdk-0 PASS. `cd S && python3 -I -B stage608.py verify-inputs` returned rc=0. `sh -n run608.sh` returned rc=0. P/sdk-0-tsccwdf6a4-offload.log, P/sdk-0-tsccwdf6a4-offload.rc and S/result608-sdk-0 are all absent (ENOENT).
- sdk-1 PASS. verify-inputs returned rc=0 and `sh -n` returned rc=0. P/sdk-1-tsccwdf6a4-offload.log, P/sdk-1-tsccwdf6a4-offload.rc and S/result608-sdk-1 are all absent.

## Check 5: launch command
- sdk-0 and sdk-1 PASS. The command is `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-sdk-N -- timeout -k 15s 2400s sh run608.sh`, with fixed finite caps. The inner command is the fixed runner, so the caller does not choose the root command. The only substitution allowed is N, picked by the manifest (0 or 1). The runner takes no caller argv. Its internal build budget is `2280 - elapsed` (run608.sh:143), which sits inside the 2400s inner limit. The doc requires >=2655s left after preflight, which covers 2460s plus margin. It also requires one launch per stage and says "Never detached". The output is redirected to a log, and the rc is captured in the foreground.

## Notes
The doc says the runner keeps a "fixed 2280s inner build budget". That refers to the build-step budget inside the outer 2400s timeout and is consistent with run608.sh.

VERDICT: APPROVE
