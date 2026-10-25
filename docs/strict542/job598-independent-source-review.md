# Independent job598 source and privilege-design review

Reviewer: Rook independent reviewer `/root/review598`, separate from implementation.
Reviewed source: `492d19b64c9bfc6aa53dd115c30c0c5892199968`, including
`a035ef950fba2865a5fa04701411dd191eff8b9c`,
`7c18fd80d6cf91d2f53a55baf1cf9db87414720d`,
`2b72ff81b644bbb6d5e0a2d1bfc3ef96f60c8906` and
`fceeb80e`.

Verdict: **APPROVE_SOURCE_ONLY**, separately **APPROVE_PRIVILEGE_DESIGN_ONLY**.
This is neither an action/tree/next-seal approval nor installation authority.
The actual admitted build artifact, logs, broker receipt, canonical action and
exact next seal require subsequent independent review, plus automatic queue598
review. No real application action is approved by this document.

Exact reviewed SHA256 identities:

| Source | SHA256 |
| --- | --- |
| apply598.py | 8971f3979c6f67f3f108c39ff911da95092f8e83dca70460e6c63eb07931d319 |
| application598.py | f65de3f8e5d5a58cc4302a29965cea17a54b24f1b3a638d0d31e22ee809bf4a0 |
| build598.sh | 534319c9c491bda8290e06ae223c6f41640b7a9951f78ee7474a791259307e77 |
| strict542-owner.service | ab297fe2afe0559c467ddc6e32a4c041a0cd143daad612ceabcf23571ae4f469 |
| 90-strict542-598.conf | 45634d116cd636458352514b15bc081fe9b78070444655b4ae2d069e18732ecc |
| root_owner_supervisor.py | 0d8bdeda5e916ddc25bda48b1e3da36252a710c88dfe36f875c1b05290709fdc |
| native_owner_server.py | a145387432fbf8e17fffbf1e552328e651054e9d603b1d9bdad2d8494dc6a373 |

The external native source remains pinned to
`bca40971a35d160ad87b5d18fd1cc7f7730a7f90d2bb5b8480f3d7d79d11c182`.
The endpoint derives identity from SO_PEERCRED, retains the original native
owner/start/cgroup/caller/MainPID predicates, and accepts only operator-read
plus cancellation. No caller-selected root command or sudo rule is introduced.
The fixed root supervisor migrates only its new endpoint into the existing HQ
cgroup. Its parent remains in the bounded system unit. Inherited address/CPU
limits, tree CPU accounting, finite lifetime and parent pidfd cancellation
constrain the migrated endpoint. This does not establish an HQ session or run.

The application holds the native admission lock, requires genuine finite HQ
binding, validates the original whole seal and exact old metadata, and invokes
the existing native quiet predicate for registered worker, fixture and remote
settlement. The existing remote lease-cancel RPC confirms stopped+revoked state;
it is an idempotent settlement operation, not a new lease or scheduler action.
Only fixed target bytes are written, and helper hashes belong to the reviewed
action. Ancestor traversal uses pinned no-follow directory descriptors.
Exclusive backups and a poison journal prevent automatic replay after partial
failure. Final verification repeats unchanged guards and seal checks.

Initial review found absent-parent refusal, unsafe pathname ancestor traversal,
incomplete gap inventory, and omitted final unchanged-guard checks. The successor
addresses each; relevant fixture test source was inspected. This reviewer did
not run tests or builds, start services, modify sealed/installed files, inspect
credentials, or invoke a live provider. Execution evidence is the implementer's
separate admitted-test/build responsibility and remains a release gate.
