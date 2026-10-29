# job608 frozen a39a source inventory: independent review

SOURCE ONLY; **595 MUST NOT APPLY.** Reviewed exact inventory commit
`6529a453143cb2829f26b291b80317c22292bb18` and its sole added file
`job608-frozena39ad5ee-source-inventory.json`, SHA256
`69eb63f9b97021a2e2e0970eb7ee94dcfea085da824201166d5d1e499c70a017`.
The working file is byte-identical to that committed file.
Reviewer: Rook `/root/review_compiler_preflight`, 2026-10-29 UTC.

Independently derived exact no-rename Git diff membership from original605 source
`877458d730d2455528fb639710ff3f9ba8aae5b2` to frozen
`a39ad5ee95609193502850d0dbb87b5dcbb5e3e3`: exactly732 unique paths,
714 additions and18 modifications, with no deletion. No missing or extra path
exists in the inventory. For every old/new side, independently read the Git tree
mode/object and streamed the complete Git blob through SHA256 in at most1 MiB
chunks. All750 present old/new entries match their recorded full SHA256 and Git
mode; all714 absent old sides are explicit and correct. The723 distinct blobs
were each hashed once. No installed or runtime target file was inspected or
inferred from these source objects.

All669 historical candidate95 inventory paths remain represented; their old-side
states, modes and hashes agree exactly. This preserves the original source
comparison without treating the historical candidate's new side as the a39a
source or installed state. Common export identity remains
`d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62`,
separately recomputed during the exact compiler export preflight review.

The inventory correctly declares SOURCE_INVENTORY_ONLY_NOT_ARTIFACT_OR_INSTALL608
and leaves build_package_receipt, application_action and next_seal null.
Accepted limited stage evidence and the active unified-0 attempt supply no final
artifact, application action, privilege, seal, automatic review or genuine HQ
handoff acceptance. The inventory does not authorize installation, application,
root/service/config/unit changes or resealing. No offload, test suite, build,
runtime/root/provider operation or large archive rehash ran for this review.

**VERDICT: APPROVE** (exact source-inventory evidence only; no artifact, action
or installed-target approval).
