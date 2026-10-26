# Independent frozen package source review, 2026-10-26

APPROVE the source preparation at
`62b41567552a830a78972f4da9e177801cab604f`, comprising initial recipe
`f92b707b4c9aa2e3655a513e9b3cef2c5e725c01`, alias correction `245ab401`,
and the final package-configuration overlay correction. No blocking finding
remains within this source policy scope. No package manager, compiler,
offload, runtime, service, auth or provider operation ran for this review.

## Findings and exact maintained source

The initial finite key list allowed real pnpm environment overlays that can
change lifecycle build allow-lists, dependency cooldown and lock verification
without changing the pinned workspace YAML. Its camel-case correction alone
did not resolve that issue. The final source refuses all case-normalized
`PNPM_CONFIG_*` and `NPM_CONFIG_*` variables by presence, as well as the
explicit workspace-directory control (`frozen-package608.py:27-33`). This
covers the earlier aliases and `NPM_CONFIG_WORKSPACE_DIR`; it also covers
the documented pnpm lifecycle, hook, cooldown and trust overlays. A real
future invocation must satisfy this clean-environment boundary. Broad refusal
may reject npm-runner-injected configuration too; no such invocation was
claimed to have passed here.

The three original pins were independently compared with `git show` of base
`c790ba44938bd90f75fb41f2f2eeaaff287df546`; all match:

| Original input | SHA-256 |
| --- | --- |
| pnpm-lock.yaml | `091ede3cb510110ed2b1ca8858100066add16cb3b91bcd0ff097d89f75035751` |
| pnpm-workspace.yaml | `5e672012b9678d1d40ec40e9fdff43283b7c4f947052cc24168b88d1f51ec872` |
| .npmrc | `f1d021e2abdf8817d83e35feb1f5d604e8c985aa0553bec3d417cf6f93e9c09c` |

`build598.sh:15-24` checks these private regular-file pins before install,
after frozen install, after the complete build/before deploy and after deploy.
The existing default command remains unchanged:

    pnpm --filter openclaw --prod deploy result598-build/runtime

Deploy failure exits before receipt preparation. The guard refuses the exact
pinned implementation's missing/inapplicable-lock fallback and forced-legacy
warning text; it requires a private regular target lock and nonempty deploy
log. The exclusive receipt records source/target lock identities, original
configuration pins, command and deploy-log hash (`frozen-package608.py:35-55`).
`build598.sh:34-44` rechecks both locks/log and binds the package receipt and
its hash into build evidence. It cannot turn absent production dependencies
or incomplete runtime output into an application-ready tree.

| Maintained file under docs/strict542/ | SHA-256 |
| --- | --- |
| frozen-package608.py | `d50f132546dd4b6489c207f7d1ec8d4a9629abab1f97ecf1a32d64fcf0089c84` |
| test_frozen_package608.py | `6432a24cb0fd1fd179f243d8fed18d5a5005db476e503b2a97af146393f1038d` |
| build598.sh | `a34161e38338a56f0432ce1273b54b609047b3d5736e65267e50222b7e216821` |
| job608-to595.md | `3677ddf8259be016abf720db03399c6baa00c6c996e310c5037ac8b11f9e5dd2` |
| job608-frozen-package-plan.md | `4c3c9084fa8b7b8d3bb96a66901845dfe79be4aea2218a60008a33ca576d636c` |

## Immutable upstream evidence

pnpm12.5.1 is pinned to commit
`859a9cfe39f2afd0c4198f14ca7ef628ee1de70e`, annotated tag object
`ea85d71ad4a9eef7285827717b5db7ae1d5129e2`. The current
[official deploy documentation](https://pnpm.io/cli/deploy) confirms injection
is unnecessary since12.2; version-specific behavior below is established by
the pinned Rust source, not by applying later documentation retroactively.

Paths below are relative to `pnpm/crates/` in that upstream commit:

| Upstream source | SHA-256 |
| --- | --- |
| cli/src/cli_args/deploy.rs | `91c04234cbfb64abd861d70402154c809594948f2bb19b4ddc18196fb173005e` |
| cli/src/cli_args/deploy/install.rs | `27479580b6892689018a12f46fd230e2d2d1444472b26cb1ed7609cef8627576` |
| cli/src/cli_args/deploy/lockfile.rs | `b2b772c37303b4cf248337242ed0578bcde1f32163af65ebfa0e745cdb4c5dc0` |
| cli/src/cli_args/deploy/target.rs | `45bfdbad0f7826b6b43e576cbca541303051c9c3247d049b63d35958fc855faa` |
| config/src/env_overlay.rs | `08d4be750146f3521c37a547772dd000d977f54ef9f7a97625d3b141196dcd16` |

[deploy.rs:181-205,262-303](https://github.com/pnpm/pnpm/blob/859a9cfe39f2afd0c4198f14ca7ef628ee1de70e/pnpm/crates/cli/src/cli_args/deploy.rs)
selects the default shared-lock path, generates dedicated target files and
passes frozen=true; legacy instead passes false. Missing or inapplicable
shared locks can fall back. Adding a frozen CLI flag is not a substitute for
retaining and verifying this path.
[install.rs:97-118,175-200,219-232](https://github.com/pnpm/pnpm/blob/859a9cfe39f2afd0c4198f14ca7ef628ee1de70e/pnpm/crates/cli/src/cli_args/deploy/install.rs)
anchors installation to the target, disables global virtual-store use and
sets the frozen lock policy. It retains lifecycle policy; the shared path
carries the source build allow-list. No injection or legacy flag is needed.

[lockfile.rs:274-315,354-374](https://github.com/pnpm/pnpm/blob/859a9cfe39f2afd0c4198f14ca7ef628ee1de70e/pnpm/crates/cli/src/cli_args/deploy/lockfile.rs)
retains build policy and defines fallback conditions.
[target.rs:21-81,222-245,329-353](https://github.com/pnpm/pnpm/blob/859a9cfe39f2afd0c4198f14ca7ef628ee1de70e/pnpm/crates/cli/src/cli_args/deploy/target.rs)
rejects unsafe targets, copies project files with CloneOrCopy and writes the
derived lock/manifest only beneath the target. Dependency installation keeps
the original workspace's clone-or-copy policy. Final runtime inventory must
still establish private inodes and valid contained relative symlinks.
[env_overlay.rs:1-11,304-367](https://github.com/pnpm/pnpm/blob/859a9cfe39f2afd0c4198f14ca7ef628ee1de70e/pnpm/crates/config/src/env_overlay.rs)
establishes environment precedence over workspace YAML and the concrete
overlays that required the final correction.

## Verification and remaining gates

At the exact final source, all SIX focused `test_frozen_package608.py` tests
passed. `sh -n docs/strict542/build598.sh` and Python compilation of helper
and tests exited0. The retained initial red log records five missing-helper
failures; the final sixth case covers the subsequently discovered policy
overlays. No full suite or real packaging run was substituted for these checks.

The helper validates pinned inputs and records identities; calling it alone
does not authenticate execution or prove the target lock's resolved graph.
Actual admitted logs, successful unchanged default deploy, complete typed build,
production dependency inventory, lifecycle results and runtime checks remain
required. Timestamp/build reproducibility is not established for pnpm12.5.1.
No actual complete runtime/tree/action/next-seal package has been approved.
Independent artifact-bound source/action/privilege/seal and actual automatic
queue reviews, original baseline/settlement checks and fresh genuine HQ
owner/run acknowledgements remain mandatory before any application.
