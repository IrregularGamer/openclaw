#!/bin/sh
set -eu
mkdir result598
EXPORT_ROOT="$PWD"
cleanup() {
  cd "$EXPORT_ROOT"
  python3 - <<'CLEAN'
from pathlib import Path
import shutil
out=Path('result598'); src=Path('source')
for name in ['strict542-checks','result598-isolated','result598-native']:
 p=src/name
 if p.exists():shutil.move(str(p),str(out/name))
# pnpm12 also creates its disposable store at the export root.
# Its index.db must not survive into the next normal transfer scan.
for name in ['source','native-source','.pnpm-store','.native608']:
 p=Path(name)
 if p.exists():shutil.rmtree(p)
CLEAN
}
trap cleanup EXIT
python3 - <<'VERIFY_ARCHIVES'
import hashlib,json
from pathlib import Path
m=json.loads(Path('export-manifest.json').read_text())
for name,key in [('source598.tar','base_source_archive_sha256'),('successor598.tar','successor_archive_sha256'),('native598.tar','native_export_sha256')]:
 h=hashlib.sha256()
 with open(name,'rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 assert h.hexdigest()==m[key],name
VERIFY_ARCHIVES
mkdir source native-source
tar -xf source598.tar -C source
tar -xf successor598.tar -C source
tar -xf native598.tar -C native-source
# Archives are consumed and digest verified. Release only these remote copies;
# retained local export archives and their committed identities remain intact.
node --input-type=module -e 'import fs from "node:fs"; import {releaseConsumedArchives} from "./source/scripts/lib/disposable-build-inputs.mjs"; const sample=phase=>console.log(JSON.stringify({kind:phase,current:fs.readFileSync("/sys/fs/cgroup/memory.current","utf8"),stat:fs.readFileSync("/sys/fs/cgroup/memory.stat","utf8")})); sample("BEFORE_ARCHIVE_RELEASE608"); releaseConsumedArchives(process.cwd()); sample("AFTER_ARCHIVE_RELEASE608")'
cd source
export NATIVE_SOURCE="$PWD/../native-source"
mkdir strict542-checks
set +e
(
set -e
node --test src/agents/sessions/selected-runtime-auth-read.test.mjs src/agents/sessions/selected-runtime-auth-integration.test.mjs src/gateway/strict542/native-owner-transport.test.mjs src/gateway/strict542/usage-preflight.test.mjs
python3 -m unittest discover -s src/gateway/strict542 -p test_native_owner_server.py -v
python3 -m unittest discover -s docs/strict542 -p test_native_preparation.py -v
python3 -m unittest discover -s src/gateway/strict542 -p test_root_owner_supervisor.py -v
python3 -m unittest discover -s docs/strict542 -p test_application598.py -v
python3 -m unittest discover -s docs/strict542 -p test_apply598.py -v
node --test docs/strict542/serial-probe598.test.mjs docs/strict542/isolated-config598.test.mjs docs/strict542/disposable-inputs608.test.mjs docs/strict542/native-compiler608.test.mjs docs/strict542/bounded-package608.test.mjs
) >strict542-checks/tests.log 2>&1
status=$?
set -e
tail -22 strict542-checks/tests.log
[ "$status" = 0 ] || exit "$status"
python3 - <<'EVIDENCE'
import json,hashlib,os
from pathlib import Path
manifest=json.loads(Path('../export-manifest.json').read_text())
checks=['gateway-scoped','native-owner','supervisor-ipc','cancellation-settlement','application-preparation']
value={'source_commit':manifest['source_commit'],'exit_code':0,'checks':checks,'test_log_sha256':hashlib.sha256(Path('strict542-checks/tests.log').read_bytes()).hexdigest()}
Path('strict542-checks/evidence.json').write_text(json.dumps(value,sort_keys=True)+'\n')
EVIDENCE
mkdir result598-isolated
# Native addon and lib tests come from two separately admitted stage runs
# (run-native608-stage.sh). Install only their manifest-pinned outputs.
python3 - <<'NATIVE_STAGES'
import hashlib,json,shutil
from pathlib import Path
m=json.loads(Path('../export-manifest.json').read_text())['native_stage_outputs']
target=Path('../.native608'); target.mkdir()
for source,name in [('compile/receipt.json','receipt.json'),('libtests/receipt.json','libtests-receipt.json'),
                    ('compile/rolldown-binding.linux-x64-gnu.node','rolldown-binding.linux-x64-gnu.node')]:
 path=Path('../native608-stages')/source
 assert path.is_file() and not path.is_symlink() and hashlib.sha256(path.read_bytes()).hexdigest()==m[source],source
 shutil.copyfile(path,target/name)
Path('result598-native').mkdir()
shutil.copyfile(target/'receipt.json','result598-native/receipt.json')
NATIVE_STAGES
rm -rf ../native608-stages
set +e
(
set -e
npm exec --yes --package=pnpm@12.5.1 -- sh -c '
set -eu
[ "$(pnpm --version)" = 12.5.1 ]
pnpm install --frozen-lockfile
'
# The installer has fully exited before its disposable store is released.
node --import ./scripts/tsx.mjs --input-type=module -e 'import fs from "node:fs"; import {readProcessMemoryCapacity} from "./scripts/lib/process-memory.mts"; console.log(JSON.stringify({kind:"BEFORE_STORE_RELEASE608",capacity:readProcessMemoryCapacity({}),stat:fs.readFileSync("/sys/fs/cgroup/memory.stat","utf8")}))'
node --input-type=module -e 'import {releaseDisposableStore} from "./scripts/lib/disposable-build-inputs.mjs"; releaseDisposableStore("..")'
node --import ./scripts/tsx.mjs --input-type=module -e 'import fs from "node:fs"; import {readProcessMemoryCapacity} from "./scripts/lib/process-memory.mts"; console.log(JSON.stringify({kind:"AFTER_STORE_RELEASE608",capacity:readProcessMemoryCapacity({}),stat:fs.readFileSync("/sys/fs/cgroup/memory.stat","utf8")}))'
node node_modules/vitest/vitest.mjs run --config test/vitest/vitest.tooling.config.ts --maxWorkers=1 --no-file-parallelism --passWithNoTests=false test/scripts/build-all-bounded608.test.ts
node --import ./scripts/tsx.mjs --test docs/strict542/native-codegen608.test.mjs
node --import ./scripts/tsx.mjs --test docs/strict542/lazy-barrel608.test.mjs
NATIVE_ADDON=$(node --input-type=module -e 'import {nativeCompiler608} from "./scripts/lib/native-compiler608.mjs"; console.log(nativeCompiler608().env.NAPI_RS_NATIVE_LIBRARY_PATH)')
NAPI_RS_NATIVE_LIBRARY_PATH="$NATIVE_ADDON" node --import ./scripts/tsx.mjs --test docs/strict542/lazy-barrel608.test.mjs
node --import ./scripts/tsx.mjs docs/strict542/isolated-probe598.mts
) >result598-isolated/probe.log 2>&1
status=$?
set -e
if [ -e isolated-probe598.json ]; then cp isolated-probe598.json result598-isolated/; fi
printf '%s\n' "$status" >result598-isolated/exit-code.txt
tail -35 result598-isolated/probe.log
cd ..
exit "$status"
