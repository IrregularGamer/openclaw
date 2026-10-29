// Preload only in a reviewed diagnostic launch, AFTER frozen package install.
// This file lives outside inventoried source and must never authorize a receipt.
import fs from 'node:fs';
import path from 'node:path';
import childProcess from 'node:child_process';
import {createRequire,syncBuiltinESMExports} from 'node:module';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {observeNativeApi608,propagateNativeObserver608} from './native-api-phases608.mjs';
import {installNativeCpuProfile608} from './native-api-cpu-profile608.mjs';
const root=fs.realpathSync.native(process.cwd());
const require=createRequire(path.join(root,'package.json'));
const resolved=require.resolve('typescript/unstable/async');
const inside=file=>{const relative=path.relative(root,file);return relative!=='..'&&!relative.startsWith('..'+path.sep)&&!path.isAbsolute(relative);};
if(!inside(resolved)||!inside(fs.realpathSync.native(resolved)))throw new Error('native observer requires physical checkout API');
const api=await import(pathToFileURL(resolved).href);
const observation=observeNativeApi608(api);
const cpuProfile=installNativeCpuProfile608(api);
process.once('beforeExit',()=>{
 if(cpuProfile.failed){
  if(!process.exitCode)process.exitCode=1;
  try{process.stderr.write('NATIVE_CPU_PROFILE_REFUSED608\n');}catch{}
 }
 if(observation.failed){
  if(!process.exitCode)process.exitCode=1;
  try{process.stderr.write('NATIVE_API_OBSERVER_REFUSED608\n');}catch{}
 }
});
propagateNativeObserver608(childProcess,fileURLToPath(import.meta.url));
syncBuiltinESMExports();
