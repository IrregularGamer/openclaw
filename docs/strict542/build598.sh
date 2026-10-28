#!/bin/sh
# SOURCE ONLY. Run only through admitted offload from a committed secretless export.
# This builds a portable directory, never an image, runtime installation or service.
set -eu
case "${1-}" in '') BUILD_MODE=ordinary;; checkpoint608) BUILD_MODE=checkpoint608;; *) exit 2;; esac
[ "$#" -le 1 ] || exit 2
[ ! -e result598-build ] || { echo 'refuse existing result598-build'; exit 2; }
mkdir result598-build
: "${STRICT542_SOURCE_COMMIT:?export exact committed source identity}"
: "${STRICT542_SOURCE_EXPORT_SHA256:?export exact git archive digest}"
: "${STRICT542_BUILD_RUN_ID:?identifier of this admitted build, independently reconciled to broker log}"
export SOURCE_DATE_EPOCH=1792944000 TZ=UTC LANG=C LC_ALL=C CI=1
export GIT_COMMIT="$STRICT542_SOURCE_COMMIT"
export OPENCLAW_BUILD_TIMESTAMP=2026-10-25T16:00:00.000Z
exec >result598-build/build.log 2>&1
node --version
pnpm --version
[ "$(pnpm --version)" = 12.5.1 ]
python3 docs/strict542/frozen-package608.py preflight
# No relaxed lock, dependency cooldown, lifecycle, kernel or workload-budget policy.
pnpm install --frozen-lockfile
# The frozen installer has exited; discard only its disposable private store.
node --input-type=module -e 'import fs from "node:fs"; import {releaseDisposableStore} from "./scripts/lib/disposable-build-inputs.mjs"; if (fs.lstatSync("../.pnpm-store",{throwIfNoEntry:false})) releaseDisposableStore("..")'
python3 docs/strict542/frozen-package608.py preflight
# Full canonical phase inventory with the separately reviewed required-native scheduler.
if [ "$BUILD_MODE" = checkpoint608 ]; then
  node --import ./scripts/tsx.mjs scripts/build-checkpoint608-owned.mjs complete
else
node --import ./scripts/tsx.mjs scripts/build-all.mts boundedPackage
fi
python3 docs/strict542/frozen-package608.py preflight
pnpm --filter openclaw --prod deploy result598-build/runtime >result598-build/deploy.log 2>&1 || {
  status=$?; tail -30 result598-build/deploy.log; exit "$status";
}
python3 docs/strict542/frozen-package608.py receipt
# A production dependency graph must be wholly contained. The receipt tool
# refuses escaping links, special files, writable content and runtime state.
python3 - <<'BUILD_EVIDENCE'
import hashlib,json,os,platform,subprocess
from pathlib import Path
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
# Test log and admission receipt are supplied from this exact committed source's
# separately completed admitted check. Never synthesize success from placeholders.
test=Path('strict542-checks/tests.log'); proof=json.loads(Path('strict542-checks/evidence.json').read_text())
package=json.loads(Path('result598-build/package-receipt.json').read_text())
assert package['source_lock_sha256']==sha('pnpm-lock.yaml')=='091ede3cb510110ed2b1ca8858100066add16cb3b91bcd0ff097d89f75035751'
assert package['target_lock_sha256']==sha('result598-build/runtime/pnpm-lock.yaml')
assert package['deploy_log_sha256']==sha('result598-build/deploy.log')
assert proof['source_commit']==os.environ['STRICT542_SOURCE_COMMIT']
assert proof['exit_code']==0 and set(proof['checks']) >= {'gateway-scoped','native-owner','supervisor-ipc','cancellation-settlement','application-preparation'}
assert sha(test)==proof['test_log_sha256']
# build.log is still open; snapshot it only after the preceding synchronous build
# and packaging commands have exited. The final receipt is written after close.
value={'source_commit':os.environ['STRICT542_SOURCE_COMMIT'],'source_export_sha256':os.environ['STRICT542_SOURCE_EXPORT_SHA256'],'lockfile_sha256':sha('pnpm-lock.yaml'),'toolchain':{'node':subprocess.check_output(['node','--version'],text=True).strip(),'pnpm':subprocess.check_output(['pnpm','--version'],text=True).strip(),'python':platform.python_version()},'execution':'admitted-offload','remote_run_id':os.environ['STRICT542_BUILD_RUN_ID'],'checks':proof['checks'],'test_exit':0,'build_exit':0,'test_log_sha256':sha(test),'build_log_sha256':sha('result598-build/build.log')}
value.update(package_receipt=package,package_receipt_sha256=sha('result598-build/package-receipt.json'),native_compile_receipt_sha256=sha('../.native608/receipt.json'),native_libtests_receipt_sha256=sha('../.native608/libtests-receipt.json'),native_addon_sha256=sha('../.native608/rolldown-binding.linux-x64-gnu.node'),compiler_route='boundedPackage-required-native608')
Path('result598-build/evidence.json').write_text(json.dumps(value,sort_keys=True)+'\n')
BUILD_EVIDENCE
python3 docs/strict542/application598.py tree --runtime result598-build/runtime --lockfile pnpm-lock.yaml --build-evidence result598-build/evidence.json --build-log result598-build/build.log --test-log strict542-checks/tests.log --output result598-build/tree.json
