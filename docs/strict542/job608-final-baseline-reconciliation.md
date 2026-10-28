# Final exact baseline reconciliation608

This source-only observation reconciles the original598 baseline through the
post619 baseline and the installed639 deadline correction. It grants no
application, privilege, release or reseal authority.

All 56 current installed_hashes entries validate by streaming SHA256. The only
permitted symlink remains /home/deploy/.local/bin/devstack pointing exactly to
/home/deploy/claw-workspace/offload/hetzner/devstack, whose target is a regular
non-symlink file. No new link or target exception is introduced.

The historical complete seal remains byte-identical to original baseline
7c404d1d04cce2bef262df508af5460a37f6228152466bc60d46e77841dbdfbb;
the original job598-observed-baseline.json remains
22253f3512e481177c7b335b768e3155cc1096ae96c475144d0ffda7c6b93f35.
The original31 amendments remain an exact prefix of current38. The first six
appended amendments match the prior reviewed reconciliation data exactly. All
seven appended amendments replay every old/new hash in order and reproduce
the entire current56-entry mapping. Only installed_hashes/amendments differ
between whole historical and current seals; unrelated fields and keysets stay
identical. The new639 amendment accounts for both dispatcher and offload bytes.
641 is not installed in this observation and is not assumed to be installed.

Current complete seal:
51170230064a8da20e074497eae6a6c968d293d262e9e31523dd7365a5c128d3.
Exact current whole seal bytes are retained in job608-final-seal-original.json
(the original seal for the future608 action); historical whole seal bytes are
retained separately in job608-final-seal-historical-original.json.
Explicit proposed baseline:
428ced690f0b3a3cb8a7a2a4fc38570ffa71fa98d7298423376a26fd3ee6a9c9.

All seven guard hashes, ownership, modes, nanosecond timestamps and xattrs match
the prior post619 proposal; only control.py differs from the historical598
baseline, exactly as amended. All six intended application targets remain
absent with lexists checks. Boot identity is unchanged. Seal bytes/metadata,
guard bytes/metadata, boot and absences were checked again for stability during
observation. Exact metadata/xattrs, installed deltas and complete amendment
hash chain are in job608-final-baseline-reconciliation.json. The canonical
application598.py baseline_inventory validator accepts the proposal shape.

Any later seal, metadata, guard, boot or target drift requires another exact
reconciliation and exact action/seal review. Never refresh an approved action
silently. The historical baseline is preserved as evidence and is not claimed
to validate current legitimately changed installed files. Exact completed
artifact/action/source/privilege/next-seal and actual automatic queue review
remain required before application. Owner, cancellation/settlement, natural
gap, budgets and fresh post-restart acknowledgement gates remain unchanged.
No installed/sealed/root/unit/sudoers/runtime/queue state was changed.
