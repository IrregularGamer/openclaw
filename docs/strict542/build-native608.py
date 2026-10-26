#!/usr/bin/env python3
"""Disposable offload compiler build; invoke only inside the reviewed export."""
from pathlib import Path
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import tarfile
import sys
import urllib.request

# Reviewed split: one admitted run compiles only the addon, another runs only the
# native lib tests. Each stage returns its own receipt; neither is install authority.
STAGES = {'compile': 'NATIVE_COMPILER608_COMPILE_STAGE', 'libtests': 'NATIVE_COMPILER608_LIBTEST_STAGE', 'lifetime': 'NATIVE_COMPILER608_LIFETIME_STAGE'}
if len(sys.argv) != 2 or sys.argv[1] not in STAGES:
    raise SystemExit('native608 requires exactly one stage: compile, libtests or lifetime')
stage = sys.argv[1]
owner = Path.cwd()
root = owner.parent / '.native608'
out = owner / 'result598-native'
if root.exists() or out.exists() or (owner / '.git').exists():
    raise SystemExit('native608 requires a fresh disposable export')
for key in os.environ:
    if key.startswith(('CARGO_', 'RUST', 'NAPI_RS_', 'ROLLDOWN_')) or key in ['CC','CXX','LD','LD_PRELOAD','LD_LIBRARY_PATH']:
        raise SystemExit('native608 refuses inherited compiler control: ' + key)
pin = json.loads((owner / 'docs/strict542/rolldown-source-pin608.json').read_text())
root.mkdir()
out.mkdir()
sha = lambda path: hashlib.file_digest(Path(path).open('rb'), 'sha256').hexdigest()
receipt = {'kind':STAGES[stage], 'stage':stage, 'upstream_commit':pin['upstream_commit'],
           'source_archive_sha256':pin['source_archive_sha256'], 'rust_archive_sha256':pin['rust_archive_sha256'],
           'owner_inputs':{p:sha(owner / p) for p in ['scripts/lib/prepare-native608.py','scripts/lib/last-use-ast608.rs',
                                                     'docs/strict542/rolldown-source-pin608.json','docs/strict542/build-native608.py']},
           'cargo_policy':{'locked':True,'jobs':1,'lto':False,'codegen_units':64,'opt_level':3},'complete':False}


def save():
    (out / 'receipt.json').write_text(json.dumps(receipt, sort_keys=True) + '\n')


def extract(archive, destination):
    destination.mkdir()
    with tarfile.open(archive) as tar:
        tar.extractall(destination, filter='data')
    entries=list(destination.iterdir())
    if len(entries) != 1 or not entries[0].is_dir() or entries[0].is_symlink():
        raise ValueError('unexpected source archive root')
    return entries[0]


save()
archive=owner.parent / 'rolldown608-source.tar.gz'
if sha(archive) != pin['source_archive_sha256']:
    raise SystemExit('native source archive digest mismatch')
unpacked=extract(archive,root / 'unpacked')
unpacked.rename(root / 'source')
archive.unlink()
spec=importlib.util.spec_from_file_location('prepare608',owner / 'scripts/lib/prepare-native608.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
receipt['patched_sources']=module.prepare(root / 'source',owner)
save()

# Install an immutable official toolchain ONLY below this disposable export.
rust_archive=root / 'rust.tar.xz'
url='https://static.rust-lang.org/dist/rust-1.98.1-x86_64-unknown-linux-gnu.tar.xz'
with urllib.request.urlopen(url, timeout=60) as response, rust_archive.open('wb') as target:
    shutil.copyfileobj(response,target,1024*1024)
if sha(rust_archive) != pin['rust_archive_sha256']:
    raise SystemExit('Rust distribution digest mismatch')
rust_source=extract(rust_archive,root / 'rust-unpacked')
subprocess.run(['sh',str(rust_source / 'install.sh'),'--prefix='+str(root / 'toolchain'),
                '--components=rustc,rust-std-x86_64-unknown-linux-gnu,cargo','--disable-ldconfig'],check=True)
shutil.rmtree(root / 'rust-unpacked')
rust_archive.unlink()
# libmimalloc-sys2 (upstream default allocator) needs cmake at build time and the
# offload image has none. Use one digest-pinned official wheel, unpacked as data;
# no pip, no allocator or feature change.
cmake_pin=('https://files.pythonhosted.org/packages/59/e8/096984b89133681533650b9078c5ed1c5c9b534e869b5487f22d4de1935c/'
           'cmake-3.31.6-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl',
           '1c8b05df0602365da91ee6a3336fe57525b137706c4ab5675498f662ae1dbcec')
cmake_wheel=root / 'cmake.whl'
with urllib.request.urlopen(cmake_pin[0], timeout=60) as response, cmake_wheel.open('wb') as target:
    shutil.copyfileobj(response,target,1024*1024)
if sha(cmake_wheel) != cmake_pin[1]:
    raise SystemExit('cmake wheel digest mismatch')
import zipfile
with zipfile.ZipFile(cmake_wheel) as wheel:
    wheel.extractall(root / 'cmake-tool')
cmake_wheel.unlink()
cmake_bin=root / 'cmake-tool/cmake/data/bin'
for tool in cmake_bin.iterdir():
    tool.chmod(0o755)
receipt['cmake_wheel_sha256']=cmake_pin[1]
env={**os.environ,'PATH':str(root / 'toolchain/bin')+os.pathsep+str(cmake_bin)+os.pathsep+os.environ['PATH'],
     'CARGO_HOME':str(root / 'cargo-home'),'CARGO_BUILD_JOBS':'1',
     'CARGO_PROFILE_RELEASE_LTO':'false','CARGO_PROFILE_RELEASE_CODEGEN_UNITS':'64',
     'CARGO_PROFILE_RELEASE_DEBUG':'false','CARGO_PROFILE_RELEASE_OPT_LEVEL':'3',
     'SOURCE_DATE_EPOCH':'1792944000','TZ':'UTC','LANG':'C','LC_ALL':'C',
     'RUSTFLAGS':'--remap-path-prefix='+str(root)+'=/strict542-native608'}
receipt['rustc']=subprocess.check_output(['rustc','--version'],env=env,text=True).strip()
assert receipt['rustc'].startswith('rustc 1.98.1 ')
receipt['cmake']=subprocess.check_output(['cmake','--version'],env=env,text=True).splitlines()[0]
assert receipt['cmake']=='cmake version 3.31.6'
wrapper=root / 'lifetime-tests.rs'
helper=(owner / 'scripts/lib/last-use-ast608.rs').read_text()
wrapper.write_text('mod table {\n'+helper+'\n}\n')
subprocess.run(['rustc','--edition=2024','--test',str(wrapper),'-o',str(root / 'lifetime-tests')],env=env,check=True)
subprocess.run([str(root / 'lifetime-tests')],env=env,check=True)
receipt['lifetime_tests_exit']=0
# The same real helper tests must detect the previous retain-through-codegen
# lifetime. This mutation changes ownership release only, never expected values.
old=helper.replace('drop(value.take());','// retain unused AST until table drop').replace(
    'drop(self.values[index].take());','// retain used AST until table drop')
assert old != helper
wrapper.write_text('mod table {\n'+old+'\n}\n')
subprocess.run(['rustc','--edition=2024','--test',str(wrapper),'-o',str(root / 'lifetime-tests-old')],env=env,check=True)
result=subprocess.run([str(root / 'lifetime-tests-old')],env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(out / 'lifetime-retention-negative.log').write_text(result.stdout)
assert result.returncode != 0 and 'unused_is_released_before_first_render ... FAILED' in result.stdout
assert 'repeated_module_survives_until_last_render_then_drops_before_next_module ... FAILED' in result.stdout
receipt['retention_negative_detected']=True
save()
if stage == 'lifetime':
    # Standalone ownership tests only; never an addon or accepted lib-test stage.
    receipt['complete']=True
    save()
    shutil.rmtree(root)
    print(json.dumps(receipt,sort_keys=True))
    raise SystemExit(0)
if stage == 'compile':
    subprocess.run(['cargo','build','--locked','--release','--jobs','1','-p','rolldown_binding'],
                   cwd=root / 'source',env=env,check=True)
    addon=root / 'rolldown-binding.linux-x64-gnu.node'
    shutil.copyfile(root / 'source/target/release/librolldown_binding.so',addon)
    receipt['addon_sha256']=sha(addon)
    shutil.copyfile(addon,out / addon.name)
else:
    subprocess.run(['cargo','test','--locked','--release','--jobs','1','-p','rolldown','--lib'],
                   cwd=root / 'source',env=env,check=True)
    receipt['native_lib_tests_exit']=0
receipt['complete']=True
save()
# Ordinary lifetime of this job's consumed build inputs, never cache/cgroup control.
shutil.rmtree(root)
print(json.dumps(receipt,sort_keys=True))
