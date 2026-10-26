# Independent job608 source review of application review gates

Reviewer: Rook `/root/review608_build`, independent from implementation.
Exact reviewed successor: `5758fc9b`; baseline: `257019fb`.

Verdict: APPROVE_SOURCE_ONLY. This is source review of the executable gate design, not an actual artifact, action, privilege-policy, next-seal, automatic queue or installation approval. The running source550dbbd0 diagnostic does not test these successor bytes; complete successor checks still require admitted offload.

I inspected the entire baseline-to-successor change and traced both staged action validation and the privileged application load/initial-check path. Distinct source/action/privilege-policy/seal/automatic-queue receipts now bind the same exact action, tree and source identity. The seal receipt separately binds the SHA256 of the exact validation.next.json before any application writes, through the existing additive fixed-target whole-seal amendment check. A privilege-policy review cannot substitute for the seal scope. Existing original-seal validation, metadata/guards, native owner checks, finite lifetime, worker quietness, rollback/poison handling and placement are unchanged.

The automatic review receipt identifies preparation build608, its actual review job and exact result hash. Application reads actual queue facts through SQLite mode=ro and requires a done build608, done review parented to608 and exact result bytes. The final correction also mirrors the installed queue transition’s first `VERDICT:\s*(APPROVE|CHANGES)` regex and requires APPROVE. No queue statuses or counters are written.

The initial182768d5 revision was rejected during this review. I executed a synthetic temporary-SQLite counterexample showing that an exact CHANGES result could pass when both jobs were done: queue reviews are done for either verdict, and later approved successors can mark ancestor builds done. Successor5758fc9b fixes this by verifying the actual first verdict. Regression cases now cover CHANGES, CHANGES followed by APPROVE, and absent verdict, all with correctly recomputed exact result hashes; they refuse.

Independent lightweight verification: `PYTHONPATH=docs/strict542 python3 -m unittest test_apply598.GuardedApplication.test_queue_gate_requires_actual_done_build_matching_review_and_exact_result test_application598.PreparationTests.test_action_binding_and_independent_reviews -v` passed2 tests. No full local suite, remote run, root operation, liveDB write, installed/sealed change or service action was performed.

Exact reviewed executable/test SHA256:

- `docs/strict542/application598.py`: `b5591e9d010e050d09075d7ac94339f3b22995882a42a54c38b854d850a304fc`
- `docs/strict542/apply598.py`: `8715a51891e45435dfb7f14789352fdc4e5d92a95dfded268fe243c04a8d2051`
- `docs/strict542/test_application598.py`: `4631dfb0b7bb62a7f8b07381da2c5e2c8117fa243b3cfc5a19f2828db9e71f6d`
- `docs/strict542/test_apply598.py`: `f0a19732b8133adb4e177b6c1c256ab6a256b1dfd2d3dea48a66fa4c5312721b`
