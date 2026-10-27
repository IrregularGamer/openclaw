# Trusted package native environment prerequisite608

Source-only prerequisite; no package promotion or build-route wiring. Combined4
continues to execute its unchanged reviewed frozen source d3925759, not this change.

Existing nativeCompiler608 remains the sole paired-receipt/source/toolchain/addon
validator. New trustedNativeCompilerEnvironment608 calls its required mode and
returns a fresh environment. Parent mode refuses every NAPI_RS_ control, including
an empty or matching caller addon. Child mode permits only the exact addon path
independently derived and revalidated from current required bytes; other NAPI_RS_
keys and different/empty paths refuse. Missing or changed bytes never select stock.
No environment-selected mode, path, binary, command or receipt owner is added.

Focused node --test docs/strict542/native-compiler608.test.mjs: prior three cases
PASS and all three new cases fail before implementation; all six PASS afterward.
These use the existing synthetic receipt fixtures and do not claim native execution.
Local temporary fixtures stayed under runs/608/unit-scratch, not tmpfs.
Full affected checks of this successor remain for the admitted package export.

Owner SHA256 old 100448541225148f805e729baf68dd87e5ee6ad1964a3373f21e20a0f59274ab
new c3670b0b3448f64a3e247beac48c62f93596620bbb2ee92d362f45bfee77ce0a
All four native compiler build owner inputs/pins remain unchanged. Both canonical
build routes and the normal4352MiB guard remain unchanged. Parent/direct driver
and declaration propagation remain UNWIRED until complete diagnostic success and
its independent acceptance permit the existing package plan. Exact independent
review of this prerequisite is PENDING; it supplies no action/privilege/seal or
automatic queue approval and no installation authority.
