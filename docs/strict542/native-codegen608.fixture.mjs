// Real stock/patched Rolldown process. Only synthetic local modules are executed.
import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {createHash} from 'node:crypto';
import {pathToFileURL} from 'node:url';
const require=createRequire(import.meta.url);
const {rolldown}=await import(pathToFileURL(require.resolve('rolldown',{paths:[path.dirname(require.resolve('tsdown'))]})).href);
const root=process.argv[2];const label=process.argv[3];
assert.ok(root && ['stock','patched'].includes(label));
const results=[];
for(const format of ['es','cjs']) for(const sourcemap of [false,true]) for(const minify of [false,true]) {
  const out=path.join(root,label,`${format}-${sourcemap}-${minify}`);
  const ext=format==='es'?'.mjs':'.cjs';
  const bundle=await rolldown({cwd:root,input:{a:'a.ts',b:'b.ts'},logLevel:'silent',experimental:{lazyBarrel:true}});
  let output;
  try {({output}=await bundle.write({dir:out,format,sourcemap,minify,entryFileNames:'[name]'+ext,chunkFileNames:'[name]-[hash]'+ext}));}
  finally {await bundle.close();}
  delete globalThis.__native608_effect;
  const a=format==='es'?await import(pathToFileURL(path.join(out,'a'+ext)).href):require(path.join(out,'a'+ext));
  const b=format==='es'?await import(pathToFileURL(path.join(out,'b'+ext)).href):require(path.join(out,'b'+ext));
  assert.equal(a.state,b.state);a.inc();assert.equal(b.state.count,1);
  assert.equal(globalThis.__native608_effect,1);
  assert.equal((await a.load()).answer,42);
  assert.equal(a.fromCjs,17);assert.equal(a.enumValue,3);assert.equal(a.externalName,'x');
  results.push({format,sourcemap,minify,outputs:output.map(asset=>({fileName:asset.fileName,
    type:asset.type,hash:createHash('sha256').update(asset.type==='chunk'?asset.code:asset.source).digest('hex')})).sort((a,b)=>a.fileName.localeCompare(b.fileName))});
}
console.log(JSON.stringify(results));
