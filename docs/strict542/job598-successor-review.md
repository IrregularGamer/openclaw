# Independent job598 successor source review

Reviewer: Rook independent reviewer `/root/review598_successor`, separate from
implementation. Reviewed exact successor
`de7369e4883abb96ac4cacac9a0ea89e2ae2ee29` relative to previously reviewed
`492d19b64c9bfc6aa53dd115c30c0c5892199968`.
The previous review is `job598-independent-source-review.md`; its source-only
and privilege-design-only limitations remain in force.

## SOURCE verdict: APPROVE_SOURCE_ONLY

The successor adds a process alarm before privileged preparation and shortens it
to the remaining genuine HQ dual-clock acknowledgement window, at most900seconds.
Expiry raises a refusal; any incomplete application retains its poison journal
and backups. The reviewed code does not restart a service or establish ownership.
The ordered HQ handoff requires independent actual source/action/privilege and
automatic598 approvals, a natural settled nonqueue gap, and fresh genuine owner
AND accepted-run acknowledgements after gateway restart. Historical510/515
acknowledgements and the obsolete586 sudo transport are explicitly rejected.
The dispatcher successor and575/588 integration remain references to their owning
source, with no duplicate553 continuation or direct queue state edits.

Exact SHA256 at the reviewed successor:

| File | SHA256 |
| --- | --- |
| apply598.py | 06089bb171dfeab0e24ed65fbeb628afa07235e8a7c6dfa57d05c877dd0229d2 |
| application598.py | f65de3f8e5d5a58cc4302a29965cea17a54b24f1b3a638d0d31e22ee809bf4a0 |
| build598.sh | 534319c9c491bda8290e06ae223c6f41640b7a9951f78ee7474a791259307e77 |
| job598-HQ-HANDOFF.md | 51b3f02ccf0a8f043dbdd3c6620f51d12d448bcaccca247586c116beda8ca1ba |
| strict542-owner.service | ab297fe2afe0559c467ddc6e32a4c041a0cd143daad612ceabcf23571ae4f469 |
| 90-strict542-598.conf | 45634d116cd636458352514b15bc081fe9b78070444655b4ae2d069e18732ecc |
| root_owner_supervisor.py | 0d8bdeda5e916ddc25bda48b1e3da36252a710c88dfe36f875c1b05290709fdc |
| native_owner_server.py | a145387432fbf8e17fffbf1e552328e651054e9d603b1d9bdad2d8494dc6a373 |

## PRIVILEGE DESIGN verdict: APPROVE_PRIVILEGE_DESIGN_ONLY

No new privilege capability is added by this successor. The fixed supervisor
and gateway dropin bytes are unchanged from the independent492d19b6 review.
Inherited-fd socket transport, kernel peer PID checks, unchanged native HQ caller/
cgroup/MainPID predicates, fixed endpoint-only cgroup migration and cancellation/
settlement remain mandatory. The finite foreground lifetime strengthens the
prepared application; no caller-selected root command or sudo rule is introduced.
The explicit future daemon-reload/restart/start command sequence requires its
separate exact action review and genuine foreground HQ execution. This review
does not approve executing those commands or staging any privileged files.

## Verification and remaining gates

This reviewer inspected the exact diff, complete current application helper,
preparation validation/build receipt path and complete HQ handoff. Python AST
parsing of both helpers and test_apply598.py and `bash -n build598.sh` passed.
No heavy test, build, service, installed/sealed/root-file mutation, credential
access or live provider call was performed. Admitted execution evidence remains
the implementer's separate responsibility. Build evidence must reconcile to real
broker admission and logs; user-supplied evidence fields are not independent proof.

This is NOT an approval of an actual runtime artifact, tree, action, next seal,
loaded generation, automatic queue review or production application. Actual built
bytes/logs/admission receipt, exact independently reviewed staged helper/action/
privilege-policy and next-seal hashes, automatic queue598 APPROVE, original seal
validation and fresh genuine HQ bindings remain gates before application.
A single deterministic canonical receipt does not prove a reproducible build.
