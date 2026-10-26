# Frozen package guard implementation plan

> Execute inline with the executing-plans and test-driven-development skills.

Goal: preserve pnpm12.5.1's default shared-lock frozen deployment and refuse
source-input drift or legacy fallback before a package receipt can be emitted.
This completes an existing preparation requirement; it grants no application authority.

The pinned implementation is pnpm commit859a9cfe39f2afd0c4198f14ca7ef628ee1de70e.
Its Rust shared path installs with frozen=true; legacy installs with false.
Workspace injection is unnecessary. Keep the existing default command and lifecycle
policy. Never substitute a legacy path or relax the original lock.
The standalone builder refuses every inherited NPM_CONFIG_/PNPM_CONFIG_ key,
including npm exec's own configuration metadata. Its eventual admitted launcher
must pass only fixed source-owner environment fields to the standalone builder,
after tool resolution; passing npm exec's environment through is unsupported.
The actual next export/launcher still requires exact independent review.

- [x] Add filesystem refusal tests for original-input drift, inherited package
  policy, missing/redirected target lock, fallback warnings and exclusive receipts.
- [x] Observe the missing guard fail, then implement a stdlib-only fixed-path
  preflight/receipt helper; it launches no command and changes no runtime state.
- [x] Wire checks before install, before deploy and before build evidence; retain
  exact command and record source/target lock and deploy-log hashes.
- [x] Correct the injection advice, run focused checks, commit/push and obtain
  independent exact source review. The final complete scoped suite and real
  packaging run remain admitted-offload requirements from committed source.

Independent source review6e687401 covers the corrected62b41567 guard. The admitted
c1bf240d scoped run subsequently passed209 checks including all6 package guard
checks, plus3 real typed-inventory checks. Actual packaging remains unexecuted.

Constraints: no installed/sealed/root/unit/service/config changes; default2GiB/1CPU;
no provider/auth/config transfer; no binary upload; full typed build and every
existing inventory, action, review, seal and genuine HQ ownership gate remain.
