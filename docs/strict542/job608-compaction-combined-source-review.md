# Independent combined diagnostic source/skeleton review608

VERDICT: CONDITIONAL ACCEPTANCE OF SOURCE AND UNUSED EXPORT SKELETON ONLY.
This records the independent read-only review of frozen source
6d9c429b4886d26c83888f1570f977ce63e215a7 and
/home/deploy/agentq/tmp/export608-native-compact-combined1. It does not approve
launch, execution outcome, package, application, action, privilege, seal or
automatic queue acceptance. The skeleton has no final manifest or receipt inputs.
This evidence document need not enter the frozen successor archive.

## Exact source and export identity

- Successor membership is exactly the prior253 paths in
  job608-native-phase-export.json union git diff --name-only00d5fe9f..6d9c429b:
  288 regular files and six directories, no links or unsafe paths. Every file
  matches frozen HEAD. Streaming git archive recreation over those exact paths
  reproduces SHA256
  20e64d26f2dd8b256ce1a760a3c78d68c17360086a66630b2d8ca3d9621b5c43.
- Runner run608.sh is byte-equal to frozen docs/strict542/run-native608.sh,
  SHA2562073d7793b2b067928853206309ba88d8f6e6e26f3afd94fa21c41b464bcabca.
  Its sole change from the predecessor adds the two compaction policy checks.
- Base source598.tar has device2049/inode1583918/size689664000/linkcount16,
  identical to the retained reviewed export608-native-phase-trace archive.
  Inherit its pin
  e79a0e45a4eaea4afe325ca94ba201d5ae43d09d8c15dc07d0695c87ba743de3;
  the690MB base was not reread or newly rehashed.
- Native native598.tar has device2049/inode1583919/size921600/linkcount16,
  identical to the predecessor. Recomputed SHA256
  d73e4e35720ffcb71856ce8168e75fa3b4fd49251fd78c811e1abded8b2701de.
  Its61 members contain no links or special entries.
- Upstream rolldown608-source.tar.gz has device2049/inode308931/size5962781/
  linkcount15, identical to the predecessor. Recomputed SHA256
  203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac.
  This unchanged official archive contains two safe relative symlinks:
  CLAUDE.md -> AGENTS.md and fixture
  packages/rolldown/tests/fixtures/builtin-plugin/import-glob/follow-symlinks/linked/my-lib
  -> ../packages/my-lib, beneath its rolldown-5b4746e442989d770c606ce08d2737e6aafbd25d
  root. The successor/native no-link finding does not apply to these inherited
  upstream source links.

## Coverage and native source consumption

The runner retains all240 required affected checks: the predecessor238 plus
two compaction policy checks. Eight stock/native parity variants, the release
trace fixture, stock/native lazy-barrel and minifier fixtures, the AI build and
all57 main configs remain present. The census includes all four portable workers
at indices46..49. The probe, fixture and worker-phase owners are unchanged from
the predecessor. Original success predicates, cancellation/settlement,
config15 tracing, capacity floor, fixed one-CPU pools and900-second probe
deadline are retained. No check or predicate was weakened.

Accepted compile receipt SHA256
4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e
matches all four frozen owning source files. Recomputed all pinned upstream
file hashes and all six prepared-source hashes without writing source; they
match the accepted receipt. Its addon pin is
0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042.

prepare-native-consumer608.py admits exactly two manifest-pinned receipt inputs,
requires completed matching compile/libtests stages and compaction proof,
rebuilds the addon from source in the new lease, then requires exact compile
receipt bytes and addon digest equality. No uploaded addon, cargo target/cache,
toolchain or dependency tree supplies that rebuild. The downstream native owner
also validates source/toolchain policy and addon identity before consumption.

## Conditions and limits

Before a combined launch, require settled independently accepted matching new
libtests evidence, then an independent exact final manifest and receipt-input
review. Historical17df receipts cannot satisfy this condition. Require normal
controller/lease admission, default2GiB1CPU, at least51 minutes of genuine
foreground worker lifetime at launch, and hard outer2700s plus15s grace.
The runner's inner5400s build timeout does not authorize a longer outer run.
Never overlap this diagnostic with the active libtests stage.

Resource and timing fit remain empirical. Recorded compilation consumed
9m40s ecmascript plus20m21s addon; the prior partial probe consumed about445s.
The complete new probe, setup and settlement may exhaust the outer bound.
No deadline increase, resource increase, check omission or unchanged retry is
authorized by this review. Missing, refused, failed or partial output is not
diagnostic success.

Declined to judge: active libtests outcome; config46 and full resource fit;
complete combined execution; typed frozen production package; application,
action, privilege, original-baseline reconciliation/seal and automatic queue
acceptance. These retain their separate evidence and review gates.

Review performed only read-only git/hash/stat/archive/source inspection. No
tests, builds, offload, runtime/protected changes or network actions were run.
The source checkout was clean at review completion. The later single-document
recording commit changes no frozen source or export input.
