# Independent package prerequisite source review608 — 2026-10-26

APPROVE ONLY the narrow source prerequisites below, inspected as an uncommitted
diff against `0b4fb1509feda9ca959479479639fe64f0c35233`. This is not approval to
promote admission, execute a package, accept an artifact or apply anything.

`nativeCompiler608(root, {required:true})` now refuses an absent native directory;
existing optional diagnostic calls retain their explicit stock result. Present
native inputs still pass the unchanged paired-receipt, owner-source, toolchain
and addon checks. The four native compile owner inputs and their pins are
unchanged. `admitBoundedPackage` now rejects inherited
`OPENCLAW_BUILD_VERBOSE` by presence: the canonical config's verbose branch
returns before installing the reviewed lazy-barrel options. Refusing empty,
zero and one values prevents the caller from selecting that alternate recipe.

Independent `node --test docs/strict542/native-compiler608.test.mjs
docs/strict542/bounded-package608.test.mjs` passed all8 tests, zero failures,
skips or cancellations (Node duration485.7ms; command wall0.63s). These are tiny
synthetic filesystem/policy fixtures; no compiler, install, offload, service,
configuration or provider operation ran. Source inspection confirms that
`build-all.mts`, `tsdown-bounded608.mts` and their canonical4352MiB guard are
unchanged by this prerequisite diff. The unchanged1625784320-byte floor,
all build phases, scanners and process-group owners are not altered.

Exact reviewed SHA-256 identities:

| File | SHA-256 |
| --- | --- |
| scripts/lib/native-compiler608.mjs | `25a85b0e2082f154d84d35b825733fe99875d27a1c744bf2358137ab2c1b68bf` |
| scripts/lib/bounded-package608.mjs | `e8cbb7543e69406529bcff3b0880ee21936c18418951ac128de65d4ed76cf31e` |
| docs/strict542/native-compiler608.test.mjs | `5278c38b63f3021e5468af1164627936ac9fb696a6b94aa8b0ae057fef4f9811` |
| docs/strict542/bounded-package608.test.mjs | `4a125dd762b8a0002b1c8007badda72c46783a66f24f40338e8c405ae9d90f58` |
| docs/strict542/job608-package-promotion-plan.md | `0421c8a196f600eb0f582d7961d6eca51417253f6e2a1870fa016c97400c2170` |

The plan correctly leaves native wiring/admission changes conditional on a
complete independently accepted combined diagnostic. Before later promotion,
inspect nested canonical declaration writers and all bundled-plugin selectors;
require native bytes before output mutation, propagate the validated native
environment to every compiler child, preserve canonical memory-derived heaps,
and make the actual builder select the bounded profile. The real full typed
build, frozen deploy, deterministic artifact and exact independent
source/action/privilege/seal plus automatic queue reviews remain outstanding.
No unbuilt artifact or future review identity is approved here.
