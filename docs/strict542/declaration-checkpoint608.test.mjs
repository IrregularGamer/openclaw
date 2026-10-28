import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { stripTypeScriptTypes } from 'node:module';
import { pathToFileURL } from 'node:url';
import { checkpointSelection608, checkpointInventory608, validateCheckpoint608 } from '../../scripts/lib/declaration-checkpoint608.mjs';

const groups=['openclaw-dts-base','openclaw-dts-extensions-1'];
const options={mode:'produce',group:groups[0],directory:'/tmp/checkpoints',sourceCommit:'a'.repeat(40),sourceExportSha256:'b'.repeat(64)};
test('checkpoint selection refuses missing identity, caller groups and incompatible modes',()=>{
 assert.deepEqual(checkpointSelection608(options,groups,groups),[groups[0]]);
 assert.deepEqual(checkpointSelection608({...options,mode:'join',group:undefined},groups,groups),groups);
 for(const change of [{sourceCommit:'a'}, {sourceExportSha256:'b'}, {mode:'cache'}, {group:'caller'}, {directory:'relative'}])
  assert.throws(()=>checkpointSelection608({...options,...change},groups,groups));
 assert.throws(()=>checkpointSelection608(options,groups.slice(1),groups));
 assert.throws(()=>checkpointSelection608({...options,mode:'join'},groups,groups));
});
test('complete private inventory rejects symlinks and detects extra, changed and missing output bytes',()=>{
 const root=fs.mkdtempSync(path.join(os.tmpdir(),'dts-checkpoint608-'));
 try {
  fs.mkdirSync(path.join(root,'dist'));fs.writeFileSync(path.join(root,'dist/index.d.ts'),'export {};');
  const inventory=checkpointInventory608(root);
  const receipt={schema:'strict542-declaration-group608-v1',status:'COMPILED_GROUP_NOT_PUBLISHED',source_commit:options.sourceCommit,source_export_sha256:options.sourceExportSha256,group:groups[0],label:'unified',generator_entry:'writer.ts',required:['index.d.ts'],identity:['policy'],record:{version:6,signature:'c'.repeat(64),inputs:['source.ts'],outputs:inventory}};
  const wanted={...receipt};delete wanted.record;
  assert.doesNotThrow(()=>validateCheckpoint608(receipt,wanted,root,()=>true,6));
  assert.throws(()=>validateCheckpoint608(receipt,wanted,root,()=>false,6),/input identity/);
  fs.writeFileSync(path.join(root,'dist/extra.d.ts'),'extra');
  assert.throws(()=>validateCheckpoint608(receipt,wanted,root,()=>true,6),/output inventory/);
  fs.unlinkSync(path.join(root,'dist/extra.d.ts'));fs.writeFileSync(path.join(root,'dist/index.d.ts'),'changed');
  assert.throws(()=>validateCheckpoint608(receipt,wanted,root,()=>true,6),/output inventory/);
  fs.unlinkSync(path.join(root,'dist/index.d.ts'));
  assert.throws(()=>validateCheckpoint608(receipt,wanted,root,()=>true,6),/output inventory/);
  fs.symlinkSync('/tmp',path.join(root,'escape'));
  assert.throws(()=>checkpointInventory608(root),/regular/);
 } finally {fs.rmSync(root,{recursive:true,force:true});}
});
test('incomplete, failed, relabelled or unsealed compiler group cannot become a join input',()=>{
 const root=fs.mkdtempSync(path.join(os.tmpdir(),'dts-checkpoint608-'));
 try {
  fs.writeFileSync(path.join(root,'output'),'x');
  const receipt={schema:'strict542-declaration-group608-v1',status:'COMPILED_GROUP_NOT_PUBLISHED',source_commit:options.sourceCommit,source_export_sha256:options.sourceExportSha256,group:groups[0],record:{version:6,signature:'c'.repeat(64),inputs:['source.ts'],outputs:checkpointInventory608(root)}};
  const wanted={...receipt};delete wanted.record;
  for(const change of [{status:'BUILT'},{source_commit:'d'.repeat(40)},{group:'caller'},{record:{...receipt.record,inputs:undefined}},{record:{...receipt.record,inputs:['../escape']}},{record:{...receipt.record,inputs:['/etc/passwd']}},{record:{...receipt.record,inputs:['source.ts','source.ts']}},{record:{...receipt.record,signature:'bad'}},{record:{...receipt.record,outputs:{'../escape':'a'.repeat(64)}}}])
   assert.throws(()=>validateCheckpoint608({...receipt,...change},wanted,root,()=>true,6));
 } finally {fs.rmSync(root,{recursive:true,force:true});}
});

test('streamed checkpoint digest covers partial and multiple chunk boundaries',()=>{
 const root=fs.mkdtempSync(path.join(os.tmpdir(),'dts-chunks608-'));
 try {
  const bytes=Buffer.alloc(2*1024*1024+37,121);bytes[1024*1024]=98;
  fs.writeFileSync(path.join(root,'large.d.ts'),bytes);
  assert.equal(checkpointInventory608(root)['large.d.ts'],createHash('sha256').update(bytes).digest('hex'));
 } finally {fs.rmSync(root,{recursive:true,force:true});}
});

const dataModule=source=>'data:text/javascript;base64,'+Buffer.from(source).toString('base64');
test('real ArtifactRecord writer/read normalization survives a declaration checkpoint roundtrip',async()=>{
 const source=fs.readFileSync(new URL('../../scripts/lib/build-artifact-cache.mts',import.meta.url),'utf8');
 // This boundary test exercises the real artifact record functions. It never
 // calls lock acquisition or compiler/toolchain resolution.
 const isolated=stripTypeScriptTypes(source).replace(/import\s*\{[^}]+\}\s*from\s*"@openclaw\/fs-safe\/file-lock";/u,
  'const acquireFileLock=()=>{throw new Error("unexpected lock")}; const acquireFileLockSync=acquireFileLock;');
 const artifacts=await import(dataModule(isolated));
 const root=fs.mkdtempSync(path.join(os.tmpdir(),'dts-record608-'));
 try {
  fs.mkdirSync(path.join(root,'data'));fs.writeFileSync(path.join(root,'data/output.d.ts'),'export {};');
  const record={version:artifacts.ARTIFACT_CACHE_VERSION,signature:'c'.repeat(64),inputs:['source.ts'],outputs:checkpointInventory608(path.join(root,'data'))};
  artifacts.writeArtifactRecord(path.join(root,'record.json'),record);
  assert.deepEqual(artifacts.readArtifactRecord(path.join(root,'record.json')),record);
  const receipt={schema:'strict542-declaration-group608-v1',status:'COMPILED_GROUP_NOT_PUBLISHED',group:groups[0],record};
  validateCheckpoint608(receipt,{schema:receipt.schema,status:receipt.status,group:receipt.group},path.join(root,'data'),()=>true,artifacts.ARTIFACT_CACHE_VERSION);
 } finally {fs.rmSync(root,{recursive:true,force:true});}
 globalThis.__declarationArtifacts608=artifacts;
});

test('actual canonical writer produces all joined sealed groups, refuses partial/tampered joins and retains original publication route',async()=>{
 const root=fs.mkdtempSync(path.join(os.tmpdir(),'dts-owner608-'));
 const originalCwd=process.cwd(),originalEnv={...process.env};
 const canonical=['openclaw-dts-base',...Array.from({length:5},(_,i)=>`openclaw-dts-extensions-${i+1}`)];
 const state={closed:false,published:0,fail:false};globalThis.__declarationState608=state;
 const artifactSource=stripTypeScriptTypes(fs.readFileSync(new URL('../../scripts/lib/build-artifact-cache.mts',import.meta.url),'utf8'))
  .replace(/import\s*\{[^}]+\}\s*from\s*"@openclaw\/fs-safe\/file-lock";/u,'const acquireFileLock=()=>{throw new Error("unexpected lock")}; const acquireFileLockSync=acquireFileLock;');
 const artifacts=await import(dataModule(artifactSource));
 globalThis.__declarationArtifacts608={...artifacts,resolveTsdownCompilerFiles:()=>[]};
 const stubs={
  './native-compiler608.mjs':'export const trustedNativeCompilerEnvironment608=(_root,env)=>({env});',
  '../tsdown-build.mts':`import fs from 'node:fs';import path from 'node:path';export const TSDOWN_DECLARATION_EXTENSIONS=['.d.ts'];export const TSDOWN_UNIFIED_CACHE_ENV=[];export const resolveStagedDeclarationConcurrency=()=>1;export const listReplaceableTsdownDeclarationOutputs=()=>[];export const prepareTsdownBuildExecution=options=>({invocations:[{args:options.args}],maxOldSpaceMb:128});export async function executeTsdownBuildPlan(plan){const s=globalThis.__declarationState608;s.closed=false;if(s.fail)return 1;for(const inv of plan.invocations){const args=inv.args,out=args[args.indexOf('--out-dir')+1],name=args[args.indexOf('--filter')+1];fs.mkdirSync(out,{recursive:true});fs.writeFileSync(path.join(out,name+'.d.ts'),'export {};');const receipt=path.join(out,'..','compiler-inputs',name+'.json');const request=JSON.parse(fs.readFileSync(receipt,'utf8'));fs.writeFileSync(receipt,JSON.stringify({...request,inputs:['src/source.ts']}));}await Promise.resolve();s.closed=true;return 0;}`,
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
  const writerPath=new URL('../../scripts/lib/tsdown-declaration-writer.mts',import.meta.url);
  let writer=stripTypeScriptTypes(fs.readFileSync(writerPath,'utf8'));
  for(const [specifier,code] of Object.entries(stubs))writer=writer.replaceAll(JSON.stringify(specifier),JSON.stringify(dataModule(code)));
  writer=writer.replaceAll(JSON.stringify('./declaration-checkpoint608.mjs'),JSON.stringify(pathToFileURL(path.resolve(originalCwd,'scripts/lib/declaration-checkpoint608.mjs')).href));
  const {writeBoundedDeclarationCheckpoint608}=await import(dataModule(writer));
  process.chdir(root);Object.assign(process.env,{OPENCLAW_608_BOUNDED_PACKAGE:'1',OPENCLAW_BUILD_CACHE:'0',STRICT542_SOURCE_COMMIT:options.sourceCommit,STRICT542_SOURCE_EXPORT_SHA256:options.sourceExportSha256});
  const opts={...options,directory:path.join(root,'checkpoints')};
  state.fail=true;await assert.rejects(writeBoundedDeclarationCheckpoint608('unified',opts),/failed/);
  assert.equal(fs.existsSync(path.join(opts.directory,opts.group)),false);state.fail=false;
  await writeBoundedDeclarationCheckpoint608('unified',opts);
  await assert.rejects(writeBoundedDeclarationCheckpoint608('unified',{...opts,mode:'join',group:undefined}));
  for(const group of canonical.slice(1))await writeBoundedDeclarationCheckpoint608('unified',{...opts,group});
  await writeBoundedDeclarationCheckpoint608('unified',{...opts,mode:'join',group:undefined});assert.equal(state.published,1);
  fs.appendFileSync(path.join(root,'src/source.ts'),'// drift');
  await assert.rejects(writeBoundedDeclarationCheckpoint608('unified',{...opts,mode:'join',group:undefined}),/input identity/);assert.equal(state.published,1);
 } finally {process.chdir(originalCwd);for(const key of Object.keys(process.env))if(!Object.hasOwn(originalEnv,key))delete process.env[key];Object.assign(process.env,originalEnv);fs.rmSync(root,{recursive:true,force:true});delete globalThis.__declarationState608;delete globalThis.__declarationArtifacts608;}
});
