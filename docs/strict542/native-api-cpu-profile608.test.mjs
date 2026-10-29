import assert from 'node:assert/strict';
import test from 'node:test';
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {installNativeCpuProfile608} from './native-api-cpu-profile608.mjs';

const turn = () => new Promise(resolve => setImmediate(resolve));
const deferred = () => {
  let resolve, reject;
  const promise = new Promise((yes, no) => { resolve = yes; reject = no; });
  return {promise, resolve, reject};
};
function fixture(options = {}) {
  const calls = [], timers = [], reports = [];
  const receipt = {kind:'NATIVE_CPU_PROFILE_RECEIPT608',complete:true,
    profile:'123-456-cpuprofile.pb.gz',sha256:'a'.repeat(64),bytes:42,limit_ms:120000};
  class API {
    constructor() { this.internal = {
      async startCPUProfile(directory) { calls.push(['start',directory]); if(options.startError) throw options.startError; },
      async stopCPUProfile() { calls.push(['stop']); if(options.stopError) throw options.stopError; return '/fixed/123-456-cpuprofile.pb.gz'; },
    }; }
    createSnapshot(...args) { calls.push(['snapshot',this,args]); return {snapshot:true}; }
  }
  class Program {
    getGlobalDiagnostics(...args) {
      calls.push(['query',this,args]);
      return options.query ? options.query() : [];
    }
  }
  const store = {directory:'/fixed',
    acceptReceipt(file) { calls.push(['accept',file]); if(options.receiptError) throw options.receiptError; return receipt; },
    writeReceipt(value) { calls.push(['write',value]); if(options.writeError) throw options.writeError; },
  };
  const state = installNativeCpuProfile608({API,Program}, {
    createStore() {calls.push(['store']);if(options.storeError) throw options.storeError;return store;},
    setTimeout(callback,delay) { const timer = {callback,delay}; timers.push(timer); return timer; },
    clearTimeout(timer) { calls.push(['clear',timer]); },
    report(event) { reports.push(event); if(options.reportError) throw options.reportError; },
  });
  const api = new API(), program = new Program();
  return {API,Program,api,program,state,calls,timers,reports,receipt};
}
const count = (f,name) => f.calls.filter(call=>call[0]===name).length;

test('install and snapshot capture do not create a store; first global creates it once',async()=>{
  const f=fixture();assert.equal(count(f,'store'),0);
  f.api.createSnapshot();assert.equal(count(f,'store'),0);
  await f.program.getGlobalDiagnostics();assert.equal(count(f,'store'),1);
});

test('fixed timer stops and finalizes while genuine global query remains unresolved', async()=>{
  const work=deferred(), f=fixture({query:()=>work.promise}), result={diagnostics:[]};
  const snapshotArgs=[{openProjects:['config']}];
  const snapshot=f.api.createSnapshot(...snapshotArgs);
  assert.deepEqual(snapshot,{snapshot:true});
  assert.deepEqual(f.calls[0],['snapshot',f.api,snapshotArgs]);
  const args=[{query:'global'},17];
  const pending=f.program.getGlobalDiagnostics(...args);
  await turn();
  assert.equal(count(f,'query'),1);
  assert.deepEqual(f.calls.find(call=>call[0]==='query'),['query',f.program,args]);
  assert.equal(f.timers[0].delay,120000);
  f.timers[0].callback();
  await turn();
  assert.equal(count(f,'stop'),1);
  assert.equal(f.state.receipt,f.receipt);
  assert.equal(count(f,'write'),1);
  work.resolve(result);
  assert.equal(await pending,result);
  assert.equal(count(f,'stop'),1);
  assert.equal(count(f,'clear'),1);
  assert.equal(f.state.failed,false);
});

test('early result clears timer and stops exactly once', async()=>{
  const result=[], f=fixture({query:()=>result});f.api.createSnapshot();
  assert.equal(await f.program.getGlobalDiagnostics(),result);
  assert.equal(count(f,'query'),1);assert.equal(count(f,'stop'),1);assert.equal(count(f,'clear'),1);
});

test('genuine rejection object survives profiling failure', async()=>{
  const original={original:true}, f=fixture({query:()=>Promise.reject(original),stopError:Error('stop')});
  f.api.createSnapshot();
  await assert.rejects(f.program.getGlobalDiagnostics(),error=>error===original);
  assert.equal(count(f,'query'),1);assert.equal(count(f,'stop'),1);assert.equal(f.state.failed,true);
  assert.equal(f.state.receipt,null);
});

test('early genuine rejection stops once and preserves the same error object',async()=>{
  const original=Error('original'),f=fixture({query:()=>Promise.reject(original)});f.api.createSnapshot();
  await assert.rejects(f.program.getGlobalDiagnostics(),error=>error===original);
  assert.equal(count(f,'query'),1);assert.equal(count(f,'stop'),1);assert.equal(count(f,'clear'),1);
  assert.equal(f.state.receipt,f.receipt);
});

test('timer and query completion race joins one stop', async()=>{
  const work=deferred(),f=fixture({query:()=>work.promise});f.api.createSnapshot();
  const pending=f.program.getGlobalDiagnostics();await turn();
  f.timers[0].callback();work.resolve('done');
  assert.equal(await pending,'done');assert.equal(count(f,'stop'),1);assert.equal(count(f,'write'),1);
});

for(const field of ['storeError','startError','stopError','receiptError','writeError','reportError']) {
  test(`${field} refuses diagnostic success but calls original query once`,async()=>{
    const f=fixture({[field]:Error(field)});f.api.createSnapshot();
    await assert.rejects(f.program.getGlobalDiagnostics(),/CPU profile diagnostic refused/);
    assert.equal(count(f,'query'),1);assert.equal(f.state.failed,true);assert.equal(f.state.receipt,null);
    assert.equal(count(f,'stop'),['storeError','startError'].includes(field)?0:1);
  });
}

test('failed start preserves a genuine synchronous query failure',async()=>{
  const original=Error('query'),f=fixture({startError:Error('start'),query(){throw original;}});
  f.api.createSnapshot();await assert.rejects(f.program.getGlobalDiagnostics(),error=>error===original);
  assert.equal(count(f,'query'),1);assert.equal(f.state.failed,true);
});

test('overlap refuses and poisons diagnostic acceptance without a second original query',async()=>{
  const work=deferred(),f=fixture({query:()=>work.promise});f.api.createSnapshot();
  const pending=f.program.getGlobalDiagnostics();await turn();
  await assert.rejects(f.program.getGlobalDiagnostics(),/CPU profile diagnostic refused/);
  work.resolve([]);await assert.rejects(pending,/CPU profile diagnostic refused/);
  assert.equal(count(f,'query'),1);assert.equal(count(f,'stop'),1);assert.equal(f.state.failed,true);
});

test('late API ambiguity immediately reports refusal after a timer receipt, preserving the original failure',async()=>{
  const work=deferred(),original=Error('genuine original failure'),f=fixture({query:()=>work.promise});
  f.api.createSnapshot();const pending=f.program.getGlobalDiagnostics();await turn();
  f.timers[0].callback();await turn();assert.equal(f.state.receipt,f.receipt);
  assert.throws(()=>new f.API().createSnapshot(),/CPU profile diagnostic refused/);
  assert.deepEqual(f.reports.filter(event=>event.phase==='refused'),[
    {kind:'NATIVE_CPU_PROFILE608',phase:'refused',reason:'ambiguous-api'},
  ]);
  await assert.rejects(f.program.getGlobalDiagnostics(),/CPU profile diagnostic refused/);
  assert.equal(f.reports.filter(event=>event.phase==='refused').length,1);
  work.reject(original);await assert.rejects(pending,error=>error===original);
  assert.equal(count(f,'query'),1);assert.equal(count(f,'stop'),1);assert.equal(f.state.failed,true);
});

test('a second API owner refuses without replacing the captured genuine owner',async()=>{
  const f=fixture();f.api.createSnapshot();
  assert.throws(()=>new f.API().createSnapshot(),/CPU profile diagnostic refused/);
  assert.equal(count(f,'snapshot'),1);assert.equal(f.state.failed,true);
});

test('global before a captured API owner refuses',async()=>{
  const f=fixture();await assert.rejects(f.program.getGlobalDiagnostics(),/CPU profile diagnostic refused/);
  assert.equal(count(f,'query'),0);assert.equal(f.state.failed,true);
});

test('production store refuses a symlink at the fixed profile directory',async()=>{
  const root=fs.mkdtempSync(path.join('/var/tmp','cpu608-test-'));
  try {
    fs.copyFileSync(new URL('./native-api-cpu-profile608.mjs',import.meta.url),path.join(root,'adapter.mjs'));
    fs.mkdirSync(path.join(root,'native-api608'));fs.mkdirSync(path.join(root,'elsewhere'));
    fs.symlinkSync(path.join(root,'elsewhere'),path.join(root,'native-api608/cpu-profile'));
    const module=await import(pathToFileURL(path.join(root,'adapter.mjs')).href);
    class API {createSnapshot(){return {};}}
    let queried=0;
    class Program {getGlobalDiagnostics(){queried++;return [];}}
    const state=module.installNativeCpuProfile608({API,Program});
    const api=new API();api.createSnapshot();
    await assert.rejects(new Program().getGlobalDiagnostics(),/CPU profile diagnostic refused/);
    assert.equal(queried,1);assert.equal(state.failed,true);
  } finally {fs.rmSync(root,{recursive:true,force:true});}
});

async function productionFixture(run) {
  const root=fs.mkdtempSync(path.join('/var/tmp','cpu608-store-'));
  try {
    fs.copyFileSync(new URL('./native-api-cpu-profile608.mjs',import.meta.url),path.join(root,'adapter.mjs'));
    fs.mkdirSync(path.join(root,'native-api608'));
    const module=await import(pathToFileURL(path.join(root,'adapter.mjs')).href);
    let directory;
    class API {
      constructor() { this.internal={
        async startCPUProfile(value) {directory=value;},
        async stopCPUProfile() {return run.stop(directory,root);},
      }; }
      createSnapshot() {return {};}
    }
    class Program {getGlobalDiagnostics() {return ['original'];}}
    const state=module.installNativeCpuProfile608({API,Program},{report(){}});
    const api=new API();api.createSnapshot();
    await run.check({root,state,program:new Program(),directory:()=>directory});
  } finally {fs.rmSync(root,{recursive:true,force:true});}
}

test('production store publishes only the finalized fixed-directory bytes and their hash',async()=>{
  await productionFixture({
    stop(directory) {const file=path.join(directory,'123-456-cpuprofile.pb.gz');fs.writeFileSync(file,'abc');return file;},
    async check({root,state,program}) {
      assert.deepEqual(await program.getGlobalDiagnostics(),['original']);
      const directory=path.join(root,'native-api608/cpu-profile');
      const receipt=JSON.parse(fs.readFileSync(path.join(directory,'receipt.json')));
      assert.equal(receipt.profile,'123-456-cpuprofile.pb.gz');assert.equal(receipt.bytes,3);
      assert.equal(receipt.sha256,'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad');
      assert.equal(receipt.max_profile_bytes,8*1024*1024);
      assert.deepEqual(state.receipt,receipt);assert.equal(fs.statSync(directory).mode & 0o777,0o700);
      assert.equal(fs.statSync(path.join(directory,'receipt.json')).mode & 0o777,0o600);
    },
  });
});

for(const fault of ['outside','empty','missing','symlink','hardlink','replaced-directory','over-cap']) {
  test(`production store refuses ${fault} profile evidence`,async()=>{
    await productionFixture({
      stop(directory,root) {
        const file=path.join(directory,'123-456-cpuprofile.pb.gz'),outside=path.join(root,'outside');
        if(fault==='outside') {fs.writeFileSync(outside,'abc');return outside;}
        if(fault==='missing') return undefined;
        if(fault==='empty') {fs.writeFileSync(file,'');return file;}
        if(fault==='symlink') {fs.writeFileSync(outside,'abc');fs.symlinkSync(outside,file);return file;}
        if(fault==='hardlink') {fs.writeFileSync(outside,'abc');fs.linkSync(outside,file);return file;}
        if(fault==='over-cap') {const fd=fs.openSync(file,'wx');try{fs.ftruncateSync(fd,8*1024*1024+1);}finally{fs.closeSync(fd);}return file;}
        fs.renameSync(directory,directory+'.saved');fs.mkdirSync(directory,{mode:0o700});
        fs.writeFileSync(file,'abc');return file;
      },
      async check({root,state,program}) {
        await assert.rejects(program.getGlobalDiagnostics(),/CPU profile diagnostic refused/);
        assert.equal(state.failed,true);assert.equal(state.receipt,null);
        assert.equal(fs.existsSync(path.join(root,'native-api608/cpu-profile/receipt.json')),false);
      },
    });
  });
}
