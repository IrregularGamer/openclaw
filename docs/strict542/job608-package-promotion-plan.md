# Native bounded package implementation plan608

> Execute inline with executing-plans and test-driven-development. Independent review is mandatory.

Spec: job608 changes round2 and job608-resume-after-workers.md.
Goal: make the existing complete typed boundedPackage route consume the exact
source-rebuilt native compiler, then produce the real frozen production package.
Use the existing native receipt validator and canonical build/memory/child owners.
No new compiler, graph partition, purity annotation or privilege mechanism.

- [ ] Add failing required-native absence and inherited verbose-control tests;
  extend the existing native owner with an explicit required mode and refuse the
  config control that bypasses lazyBarrel. Verify the focused tests and review.
- [ ] ONLY after the complete first native+split+lazy diagnostic succeeds and its
  actual outcome is independently accepted, wire boundedPackage's parent and
  direct driver to required validated native bytes before output mutation/native
  imports. Reject caller native controls; propagate only the derived trusted
  environment to every canonical phase, including both declaration writers.
  Keep canonical memory-derived heap/concurrency, unchanged1625784320-byte floor,
 2GiB1CPU ceiling, 900s compiler/2700s build deadlines and real settlement/scanners.
  Normal full/package4352MiB admission remains unchanged. No guard promotion on a
  partial or resource-refused diagnostic.
- [ ] Keep exactly the canonical ordered package phases and frozen deploy owner;
  change build598.sh's actual compiler route to boundedPackage. Resolve pnpm12.5.1
  before entering the clean builder environment; do not inherit npm-runner policy.
  Inspect nested declaration invocations before selecting the exact correction.
- [ ] Independently review exact source/export and run the full affected checks,
  typed inventory, real native parity/lazy/minifier fixtures, full typed build and
  production package from a committed secretless export through admitted offload.
  Retain actual artifact receipt and old/new identities, then independent exact
  source/action/privilege/seal reviews and actual automatic queue608 review.

Review focus: missing addon must never select stock; caller controls must not
disable optimization/checks; typed writers and publication must remain canonical;
derived heap limits must not become overrides; runner must actually choose the
reviewed bounded route. A diagnostic is never package evidence.

No installed/sealed/root/unit/sudoers/service/config/provider action.595's exact
natural-gap handoff and fresh post-restart owner+accepted-run gates remain
job608-to595.md and job598-HQ-HANDOFF.md; downstream575/588 and553 stay by reference.
