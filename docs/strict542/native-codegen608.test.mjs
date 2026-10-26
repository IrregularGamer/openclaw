import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
import {test} from 'node:test';
import {nativeCompiler608} from '../../scripts/lib/native-compiler608.mjs';
const fixture=fileURLToPath(new URL('./native-codegen608.fixture.mjs',import.meta.url));
test('native last-use codegen is byte-equal to stock for shared graphs, ESM/CJS, maps and minification',async t=>{
  const native=nativeCompiler608();assert.ok(native.receipt,'patched native compiler is required');
  const root=await fs.mkdtemp(path.join(os.tmpdir(),'native608-'));
  t.after(()=>fs.rm(root,{recursive:true,force:true}));
  const files={
    'package.json':JSON.stringify({type:'module'}),
    'singleton.ts':'export const state:{count:number}={count:0}; export function inc(){state.count++}',
    'barrel.ts':'export {state,inc} from "./singleton.ts"; export {effect} from "./effect.ts";',
    'effect.ts':'globalThis.__native608_effect=(globalThis.__native608_effect??0)+1; export const effect=true;',
    'dynamic.ts':'export const answer:number=42;',
    'legacy.cjs':'module.exports={value:17};',
    'a.ts':'import path from "node:path"; import legacy from "./legacy.cjs"; export {state,inc} from "./barrel.ts"; export const load=()=>import("./dynamic.ts"); enum E{a=3}; export const enumValue=E.a; export const fromCjs=legacy.value; export const externalName=path.basename("/synthetic/x");',
    'b.ts':'export {state} from "./barrel.ts";',
  };
  for(const [name,content] of Object.entries(files)) await fs.writeFile(path.join(root,name),content);
  const results=[];
  for(const label of ['stock','patched']) {
    const env={...process.env,ROLLDOWN_WORKER_THREADS:'1',ROLLDOWN_MAX_BLOCKING_THREADS:'1',RAYON_NUM_THREADS:'1',TOKIO_WORKER_THREADS:'1',MIMALLOC_ALLOW_THP:'0'};
    for(const key of Object.keys(env)) if (/^NAPI_RS_/iu.test(key)) delete env[key];
    if(label==='patched') Object.assign(env,native.env);
    const result=spawnSync(process.execPath,[fixture,root,label],{env,encoding:'utf8',timeout:60_000,maxBuffer:8*1024**2});
    assert.equal(result.error,undefined);assert.equal(result.signal,null);
    assert.equal(result.status,0,result.stderr);results.push(JSON.parse(result.stdout));
  }
  assert.equal(results[0].length,8);assert.deepEqual(results[1],results[0]);
  await fs.writeFile('result598-native/stock-patched-equality.json',JSON.stringify({addon_sha256:native.receipt.addon_sha256,variants:results[0]})+'\n');
});
