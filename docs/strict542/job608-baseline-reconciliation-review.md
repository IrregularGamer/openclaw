# Independent explicit baseline reconciliation review608

VERDICT: APPROVE the exact reconciliation and successor PROPOSAL for reference
in a FUTURE newly reviewed exact artifact/action baseline. This approval does
not replace the original baseline, approve an action or authorize installation,
resealing, privilege changes, runtime changes or application. No original seal
is claimed to validate legitimately changed current files.

Reviewed builder commit26985d0be9e0ce091077d55da75a92ef0d91aba1, which adds only
the two proposal documents. Exact raw SHA256 identities independently verified:

- job608-baseline-reconciliation.json:
  52391a10ebc2dfb917a5c7f82ecb4dbfd64a5ea658ad31ec6b8538f22e936bda.
- job608-baseline-successor-proposal.json:
  f3b3ced66253d30951005decf574c71be695f4ab42a6311a29509d4415042d92.
- Original job598-observed-baseline.json:
  22253f3512e481177c7b335b768e3155cc1096ae96c475144d0ffda7c6b93f35,
  byte-unchanged from frozen source6d9c429b.
- Retained original complete root seal
  /var/lib/agentq-safety/validation.json.bak-20261026T2153Z-continue:
  7c404d1d04cce2bef262df508af5460a37f6228152466bc60d46e77841dbdfbb,
  matching the original baseline's complete seal pin.
- Current complete /var/lib/agentq-safety/validation.json:
  0cdd4aa5a932e149f4b816a251656f9aa257dc23ecd20c30fe046bed8aad9aa3,
  matching the proposal and reconciliation record. Current seal metadata matches
  both documents exactly, including mode/uid/gid/timestamps/xattr digest. Seal
  bytes and metadata remained stable through the read-only verification.

## Independently verified reconciliation

Old/current complete seals have identical top-level keys and identical56-path
installed_hashes keysets. Only installed_hashes and amendments differ. The old31
amendments are an exact prefix of the current33. The appended two amendments
equal the reconciliation document and bind exactly all three installed deltas:

- /home/deploy/agentq/agentq.py:
  96d8542d668a961168a944e020a5366e30ae66921a1abe0724c5473eabd9d9ea ->
  fa9a63fd9581a23f2acfbfe9455c9a53c8ba5d38d329c40a278aaab770d7bd8e.
  The2026-10-26T22:30:11.379096+00:00 amendment records the reviewed soft-requeue
  continuation correction and its authorization/test history.
- /usr/local/libexec/agentq-safety/control.py:
  12f462f1259280896e7be8056252204298667fd03c81dcd309ef614ed3ddcd16 ->
  f47ac601705df39e44475859dbef352016fdb19ec1ee29920219a91700380789.
- /etc/systemd/system/agentq-work.slice:
  0b7edd43dcafd6a3848ea55333ce567b77069727b285a7689a015d4b6c336274 ->
  d17a978654c35ef3ea5a4e64a66b1e74df8e07ea73232a38c846a5a2070d9879.
  The2026-10-27T01:29:17.022060+00:00 amendment binds both latter changes to
  INC-261027-09's MemoryHigh correction and records review/authorization history.
  Its string-encoded files/hash maps were parsed as data and matched exactly.

Independently read and hashed all56 currently sealed files, totaling295929bytes;
every digest matches both the complete current seal and the reconciliation's
exact check inventory. The only inherited sealed symlink is the existing
/home/deploy/.local/bin/devstack ->
/home/deploy/claw-workspace/offload/hetzner/devstack; its exact target and target
file type match apply598.py's existing ORIGINAL_SEAL_LINKS contract. This grants
no new link or write target.

Boot5a127a2b-505e-40f1-93d6-fdad224520c8 matches both baselines and live procfs.
All seven observed guards were checked for regular file type, raw hash and
complete metadata. Only control.py differs from the original; the other six
guards match the original exactly. All six application targets remain absent,
using lexists so broken links would not count as absence.

Reconstructing the proposal from the original changes exactly seal_sha256,
seal_metadata and observed_guards[control.py]'s hash/metadata. All remaining
fields are identical. The canonical application598.py baseline_inventory
validator accepts its shape. The proposal adds no target and weakens no guard.

## Scope and future gates

The original baseline still fails the live seal/control guards. Keep it intact
as historical evidence. A future artifact/action may explicitly reference this
exact independently reviewed successor proposal; it must be newly prepared and
reviewed against the actual completed artifact and current baseline. Do not
silently refresh an approved baseline or reuse a historical action/review.

At action time, verify complete current seal validity and exact seal metadata,
all guard bytes/metadata, boot and target absence again. Any subsequent drift
requires new exact reconciliation/review. Full build/package and independent
source/action/privilege-policy/next-seal reviews and actual automatic queue608
approval remain mandatory. Preserve the genuine finite foreground nonqueue HQ
owner, natural settled gap, native admission/settlement guards, exclusive
backups, and fresh post-restart HQ owner binding plus accepted-run acknowledgements.

Declined to judge: reapproval of historical incident implementations or their
human authorization; compiler/libtests or combined diagnostic outcomes; a future
artifact, action, privilege policy, next seal, automatic review or HQ application.
This review verifies the exact recorded amendment bindings and observed state;
it supplies none of those separate approvals.

Only bounded read-only root/file/hash/source inspection and the pure baseline
shape validator were used. No protected/root/runtime state was changed; no
heavy tests, build, offload, network, service or queue action was run. The active
sole libtests stage was untouched. This recording commit adds only this review.
