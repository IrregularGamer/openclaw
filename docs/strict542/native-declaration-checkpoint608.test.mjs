import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { stripTypeScriptTypes } from 'node:module';
import { pathToFileURL } from 'node:url';
import { fixture } from './native-compiler608-fixture.mjs';

// Native declaration producer/join boundary: the REAL native-compiler608 owner
// (no stub) validates the pinned native receipts/addon for every group produce
// and join. Compiler execution and publication are fixture stubs; nothing here
// is admitted compiler evidence or BUILT authority. Run from the repo root.
const dataModule=source=>'data:text/javascript;base64,'+Buffer.from(source).toString('base64');
const options={mode:'produce',group:'openclaw-dts-base',sourceCommit:'a'.repeat(40),sourceExportSha256:'b'.repeat(64)};
test('real native owner gates declaration produce/join: refusal, tamper, control injection and cancellation leave no checkpoint',async t=>{
 const originalCwd=process.cwd(),originalEnv={...process.env};
 const root=fixture(t);
 const canonical=['openclaw-dts-base',...Array.from({length:5},(_,i)=>`openclaw-dts-extensions-${i+1}`)];
 const state={closed:false,published:0,fail:false,cancel:false};globalThis.__declarationState608=state;
 const artifactSource=stripTypeScriptTypes(fs.readFileSync(new URL('../../scripts/lib/build-artifact-cache.mts',import.meta.url),'utf8'))
  .replace(/import\s*\{[^}]+\}\s*from\s*"@openclaw\/fs-safe\/file-lock";/u,'const acquireFileLock=()=>{throw new Error("unexpected lock")}; const acquireFileLockSync=acquireFileLock;');
 const artifacts=await import(dataModule(artifactSource));
 globalThis.__declarationArtifacts608={...artifacts,resolveTsdownCompilerFiles:()=>[]};
 const stubs={
   '../tsdown-build.mts':`import fs from 'node:fs';import path from 'node:path';export const TSDOWN_DECLARATION_EXTENSIONS=['.d.ts'];export const TSDOWN_UNIFIED_CACHE_ENV=[];export const resolveStagedDeclarationConcurrency=()=>1;export const listReplaceableTsdownDeclarationOutputs=()=>[];export const prepareTsdownBuildExecution=options=>({invocations:[{args:options.args}],maxOldSpaceMb:128});export async function executeTsdownBuildPlan(plan){const s=globalThis.__declarationState608;s.closed=false;if(s.fail)return 1;if(s.cancel){const out=plan.invocations[0].args[plan.invocations[0].args.indexOf('--out-dir')+1];fs.mkdirSync(out,{recursive:true});fs.writeFileSync(path.join(out,'partial.d.ts'),'x');throw Object.assign(new Error('cancelled'),{name:'AbortError'});}for(const inv of plan.invocations){const args=inv.args,out=args[args.indexOf('--out-dir')+1],name=args[args.indexOf('--filter')+1];fs.mkdirSync(out,{recursive:true});fs.writeFileSync(path.join(out,name+'.d.ts'),'export {};');const receipt=path.join(out,'..','compiler-inputs',name+'.json');const request=JSON.parse(fs.readFileSync(receipt,'utf8'));fs.writeFileSync(receipt,JSON.stringify({...request,inputs:['src/source.ts']}));}await Promise.resolve();s.closed=true;return 0;}`,
  './build-artifact-cache.mts':'export const {ARTIFACT_CACHE_VERSION,listCacheFiles,readArtifactRecord,writeArtifactRecord,finalizeBuildStepCache,portableRelativePath,restoreBuildStepCacheOutputs,resolveBuildStepCacheState,resolveTsdownCompilerFiles}=globalThis.__declarationArtifacts608;',
  './compiler-input-snapshot.mts':`import fs from 'node:fs';import path from 'node:path';import {createHash} from 'node:crypto';export class CompilerInputSnapshot {constructor(root){this.root=root;}signature(config,args,inputs){return createHash('sha256').update(JSON.stringify([args,inputs.map(file=>[file,fs.readFileSync(path.join(this.root,file),'utf8')])])).digest('hex');}seal(config,args,inputs){if(!globalThis.__declarationState608.closed)throw new Error('unsettled compiler');return {signature:this.signature(config,args,inputs),inputs};}}`,
  './declaration-stage.mts':`import fs from 'node:fs';import path from 'node:path';export async function publishStagedDeclarations(plan,sources,staging,dist,required,previous,seal){if(plan.invocations.length)throw new Error('join tried compiler');for(const source of sources)for(const file of source.required)if(!fs.existsSync(path.join(source.output,file)))throw new Error('missing canonical output');seal();globalThis.__declarationState608.published++;}`,
  './dist-artifact-ownership.mts':'export const withDistArtifactOwnership=async(_cwd,fn)=>fn();',
  './managed-child-process.mts':'export const hasUnjoinedWork=()=>false;',
  './tsdown-declaration-generator-inputs.mts':'export const resolveTsdownDeclarationGeneratorInputs=()=>[];',
  './tsdown-declaration-inputs.mts':`import fs from 'node:fs';import path from 'node:path';export const createDeclarationStage=root=>fs.mkdtempSync(path.join(root,'.artifacts/stage-'));export function requestDeclarationInputs(out,name,roots){const dir=path.join(out,'..','compiler-inputs');fs.mkdirSync(dir,{recursive:true});fs.writeFileSync(path.join(dir,name+'.json'),JSON.stringify({roots}));}export const readDeclarationInputs=(out,name)=>JSON.parse(fs.readFileSync(path.join(out,'..','compiler-inputs',name+'.json'),'utf8')).inputs;`,
  './tsdown-config-groups.mts':`export const TSDOWN_NON_SDK_DTS_CONFIG_GROUPS=${JSON.stringify(canonical)};export const TSDOWN_PLUGIN_SDK_DTS_CONFIG_GROUPS=['openclaw-dts-plugin-sdk-1','openclaw-dts-plugin-sdk-2'];`,
 };
 try {
  fs.mkdirSync(path.join(root,'.artifacts'));fs.mkdirSync(path.join(root,'src'));fs.mkdirSync(path.join(root,'checkpoints'));
  fs.writeFileSync(path.join(root,'src/source.ts'),'export {};');
  fs.writeFileSync(path.join(root,'tsdown.config.ts'),'export default '+JSON.stringify(canonical.map(name=>({name,entry:{[name]:'src/source.ts'},dts:{entry:['src/source.ts'],compilerOptions:{stableTypeOrdering:true}}})))+';');
  let writer=stripTypeScriptTypes(fs.readFileSync(new URL('../../scripts/lib/tsdown-declaration-writer.mts',import.meta.url),'utf8'));
  for(const [specifier,code] of Object.entries(stubs))writer=writer.replaceAll(JSON.stringify(specifier),JSON.stringify(dataModule(code)));
  for(const owner of ['./declaration-checkpoint608.mjs','./native-compiler608.mjs'])
   writer=writer.replaceAll(JSON.stringify(owner),JSON.stringify(pathToFileURL(path.resolve(originalCwd,'scripts/lib',owner)).href));
  assert.match(writer,/native-compiler608\.mjs/u);
  const {writeBoundedDeclarationCheckpoint608}=await import(dataModule(writer));
  process.chdir(root);Object.assign(process.env,{OPENCLAW_608_BOUNDED_PACKAGE:'1',OPENCLAW_BUILD_CACHE:'0',STRICT542_SOURCE_COMMIT:options.sourceCommit,STRICT542_SOURCE_EXPORT_SHA256:options.sourceExportSha256});
  const opts={...options,directory:path.join(root,'checkpoints')};
  const native=path.join(root,'../.native608'),addon=path.join(native,'rolldown-binding.linux-x64-gnu.node');
  const none=()=>assert.deepEqual(fs.readdirSync(opts.directory),[]);
  // cache-on and caller native controls are refused before any compiler runs
  process.env.OPENCLAW_BUILD_CACHE='1';await assert.rejects(writeBoundedDeclarationCheckpoint608('unified',opts),/disabled caches/u);process.env.OPENCLAW_BUILD_CACHE='0';
  process.env.NAPI_RS_LOG='debug';await assert.rejects(writeBoundedDeclarationCheckpoint608('unified',opts),/native compiler control/u);delete process.env.NAPI_RS_LOG;
  process.env.NAPI_RS_NATIVE_LIBRARY_PATH='/other/addon.node';await assert.rejects(writeBoundedDeclarationCheckpoint608('unified',opts),/native compiler control/u);delete process.env.NAPI_RS_NATIVE_LIBRARY_PATH;
  none();
  // tampered and absent native addon refuse the producer
  const bytes=fs.readFileSync(addon);fs.appendFileSync(addon,'tamper');
  await assert.rejects(writeBoundedDeclarationCheckpoint608('unified',opts),/addon mismatch/u);fs.writeFileSync(addon,bytes);
  fs.renameSync(native,native+'.away');
  await assert.rejects(writeBoundedDeclarationCheckpoint608('unified',opts),/required native compiler/u);fs.renameSync(native+'.away',native);
  none();
  // cancellation after partial compiler output leaves no checkpoint or publication
  state.cancel=true;await assert.rejects(writeBoundedDeclarationCheckpoint608('unified',opts),/cancelled/u);state.cancel=false;
  none();assert.equal(state.published,0);
  // valid native pin: every canonical group produces, then join publishes once
  for(const group of canonical)await writeBoundedDeclarationCheckpoint608('unified',{...opts,group});
  assert.deepEqual(fs.readdirSync(opts.directory).sort(),[...canonical].sort());
  // native drift between produce and join refuses the join without publication
  fs.appendFileSync(addon,'drift');
  await assert.rejects(writeBoundedDeclarationCheckpoint608('unified',{...opts,mode:'join',group:undefined}),/addon mismatch/u);
  assert.equal(state.published,0);fs.writeFileSync(addon,bytes);
  // the trusted addon path itself is inherited, not caller-selected, and the join then publishes
  process.env.NAPI_RS_NATIVE_LIBRARY_PATH=addon;
  await writeBoundedDeclarationCheckpoint608('unified',{...opts,mode:'join',group:undefined});assert.equal(state.published,1);
 } finally {process.chdir(originalCwd);for(const key of Object.keys(process.env))if(!Object.hasOwn(originalEnv,key))delete process.env[key];Object.assign(process.env,originalEnv);delete globalThis.__declarationState608;delete globalThis.__declarationArtifacts608;}
});
