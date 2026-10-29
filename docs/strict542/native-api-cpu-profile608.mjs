// Source-only diagnostic adapter; no launch or build acceptance authority.
import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';

const LIMIT_MS = 120000;
const MAX_PROFILE_BYTES = 8 * 1024 * 1024;
const installed = new WeakSet();
const refused = () => new Error('CPU profile diagnostic refused');

function fixedStore() {
  const base = path.dirname(fileURLToPath(import.meta.url));
  const result = path.join(base,'native-api608');
  const directory = path.join(result,'cpu-profile');
  for (const ancestor of [base,result]) {
    const stat = fs.lstatSync(ancestor);
    if (!stat.isDirectory() || stat.isSymbolicLink() || fs.realpathSync.native(ancestor)!==ancestor)
      throw refused();
  }
  fs.mkdirSync(directory,{mode:0o700}); // Refuse reuse, including a symlink.
  const directoryStat = fs.lstatSync(directory);
  if (!directoryStat.isDirectory() || directoryStat.isSymbolicLink() ||
      directoryStat.uid!==process.getuid() || (directoryStat.mode & 0o777)!==0o700)
    throw refused();
  const validateDirectory = () => {
    const current=fs.lstatSync(directory);
    if (!current.isDirectory() || current.isSymbolicLink() || current.dev!==directoryStat.dev ||
        current.ino!==directoryStat.ino || current.uid!==directoryStat.uid ||
        (current.mode & 0o777)!==0o700 || fs.realpathSync.native(directory)!==directory) throw refused();
  };
  return {
    directory,
    acceptReceipt(file) {
      validateDirectory();
      if (typeof file!=='string' || !path.isAbsolute(file) || path.dirname(file)!==directory ||
          !/^\d+-\d+-cpuprofile\.pb\.gz$/u.test(path.basename(file))) throw refused();
      const fd = fs.openSync(file,fs.constants.O_RDONLY | fs.constants.O_NOFOLLOW);
      try {
        const stat = fs.fstatSync(fd);
        if (!stat.isFile() || stat.nlink!==1 || stat.uid!==process.getuid() || stat.size<=0 ||
            stat.size>MAX_PROFILE_BYTES ||
            fs.realpathSync.native(file)!==file) throw refused();
        const hash=createHash('sha256'),buffer=Buffer.alloc(64*1024);
        let bytes=0;
        while (bytes<stat.size) {
          const read=fs.readSync(fd,buffer,0,Math.min(buffer.length,stat.size-bytes),bytes);
          if (read===0) throw refused();
          hash.update(buffer.subarray(0,read));bytes+=read;
        }
        if (fs.readSync(fd,buffer,0,1,bytes)!==0) throw refused();
        const after = fs.fstatSync(fd);
        if (bytes!==stat.size || after.size!==stat.size || after.mtimeMs!==stat.mtimeMs ||
            after.ctimeMs!==stat.ctimeMs) throw refused();
        return {kind:'NATIVE_CPU_PROFILE_RECEIPT608',complete:true,profile:path.basename(file),
          sha256:hash.digest('hex'),bytes,limit_ms:LIMIT_MS,max_profile_bytes:MAX_PROFILE_BYTES};
      } finally { fs.closeSync(fd); }
    },
    writeReceipt(receipt) {
      validateDirectory();
      fs.writeFileSync(path.join(directory,'receipt.json'),JSON.stringify(receipt)+'\n',
        {flag:'wx',mode:0o600});
    },
  };
}

/** Hooks isolate timers/filesystem/reporting in tests; production supplies only api. */
export function installNativeCpuProfile608(api, hooks = {}) {
  const state = {failed:false,reason:null,receipt:null};
  const createStore = hooks.createStore ?? fixedStore;
  const schedule = hooks.setTimeout ?? setTimeout;
  const clear = hooks.clearTimeout ?? clearTimeout;
  const report = hooks.report ?? (event => process.stderr.write(JSON.stringify(event)+'\n'));
  const fail = reason => {
    if (state.failed) return;
    state.failed=true;state.reason=reason;
    // Emit immediately: a later outer timeout may kill us before beforeExit.
    try { report({kind:'NATIVE_CPU_PROFILE608',phase:'refused',reason}); } catch {}
  };
  const patches = [
    [api.API?.prototype,'createSnapshot'],
    [api.Program?.prototype,'getGlobalDiagnostics'],
  ].map(([prototype,name])=>({prototype,name,descriptor:prototype && Object.getOwnPropertyDescriptor(prototype,name)}));
  if (patches.some(({prototype,descriptor})=>!prototype || installed.has(prototype) ||
      typeof descriptor?.value!=='function' || !descriptor.writable)) throw refused();
  let owner=null, used=false;
  const snapshot=patches[0], global=patches[1];
  Object.defineProperty(snapshot.prototype,snapshot.name,{...snapshot.descriptor,value:function(...args) {
    if (!(this instanceof api.API) || (owner!==null && owner!==this)) {
      fail('ambiguous-api');throw refused();
    }
    owner=this;
    return Reflect.apply(snapshot.descriptor.value,this,args);
  }});
  Object.defineProperty(global.prototype,global.name,{...global.descriptor,value:async function(...args) {
    if (owner===null || used || state.failed || !(this instanceof api.Program)) {
      fail(owner===null?'missing-api':'overlapping-global');throw refused();
    }
    used=true;
    let store, started=false, timer, stopPromise;
    const stop = () => {
      if (!stopPromise) stopPromise=(async()=>{
        let file, receipt;
        try { file=await owner.internal.stopCPUProfile(); }
        catch { fail('profile-stop');return; }
        try { receipt=store.acceptReceipt(file); }
        catch { fail('profile-receipt');return; }
        if (state.failed) return;
        try { report({kind:'NATIVE_CPU_PROFILE608',phase:'finalized',receipt}); }
        catch { fail('profile-report');return; }
        try { store.writeReceipt(receipt); }
        catch { fail('profile-write');return; }
        state.receipt=receipt;
      })();
      return stopPromise;
    };
    try { store=createStore(); } catch { fail('profile-directory'); }
    if (store) {
      try { await owner.internal.startCPUProfile(store.directory);started=true; }
      catch { fail('profile-start'); }
    }
    if (started) {
      try { timer=schedule(()=>{void stop();},LIMIT_MS); }
      catch { fail('profile-timer'); }
    }
    let result, queryError, queryFailed=false;
    try { result=await Reflect.apply(global.descriptor.value,this,args); }
    catch (error) { queryFailed=true;queryError=error; }
    finally {
      if (timer!==undefined) {
        try { clear(timer); } catch { fail('profile-timer'); }
      }
      if (started) await stop();
    }
    if (queryFailed) throw queryError;
    if (state.failed || state.receipt===null) throw refused();
    return result;
  }});
  for (const {prototype} of patches) installed.add(prototype);
  return state;
}
