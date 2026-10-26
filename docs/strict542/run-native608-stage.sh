#!/bin/sh
# One admitted native608 stage: compile (addon only), libtests (native lib tests only)
# or lifetime (standalone AST ownership tests only; never addon or lib-test authority).
# Inputs: export-manifest.json, successor598.tar, rolldown608-source.tar.gz. Output:
# result-native608-<stage>/ (receipt, addon for compile, build log). Diagnostic only.
set -eu
stage="${1:-}"
case "$stage" in compile|libtests|lifetime) ;; *) echo "native608 stage must be compile, libtests or lifetime" >&2; exit 2;; esac
out="result-native608-$stage"
[ ! -e "$out" ] && [ ! -e source ] && [ ! -e .native608 ] || { echo "native608 stage requires a fresh export" >&2; exit 2; }
mkdir "$out"
EXPORT_ROOT="$PWD"
cleanup() {
  cd "$EXPORT_ROOT"
  if [ -d source/result598-native ]; then cp -R source/result598-native/. "$out"/; fi
  if [ -f source/build.log ]; then cp source/build.log "$out"/build.log; fi
  rm -rf source .native608
}
trap cleanup EXIT
python3 - <<'VERIFY_ARCHIVES'
import hashlib,json
from pathlib import Path
m=json.loads(Path('export-manifest.json').read_text())
for name,key in [('successor598.tar','successor_archive_sha256'),('rolldown608-source.tar.gz','compiler_upstream_archive_sha256')]:
 h=hashlib.sha256()
 with open(name,'rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 assert h.hexdigest()==m[key],name
VERIFY_ARCHIVES
mkdir source
tar -xf successor598.tar -C source
cd source
# Reviewed per-stage deadline: 5400s (the single 2400s run covering tests, toolchain,
# dependency graph and both cargo invocations ended at crate rolldown). Budget unchanged.
timeout -k 15s 5400s python3 docs/strict542/build-native608.py "$stage" >build.log 2>&1 || { status=$?; tail -25 build.log; exit "$status"; }
tail -3 build.log
