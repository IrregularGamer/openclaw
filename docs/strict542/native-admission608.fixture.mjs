// Exercise the real emitter/filesystem/boundary composition with a tiny API
// driver. Compiler and seal doubles isolate admission; they prove no compiler
// correctness or successful build. Full native suites remain required remotely.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {registerHooks} from 'node:module';

const which=process.argv[2];
const scratchParent=path.resolve('.artifacts');
fs.mkdirSync(scratchParent,{recursive:true});
assert.ok(fs.lstatSync(scratchParent).isDirectory()&&!fs.lstatSync(scratchParent).isSymbolicLink());
const scratch=fs.mkdtempSync(path.join(scratchParent,'admission608-'));
const root=path.join(scratch,'source'),outside=path.join(scratch,'outside');
fs.mkdirSync(root);fs.mkdirSync(outside);
const probe=path.join(root,'probe.ts'),pkg=path.join(root,'package.json');
fs.writeFileSync(probe,'disk bytes');fs.writeFileSync(pkg,'{}');
fs.writeFileSync(path.join(root,'tsconfig.json'),'{}');
fs.writeFileSync(path.join(outside,'probe.ts'),'outside bytes');
let physical=0,custom=0,seenVirtual;
const nativeRealpath=fs.realpathSync.native;
const state=globalThis.__admission608={root,pkg,
  readText(file){return file===probe?'captured bytes':fs.readFileSync(file,'utf8');},
  async exercise(view,config){
    if(which==='lookups') {
      fs.realpathSync.native=function(file,...rest){if(file===probe)physical++;return nativeRealpath(file,...rest);};
      try {assert.equal(view.fileExists(probe),true);assert.equal(view.fileExists(probe),true);}
      finally {fs.realpathSync.native=nativeRealpath;}
    } else if(which==='policy') {
      assert.equal(view.fileExists(probe),false);
    } else if(which==='retarget'||which==='missing-retarget') {
      const local=path.join(root,'link');
      if(which==='retarget') {
        fs.symlinkSync(probe,local);assert.equal(view.fileExists(local),true);
        fs.unlinkSync(local);fs.symlinkSync(path.join(outside,'probe.ts'),local);
        assert.equal(view.fileExists(local),false);
      } else {
        fs.mkdirSync(path.join(root,'inner'));fs.symlinkSync(path.join(root,'inner'),local);
        assert.equal(view.fileExists(path.join(local,'probe.ts')),false);
        fs.unlinkSync(local);fs.symlinkSync(outside,local);
        assert.equal(view.fileExists(path.join(local,'probe.ts')),false);
      }
    } else if(which==='identity-escape') {
      const local=path.join(root,'link');fs.symlinkSync(outside,local);
      assert.equal(view.readFile(path.join(local,'probe.ts')),null);
      assert.equal(view.fileExists(path.join(local,'probe.ts')),false);
      assert.equal(view.directoryExists(local),false);
      assert.equal(view.realpath(local),local);
      assert.deepEqual(view.getAccessibleEntries(local),{files:[],directories:[]});
    } else if(which==='pinned-read') {
      assert.equal(view.readFile(probe),'captured bytes');
      seenVirtual=config;assert.match(view.readFile(config),/"extends"/);
    } else if(which==='lexical-outside') {
      const alias=path.join(outside,'inside-alias.ts');fs.symlinkSync(probe,alias);
      assert.equal(view.fileExists(alias),false);
    } else throw new Error('unknown fixture');
  }};
const modules={
  'typescript/unstable/async':`export const EmitOnly={OnlyDts:1};export class API {
    constructor(options){this.fs=options.fs;}
    async parseConfigFile(config){await globalThis.__admission608.exercise(this.fs,config);return {options:{},fileNames:[]};}
    async createSnapshot(){return {getConfiguredProject:()=>({program:{getSourceFileNames:async()=>[]}})};}
    async close(){}
  }`,
  './compiler-input-snapshot.mts':`export class CompilerInputSnapshot {
    constructor(root,policy){this.policy=policy;}
    readText=(file)=>{this.policy.assertInput?.(file);return globalThis.__admission608.readText(file);};
    signature(){return '';}
    seal(){}
  }`,
  './native-typescript-diagnostics.mts':`export async function collectNativeTypeScriptDiagnosticsAsync(){return [];}export function formatNativeTypeScriptDiagnostics(){return '';}`,
  './native-typescript-toolchain.mts':`export function nativeTypeScriptToolchainFiles(){return [];}`,
  './native-typescript.mts':`export function resolveInstalledNativeTypeScriptCompiler(){return {executable:'unused-api-driver',packageJson:globalThis.__admission608.pkg};}`,
};
const hook=registerHooks({resolve(specifier,context,next){
  if(Object.hasOwn(modules,specifier))return {url:'data:text/javascript,'+encodeURIComponent(modules[specifier]),shortCircuit:true};
  return next(specifier,context);
}});
try {
  const {compileNativeProject}=await import('../../scripts/lib/native-declaration-emitter.mts');
  const compile=()=>compileNativeProject({cwd:root,configFile:path.join(root,'tsconfig.json'),roots:[],emit:false,
    assertInput(file){if(file===probe){custom++;if(which==='policy')throw new Error('custom policy608');}return file;}});
  if(which==='policy')await assert.rejects(compile,/custom policy608/);
  else if(['retarget','missing-retarget','identity-escape'].includes(which))await assert.rejects(compile,/Declaration input escapes checkout/);
  else {
    const result=await compile();
    if(which==='lookups'){assert.equal(custom,2);assert.equal(physical,2,'one internal physical assertion per native lookup');}
    if(which==='pinned-read'){assert.ok(result.inputs.includes(probe));assert.ok(!result.inputs.includes(seenVirtual));}
  }
  console.log(JSON.stringify({case:which,physical,custom,status:'PASS'}));
} finally {hook.deregister();fs.realpathSync.native=nativeRealpath;delete globalThis.__admission608;fs.rmSync(scratch,{recursive:true,force:true});}
