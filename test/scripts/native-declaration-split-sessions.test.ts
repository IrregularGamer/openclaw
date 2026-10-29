import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import { emitNativeDeclarations } from "../../scripts/lib/native-declaration-emitter.mts";

const dirs: string[] = [];
function fixture(source: string) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), "native-split-"));
  dirs.push(root);
  fs.mkdirSync(path.join(root, "src"));
  fs.writeFileSync(path.join(root, "package.json"), JSON.stringify({ name: "fixture", type: "module" }));
  fs.writeFileSync(
    path.join(root, "tsconfig.json"),
    JSON.stringify({ compilerOptions: { strict: true, module: "nodenext", target: "es2022", skipLibCheck: true, types: [] }, include: ["src"] }),
  );
  fs.writeFileSync(path.join(root, "src/ambient.d.ts"), "declare const AMBIENT: number;\n");
  fs.writeFileSync(path.join(root, "src/index.ts"), source);
  return root;
}
const run = (root: string) =>
  emitNativeDeclarations({
    cwd: root,
    configFile: path.join(root, "tsconfig.json"),
    roots: [path.join(root, "src/index.ts")],
  });

afterEach(() => {
  for (const dir of dirs.splice(0)) fs.rmSync(dir, { recursive: true, force: true });
});

describe("split native declaration sessions (job650)", () => {
  it("emits declarations after the full-check session passes", async () => {
    const root = fixture("export const value = AMBIENT + 1;\n");
    const { declarations } = await run(root);
    const index = fs.realpathSync(path.join(root, "src/index.ts"));
    expect(declarations.get(index)?.code).toContain("export declare const value: number;");
  }, 120_000);

  it("still fails on semantic errors that only the full check reports", async () => {
    const root = fixture('export const value: number = "text";\n');
    await expect(run(root)).rejects.toThrow(/TS2322/u);
  }, 120_000);

  it("still fails on unresolved names beside ambient files", async () => {
    const root = fixture("export const value = UNDECLARED_AMBIENT;\n");
    await expect(run(root)).rejects.toThrow(/TS2304/u);
  }, 120_000);
});

describe("split native declaration sessions keep emit-only checks (job650 review)", () => {
  it("still reports declaration-emit diagnostics from the noCheck emit session", async () => {
    const root = fixture("class Hidden {}\nexport function make() { return new Hidden(); }\nexport const x = AMBIENT;\n");
    fs.writeFileSync(
      path.join(root, "tsconfig.json"),
      JSON.stringify({ compilerOptions: { strict: true, module: "nodenext", target: "es2022", skipLibCheck: true, types: [], isolatedDeclarations: true }, include: ["src"] }),
    );
    await expect(run(root)).rejects.toThrow(/TS9007|TS9010|TS4\d{3}/u);
  }, 120_000);

  it("ignores a caller-supplied check:false so the full check cannot be skipped", async () => {
    const root = fixture('export const value: number = "text";\n');
    await expect(
      emitNativeDeclarations({
        cwd: root,
        configFile: path.join(root, "tsconfig.json"),
        roots: [path.join(root, "src/index.ts")],
        ...({ check: false } as object),
      }),
    ).rejects.toThrow(/TS2322/u);
  }, 120_000);
});
