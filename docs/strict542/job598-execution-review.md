# Independent job598 execution-evidence review

Reviewer: Rook `/root/review598_successor`, separate from implementation.
Scope: documentation and preserved execution evidence only. Implementation remains
`de7369e4883abb96ac4cacac9a0ea89e2ae2ee29`, independently source/design reviewed
in6766a334. Provenance separation reviewed at
`97f967504e371cf9a01e63e8329c5c8eff30e7f6`; final unit/provenance correction
reviewed at `bf87b2c17ee180002bbbc10a8fe56872b80ee6c0`.
Final execution-evidence.json SHA256 is
`19262e260a9149375881a651cf9690f04e939b0ded411622824d2d399b714dd1`.
Final HQ-HANDOFF.md SHA256 is
`ab0ab154187cf49d27d6da40d89763b31ddc425d656f31dce1eb361f1c8c8c9c`.

Verdict: APPROVE_EVIDENCE_ONLY. Job598 is incomplete. No runtime artifact, action,
next seal, loaded generation, production application or automatic queue approval
is approved or established by this review.

Both preserved test logs record101 passing Node tests and Python groups
15+18+13+19+9=74, totaling175 successful relevant tests per run. I independently
recomputed their hashes, inspected the summaries and compared the committed bytes
to the two preserved export outputs. This is review of actual execution evidence,
not a claim that this reviewer reran the tests.

| Preserved evidence | SHA256 |
| --- | --- |
| job598-execution-tests.txt | ea103af172f8c72313f728eff1dd1d9f1c652bfab1f43d7fe33947d7186daf2a |
| job598-pinned-execution-tests.txt | f97165515f512aeba6a0f3a2d1d0bc869d45e2d397541d31c2793a8b1eabbd54 |
| job598-build-refusal.txt | fe16ab555ac1924bb5938c626bea938577e3f437c594f1a45e40185a6637fbe9 |

The first attempt refused pnpm9.15.4 against exact required12.5.1. The second
log records a completed frozen installation using12.5.1, then an upstream build
preflight refusal: resolved839MB heap against required4352MB, exit1 before build
output generation. A successful dependency installation is not a successful build.

I inspected exact de7369e4 scripts/tsdown-build.mts (SHA256
96a82d7ed394cf75eb51f2cbd33036e4d1dfdf6e1212aa7f58990e9adbf091db)
and scripts/build-all.mts (SHA256
a1849e7453147791d866994a850c0dd158a0ad9b79dc525335399b3aa9f90e91).
The complete full/package/ciArtifacts/strictSmoke/pluginSdkStrictSmoke plans
share the full-plan memory preflight. Upstream comments report4730MiB peak for
a5GiB slice and prior4GiB/2816MiB unified-runtime failures even without declaration
emission. That historical upstream measurement is not a measurement by this
refused run. Partial/watch profiles do not establish a complete reviewed runtime
artifact within2GiB. No supported complete2GiB path was established by this review.

The handoff accurately preserves the incomplete build gate and forbids overriding
the heap guard, exceeding broker budgets, local/Docker builds, synthetic receipts,
or applying the package in595. Continuation requires a reviewed bounded source
correction or another supported admitted build path, then actual passing build,
exact artifact/action/privilege-policy/next-seal reviews and automatic queue review.
No runtime mutation or heavy execution was performed by this reviewer.
