"""INC-261027-18 finite stage helper for the job608 package run.

The single run-package608.sh run (53 min) does not fit one 1h worker. The
manifest, not the caller, selects one stage; each stage is one admitted
offload of at most 40 min. Every original check runs unchanged in exactly one
stage. Later stages consume earlier stage outputs only after verifying the
manifest pins, the producing stage receipt and the independently pinned native
receipts/addon digest.
"""
import hashlib,json,shutil,sys
from pathlib import Path

STAGES={'native':[],'checks':[],'compiler':['native'],'package':['native','checks','compiler']}
OUTPUTS={'native':['native/receipt.json','native/libtests-receipt.json','native/rolldown-binding.linux-x64-gnu.node'],
         'checks':['checks/tests.log','checks/installed.json'],
         'compiler':['compiler/tests.log']}
ADDON='rolldown-binding.linux-x64-gnu.node'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()


def manifest(root):
    m=json.loads((root/'export-manifest.json').read_text())
    if m.get('stage') not in STAGES:raise ValueError('manifest selects no known stage')
    return m


def regular(p):
    if p.is_symlink() or not p.is_file():raise ValueError('stage input must be a private regular file: '+str(p))
    return p


def verify_inputs(root):
    """Exact staged input set: pinned files plus one receipt per required stage."""
    m=manifest(root);base=root/'stage608-inputs';needed=STAGES[m['stage']]
    pins=m.get('stage_inputs',{})
    expected={n+'/stage-receipt.json' for n in needed}|{o for n in needed for o in OUTPUTS[n]}
    present={str(p.relative_to(base)) for p in base.rglob('*') if p.is_file() or p.is_symlink()} if base.exists() else set()
    if set(pins)!=expected or present!=expected:raise ValueError('stage inputs differ from the exact required set')
    for name,digest in pins.items():
        if sha(regular(base/name))!=digest:raise ValueError('stage input digest mismatch: '+name)
    for n in needed:
        r=json.loads((base/n/'stage-receipt.json').read_text())
        if (r.get('kind')!='JOB608_STAGE_RECEIPT' or r.get('stage')!=n or r.get('exit_code')!=0 or
            r.get('source_commit')!=m['source_commit'] or r.get('outputs')!={o:pins[o] for o in OUTPUTS[n]}):
            raise ValueError('unaccepted producing stage receipt: '+n)
    if 'native' in needed:
        compile_bytes=(base/'native/receipt.json').read_bytes()
        if (hashlib.sha256(compile_bytes).hexdigest()!=m['native_stage_outputs']['compile/receipt.json'] or
            sha(base/'native/libtests-receipt.json')!=m['native_stage_outputs']['libtests/receipt.json'] or
            sha(base/'native'/ADDON)!=json.loads(compile_bytes)['addon_sha256']):
            raise ValueError('staged native output differs from independently pinned compile artifact')


def stage_native(root):
    """Place the verified rebuilt native outputs where nativeCompiler608 reads them."""
    target=root/'.native608';target.mkdir()
    for name in ['receipt.json','libtests-receipt.json',ADDON]:
        shutil.copyfile(root/'stage608-inputs/native'/name,target/name)


def merge_logs(root,out):
    """checks + compiler logs form the same tests.log the single run appended."""
    base=root/'stage608-inputs'
    Path(out).write_bytes((base/'checks/tests.log').read_bytes()+(base/'compiler/tests.log').read_bytes())


def receipt(root,result):
    m=manifest(root);result=Path(result)
    value={'kind':'JOB608_STAGE_RECEIPT','stage':m['stage'],'run_id':m['run_id'],'source_commit':m['source_commit'],
           'manifest_sha256':sha(root/'export-manifest.json'),'exit_code':0,
           'outputs':{o:sha(regular(result/o)) for o in OUTPUTS.get(m['stage'],[])}}
    (result/m['stage']).mkdir(exist_ok=True)
    (result/m['stage']/'stage-receipt.json').write_text(json.dumps(value,sort_keys=True)+'\n')


if __name__=='__main__':
    root=Path.cwd();command=sys.argv[1:]
    if command==['stage']:print(manifest(root)['stage'])
    elif command==['verify-inputs']:verify_inputs(root)
    elif command==['stage-native']:stage_native(root)
    elif len(command)==2 and command[0]=='merge-logs':merge_logs(root,command[1])
    elif len(command)==2 and command[0]=='receipt':receipt(root,command[1])
    else:raise SystemExit('unknown stage608 command')
