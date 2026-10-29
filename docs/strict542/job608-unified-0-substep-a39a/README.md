# job608 unified-0 a39a: actual timeout evidence

SOURCE ONLY; **595 MUST NOT APPLY.** The ONE reviewed launch (preflight
713ec981) began 2026-10-29 ~04:57 UTC; remote stage began ~05:00:54.
Command: `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts
result608-unified-0 -- timeout -k 15s 2400s sh run608.sh`.

Actual client exited124 (~05:40 UTC). The inner build printed
`STEP608 unified-0-build-fail 124 +2280s`, preserving the fixed2258s build
budget after setup. It reached `openclaw-dts-base: cache miss (disabled)`
after pnpm's2m3.1s frozen install and then repeated tsdown liveness messages.
No native API phase was reported. Do not infer first-global completion,
checker eviction, memory pressure or the precise stalled operation from this tail.
No result608-unified-0 directory, stage receipt, checkpoint, artifact or package
was returned. This immutable prelaunch manifest still says UNUSED; actual
attempt state is **SPENT/FAILURE; never replay**. outcome.json is failure
evidence, not a successful stage receipt. It records exact raw log digest.

Accepted checks/native/runtime remain accepted at a39a. Compiler preflight
3d36a234/independent9248f534 remains UNUSED and must not launch after this
failed prerequisite. No further build stage is promoted. Use the source-owner
analysis in ../job608-single-config-owner-analysis.md: unified-0 already owns
ONE config and explicit emit root. Its stale config-subset fallback is invalid.
Next is a NEW reviewed finite API observer rebound to a39a/current inputs,
not the historical1bed helper or spent export. Preserve all six diagnostics,
roots, input seal, cancellation, close/publication and budgets. The source-backed
checker-cache scheduling candidate is unproven for this actual timeout.

No installed/sealed/root/unit/sudoers/service/budget, auth/config/credential,
provider, scheduler or production changes occurred. All final package, artifact,
action, privilege, seal, automatic-review and genuine HQ gates remain open.
