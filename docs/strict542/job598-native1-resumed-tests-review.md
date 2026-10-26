# Independent resumed native-pool diagnostic input and test review

Reviewer: Rook `/root/outcome_review`, 2026-10-26 UTC.
Exact reviewed checkpoint: `3f6fb8c0edac76a23b13791d89105e606b079dc4`.
Verdict: **APPROVE INPUT AND TEST EVIDENCE ONLY**.

The retained export manifest byte-matches committed job598-native1-export.json
and binds exact source `8ce523c01d7299d516dfd3bf05882b9a75567370`.
Independently hashed the actual successor archive:
`697e339cf97a9917a1e330147a177d22422612be48d293ec1ce3b8a62092c92e`.
All 57 regular-file paths match the manifest and every payload matches its
exact committed source8ce bytes. Remaining members are ordinary directories.
The actual runner hash is
`4ddaa154badc56d2c8f1fc62def549fa52e9e8e7e7383000cb5793dc95a4c037`
and its bytes match source8ce run-isolated598.sh. This reviewer did not repeat
the large base archive read: the runner asserts all three archive digests before
its tests, and the actual resumed test output establishes those assertions ran
successfully. Parent-reported fresh local archive hashes are corroboration,
not an independently repeated large-archive hash claim by this reviewer.

Actual runs/598/native1-resumed-partial/strict542-checks/tests.log and
evidence.json byte-match the checkpoint's job598-native1-resumed-tests.txt/json.
Independently computed actual test log SHA256:
`4bc1703bcbb55f242705bd1951ad68163dd8d5d2692c77005644cd5faf51fea5`.
It matches the source-bound exit0 receipt. Counts are 101 Node gateway/auth/
transport tests, Python groups15+18+13+19+9, and11 isolated-config/policy tests:
186 total, all passing. This includes supervisor/IPC refusal, cancellation/
settlement and application preparation tests invoked by the exact runner.
The review inspected the actual already-executed log; it launched no duplicate
suite, offload command or runtime service.

The checkpoint correctly says the compiler diagnostic remains active. Neither
these tests nor earlier source review prove compilation feasibility, the full
owning build/profile/declaration/postbuild/package sequence, deterministic final
artifacts, installation, privilege-policy or release approval. No final compiler
outcome or cleanup result was available for this checkpoint. Automatic598 review
and every595 application gate, original seals, narrow release scope and fresh
genuine post-restart nonqueue HQ ownership/accepted-run acknowledgements remain
required. No concurrent retry, alternate slot or policy change follows.
