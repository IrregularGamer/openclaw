import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {test} from 'node:test';
import * as nativeOwner from '../../scripts/lib/native-compiler608.mjs';
const {nativeCompiler608}=nativeOwner;
const sha=bytes=>createHash('sha256').update(bytes).digest('hex');
import {fixture} from './native-compiler608-fixture.mjs';
test('accepts matching compile and lib-test stage receipts with the pinned addon',t=>{
  const root=fixture(t);const native=nativeCompiler608(root);
  assert.equal(native.env.NAPI_RS_NATIVE_LIBRARY_PATH,path.join(root,'../.native608/rolldown-binding.linux-x64-gnu.node'));
});
test('required native compiler refuses absence while diagnostic stock mode stays explicit',t=>{
  const base=fs.mkdtempSync(path.join(os.tmpdir(),'compiler608-absent-'));
  t.after(()=>fs.rmSync(base,{recursive:true,force:true}));
  const root=path.join(base,'source');fs.mkdirSync(root);
  assert.deepEqual(nativeCompiler608(root),{env:{},receipt:null});
  assert.throws(()=>nativeCompiler608(root,{required:true}),/required native compiler/u);
  assert.ok(nativeCompiler608(fixture(t),{required:true}).receipt);
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
    [r=>{delete r.compile.compaction_tests_exit;},/unaccepted/u],
    [r=>{r.libtests.compaction_tests_exit=1;},/unaccepted/u],
    [r=>{r.compile.owner_inputs['docs/strict542/build-native608.py']='0'.repeat(64);},/owner source mismatch/u],
    [(r,dir)=>{r.compile.addon_sha256=sha(Buffer.from('other'));},/addon mismatch/u],
  ];
  for(const [mutate,error] of cases) assert.throws(()=>nativeCompiler608(fixture(t,mutate)),error);
});

test('trusted native environment derives required bytes without mutating the caller',t=>{
  const root=fixture(t), env={PATH:'/fixed/bin',OPENCLAW_BUILD_CACHE:'0'};
  const before={...env};
  const result=nativeOwner.trustedNativeCompilerEnvironment608(root,env);
  assert.deepEqual(env,before);
  assert.deepEqual(result.env,{...env,...nativeCompiler608(root,{required:true}).env});
  assert.equal(result.receipt.complete,true);
});
test('parent refuses native controls and child accepts only the exact validated addon',t=>{
  const root=fixture(t), trusted=nativeCompiler608(root,{required:true}).env;
  for (const value of ['', '/other/addon.node',trusted.NAPI_RS_NATIVE_LIBRARY_PATH])
    assert.throws(()=>nativeOwner.trustedNativeCompilerEnvironment608(root,{NAPI_RS_NATIVE_LIBRARY_PATH:value}),/native compiler control/u);
  assert.deepEqual(nativeOwner.trustedNativeCompilerEnvironment608(root,trusted,{inherited:true}).env,trusted);
  for (const env of [{NAPI_RS_NATIVE_LIBRARY_PATH:''},{NAPI_RS_NATIVE_LIBRARY_PATH:'/other/addon.node'},
      {...trusted,NAPI_RS_FORCE_WASI:''},{...trusted,NAPI_RS_LOG:'debug'}])
    assert.throws(()=>nativeOwner.trustedNativeCompilerEnvironment608(root,env,{inherited:true}),/native compiler control/u);
});
test('trusted child revalidates bytes and cannot fall back when the required compiler disappears',t=>{
  const root=fixture(t), inherited=nativeCompiler608(root,{required:true}).env;
  fs.appendFileSync(inherited.NAPI_RS_NATIVE_LIBRARY_PATH,'changed');
  assert.throws(()=>nativeOwner.trustedNativeCompilerEnvironment608(root,inherited,{inherited:true}),/addon mismatch/u);
  fs.rmSync(path.join(root,'../.native608'),{recursive:true});
  assert.throws(()=>nativeOwner.trustedNativeCompilerEnvironment608(root,{}, {inherited:true}),/required native compiler/u);
});
