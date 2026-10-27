#!/bin/sh
# INC-261027-18: run-package608.sh split at its STEP608 markers into finite
# stages (native, checks, compiler, package). The export manifest selects the
# stage; each stage is one admitted offload of at most 40 min. All checks and
# deadlines are the ones from run-package608.sh, unchanged.
set -eu
EXPORT_ROOT="$PWD"
STAGE=$(python3 stage608.py stage)
RESULT="result608-$STAGE"
mkdir "$RESULT"
cleanup() {
  status=$?
  printf '%s\n' "$status" >"$EXPORT_ROOT/$RESULT/exit-code.txt"
  cd "$EXPORT_ROOT"
  STAGE608_RESULT="$RESULT" python3 - <<'CLEAN'
import os,shutil
from pathlib import Path
out=Path(os.environ['STAGE608_RESULT']); src=Path('source')
for name in ['strict542-checks','result598-build','result598-native']:
 p=src/name
 if p.exists():shutil.move(str(p),str(out/name))
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
python3 stage608.py verify-inputs
python3 - <<'ORDINARY_ENV'
import os
assert 'OPENCLAW_608_BOUNDED_PACKAGE' not in os.environ, 'inherited bounded package policy'
assert not any(key.startswith('NAPI_RS_') for key in os.environ), 'inherited native compiler control'
ORDINARY_ENV
mkdir source native-source
tar -xf source598.tar -C source
tar -xf successor598.tar -C source
tar -xf native598.tar -C native-source
node --input-type=module -e 'import fs from "node:fs"; import {releaseConsumedArchives} from "./source/scripts/lib/disposable-build-inputs.mjs"; const sample=phase=>console.log(JSON.stringify({kind:phase,current:fs.readFileSync("/sys/fs/cgroup/memory.current","utf8"),stat:fs.readFileSync("/sys/fs/cgroup/memory.stat","utf8")})); sample("BEFORE_ARCHIVE_RELEASE608"); releaseConsumedArchives(process.cwd()); sample("AFTER_ARCHIVE_RELEASE608")'
cd source
export NATIVE_SOURCE="$PWD/../native-source"
mkdir strict542-checks
case "$STAGE" in
native)
  # Same reviewed rebuild and 2400s deadline; it needs no node_modules.
  timeout -k 15s 2400s python3 docs/strict542/prepare-native-consumer608.py >strict542-checks/native-rebuild.log 2>&1 || { status=$?; tail -20 strict542-checks/native-rebuild.log; exit "$status"; }
  echo STEP608 native-rebuild-pass
  mkdir "../$RESULT/native"
  cp ../.native608/receipt.json ../.native608/libtests-receipt.json ../.native608/rolldown-binding.linux-x64-gnu.node "../$RESULT/native/"
  ;;
checks)
  set +e
  (
  set -e
  node --test src/agents/sessions/selected-runtime-auth-read.test.mjs src/agents/sessions/selected-runtime-auth-integration.test.mjs src/gateway/strict542/native-owner-transport.test.mjs src/gateway/strict542/usage-preflight.test.mjs
  python3 -m unittest discover -s src/gateway/strict542 -p test_native_owner_server.py -v
  python3 -m unittest discover -s docs/strict542 -p test_native_preparation.py -v
  python3 -m unittest discover -s src/gateway/strict542 -p test_root_owner_supervisor.py -v
  python3 -m unittest discover -s docs/strict542 -p test_application598.py -v
  python3 -m unittest discover -s docs/strict542 -p test_apply598.py -v
  python3 -m unittest discover -s docs/strict542 -p test_native_consumer608.py -v
  python3 -m unittest discover -s docs/strict542 -p test_native_finalizer608.py -v
  python3 -m unittest discover -s docs/strict542 -p test_native_compaction608.py -v
  python3 -m unittest discover -s docs/strict542 -p test_frozen_package608.py -v
  python3 -m unittest discover -s docs/strict542 -p test_lease619_suite_gate.py -v
  node --test docs/strict542/worker-phases608.test.mjs docs/strict542/serial-probe598.test.mjs docs/strict542/isolated-config598.test.mjs docs/strict542/disposable-inputs608.test.mjs docs/strict542/native-compiler608.test.mjs docs/strict542/bounded-package608.test.mjs
  ) >strict542-checks/tests.log 2>&1
  status=$?
  set -e
  tail -22 strict542-checks/tests.log
  [ "$status" = 0 ] || exit "$status"
  npm exec --yes --package=pnpm@12.5.1 -- sh -c 'set -eu; [ "$(pnpm --version)" = 12.5.1 ]; pnpm install --frozen-lockfile'
  node node_modules/vitest/vitest.mjs run --config test/vitest/vitest.tooling.config.ts --maxWorkers=1 --no-file-parallelism --maxConcurrency=1 --passWithNoTests=false --reporter=default --reporter=json --outputFile.json=strict542-checks/installed.json test/scripts/build-all-bounded608.test.ts test/scripts/tsdown-build.test.ts test/scripts/write-unified-entry-dts.test.ts test/scripts/write-plugin-sdk-entry-dts.test.ts >strict542-checks/installed.log 2>&1 || { status=$?; tail -60 strict542-checks/installed.log; exit "$status"; }
  cat strict542-checks/installed.log >>strict542-checks/tests.log
  echo STEP608 installed-checks-pass
  mkdir "../$RESULT/checks"
  cp strict542-checks/tests.log strict542-checks/installed.json "../$RESULT/checks/"
  ;;
compiler)
  (cd .. && python3 stage608.py stage-native)
  npm exec --yes --package=pnpm@12.5.1 -- sh -c 'set -eu; [ "$(pnpm --version)" = 12.5.1 ]; pnpm install --frozen-lockfile'
  node --input-type=module -e 'import {releaseDisposableStore} from "./scripts/lib/disposable-build-inputs.mjs"; releaseDisposableStore("..")'
  set +e
  (
  set -e
  node --test docs/strict542/worker-minify608.test.mjs
  node --import ./scripts/tsx.mjs --test docs/strict542/native-codegen608.test.mjs
  node --import ./scripts/tsx.mjs --test docs/strict542/lazy-barrel608.test.mjs
  NATIVE_ADDON=$(node --input-type=module -e 'import {nativeCompiler608} from "./scripts/lib/native-compiler608.mjs"; console.log(nativeCompiler608(process.cwd(),{required:true}).env.NAPI_RS_NATIVE_LIBRARY_PATH)')
  NAPI_RS_NATIVE_LIBRARY_PATH="$NATIVE_ADDON" node --import ./scripts/tsx.mjs --test docs/strict542/lazy-barrel608.test.mjs
  NAPI_RS_NATIVE_LIBRARY_PATH="$NATIVE_ADDON" node --test docs/strict542/worker-minify608.test.mjs
  ) >strict542-checks/tests.log 2>&1
  status=$?
  set -e
  [ "$status" = 0 ] || { tail -40 strict542-checks/tests.log; exit "$status"; }
  echo STEP608 compiler-checks-pass
  mkdir "../$RESULT/compiler"
  cp strict542-checks/tests.log "../$RESULT/compiler/"
  ;;
package)
  (cd .. && python3 stage608.py stage-native && python3 stage608.py merge-logs source/strict542-checks/tests.log)
  # Same evidence the single run wrote after its passing checks; the merged
  # log is exactly the checks + compiler stage logs pinned by their receipts.
  python3 - <<'CHECK_EVIDENCE'
import json,hashlib
from pathlib import Path
m=json.loads(Path('../export-manifest.json').read_text())
value={'source_commit':m['source_commit'],'exit_code':0,'checks':['gateway-scoped','native-owner','supervisor-ipc','cancellation-settlement','application-preparation','frozen-package-policy','typed-package-owners','native-codegen-parity','native-lazy-minifier'],'test_log_sha256':hashlib.sha256(Path('strict542-checks/tests.log').read_bytes()).hexdigest()}
Path('strict542-checks/evidence.json').write_text(json.dumps(value,sort_keys=True)+'\n')
CHECK_EVIDENCE
  # build598.sh performs its own frozen install; only resolve the physical pnpm here.
  npm exec --yes --package=pnpm@12.5.1 -- sh -c 'set -eu; [ "$(pnpm --version)" = 12.5.1 ]; command -v pnpm >strict542-checks/pnpm-path.txt'
  PNPM_COMMAND=$(cat strict542-checks/pnpm-path.txt)
  PNPM_PHYSICAL=$(realpath "$PNPM_COMMAND")
  [ -x "$PNPM_PHYSICAL" ]
  [ "$("$PNPM_PHYSICAL" --version)" = 12.5.1 ]
  NODE_PHYSICAL=$(realpath "$(command -v node)")
  eval "$(python3 - <<'BUILDER_IDENTITIES'
import json,shlex
from pathlib import Path
m=json.loads(Path('../export-manifest.json').read_text())
for key,field in [('STRICT542_SOURCE_COMMIT','source_commit'),('STRICT542_SOURCE_EXPORT_SHA256','source_export_sha256'),('STRICT542_BUILD_RUN_ID','run_id')]:print(key+'='+shlex.quote(m[field]))
BUILDER_IDENTITIES
)"
  echo STEP608 builder-start
  env -i HOME="$HOME" PATH="$(dirname "$PNPM_COMMAND"):$(dirname "$NODE_PHYSICAL"):/usr/bin:/bin" STRICT542_SOURCE_COMMIT="$STRICT542_SOURCE_COMMIT" STRICT542_SOURCE_EXPORT_SHA256="$STRICT542_SOURCE_EXPORT_SHA256" STRICT542_BUILD_RUN_ID="$STRICT542_BUILD_RUN_ID" sh docs/strict542/build598.sh
  echo STEP608 builder-pass
  ;;
esac
cd "$EXPORT_ROOT"
python3 stage608.py receipt "$RESULT"
