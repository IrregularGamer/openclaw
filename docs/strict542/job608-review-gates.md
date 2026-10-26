# Job608 source preparation review-gate correction

The current maintained application preparation now requires distinct independent
source, action, privilege-policy, seal and automatic-queue scopes, all bound to
the exact action/tree/source. The seal scope separately binds validation.next.json
in the privileged application's additive amendment check. A privilege review
alone cannot supply the seal review.

The stale literal APPROVE598 label is removed from the application gate. A future
real automatic queue review must identify build608 and its actual positive review
job ID and queue result SHA256. Immediately before application the helper reads
the queue read-only:608 must be a done build, and the specified job must be a done
review parented to608 with exactly the externally reviewed result bytes. No queue
state is changed. The exact result must also have an APPROVE first verdict,
using the existing queue transition syntax. Done ancestors and done CHANGES
reviews cannot substitute for this build's actual approval. The queue's own status transition remains the approval owner.
Future queue review identities cannot be invented during preparation.

The new fixture checks reject absent seal/automatic review, obsolete598 identity,
unfinished build, wrong review parent, absent review and changed result digest.
Only synthetic temporary fixture databases are written. This is source only;
no live seal, staged input, installed helper, unit or sudoers file is changed.
No exact artifact/action/privilege/seal/automatic approval is claimed here.

This source correction supersedes only the review-gate paragraphs of the old
job598-HQ-HANDOFF.md. Its whole-seal/original guard, inventory/backup/rollback,
finite native owner/admission/settlement, actual natural gap, fresh post-restart
owner binding AND accepted-run acknowledgements and downstream authority rules
remain mandatory. The running550dbbd0 diagnostic predates this correction; its
test results cannot be attributed to these successor bytes. A final admitted
check of the complete successor is still required before application readiness.
