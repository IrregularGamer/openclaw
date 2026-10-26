# Independent job608 bounded diagnostic source review

Reviewer: Rook `/root/review608_build`, independent of implementation and runner.
Exact source: `550dbbd01425bb3eb027de9f0b9d94d5006a70d2`; prior head: `877458d7`.

Verdict: APPROVE_FOR_SINGLE_DIAGNOSTIC_ONLY. This grants no artifact, action, privilege-policy, seal, automatic queue or application approval. Exact export/archive inputs require their separate review.

I inspected all seven changed files against the prior head and traced the existing owning config, memory reader, normal build preflight, config census and runner lifecycle. The correction enables pinned Rolldown1.2.9 lazyBarrel only for the existing complete shared runtime graph. No new purity annotation, dependency externalization, entry split, owner identity or cancellation predicate is introduced. Existing experimental options are merged. The unchanged verbose-mode early return is irrelevant to the admitted diagnostic because inherited OPENCLAW compiler controls are refused.

The exact upstream option exists in https://github.com/rolldown/rolldown/blob/v1.2.9/packages/rolldown/src/options/input-options.ts . Its existing-side-effect-annotation contract is documented at https://rolldown.rs/in-depth/lazy-barrel-optimization . The new remote fixture checks the owning config selection and compares enabled/disabled bundler behavior for unannotated side effects, cross-entry mutable singleton identity, pure unused exports and dynamic exports. These two installed-dependency tests MUST pass remotely before compiler success is accepted; I did not execute them locally.

The runner verifies all three archive digests and completes extraction before deleting the fixed consumed remote archive names. It never deletes retained local inputs. Store cleanup follows complete installer exit, checks the committed isolated/clone-or-copy policy, requires real source/node_modules/store directories, and resolves installed symlinks before removing only the disposable export store. Symlinks escaping the source or broken links refuse before deletion. Dependency files are private clones/copies under the pinned install policy; deletion does not change their bytes. This is task-owned input cleanup, not kernel cache manipulation or added admission credit.

The new before/after memory samples and admission capacity record make the hypothesis measurable. No measured improvement is asserted in this review. The existing capacity/remaining-budget distinction,1625784320-byte floor, default2GiB/1CPU containment, fixed native pools, allocator setting,900s shared compiler deadline and process-group settlement remain unchanged. The normal full-build4352MiB heap gate also remains unchanged; an isolated runtime diagnostic cannot satisfy the required full typed build/package receipt.

The shell fails on digest/extraction/cleanup/test/install/fixture/admission/compiler failures and retains actual logs/status through its existing EXIT cleanup. Small checks remain before install; installed bundler tests remain before the compiler. No service, unit, sudoers, installed/sealed file, runtime credential, configuration, provider call, live install or scheduler action is added.

Independent verification: `sh -n docs/strict542/run-bounded608.sh`; Node syntax checks of the cleanup module and real-bundler fixture; `node --test docs/strict542/serial-probe598.test.mjs docs/strict542/isolated-config598.test.mjs docs/strict542/disposable-inputs608.test.mjs`:17 passing,0 failing/skipped/cancelled. No full suite or heavy local test was run.

Exact reviewed file SHA256:

- `tsdown.config.ts`: `6b73cafa59023041a6a3e51e2ebf0e819b7cdb0c25bf129e76c179087feaba12`
- `scripts/lib/disposable-build-inputs.mjs`: `f116ae6b0a0417f56878de9b2ba91bab92de3a767fa060f07b3e60c9344d7695`
- `docs/strict542/run-bounded608.sh`: `6c90a6e53001ac941cd33ca44e392c6905f99973408d3da741544008ba64ef5c`
- `docs/strict542/isolated-probe598.mts`: `b73ecb436275d42bf7223f64b3f2ac77575f4bb3437b6cf3c2e9f7111693031e`
- `docs/strict542/lazy-barrel608.test.mjs`: `6b83adc269c3fbd08a576f28a0ad690fe1e9e1ae3de1f007c67e39f6ae1b66b9`
- `docs/strict542/disposable-inputs608.test.mjs`: `044b55ce8970dd6bddb63cee6ad36cf2c5af68198182dfba3fa69e8909f6b831`
