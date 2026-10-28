#!/bin/sh
# Fixed, finite build continuation inside a committed secretless admitted export.
set -eu
case "${1-}" in runtime|unified-[0-5]|middle|sdk-[0-1]|tail) STAGE="$1";; *) exit 2;; esac
: "${STRICT542_SOURCE_COMMIT:?}"
: "${STRICT542_SOURCE_EXPORT_SHA256:?}"
: "${STRICT542_BUILD_RUN_ID:?}"
export SOURCE_DATE_EPOCH=1792944000 TZ=UTC LANG=C LC_ALL=C CI=1
export GIT_COMMIT="$STRICT542_SOURCE_COMMIT"
export OPENCLAW_BUILD_TIMESTAMP=2026-10-25T16:00:00.000Z
node --version
[ "$(pnpm --version)" = 12.5.1 ]
python3 docs/strict542/frozen-package608.py preflight
pnpm install --frozen-lockfile
node --input-type=module -e 'import fs from "node:fs"; import {releaseDisposableStore} from "./scripts/lib/disposable-build-inputs.mjs"; if (fs.lstatSync("../.pnpm-store",{throwIfNoEntry:false})) releaseDisposableStore("..")'
python3 docs/strict542/frozen-package608.py preflight
node --import ./scripts/tsx.mjs scripts/build-checkpoint608.mts "$STAGE"
