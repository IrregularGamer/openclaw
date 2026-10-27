# Independent recovered outcome and baseline review — APPROVE evidence only

Exact recovered evidence commit2d59ca37; baseline report committed bfcbb2c8.
Independently recomputed all seven recovered-file SHA256 values in
job608-native-phase-recovered.json. Scoped check log identity matches its receipt
and source00d5fe9f5a99ff7fda6fc3a365ab7edb3d78ea29. Count reconciliation:
101+34 scoped Node checks,15+18+13+19+11+3+5+6=90 Python checks,3 typed
checks and five real fixture files with2checks each total238PASS. Parity has8
variants and addon17df206117097742019de475e8cd194fb1022f48d9c2b507195100abd13eb627,
matching the recovered compile receipt. Every receipt owner-input hash matches
the historical source commit. Probe has48results: AI and main0..45 succeed;
main46 ends SIGKILL after155208.871802ms. This is an incomplete diagnostic,
not package/build success; the exact killer remains unproven.

Independently performed read-only root file/metadata/hash inspection. The original
job598-observed-baseline.json is unchanged in working tree and committed HEAD:
SHA25622253f3512e481177c7b335b768e3155cc1096ae96c475144d0ffda7c6b93f35.
Current complete seal SHA2560cdd4aa5a932e149f4b816a251656f9aa257dc23ecd20c30fe046bed8aad9aa3
and metadata differ from original recorded seal7c404d1d04cce2bef262df508af5460a37f6228152466bc60d46e77841dbdfbb.
All56 current seal entry file hashes match. Of seven original guards, exactly
control.py changed bytes/metadata: old12f462f1259280896e7be8056252204298667fd03c81dcd309ef614ed3ddcd16,
current f47ac601705df39e44475859dbef352016fdb19ec1ee29920219a91700380789.
The other six guards match, boot identity matches, and all six installation
targets remain absent. Report guard deltas match independently recomputed values.

The current original-baseline application gates FAIL. A valid current56-entry
seal does not satisfy the original byte/metadata/guard predicates. Keep the
original baseline and require fresh exact independent reconciliation/review before
constructing any future action; do not refresh it silently or waive predicates.
This review accepts the report as evidence only. It supplies no action,
privilege-policy, seal/reseal, automatic-queue, installation or release approval.
No protected file or installed state was changed by this review. Build/package,
575/588/592 references,595 natural-gap ownership and fresh post-restart genuine
HQ binding/accepted-run acknowledgements remain required.
