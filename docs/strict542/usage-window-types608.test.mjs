import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import test from "node:test";

// Compile the actual parser/type bytes, without the gateway import graph.
// Node's type stripping does not check this declaration-build contract.
test("actual usage window parser typechecks with checked indexed access", () => {
  const source = readFileSync("src/gateway/strict542/usage-preflight.ts", "utf8");
  const windowType = source.match(/^export type UsagePreflightWindow = .+;$/m)?.[0];
  assert.ok(windowType, "actual window type declaration required");
  const begin = source.indexOf("const WINDOW_LABELS:");
  const end = source.indexOf("/** Single GET", begin);
  assert.ok(begin >= 0 && end > begin, "actual parser source boundaries required");
  const root = mkdtempSync(path.join(tmpdir(), "usage-window-types608-"));
  try {
    const input = path.join(root, "usage-window-parser.ts");
    writeFileSync(input, windowType + "\n" + source.slice(begin, end));
    const result = spawnSync(process.execPath, [
      path.resolve("node_modules/typescript/bin/tsc"), "--strict",
      "--noUncheckedIndexedAccess", "--target", "es2022", "--module", "esnext",
      "--typeRoots", root,
      "--skipLibCheck", "--noEmit", input,
    ], {
      // Run outside the repo so tsc never discovers the root tsconfig.json
      // (TS5112 refuses explicit files when one is present).
      cwd: root, encoding: "utf8", timeout: 30000, maxBuffer: 1024 * 1024,
    });
    assert.equal(result.error, undefined, String(result.error));
    assert.equal(result.signal, null);
    assert.equal(result.status, 0, result.stdout + result.stderr);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});
