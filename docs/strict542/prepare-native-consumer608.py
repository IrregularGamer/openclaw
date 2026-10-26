#!/usr/bin/env python3
"""Build the diagnostic addon from source in this admitted export; no binary input."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys


def prepare(owner):
    owner=Path(owner).resolve()
    inputs=owner.parent/'native608-stages'
    manifest=json.loads((owner.parent/'export-manifest.json').read_text())
    expected=manifest['native_stage_outputs']
    names={'compile/receipt.json','libtests/receipt.json'}
    if set(expected) != names:
        raise ValueError('source-only consumer accepts exactly two receipt inputs')
    if inputs.is_symlink() or not inputs.is_dir():
        raise ValueError('receipt input directory required')
    actual={p.relative_to(inputs).as_posix() for p in inputs.rglob('*') if not p.is_dir()}
    if actual != names or any(p.is_symlink() for p in inputs.rglob('*')):
        raise ValueError('source-only consumer refuses binary or redirected inputs')
    receipts={}
    for name in sorted(names):
        path=inputs/name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=expected[name]:
            raise ValueError('stage receipt digest mismatch: '+name)
        receipts[name.split('/')[0]]=json.loads(path.read_bytes())
    compile_receipt=receipts['compile'];tests=receipts['libtests']
    if (compile_receipt.get('kind')!='NATIVE_COMPILER608_COMPILE_STAGE' or
        compile_receipt.get('stage')!='compile' or compile_receipt.get('complete') is not True or
        tests.get('kind')!='NATIVE_COMPILER608_LIBTEST_STAGE' or tests.get('stage')!='libtests' or
        tests.get('complete') is not True or tests.get('native_lib_tests_exit')!=0):
        raise ValueError('completed compile and native lib-test receipts required')
    for key in ['owner_inputs','patched_sources','cargo_policy','rustc','cmake','cmake_wheel_sha256',
                'upstream_commit','source_archive_sha256','rust_archive_sha256',
                'lifetime_tests_exit','retention_negative_detected']:
        if key not in compile_receipt or compile_receipt[key]!=tests.get(key):
            raise ValueError('stage receipt source/toolchain mismatch: '+key)
    # Same reviewed build recipe, toolchain, source and hard lease. No uploaded
    # addon, cargo target/cache, toolchain binary or dependency tree is consumed.
    subprocess.run([sys.executable,str(owner/'docs/strict542/build-native608.py'),'compile'],
                   cwd=owner,check=True)
    output=owner/'result598-native'
    rebuilt=json.loads((output/'receipt.json').read_bytes())
    addon=output/'rolldown-binding.linux-x64-gnu.node'
    if rebuilt!=compile_receipt or hashlib.sha256(addon.read_bytes()).hexdigest()!=compile_receipt['addon_sha256']:
        raise ValueError('native source rebuild differs from independently pinned compile artifact')
    target=owner.parent/'.native608';target.mkdir()
    shutil.copyfile(output/'receipt.json',target/'receipt.json')
    shutil.copyfile(addon,target/addon.name)
    shutil.copyfile(inputs/'libtests/receipt.json',target/'libtests-receipt.json')


if __name__=='__main__':
    if len(sys.argv)!=1:raise SystemExit('native consumer accepts no arguments')
    prepare(Path.cwd())
