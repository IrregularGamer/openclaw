# Independent compaction compile export review — APPROVE ONE bounded stage

Exact source2f6788455aea5051cdc5b748cd06554f3ab039a1, manifest-only3bfc1085.
Export /home/deploy/agentq/tmp/export608-native-compact1.
Manifest SHA256 0e3404864bf45469a9b859555200492475436461a7537e9af099080b22836584.
Independently recomputed manifest, runner, successor and upstream archive hashes;
all match committed job608-compaction-compile-export.json. Successor contains
exactly the four declared regular owning source files, byte-identical to the
source commit, with no symlink/hardlink entries. Export has only manifest,
runner, successor source tar and pinned upstream source archive; no runtime
config/auth/credentials/database/toolchain/dependency/cache/addon input.

Runner SHA256 2c6e313a9aa7dddfbbdfe36986325bed7f46346d6e05822d4c032ca344290e57.
Successor SHA256 5de54d460fc20c2fa9a6b5535ff649315a0bb9432bf93a099d5ad4b605611ed8.
Upstream SHA256 203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac.
Runner is byte-identical to maintained run-native608-stage.sh, verifies archive
digests before extraction, stages disposable source, captures receipts/logs,
and removes only its disposable source/native tree on ordinary exit.

Approve ONE foreground `compile` stage only through ordinary admitted offload,
default2GiB1CPU, with a HARD OUTER2400s deadline plus15s termination grace and
at least46min remaining foreground worker lifetime at launch. The runner's
internal5400s guard is longer; this approval REQUIRES the outer2400s bound and
does not authorize5400s execution. No unchanged retry or concurrent stages.
Exact source review is job608-compaction-source-review.md. The real full
 ecmascript libsuite and named regression, standalone7 lifetime tests and
retention negative control precede addon acceptance. Outcome must be retained
and independently reviewed; a successful compile alone is not build/package
or application authority. No native binary or dependency tree is uploaded.
No local heavy execution, cgroup/budget/privilege/unit/runtime/seal mutation.
