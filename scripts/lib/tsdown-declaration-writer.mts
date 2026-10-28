// Canonical declaration groups share one private compiler and publication lifetime.
import fs from "node:fs";
import { trustedNativeCompilerEnvironment608 } from "./native-compiler608.mjs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { isDeepStrictEqual } from "node:util";
import {
  prepareTsdownBuildExecution,
  resolveStagedDeclarationConcurrency,
  TSDOWN_DECLARATION_EXTENSIONS,
  TSDOWN_UNIFIED_CACHE_ENV,
  executeTsdownBuildPlan,
  listReplaceableTsdownDeclarationOutputs,
} from "../tsdown-build.mts";
import {
  ARTIFACT_CACHE_VERSION,
  listCacheFiles,
  readArtifactRecord,
  writeArtifactRecord,
  finalizeBuildStepCache,
  portableRelativePath,
  restoreBuildStepCacheOutputs,
  resolveBuildStepCacheState,
  resolveTsdownCompilerFiles,
  type BuildCacheStep,
} from "./build-artifact-cache.mts";
import { CompilerInputSnapshot } from "./compiler-input-snapshot.mts";
import { publishStagedDeclarations } from "./declaration-stage.mts";
import { withDistArtifactOwnership } from "./dist-artifact-ownership.mts";
import { hasUnjoinedWork } from "./managed-child-process.mts";
import { resolveTsdownDeclarationGeneratorInputs } from "./tsdown-declaration-generator-inputs.mts";
import {
  createDeclarationStage,
  readDeclarationInputs,
  requestDeclarationInputs,
} from "./tsdown-declaration-inputs.mts";
import { TSDOWN_NON_SDK_DTS_CONFIG_GROUPS, TSDOWN_PLUGIN_SDK_DTS_CONFIG_GROUPS } from "./tsdown-config-groups.mts";
import { checkpointSelection608, checkpointAncestry608, checkpointInventory608, checkpointTopology608, validateCheckpoint608 } from "./declaration-checkpoint608.mjs";

export type DeclarationCheckpoint608 = {
  mode: "produce" | "join";
  group?: string;
  directory: string;
  sourceCommit: string;
  sourceExportSha256: string;
};

/** Fixed canonical entry point for admitted per-group stages and complete joins. */
export async function writeBoundedDeclarationCheckpoint608(kind: "unified" | "sdk", checkpoint: DeclarationCheckpoint608) {
  if (kind === "unified") {
    return writeTsdownDeclarations(TSDOWN_NON_SDK_DTS_CONFIG_GROUPS, "tsdown-unified",
      (root) => listReplaceableTsdownDeclarationOutputs({cwd:root, roots:["dist"]}),
      "scripts/write-unified-entry-dts.ts", checkpoint);
  }
  if (kind !== "sdk") throw new Error("unknown canonical declaration writer");
  return writeTsdownDeclarations(TSDOWN_PLUGIN_SDK_DTS_CONFIG_GROUPS, "tsdown-plugin-sdk",
    (root) => listCacheFiles(root, [{path:"dist/plugin-sdk", extensions:TSDOWN_DECLARATION_EXTENSIONS, recursive:false}], fs),
    "scripts/write-plugin-sdk-entry-dts.ts", checkpoint);
}

export async function writeTsdownDeclarations(
  groups: readonly string[],
  label: string,
  previousOutputs: (root: string) => string[],
  generatorEntry: string,
  checkpoint?: DeclarationCheckpoint608,
) {
  const root = fs.realpathSync.native(process.cwd());
  const compilerEnv = Object.hasOwn(process.env, "OPENCLAW_608_BOUNDED_PACKAGE")
    ? trustedNativeCompilerEnvironment608(root, process.env, { inherited: true }).env
    : process.env;
  if (Object.hasOwn(compilerEnv, "OPENCLAW_608_BOUNDED_PACKAGE") &&
      compilerEnv.OPENCLAW_608_BOUNDED_PACKAGE !== "1") throw new Error("invalid bounded native package policy");
  if (compilerEnv.OPENCLAW_608_BOUNDED_PACKAGE === "1" && compilerEnv.OPENCLAW_BUILD_CACHE !== "0") {
    throw new Error("native bounded declarations require disabled caches");
  }
  if (compilerEnv.OPENCLAW_608_BOUNDED_PACKAGE === "1") Object.assign(process.env, compilerEnv);
  const canonical = label === "tsdown-unified" ? TSDOWN_NON_SDK_DTS_CONFIG_GROUPS
    : label === "tsdown-plugin-sdk" ? TSDOWN_PLUGIN_SDK_DTS_CONFIG_GROUPS : [];
  const selectedGroups = checkpoint ? checkpointSelection608(checkpoint, groups, canonical) : groups;
  if (checkpoint) {
    if (compilerEnv.OPENCLAW_608_BOUNDED_PACKAGE !== "1" || compilerEnv.OPENCLAW_BUILD_CACHE !== "0") {
      throw new Error("declaration checkpoints require the admitted bounded no-cache owner");
    }
    if (checkpoint.sourceCommit !== compilerEnv.STRICT542_SOURCE_COMMIT ||
        checkpoint.sourceExportSha256 !== compilerEnv.STRICT542_SOURCE_EXPORT_SHA256) {
      throw new Error("declaration checkpoint differs from the verified export runner identity");
    }
    checkpointAncestry608(checkpoint.directory);
  }
  const stages: string[] = [];
  const createStage = () => {
    const stage = createDeclarationStage(root);
    stages.push(stage);
    return stage;
  };
  const failures: unknown[] = [];
  try {
    // The private child retains declared cwd ownership; snapshot/output paths are physical.
    await withDistArtifactOwnership(process.cwd(), async () => {
      const { default: configs }: { default: typeof import("../../tsdown.config.ts").default } =
        await import(pathToFileURL(path.join(root, "tsdown.config.ts")).href);
      const staging = createStage();
      const output = path.join(staging, "dist");
      const environment = TSDOWN_UNIFIED_CACHE_ENV.map((name) =>
        JSON.stringify([name, process.env[name] ?? ""]),
      );
      const generatorInputs = resolveTsdownDeclarationGeneratorInputs(root, generatorEntry);
      const snapshot = () =>
        new CompilerInputSnapshot(root, {
          toolchainFiles: resolveTsdownCompilerFiles(),
          generatorInputs,
          isGeneratorInput: (file) => /(?:^|\/)(?:package|openclaw\.plugin)\.json$/u.test(file),
        });
      // All groups share the same before/after reads of configuration, topology,
      // tools and overlapping sources. Only compiler membership differs.
      const before = snapshot();
      const liveDist = path.join(root, "dist");
      const prepared = selectedGroups.map((name: string) => {
        const config = configs.find((candidate: { name?: string }) => candidate.name === name);
        if (
          !config?.dts ||
          typeof config.dts !== "object" ||
          !Array.isArray(config.dts.entry) ||
          !config.entry ||
          typeof config.entry !== "object" ||
          Array.isArray(config.entry)
        ) {
          throw new Error(`Missing canonical declaration group ${name}`);
        }
        // Runtime worker entries are absolute; declaration partitions are checkout-relative.
        const entries = Object.entries(config.entry).map(
          ([entry, inputs]) =>
            [entry, [inputs].flat().map((input) => path.resolve(root, input))] as const,
        );
        const required = config.dts.entry.map((source) => {
          const resolved = path.resolve(root, source);
          const selected = entries.find(([, inputs]) => inputs.includes(resolved));
          if (!selected) {
            throw new Error(`Missing canonical declaration entry for ${source}`);
          }
          return `${selected[0]}.d.ts`;
        });
        const identity = [
          ...environment,
          JSON.stringify({
            name,
            entry: Object.fromEntries(
              entries.map(([entry, sources]) => [
                entry,
                sources.map((source) => portableRelativePath(root, source)),
              ]),
            ),
            declarations: config.dts.entry,
            ...(checkpoint ? {declarationOptions: config.dts,
              tsconfig: config.tsconfig} : {}),
            sourcemap: config.sourcemap,
          }),
        ];
        const stage = createStage();
        const groupOutput = path.join(stage, "dist");
        requestDeclarationInputs(groupOutput, name, config.dts.entry);
        if (compilerEnv.OPENCLAW_608_BOUNDED_PACKAGE === "1") {
          trustedNativeCompilerEnvironment608(root, compilerEnv, { inherited: true });
        }
        const plan = prepareTsdownBuildExecution(
          {
            env: compilerEnv,
            args: ["--config", "tsdown.config.ts", "--filter", name, "--out-dir", groupOutput],
          },
          {
            // Every compiler owns a fresh stage; live runtime outputs stay intact.
            cleanup() {},
            reportShortfall(shortfall) {
              console.error(shortfall.message);
            },
          },
        );
        if (!plan) {
          throw new Error("Insufficient memory for declaration build");
        }
        const receipt = `compiler-inputs/${name}.json`;
        const step: BuildCacheStep = {
          label: `${label}-${name}`,
          cache: {
            env: TSDOWN_UNIFIED_CACHE_ENV,
            inputs: generatorInputs,
            // An empty canonical partition still owns its successful compiler
            // receipt. Ordinary cache records never admit an empty inventory.
            outputs: [{ path: "dist", extensions: TSDOWN_DECLARATION_EXTENSIONS }, receipt],
            requiredOutputs: [...required.map((entry) => `dist/${entry}`), receipt],
            restore: "always",
          },
        };
        const params = {
          rootDir: root,
          artifactRoot: stage,
          env: {
            ...compilerEnv,
            OPENCLAW_BUILD_PRIVATE_QA: process.env.OPENCLAW_BUILD_PRIVATE_QA === "1" ? "1" : "0",
          },
          inputSignature: (inputs: string[]) =>
            before.signature("tsconfig.json", identity, inputs, liveDist),
        };
        const state =
          process.env.OPENCLAW_BUILD_CACHE === "0"
            ? undefined
            : resolveBuildStepCacheState(step, params);
        if (!state) {
          params.inputSignature([]);
        }
        // Record the lookup before compilation replaces the signature and cache record.
        console.error(
          `[${label}] ${name}: cache ${state?.fresh ? "hit" : "miss"} (${state?.reason ?? "disabled"})`,
        );
        return { name, stage, output: groupOutput, required, identity, plan, step, params, state };
      });
      const required = prepared.flatMap((group) => group.required);
      if (!required.length && !checkpoint) {
        throw new Error("Canonical declaration selection is empty");
      }
      const startedAt = Date.now();
      const checkpointIdentity = (group: (typeof prepared)[number]) => ({
        schema:"strict542-declaration-group608-v1", status:"COMPILED_GROUP_NOT_PUBLISHED",
        source_commit:checkpoint!.sourceCommit, source_export_sha256:checkpoint!.sourceExportSha256,
        group:group.name, label, generator_entry:generatorEntry, required:group.required, identity:group.identity,
      });
      if (checkpoint?.mode === "produce") {
        const group = prepared[0]!;
        const target = path.join(checkpoint.directory, group.name);
        if (fs.existsSync(target)) throw new Error("declaration checkpoint already exists");
        const exit = await executeTsdownBuildPlan(group.plan, 1);
        if (exit !== 0) throw new Error(`Declaration checkpoint compiler failed with exit ${exit}`);
        // executeTsdownBuildPlan joins the entire compiler tree; the native
        // declaration plugin closes its API before publishing membership.
        const inputs = readDeclarationInputs(group.output, group.name);
        const sealed = snapshot().seal("tsconfig.json", group.identity, inputs, before, startedAt, liveDist);
        const temporary = fs.mkdtempSync(path.join(checkpoint.directory, ".declaration-group-"));
        try {
          fs.chmodSync(temporary, 0o700);
          const data = path.join(temporary,"data");
          checkpointInventory608(group.stage);
          fs.cpSync(group.stage,data,{recursive:true,errorOnExist:true,force:false});
          const record = {version:ARTIFACT_CACHE_VERSION,signature:sealed.signature,
            outputs:checkpointInventory608(data),inputs:sealed.inputs};
          writeArtifactRecord(path.join(temporary,"artifact-record.json"),record);
          fs.writeFileSync(path.join(temporary,"receipt.json"),JSON.stringify({...checkpointIdentity(group),
            record,topology:checkpointTopology608(data)})+"\n",{flag:"wx",mode:0o600});
          // A receipt is never written on failure or while a child owns its stage.
          if (fs.existsSync(target)) throw new Error("declaration checkpoint publication collision");
          fs.renameSync(temporary,target);
        } catch(error) {
          fs.rmSync(temporary,{recursive:true,force:true});
          throw error;
        }
        return;
      }
      if (checkpoint?.mode === "join") {
        for (const group of prepared) {
          const stored = path.join(checkpoint.directory,group.name);
          checkpointAncestry608(stored);
          if (JSON.stringify(fs.readdirSync(stored).sort()) !== JSON.stringify(["artifact-record.json","data","receipt.json"])) {
            throw new Error("declaration checkpoint contains unexpected entries");
          }
          for (const file of ["receipt.json","artifact-record.json"]) {
            const stat=fs.lstatSync(path.join(stored,file));
            if (!stat.isFile() || stat.isSymbolicLink() || stat.nlink!==1) throw new Error("checkpoint receipt must be private regular file");
          }
          const receipt = JSON.parse(fs.readFileSync(path.join(stored,"receipt.json"),"utf8"));
          if (!Array.isArray(receipt.topology)) throw new Error("missing exact declaration checkpoint topology");
          const record = readArtifactRecord(path.join(stored,"artifact-record.json"));
          if (!record || !isDeepStrictEqual(record,receipt.record)) throw new Error("checkpoint artifact record drift");
          validateCheckpoint608(receipt, checkpointIdentity(group), path.join(stored,"data"),
            (record: {signature:string; inputs:string[]}) => before.signature("tsconfig.json",group.identity,record.inputs,liveDist)===record.signature, ARTIFACT_CACHE_VERSION);
          fs.cpSync(path.join(stored,"data"),group.stage,{recursive:true});
          // Recheck copied bytes and real input membership before publication.
          validateCheckpoint608(receipt, checkpointIdentity(group), group.stage,
            (record: {signature:string; inputs:string[]}) => JSON.stringify(readDeclarationInputs(group.output,group.name))===JSON.stringify(record.inputs), ARTIFACT_CACHE_VERSION);
        }
      }
      for (const group of prepared) {
        if (group.state?.fresh && !restoreBuildStepCacheOutputs(group.state, group.params)) {
          throw new Error("Declaration cache changed before restoration; rerun the build");
        }
      }
      // Only nonempty single-compiler private stages may overlap. Publication
      // still joins the complete batch before merging any group's declarations.
      const misses = checkpoint?.mode === "join" ? [] : prepared.filter((group) => !group.state?.fresh);
      const concurrency = misses.every(
        (group) => group.required.length > 0 && group.plan.invocations.length === 1,
      )
        ? resolveStagedDeclarationConcurrency(
            misses.map((group) => ({ name: group.name, maxOldSpaceMb: group.plan.maxOldSpaceMb })),
          )
        : 1;
      const plan = {
        ...prepared[0]!.plan,
        invocations: misses.flatMap((group) => group.plan.invocations),
      };
      await publishStagedDeclarations(
        plan,
        prepared.map((group) => ({ output: group.output, required: group.required })),
        output,
        liveDist,
        required,
        previousOutputs(root).map((file) => portableRelativePath(liveDist, file)),
        () => {
          const after = snapshot();
          for (const group of prepared) {
            const sealed = after.seal(
              "tsconfig.json",
              group.identity,
              readDeclarationInputs(group.output, group.name),
              before,
              startedAt,
              liveDist,
            );
            if (group.state?.fresh && sealed.signature !== group.state.signature) {
              throw new Error(`Cached declaration membership changed: ${group.name}`);
            }
            if (group.state) {
              group.state.signature = sealed.signature;
              group.state.consumedInputs = sealed.inputs;
            }
          }
        },
        concurrency,
      );
      for (const group of prepared) {
        if (group.state && !group.state.fresh) {
          finalizeBuildStepCache(group.step, group.state, group.params);
        }
      }
      if (prepared.every((group) => group.state?.fresh)) {
        console.log(`[${label}] restored complete cached generation`);
      }
    });
  } catch (error) {
    failures.push(error);
  }
  // An unjoined child may still be writing a stage; retain its inputs and error
  // under the checkout's existing fail-closed ownership until explicit recovery.
  for (const stage of failures.some(hasUnjoinedWork) ? [] : stages) {
    try {
      fs.rmSync(stage, { recursive: true, force: true });
    } catch (error) {
      failures.push(error);
    }
  }
  // The private entry observes this after module evaluation. Keep unjoined build
  // metadata even if removing the private staging tree also failed.
  if (failures.length) {
    throw failures.length === 1
      ? failures[0]
      : new AggregateError(failures, "Declaration build and staging cleanup failed");
  }
}
