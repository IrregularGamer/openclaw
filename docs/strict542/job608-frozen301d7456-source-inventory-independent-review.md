# Independent frozen 301d7456 source inventory review

Reviewed inventory-only commit `70efe115a0f37584383342ed4a13772145ebb5b0` on
2026-10-30. The working inventory
`job608-frozen301d7456-source-inventory.json` is byte-identical to that commit,
SHA256 `0ba67e6dd0031938d2f224dd4634c2c64b9f4f0b53cb853d192ad2c76a97e184`.

VERDICT: APPROVE EXACT SOURCE INVENTORY ONLY. No findings. 595 MUST NOT APPLY.

I independently recomputed the complete no-renames Git diff from original605
`877458d730d2455528fb639710ff3f9ba8aae5b2` through frozen source
`301d7456bf5b0c4179b27d0db97eac7b07143f4a`. It contains exactly 1,252 unique,
sorted changed paths: 1,232 additions, 20 modifications, no deletions. The
inventory has exactly those paths, with no missing, duplicate or extra entry.
The name-only and raw no-renames diffs agree, and I independently checked the
old and new Git trees for every changed path.

I streamed all 1,131 distinct old/new Git blobs through SHA256, in chunks no
larger than 1 MiB: 19,807,042 total bytes; largest blob 1,587,906 bytes. Every
recorded old/new presence or absence, Git mode and SHA256 matches its exact
Git tree/blob. There are 20 present and 1,232 absent old sides, and 1,252 present
new sides. The 1,272 present sides comprise 1,271 mode100644 and one mode100755.
The entire original605-to-301d inventory was checked directly rather than
inferred from a prior inventory. No source file was executed, and this is not a
broad rereview of previously approved code.

The declared new source is exact 301d7456. The complete declared export digest
`99add7e14c96b379a907d8f39fb30e96c515e5edb9737aaa8cfec47cc900291d` matches
`job608-runtime-301d-preflight.json` and the actual accepted checks receipt at
`job608-checks-301d/result608-checks/checks/stage-receipt.json`. Both bind that
digest to the exact new source commit. The receipt has kind
`JOB608_STAGE_RECEIPT`, stage `checks`, run ID `stage608-checks-301d`, exit code
0, and SHA256
`65c44316dc17ef6c1a5919a9f883c4ddba115bcaecde359a3a9c35fc77232c9b`, matching
its recorded result-files digest. Its independent acceptance records
`VERDICT: ACCEPT`. This checks the source-export identity linkage; it does not
recompute an export archive or rerun checks.

The inventory kind remains `SOURCE_INVENTORY_ONLY_NOT_ARTIFACT_OR_INSTALL608`;
`application_action`, `build_package_receipt` and `next_seal` are all null. Its
note explicitly leaves final package/installed-target inventory and exact
action, privilege, seal and automatic queue reviews pending.

This approves completeness and exact identity of this frozen source inventory.
It grants no package/artifact/action/privilege/installed-target/whole-seal/
automatic-review/HQ595 application approval or deployment authority. Those later
gates remain open. Only this requested review document was written; no build,
test suite, offload, runtime authorization, config, installed/root, seal,
service or queue state was changed. No commit or push was performed by this
reviewer. The review document passes `git diff --no-index --check` against
`/dev/null`.

595 MUST NOT APPLY.
