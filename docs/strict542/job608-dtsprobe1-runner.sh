#!/bin/sh
# Diagnostic only: one upstream test, base c790ba44 vs successor overlay. Always settles.
set -u
python3 - <<'V'
import hashlib,json
m=json.load(open('export-manifest.json'))
for n,k in [('source598.tar','base_source_archive_sha256'),('successor598.tar','successor_archive_sha256')]:
 assert hashlib.sha256(open(n,'rb').read()).hexdigest()==m[k],n
V
T='test/scripts/write-unified-entry-dts.test.ts'
for variant in base successor; do
  rm -rf src; mkdir src; tar -xf source598.tar -C src
  [ $variant = successor ] && tar -xf successor598.tar -C src
  (cd src && npm exec --yes --package=pnpm@12.5.1 -- pnpm install --frozen-lockfile >/dev/null 2>&1; echo "VARIANT $variant install=$?"
   start=$(date +%s)
   node node_modules/vitest/vitest.mjs run --config test/vitest/vitest.tooling.config.ts --maxWorkers=1 --no-file-parallelism $T -t 'reuses unaffected canonical groups' >../$variant.log 2>&1; s=$?
   echo "VARIANT $variant exit=$s seconds=$(( $(date +%s)-start ))")
  sed 's/\x1b\[[0-9;]*m//g' $variant.log | grep -E "phases\]|Tests |timed out|✓|FAIL" | cut -c1-1500 | head -12
done
rm -rf src .pnpm-store
exit 0
