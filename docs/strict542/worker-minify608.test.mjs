// Real pinned bundler/minifier only in admitted offload with frozen dependencies.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {test} from 'node:test';
import {spawnSync} from 'node:child_process';
import {createRequire,SourceMap} from 'node:module';
import {pathToFileURL,fileURLToPath} from 'node:url';
const require=createRequire(import.meta.url);
const {rolldown}=await import(pathToFileURL(require.resolve('rolldown',{paths:[path.dirname(require.resolve('tsdown'))]})).href);
const minifier=fileURLToPath(new URL('../../scripts/minify-worker608.mjs',import.meta.url));
const policy={ROLLDOWN_WORKER_THREADS:'1',ROLLDOWN_MAX_BLOCKING_THREADS:'1',RAYON_NUM_THREADS:'1',TOKIO_WORKER_THREADS:'1',MIMALLOC_ALLOW_THP:'0'};
function minify(root,maps) {return spawnSync(process.execPath,[minifier,'worker/worker',String(maps)],{cwd:root,env:{...process.env,...policy},encoding:'utf8',timeout:30_000,maxBuffer:1024**2});}
test('real split worker retains side effects, names, dynamic imports, maps and legal text',async t=>{
 const root=await fs.mkdtemp(path.join(os.tmpdir(),'worker608-'));t.after(()=>fs.rm(root,{recursive:true,force:true}));
 await fs.writeFile(path.join(root,'entry.js'),'/*! @license synthetic608 */\nglobalThis.__worker608=(globalThis.__worker608??0)+1; export class PreservedWorkerName {} export function PreservedFunctionName(){return 42}; export const load=()=>import("./dynamic.js");');
 await fs.writeFile(path.join(root,'dynamic.js'),'export const answer=91;');
 for(const maps of [false,true]) {
  const out=path.join(root,String(maps));await fs.mkdir(out);
  const bundle=await rolldown({input:path.join(root,'entry.js'),platform:'node'});
  try {await bundle.write({dir:path.join(out,'dist/worker'),format:'es',entryFileNames:'worker.mjs',codeSplitting:false,sourcemap:maps,minify:false});}finally{await bundle.close();}
  const result=minify(out,maps);assert.equal(result.status,0,result.stderr);assert.equal(result.signal,null);
  const code=await fs.readFile(path.join(out,'dist/worker/worker.mjs'),'utf8');assert.ok(code.includes('@license synthetic608'));
  const mod=await import(pathToFileURL(path.join(out,'dist/worker/worker.mjs')).href);
  assert.equal(mod.PreservedWorkerName.name,'PreservedWorkerName');assert.equal(mod.PreservedFunctionName.name,'PreservedFunctionName');assert.equal(mod.PreservedFunctionName(),42);assert.equal((await mod.load()).answer,91);
  if(maps){const map=JSON.parse(await fs.readFile(path.join(out,'dist/worker/worker.mjs.map'),'utf8'));assert.ok(map.sources.some(s=>s.endsWith('entry.js')));assert.ok(map.mappings.length);const sm=new SourceMap(map);assert.ok(sm.findEntry(0,Math.max(0,code.indexOf('42'))).originalSource?.endsWith('entry.js'));}
 }
 assert.equal(globalThis.__worker608,2);delete globalThis.__worker608;
});
test('real minifier rejects parse failure and redirected output without replacing bytes',async t=>{
 const root=await fs.mkdtemp(path.join(os.tmpdir(),'worker608-refusal-'));t.after(()=>fs.rm(root,{recursive:true,force:true}));await fs.mkdir(path.join(root,'dist/worker'),{recursive:true});
 const file=path.join(root,'dist/worker/worker.mjs');const invalid='export const = syntax error';await fs.writeFile(file,invalid);
 assert.notEqual(minify(root,false).status,0);assert.equal(await fs.readFile(file,'utf8'),invalid);
 await fs.unlink(file);await fs.writeFile(path.join(root,'outside'),'export const x=1;');await fs.symlink(path.join(root,'outside'),file);assert.notEqual(minify(root,false).status,0);assert.equal(await fs.readFile(path.join(root,'outside'),'utf8'),'export const x=1;');
});
