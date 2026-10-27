# Job608 review of guarded pre-restart rollback ad7d4365

Reviewer: Claude (separate session from the ad7d4365 author, Rook). Source-only;
no root, unit, seal, sudoers, service or offload action was run.

## Scope read
`git show ad7d4365` for apply598.py, application598.py and test_apply598.py.

## Findings
- APPROVE: rollback is limited to the exact complete disk application
  (`DISK_APPLIED_SERVICES_UNCHANGED`, same action hash, complete target list),
  the original pre-restart owner (journal `application_owner` == ack, same boot),
  the six originally absent fixed targets, and the fixed exclusive backup root.
  All targets, guards, the original seal backup and absence markers are checked
  before mutation; poison is checkpointed first; targets are renamed (never
  deleted) into a root-only quarantine and re-verified; owner/quiet/service/guard/
  seal checks repeat per step; the original whole seal bytes, mode, owner, xattrs
  and mtime are restored and revalidated. Gateway restart is refused because the
  original owner PID binding no longer matches.
- CORRECTED (this commit): `rollback_service_unchanged` relied on
  `systemctl show` MainPID/ActiveState/ExecMainStartTimestampMonotonic. systemd
  drops those once an inactive unit is garbage-collected, so a supervisor started,
  stopped and unloaded would look pristine. Added a fixed read-only
  `journalctl --boot --unit strict542-owner.service` query; any record or an
  unreadable journal refuses. Test extended (both new refusal cases, argv pinned).
- No owner predicate, cancellation, settlement or budget check was weakened.

## Verification
`python3 -m unittest test_apply598` in docs/strict542: 17 tests OK.

## Not covered
Full package, artifact receipt, action/privilege/seal reviews of the exact
artifact and the queue review remain open.
