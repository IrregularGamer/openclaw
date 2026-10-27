// Source-build compiler identity only. No gateway-native or installation authority.
import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
const digest = file => createHash('sha256').update(fs.readFileSync(file)).digest('hex');
function regular(file) {
  const stat=fs.lstatSync(file);
  if (!stat.isFile() || stat.isSymbolicLink()) throw new Error('native608 requires private regular files');
}
export function nativeCompiler608(root=process.cwd(), {required=false}={}) {
  const directory=path.resolve(root,'../.native608');
  if (!fs.existsSync(directory)) {
    if (required) throw new Error('required native compiler is absent');
    return {env:{},receipt:null};
  }
  if (!fs.lstatSync(directory).isDirectory() || fs.lstatSync(directory).isSymbolicLink())
    throw new Error('invalid native compiler directory');
  const pin=JSON.parse(fs.readFileSync(path.join(root,'docs/strict542/rolldown-source-pin608.json'),'utf8'));
  const owners=['scripts/lib/prepare-native608.py','scripts/lib/last-use-ast608.rs',
    'docs/strict542/rolldown-source-pin608.json','docs/strict542/build-native608.py'];
  // The reviewed split returns one compile receipt and one lib-test receipt from
  // separate admitted runs. Both must describe the identical patched source and toolchain.
  const read=(name,kind,stage)=>{
    const file=path.join(directory,name);regular(file);
    const receipt=JSON.parse(fs.readFileSync(file,'utf8'));
    if (receipt.kind!==kind || receipt.stage!==stage || receipt.complete!==true ||
        receipt.upstream_commit!==pin.upstream_commit || receipt.source_archive_sha256!==pin.source_archive_sha256 ||
        receipt.rust_archive_sha256!==pin.rust_archive_sha256 || receipt.lifetime_tests_exit!==0 ||
        receipt.retention_negative_detected!==true || receipt.compaction_tests_exit!==0 ||
        JSON.stringify(receipt.cargo_policy)!==JSON.stringify({codegen_units:64,jobs:1,locked:true,lto:false,opt_level:3}))
      throw new Error('unaccepted native compiler receipt');
    if (JSON.stringify(Object.keys(receipt.owner_inputs ?? {}).sort())!==JSON.stringify([...owners].sort()))
      throw new Error('native compiler source inventory mismatch');
    for(const owner of owners) {
      const source=path.join(root,owner);regular(source);
      if (digest(source)!==receipt.owner_inputs[owner]) throw new Error('native compiler owner source mismatch');
    }
    return receipt;
  };
  const receipt=read('receipt.json','NATIVE_COMPILER608_COMPILE_STAGE','compile');
  const libtests=read('libtests-receipt.json','NATIVE_COMPILER608_LIBTEST_STAGE','libtests');
  if (libtests.native_lib_tests_exit!==0) throw new Error('unaccepted native lib test receipt');
  for (const key of ['patched_sources','rustc','cmake','cmake_wheel_sha256'])
    if (JSON.stringify(receipt[key])!==JSON.stringify(libtests[key]) || receipt[key]===undefined)
      throw new Error('native compiler stage receipts disagree: '+key);
  const addon=path.join(directory,'rolldown-binding.linux-x64-gnu.node');regular(addon);
  if (!/^[a-f0-9]{64}$/u.test(receipt.addon_sha256 ?? '') || digest(addon)!==receipt.addon_sha256)
    throw new Error('native compiler addon mismatch');
  return {env:{NAPI_RS_NATIVE_LIBRARY_PATH:addon},receipt};
}
