#!/usr/bin/env python3
"""One finite, source-only diagnostic of the accepted 5f unified-0 boundary.

Run only in a fresh admitted export. Instrumentation is disposable and cannot
produce an accepted checkpoint, package receipt, or installation authority.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

FREEZE = '5f7d810b7f254e4f06dbf7761b557ba90bf1a2b0'
PINS = {
    'native-declaration-emitter.mts': '8e1ba4705f959b85a7330494bc8ad60a0b17a6d059f75feed2e2d5a446c50927',
    'native-typescript-diagnostics.mts': 'b9b5ca10a73e3eb93ebfdc3aa90eeae5b952f615b76851dc5e96b0108a4ed15c',
}

PROFILER = r'''
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { Worker } from 'node:worker_threads';
import childProcess from 'node:child_process';
import { syncBuiltinESMExports } from 'node:module';
const self=fileURLToPath(import.meta.url),output=path.join(path.dirname(self),'result608-unified-0/profiles');
fs.mkdirSync(output,{recursive:true});
// Observe every actual Node compiler child, without changing its environment,
// source files, command selection, cancellation/settlement, or admission policy.
const spawn=childProcess.spawn;
childProcess.spawn=function(command,args,options){
 if(command!==process.execPath)return spawn.apply(this,arguments);
 const argv=Array.isArray(args)?args:[],settings=(Array.isArray(args)||args==null)?options:args;
 const observed=argv.includes(self)?argv:['--import',self,...argv];
 return spawn.call(this,command,observed,settings);
};
syncBuiltinESMExports();
const worker=new Worker(new URL('./profiler-worker608.cjs',import.meta.url),{execArgv:[],workerData:{output}});
await new Promise((resolve,reject)=>{worker.once('error',reject);worker.once('message',message=>message==='ready'?resolve():reject(new Error(String(message))));});
worker.on('error',error=>{console.error('DIAGNOSTIC_PROFILE_ERROR608',String(error));process.exitCode=1;});
worker.on('message',message=>{if(message?.error){console.error('DIAGNOSTIC_PROFILE_ERROR608',message.error);process.exitCode=1;}});
worker.unref();
console.error('DIAGNOSTIC_PROFILER608',process.pid,Date.now());
process.once('beforeExit',()=>{worker.ref();worker.postMessage('stop');});
'''


PROFILE_WORKER = r'''
const fs=require('node:fs'),path=require('node:path');
const {parentPort,workerData}=require('node:worker_threads');
const {Session}=require('node:inspector');
const session=new Session();session.connectToMainThread();
const post=(name,args={})=>new Promise((resolve,reject)=>session.post(name,args,(error,result)=>error?reject(error):resolve(result)));
let running=false,stopping=false,index=0,timer,chain=Promise.resolve();
async function capture(restart){
 if(running){const {profile}=await post('Profiler.stop');running=false;fs.writeFileSync(path.join(workerData.output,`node-${process.pid}-${index++}.cpuprofile`),JSON.stringify(profile));}
 if(restart&&!stopping){await post('Profiler.start');running=true;}
}
function fail(error){parentPort.postMessage({error:String(error)});clearInterval(timer);session.disconnect();parentPort.close();process.exitCode=1;}
// Keep the worker alive while inspector commands to the busy main thread settle.
parentPort.on('message',message=>{
 if(message!=='stop'||stopping)return;
 stopping=true;clearInterval(timer);
 chain=chain.then(()=>capture(false)).then(()=>{session.disconnect();parentPort.close();}).catch(fail);
});
(async()=>{
 await post('Profiler.enable');await post('Profiler.setSamplingInterval',{interval:10000});await post('Profiler.start');running=true;
 timer=setInterval(()=>{chain=chain.then(()=>capture(true)).catch(fail);},60000);
 parentPort.postMessage('ready');
})().catch(fail);
'''


def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('diagnostic source boundary changed: ' + old[:80])
    return text.replace(old, new, 1)


def sample():
    processes = []
    for entry in Path('/proc').iterdir():
        if not entry.name.isdecimal():
            continue
        try:
            # No command lines or environment: only pid/name/state/CPU/RSS/wait.
            stat = (entry/'stat').read_text()
            tail = stat[stat.rindex(')')+2:].split()
            processes.append({'pid':int(entry.name),'name':stat[stat.index('(')+1:stat.rindex(')')],
                              'state':tail[0],'ppid':int(tail[1]),'utime':int(tail[11]),
                              'stime':int(tail[12]),'rss_pages':int(tail[21]),
                              'wchan':(entry/'wchan').read_text().strip()})
        except (OSError, ValueError, IndexError):
            continue
    counters = {}
    for name in ['cpu.stat','memory.current','memory.peak','memory.events','memory.pressure','cpu.pressure']:
        counters[name] = (Path('/sys/fs/cgroup')/name).read_text()
    return {'at':time.time(),'processes':processes,'cgroup':counters}


def main():
    if sys.argv[1:]:
        raise ValueError('no caller-selected diagnostic command')
    manifest = json.loads(Path('export-manifest.json').read_text())
    if manifest['source_commit'] != FREEZE or manifest['stage'] != 'unified-0':
        raise ValueError('diagnostic requires frozen unified-0')
    runner = Path('run608.sh').read_bytes()
    if hashlib.sha256(runner).hexdigest() != manifest['runner_sha256']:
        raise ValueError('runner pin mismatch')
    script = once(runner.decode(), 'sh docs/strict542/run-build-stage608.sh "$STAGE"', 'sh ../diagnostic-build608.sh "$STAGE"')
    script = once(script, 'python3 stage608.py archive-build "$RESULT"', 'echo DIAGNOSTIC_ONLY_NO_CHECKPOINT608')
    script = once(script, 'python3 stage608.py receipt "$RESULT"', 'echo DIAGNOSTIC_ONLY_NO_STAGE_RECEIPT608')
    Path('diagnostic-inner608.sh').write_text(script)
    Path('profiler608.mjs').write_text(PROFILER)
    Path('profiler-worker608.cjs').write_text(PROFILE_WORKER)
    # Keep all inventoried source bytes pristine. Only the external launch gains
    # an observer preload; the existing build gates/owner remain the entry point.
    Path('diagnostic-build608.sh').write_text('''set -eu
python3 - <<'PRISTINE'
import hashlib
from pathlib import Path
pins = ''' + repr(PINS) + '''
for name,digest in pins.items():
 p=Path('scripts/lib')/name
 assert not p.is_symlink() and hashlib.sha256(p.read_bytes()).hexdigest()==digest,name
p=Path('docs/strict542/run-build-stage608.sh')
s=p.read_text()
a='node --import ./scripts/tsx.mjs scripts/build-checkpoint608-owned.mjs "$STAGE"'
b='node --import ../profiler608.mjs --import ./scripts/tsx.mjs scripts/build-checkpoint608-owned.mjs "$STAGE"'
assert s.count(a)==1
Path('../diagnostic-launch608.sh').write_text(s.replace(a,b))
PRISTINE
timeout -k 15s 600s sh ../diagnostic-launch608.sh "$1"
''')
    result = Path('diagnostic608')
    result.mkdir()
    started = time.time()
    with (result/'runner.log').open('w') as log, (result/'samples.jsonl').open('w') as stats:
        child = subprocess.Popen(['sh','diagnostic-inner608.sh'],stdout=log,stderr=subprocess.STDOUT)
        while child.poll() is None:
            stats.write(json.dumps(sample(),sort_keys=True)+'\n');stats.flush()
            time.sleep(10)
        rc = child.wait()
    outcome = Path('result608-unified-0')
    if outcome.exists():
        outcome.rename(result/'unified-0')
    receipt = {'kind':'DIAGNOSTIC_ONLY_NOT_BUILD_RECEIPT608','source_commit':FREEZE,
               'source_export_sha256':manifest['source_export_sha256'],'command_exit':rc,
               'elapsed_seconds':time.time()-started,'compiler_wall_limit_seconds':600,
               'purpose':'phase/CPU/wait diagnosis only; no checkpoint/package/install authority'}
    (result/'diagnostic.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt),flush=True)
    # A deliberate finite timeout is evidence. Other failures are real failures.
    if rc not in (0,124):
        raise SystemExit(rc)


if __name__ == '__main__':
    main()
