# Native diagnostic scheduling candidate; no build acceptance

The admitted API-phase observation of unchanged source 1bed established that
`API.createSnapshot` returned after about 104.6 seconds. The subsequent config
and program diagnostics returned, and `Program.getGlobalDiagnostics` started.
Its completed outcome belongs to the separate actual diagnostic receipt; this
candidate does not presume that outcome or claim to fix its CPU cost.

The installed TypeScript package is `7.1.0-dev.20260920.1`, gitHead
`f29aeb9f825d96feea27841f3f7342dbf0df68a8`. Exact primary source establishes:

- [API session owner](https://github.com/microsoft/TypeScript/blob/f29aeb9f825d96feea27841f3f7342dbf0df68a8/tsc/internal/api/session.go#L4593)
  forces a complete semantic pass before returning global diagnostics. The
  global diagnostic request is mandatory and remains unchanged.
- [Project program construction](https://github.com/microsoft/TypeScript/blob/f29aeb9f825d96feea27841f3f7342dbf0df68a8/tsc/internal/project/project.go#L549)
  does not override `SingleThreaded` in its program options.
- [Compiler program owner](https://github.com/microsoft/TypeScript/blob/f29aeb9f825d96feea27841f3f7342dbf0df68a8/tsc/internal/compiler/program.go#L553)
  therefore uses the configured `singleThreaded` value. Its external checker
  pool path otherwise queues concurrent work for all eligible source files.
- [Option declaration](https://github.com/microsoft/TypeScript/blob/f29aeb9f825d96feea27841f3f7342dbf0df68a8/tsc/internal/tsoptions/declscompiler.go#L233)
  supports the boolean `singleThreaded` option, including in configuration;
  it has no command-line-only restriction.
- [Work queue owner](https://github.com/microsoft/TypeScript/blob/f29aeb9f825d96feea27841f3f7342dbf0df68a8/tsc/internal/core/workgroup.go#L20)
  selects a sequential work queue for that option. This controls compiler
  scheduling within the existing single-CPU budget.

Downloaded exact-source SHA256 receipts (copies retained under
`runs/608/upstream-snapshot-owner/`):

| File | SHA256 |
| --- | --- |
| `session.go` | `39321b51fd3f01e503e7834573f84cae55b5e1c90fef203f93e051ad25c376b1` |
| `project.go` | `e8c70a7d2aa2a30f5d2db17733e1379f42d803f6309a700f5c2b57b523a17d03` |
| `program.go` | `72f0b97bca110d5893b03c6ac8349dcdabe627c55f58f05a0dbd9b5a6da6cadb` |
| `checkerpool.go` | `3737b2244b8eb094e81ac80bd77199676512dc76327fc8cc1ed6cd2927aeaf56` |
| `compileroptions.go` | `0c8e18176a1a7da22a23a1232d516e5c84cb60dfe54490bdcf0c48c21fc5f6a8` |
| `declscompiler.go` | `cb46ae4601fe0cdfa0ef15144784ad58987601395bf33870b9e702cde5bf4e4c` |
| `workgroup.go` | `3a7cdb6ec7932d1c7572dac0b4cec3ef937fbd941a0572c733f519547e3e9266` |

The maintained emitter now sets `singleThreaded: true` in its final virtual
compiler configuration, after caller options. Previous emitter SHA256 was
`2f8a05d0b713daf4d60d4e0359efe677b8f2710b05b1fd594e401adf1a3a2431`;
candidate SHA256 is
`330ebfd5240be7449c7c374ef7a57a6446dead50117e22ed2d81100934d3d547`.
There is no root-set, semantic/global diagnostic, source-membership, input-seal,
native-close, cancellation, emission, publication or memory-floor change.
The existing 4 GiB/one-CPU/zero-swap admitted budget is not modified.

Two behavioral fixture cases inspect the actual final virtual configuration:
the default caller and an attempted `singleThreaded:false` override. They also
retain explicit plus ambient roots, require all diagnostics (semantic included),
retain the complete snapshot request, and require close before the input seal.
The new cases first failed against the old emitter (missing/false option), then
all nine admission composition cases passed after the small owner change.
Command: `node --test docs/strict542/native-admission608.test.mjs`.
Compressed actual RED/GREEN logs accompany this note. API/compiler/seal doubles
isolate composition; these results do not establish native output equivalence,
performance, a complete build, or a package receipt.

Next gates: independent exact source review; admitted native parity checks from
a committed secretless export; measured config-15 execution; then a new exact
source freeze/inventory and all required compiler/build/package stages. Old
receipts keep their original source identity. Keep every original application,
privilege, seal, automatic review and HQ ownership gate. Job595 must not apply.
