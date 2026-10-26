#!/bin/sh
# Fresh committed source-only scoped checks; no compiler, package or application.
set -eu
mkdir result608-inventory
EXPORT_ROOT="$PWD"
cleanup() {
  cd "$EXPORT_ROOT"
  python3 - <<'CLEAN'
from pathlib import Path
import shutil
for name in ['source','native-source','.pnpm-store']:
 p=Path(name)
 if p.exists():shutil.rmtree(p)
CLEAN
}
trap cleanup EXIT
python3 - <<'VERIFY'
import hashlib,json
from pathlib import Path
m=json.loads(Path('export-manifest.json').read_text())
for name,key in [('source598.tar','base_source_archive_sha256'),('successor598.tar','successor_archive_sha256'),('native598.tar','native_export_sha256')]:
 with open(name,'rb') as stream:assert hashlib.file_digest(stream,'sha256').hexdigest()==m[key],name
VERIFY
mkdir source native-source
tar -xf source598.tar -C source
tar -xf successor598.tar -C source
tar -xf native598.tar -C native-source
node --input-type=module -e 'import {releaseConsumedArchives} from "./source/scripts/lib/disposable-build-inputs.mjs"; releaseConsumedArchives(process.cwd())'
cd source
export NATIVE_SOURCE="$PWD/../native-source"
exec >../result608-inventory/tests.log 2>&1
node --test src/agents/sessions/selected-runtime-auth-read.test.mjs src/agents/sessions/selected-runtime-auth-integration.test.mjs src/gateway/strict542/native-owner-transport.test.mjs src/gateway/strict542/usage-preflight.test.mjs
python3 -m unittest discover -s src/gateway/strict542 -p test_native_owner_server.py -v
python3 -m unittest discover -s docs/strict542 -p test_native_preparation.py -v
python3 -m unittest discover -s src/gateway/strict542 -p test_root_owner_supervisor.py -v
python3 -m unittest discover -s docs/strict542 -p test_application598.py -v
python3 -m unittest discover -s docs/strict542 -p test_apply598.py -v
python3 -m unittest discover -s docs/strict542 -p test_native_consumer608.py -v
python3 -m unittest discover -s docs/strict542 -p test_frozen_package608.py -v
node --test docs/strict542/serial-probe598.test.mjs docs/strict542/isolated-config598.test.mjs docs/strict542/disposable-inputs608.test.mjs docs/strict542/native-compiler608.test.mjs docs/strict542/bounded-package608.test.mjs
npm exec --yes --package=pnpm@12.5.1 -- sh -c 'set -eu; [ "$(pnpm --version)" = 12.5.1 ]; pnpm install --frozen-lockfile'
node node_modules/vitest/vitest.mjs run --config test/vitest/vitest.unit-fast.config.ts --maxWorkers=1 --no-file-parallelism --passWithNoTests=false --reporter=json --outputFile=../result608-inventory/vitest.json test/scripts/build-all-bounded608.test.ts
python3 - <<'RESULT'
import hashlib,json
from pathlib import Path
out=Path('../result608-inventory');v=json.loads((out/'vitest.json').read_text())
assert v['success'] is True and v['numTotalTests']==3 and v['numPassedTests']==3 and v['numFailedTests']==0
manifest=json.loads(Path('../export-manifest.json').read_text())
value={'source_commit':manifest['source_commit'],'exit_code':0,'kind':'SCOPED_TESTS_ONLY_NOT_BUILD_OR_APPLICATION','typed_inventory_tests':3,'vitest_sha256':hashlib.sha256((out/'vitest.json').read_bytes()).hexdigest(),'test_log_sha256':hashlib.sha256((out/'tests.log').read_bytes()).hexdigest()}
(out/'evidence.json').write_text(json.dumps(value,sort_keys=True)+'\n')
RESULT
