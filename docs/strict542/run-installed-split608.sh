#!/bin/sh
# Source-only affected installed tests; no native compilation or package promotion.
set -eu
mkdir result608-installed
EXPORT_ROOT="$PWD"
cleanup() {
  status=$?
  printf '%s\n' "$status" >"$EXPORT_ROOT/result608-installed/exit-code.txt"
  cd "$EXPORT_ROOT"
  python3 - <<'CLEAN'
from pathlib import Path
import shutil
for name in ['source', '.pnpm-store']:
 p=Path(name)
 if p.exists():shutil.rmtree(p)
CLEAN
}
trap cleanup EXIT
python3 - <<'VERIFY_ARCHIVES'
import hashlib,json
from pathlib import Path
m=json.loads(Path('export-manifest.json').read_text())
for name,key in [('source598.tar','base_source_archive_sha256'),('successor598.tar','successor_archive_sha256'),('native598.tar','native_export_sha256'),('rolldown608-source.tar.gz','compiler_upstream_archive_sha256')]:
 h=hashlib.sha256()
 with open(name,'rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 assert h.hexdigest()==m[key],name
for name,expected in m['native_stage_outputs'].items():
 p=Path('native608-stages')/name
 assert p.is_file() and not p.is_symlink(),name
 assert hashlib.sha256(p.read_bytes()).hexdigest()==expected,name
assert {str(p.relative_to('native608-stages')) for p in Path('native608-stages').rglob('*') if p.is_file()}=={'compile/receipt.json','libtests/receipt.json'}
VERIFY_ARCHIVES
# Ordinary tooling fixtures must not inherit the package-only native route.
python3 - <<'ORDINARY_ENV'
import os
assert 'OPENCLAW_608_BOUNDED_PACKAGE' not in os.environ, 'inherited bounded package policy'
assert not any(key.startswith('NAPI_RS_') for key in os.environ), 'inherited native compiler control'
ORDINARY_ENV
mkdir source
tar -xf source598.tar -C source
tar -xf successor598.tar -C source
cd source
npm exec --yes --package=pnpm@12.5.1 -- sh -c 'set -eu; [ "$(pnpm --version)" = 12.5.1 ]; pnpm install --frozen-lockfile' >../result608-installed/install.log 2>&1 || { status=$?; tail -30 ../result608-installed/install.log; exit "$status"; }
node node_modules/vitest/vitest.mjs run --config test/vitest/vitest.tooling.config.ts --maxWorkers=1 --no-file-parallelism --maxConcurrency=1 --passWithNoTests=false --reporter=default --reporter=json --outputFile.json=../result608-installed/installed.json test/scripts/write-unified-entry-dts.test.ts >../result608-installed/installed.log 2>&1 || { status=$?; tail -70 ../result608-installed/installed.log; exit "$status"; }
tail -18 ../result608-installed/installed.log
python3 - <<'RESULT'
import hashlib,json
from pathlib import Path
p=Path('../result608-installed');r=json.loads((p/'installed.json').read_text())
assert r['success'] is True and r['numFailedTests']==0 and r['numPendingTests']==0 and r['numTodoTests']==0
assert r['numPassedTests']==14, r['numPassedTests']
assert len(r['testResults'])==1
names=[x['fullName'] for x in r['testResults'][0]['assertionResults'] if 'canonical group cache history' in x['fullName']]
assert len(names)==4, names
m=json.loads(Path('../export-manifest.json').read_text())
value={'source_commit':m['source_commit'],'source_export_sha256':m['source_export_sha256'],'run_id':m['run_id'],'exit_code':0,'passed':r['numPassedTests'],'split_cases':names,'results_sha256':hashlib.sha256((p/'installed.json').read_bytes()).hexdigest(),'log_sha256':hashlib.sha256((p/'installed.log').read_bytes()).hexdigest(),'scope':'affected installed owner file only; full package and remaining checks still required'}
(p/'evidence.json').write_text(json.dumps(value,sort_keys=True)+'\n')
print(json.dumps(value,sort_keys=True))
RESULT
