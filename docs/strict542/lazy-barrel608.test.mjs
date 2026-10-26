// Runs only after pinned dependencies are installed, inside admitted offload.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
import {test} from 'node:test';
const require=createRequire(import.meta.url);
const {rolldown}=await import(pathToFileURL(require.resolve('rolldown',{paths:[path.dirname(require.resolve('tsdown'))]})).href);

test('owning config enables lazy barrels only for the complete shared runtime graph',async()=>{
  process.env.OPENCLAW_RUN_NODE_SKIP_DTS_BUILD='1';
  const {default:configs}=await import('../../tsdown.config.ts');
  const selected=configs.filter(c=>typeof c.inputOptions==='function' && c.inputOptions({})?.experimental?.lazyBarrel);
  assert.equal(selected.length,1);
  assert.equal(selected[0].dts,false);
  assert.ok(Object.keys(selected[0].entry).length>2);
  assert.equal(selected[0].inputOptions({experimental:{attachDebugInfo:'none'}}).experimental.attachDebugInfo,'none');
});

test('lazy barrels preserve side effects, live singleton identity and dynamic exports',async t=>{
  const root=await fs.mkdtemp(path.join(os.tmpdir(),'lazy608-'));
  t.after(()=>fs.rm(root,{recursive:true,force:true}));
  const files={
    'package.json':JSON.stringify({type:'module'}),
    'singleton.js':'export const state={count:0}; export function inc(){state.count++}',
    'barrel.js':'export {state,inc} from "./singleton.js"; export {unused} from "./unused.js";',
    'unused.js':'globalThis.__lazy608_effect=(globalThis.__lazy608_effect??0)+1; export const unused=1;',
    'pure/package.json':JSON.stringify({type:'module',sideEffects:false}),
    'pure/barrel.js':'export {value} from "./used.js"; export {unused} from "./unused.js";',
    'pure/used.js':'export const value=42;',
    'pure/unused.js':'export const unused="PURE_UNUSED608";',
    'dynamic.js':'export const dynamicValue=91;',
    'a.js':'export {state,inc} from "./barrel.js"; export {value} from "./pure/barrel.js"; export const load=()=>import("./dynamic.js");',
    'b.js':'export {state} from "./barrel.js";',
  };
  for (const [name,contents] of Object.entries(files)) {
    await fs.mkdir(path.dirname(path.join(root,name)),{recursive:true});
    await fs.writeFile(path.join(root,name),contents);
  }
  for (const lazyBarrel of [false,true]) {
    delete globalThis.__lazy608_effect;
    const out=path.join(root,String(lazyBarrel));
    const bundle=await rolldown({cwd:root,input:{a:'a.js',b:'b.js'},experimental:{lazyBarrel}});
    try {await bundle.write({dir:out,format:'es',entryFileNames:'[name].mjs',chunkFileNames:'[name]-[hash].mjs'});}
    finally {await bundle.close();}
    const a=await import(pathToFileURL(path.join(out,'a.mjs')).href);
    const b=await import(pathToFileURL(path.join(out,'b.mjs')).href);
    assert.equal(a.state,b.state);a.inc();assert.equal(b.state.count,1);
    assert.equal(globalThis.__lazy608_effect,1);assert.equal(a.value,42);
    assert.equal((await a.load()).dynamicValue,91);
    const output=(await Promise.all((await fs.readdir(out)).map(n=>fs.readFile(path.join(out,n),'utf8')))).join('\n');
    assert.equal(output.includes('PURE_UNUSED608'),false);
  }
  delete globalThis.__lazy608_effect;
});
