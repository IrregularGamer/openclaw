# job608 native stage preflight (UNUSED export, frozen 1bed)

Source-only preparation. No install, build-package or application authority. **595 MUST NOT APPLY.**

- Export: `/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-native-1bed` (private staging approved by review 1e4c30d0, init receipt db1969ac).
- Prepared 2026-10-28T19:24Z with the committed preparer `git show 1bed4d1b:docs/strict542/prepare-stage608-export.py` (sha256 1e701de0…, identical to HEAD), `--base <root>/base --commit 1bed4d1b… --stage native`, under ulimit -v 512MiB, rc 0. Archives are hard links of the digest-verified base (source598.tar link count 2, same inode).
- `storage608.py check --stage native` before prep: OK, unique 710027557 B, free 6614769664 B, return cap 64 MiB.
- Manifest sha256 31330bc3c8d6878a6f6bf89a1d958bf9d5ecb2cb7f84fa4a4427739826f6931f: stage native, execution_state UNUSED, run_id stage608-native-1bed, source 1bed4d1b, source_export 5d7e9d57… (same common export as checks r2), runner eac266cf…, helper a558db9a…, successor ea5b2c39… (byte-identical to base), predecessor manifest 20111ce5…, stage_inputs {}. Native has no stage predecessors (stage608.py STAGES), so the checks r2 receipt is not an input.
- On-disk sha256 of run608.sh, stage608.py, successor598.tar, native598.tar (d73e4e35…) and rolldown608-source.tar.gz (203aa483…) match the pins.
- Planned single launch (per job608-after-carrier-continuation.md): from the export dir, `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh`, only with >=2655 s worker life left. Afterwards run `storage608.py result --stage native` on the return before accepting it. On failure or timeout, do not rerun unchanged.
