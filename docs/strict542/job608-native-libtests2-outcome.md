# Native libtests2 accepted outcome

The foreground run in export608-native-libtests2 settled rc0. The captured
result reports 112 Rust library tests passed, zero failed, plus seven standalone
lifetime tests and a detected old-retention negative control. The receipt is
complete; every shared source, patched-source, toolchain and policy field
matches job608-native-compile3-receipt.json. All four owner input hashes match
current committed source. This accepts the libtest stage only.

The new addon is 46d32ba682581adc9d25b10c4f160b462065b216f2deba5494acd05509208c18.
The older f8b7634b addon/receipts cannot satisfy these changed owner inputs.
No combined compiler diagnostic, package or installation is accepted here.
