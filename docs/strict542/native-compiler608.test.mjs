import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {test} from 'node:test';
import {nativeCompiler608} from '../../scripts/lib/native-compiler608.mjs';
const owners=['scripts/lib/prepare-native608.py','scripts/lib/last-use-ast608.rs',
  'docs/strict542/rolldown-source-pin608.json','docs/strict542/build-native608.py'];
const sha=bytes=>createHash('sha256').update(bytes).digest('hex');
function fixture(t,mutate=()=>{}) {
  const base=fs.mkdtempSync(path.join(os.tmpdir(),'compiler608-'));t.after(()=>fs.rmSync(base,{recursive:true,force:true}));
  const root=path.join(base,'source');
  for(const owner of owners){fs.mkdirSync(path.dirname(path.join(root,owner)),{recursive:true});fs.copyFileSync(owner,path.join(root,owner));}
  const pin=JSON.parse(fs.readFileSync('docs/strict542/rolldown-source-pin608.json','utf8'));
  const dir=path.join(base,'.native608');fs.mkdirSync(dir);
  const addon=Buffer.from('addon608');fs.writeFileSync(path.join(dir,'rolldown-binding.linux-x64-gnu.node'),addon);
  const common={upstream_commit:pin.upstream_commit,source_archive_sha256:pin.source_archive_sha256,rust_archive_sha256:pin.rust_archive_sha256,
    owner_inputs:Object.fromEntries(owners.map(o=>[o,sha(fs.readFileSync(o))])),cargo_policy:{codegen_units:64,jobs:1,locked:true,lto:false,opt_level:3},
    lifetime_tests_exit:0,retention_negative_detected:true,complete:true,patched_sources:{a:'1'},rustc:'rustc 1.98.1 x',cmake:'cmake version 3.31.6',cmake_wheel_sha256:'c'};
  const receipts={compile:{...common,kind:'NATIVE_COMPILER608_COMPILE_STAGE',stage:'compile',addon_sha256:sha(addon)},
    libtests:{...common,kind:'NATIVE_COMPILER608_LIBTEST_STAGE',stage:'libtests',native_lib_tests_exit:0}};
  mutate(receipts,dir);
  if(receipts.compile) fs.writeFileSync(path.join(dir,'receipt.json'),JSON.stringify(receipts.compile));
  if(receipts.libtests) fs.writeFileSync(path.join(dir,'libtests-receipt.json'),JSON.stringify(receipts.libtests));
  return root;
}
test('accepts matching compile and lib-test stage receipts with the pinned addon',t=>{
  const root=fixture(t);const native=nativeCompiler608(root);
  assert.equal(native.env.NAPI_RS_NATIVE_LIBRARY_PATH,path.join(root,'../.native608/rolldown-binding.linux-x64-gnu.node'));
});
test('refuses missing, swapped, failed or disagreeing stage receipts and a changed addon',t=>{
  const cases=[
    [r=>{delete r.libtests;},/ENOENT/u],
    [r=>{r.libtests.native_lib_tests_exit=1;},/lib test/u],
    [r=>{delete r.libtests.native_lib_tests_exit;},/lib test/u],
    [r=>{[r.compile,r.libtests]=[r.libtests,r.compile];},/unaccepted/u],
    [r=>{r.libtests.patched_sources={a:'2'};},/disagree: patched_sources/u],
    [r=>{r.libtests.rustc='rustc 1.98.1 y';},/disagree: rustc/u],
    [r=>{r.compile.retention_negative_detected=false;},/unaccepted/u],
    [r=>{r.compile.owner_inputs['docs/strict542/build-native608.py']='0'.repeat(64);},/owner source mismatch/u],
    [(r,dir)=>{r.compile.addon_sha256=sha(Buffer.from('other'));},/addon mismatch/u],
  ];
  for(const [mutate,error] of cases) assert.throws(()=>nativeCompiler608(fixture(t,mutate)),error);
});
