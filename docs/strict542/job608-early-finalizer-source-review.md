# Independent early-finalizer source review608 — 2026-10-26

Conditional source-only approval of the narrow candidate against53abb80b. No
confirmed correctness blocker was found in these exact bytes. This is not
compiler-build, parity, memory-fit, package, artifact or application acceptance.

| File | SHA-256 |
| --- | --- |
| scripts/lib/prepare-native608.py | `db1c2df8fd0a27930782d5b6678b3849bfb629d9f24a253b47d042a4f559fa92` |
| scripts/lib/last-use-ast608.rs | `8d293f921d754f3ffca6f60eaec8b61fc577ebef779d9c5714db5f46c4cf2da4` |
| docs/strict542/rolldown-source-pin608.json | `644d4ab9b970df0aaa34070cd8db96add012fb82db9f72bce7878571549988ca` |
| docs/strict542/build-native608.py | `514a093d3f5198627a8a86428199930f36d695ae41fd2c734dc363e903f921f8` |
| docs/strict542/test_native_finalizer608.py | `6213bd8674bc2ec3d3214598888c5b0f1e2cf62f535a1b12de818e7d04557e78` |

The patch extracts the exact original finalizer predicate once, then uses the
same closure both for retention and the existing filter. Required-order runtime
and strict live-chunk behavior remain present. The mask unions that predicate
with every normal module.idx in every chunk, including chunks filtered only
after rendering. Canonical index equality is asserted; only unneeded Option
values are taken, preserving table length, indices and retained missing-AST
behavior. Pruning occurs inside finalize_modules after prior metadata readers
and before parallel finalizer allocations. The pinned generate-stage call path
then passes the AST table to the renderer; its complete chunk census is retained.
The other original finalizer bytes reconstruct identically in the focused test.
No graph, entry, dependency, purity, finalizer predicate or output-order policy
change is introduced.

The generic release helper checks census length and has drop-observer coverage
for finalizer-only, renderer-only, shared and unused slots plus incomplete
census refusal. The new lifetime stage retains existing digest-verified source
and official toolchain setup, actual standalone Rust helper tests, and the
existing old-retention negative control. It exits before cargo/addon/libtests,
emits a distinct LIFETIME kind/stage and cannot satisfy the native consumer's
required compile/libtest receipt identities. Changed owner inputs and patched
source inventory invalidate old native receipts; no prior addon pin or passing
receipt can be reused for this correction.

Independent verification: both Python patch-contract tests passed in0.762s using
the digest-pinned upstream archive; all9 focused Node native/policy tests passed
in347.7ms. Generated finalizer source was also inspected. These checks did not
compile the modified Rolldown finalizer or execute Rust helper tests. Rust API,
borrow-checking, real finalizer behavior, output parity and resource fit remain
unproven until their actual admitted validation. No local heavy run occurred.

This source is suitable for a separately reviewed fresh secretless lifetime-only
export and one normally admitted finite validation, with no uploaded binary or
old native receipt input. Exact export/runner review and a full outer-deadline,
kill-grace, transfer and settlement window within the foreground owner's actual
lifetime are prerequisites. At16:54:10UTC the worker expiring16:59:08 has298s
left, so a full300s command plus handling cannot be admitted in that window;
use a separately reviewed shorter bound only if it actually fits, or defer.
No lifetime result is predicted. Any subsequent compiler/libtest/combined run
needs fresh identities and its own reviewed plan. Existing4352MiB package guard,
1625784320-byte floor and all application gates remain unchanged. No guard
promotion or unchanged failed-diagnostic retry is authorized here.
