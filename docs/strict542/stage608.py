"""INC-261027-18 finite stage helper for the job608 package run.

The manifest selects one admitted finite stage. Canonical declaration groups
compile separately; only their existing owner may join and publish them. Each
consumer verifies exact producing receipts, common source/export identity,
all output digests and independently pinned native receipts/addon bytes.
"""
import hashlib,json,shutil,sys,tarfile
from pathlib import Path

BUILD_STAGES=['runtime']+['unified-'+str(i) for i in range(6)]+['middle','sdk-0','sdk-1','tail']
STAGES={'native':[],'checks':[],'compiler':['native'],'runtime':['native'],
        **{'unified-'+str(i):['native','runtime'] for i in range(6)},
        'middle':['native','runtime']+['unified-'+str(i) for i in range(6)],
        **{'sdk-'+str(i):['native','middle'] for i in range(2)},
        'tail':['native','middle','sdk-0','sdk-1'],
        'package':['native','checks','compiler','tail']}
OUTPUTS={'native':['native/receipt.json','native/libtests-receipt.json','native/rolldown-binding.linux-x64-gnu.node'],
         'checks':['checks/tests.log','checks/installed.json'],
         'compiler':['compiler/tests.log']}
OUTPUTS.update({n:[n+'/checkpoint.tar',n+'/build.log'] for n in BUILD_STAGES})
ADDON='rolldown-binding.linux-x64-gnu.node'
def sha(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()


def checkpoint_path(stage):
    if stage.startswith('unified-'):
        i=int(stage.split('-')[1]);return 'unified/'+(['openclaw-dts-base']+['openclaw-dts-extensions-'+str(n) for n in range(1,6)])[i]
    if stage.startswith('sdk-'):return 'sdk/openclaw-dts-plugin-sdk-'+str(int(stage.split('-')[1])+1)
    if stage not in ('runtime','middle','tail'):raise ValueError('stage owns no build checkpoint')
    return stage


def extract_checkpoint(archive,directory,stage):
    """Extract only fixed checkpoint ownership; reject redirects before any write."""
    expected=checkpoint_path(stage);directory=Path(directory)
    with tarfile.open(regular(Path(archive)),'r:') as source:
        entries=source.getmembers();seen=set();types={}
        sidecar=expected+'.build608.json' if stage.startswith(('unified-','sdk-')) else None
        for entry in entries:
            name=entry.name.rstrip('/');parts=Path(name).parts
            if (not name or name in seen or name.startswith('/') or '..' in parts or
                not (name==expected or name==sidecar or name.startswith(expected+'/')) or
                not (entry.isdir() or entry.isfile() or entry.issym()) or entry.mode&0o7000):
                raise ValueError('unsafe or duplicate checkpoint archive entry')
            seen.add(name)
            types[name]=entry.isdir()
            if name==sidecar and not entry.isfile():raise ValueError('checkpoint binding must be regular')
            if entry.issym():
                # Checkpoints record generated links relative to the data root only.
                target=Path(name).parent/entry.linkname
                from posixpath import normpath
                normalized=normpath(str(target))
                if entry.linkname.startswith('/') or not normalized.startswith(expected+'/data/'):
                    raise ValueError('escaping checkpoint archive link')
        if expected not in seen or not entries or (sidecar and sidecar not in seen):raise ValueError('missing checkpoint archive root or binding')
        for name in seen:
            for parent in Path(name).parents:
                if str(parent) in types and not types[str(parent)]:
                    raise ValueError('checkpoint archive parent is not directory')
        directory.mkdir(exist_ok=True)
        if directory.is_symlink() or not directory.is_dir():raise ValueError('real checkpoint directory required')
        if (directory/expected).exists() or (directory/expected).is_symlink():raise ValueError('checkpoint restore collision')
        source.extractall(directory,filter='data')
        # Python's data filter deliberately strips group-write bits. The owning
        # checkpoint verifies exact modes; restore only already-validated bits.
        for entry in reversed(entries):
            if not entry.issym():(directory/entry.name).chmod(entry.mode&0o777)


def restore_build(root):
    verify_inputs(root);m=manifest(root)
    for n in STAGES[m['stage']]:
        if n in BUILD_STAGES:extract_checkpoint(root/'stage608-inputs'/n/'checkpoint.tar',root/'build608-checkpoints',n)


def archive_build(root,result):
    m=manifest(root);stage=m['stage'];name=checkpoint_path(stage)
    base=root/'build608-checkpoints';target=base/name
    if target.is_symlink() or not target.is_dir():raise ValueError('missing build owner checkpoint')
    out=Path(result)/stage;out.mkdir(exist_ok=True)
    with tarfile.open(out/'checkpoint.tar','x',format=tarfile.PAX_FORMAT) as archive:
        archive.add(target,arcname=name)
        if stage.startswith(('unified-','sdk-')):
            sidecar=regular(base/(name+'.build608.json'))
            archive.add(sidecar,arcname=name+'.build608.json')


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
        if r.get('source_export_sha256')!=m['source_export_sha256']:
            raise ValueError('unaccepted producing stage receipt common export identity: '+n)
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
           'source_export_sha256':m['source_export_sha256'],'stage_inputs':m.get('stage_inputs',{}),
           'manifest_sha256':sha(root/'export-manifest.json'),'exit_code':0,
           'outputs':{o:sha(regular(result/o)) for o in OUTPUTS.get(m['stage'],[])}}
    (result/m['stage']).mkdir(exist_ok=True)
    (result/m['stage']/'stage-receipt.json').write_text(json.dumps(value,sort_keys=True)+'\n')


if __name__=='__main__':
    root=Path.cwd();command=sys.argv[1:]
    if command==['stage']:print(manifest(root)['stage'])
    elif command==['verify-inputs']:verify_inputs(root)
    elif command==['stage-native']:stage_native(root)
    elif command==['restore-build']:restore_build(root)
    elif len(command)==2 and command[0]=='archive-build':archive_build(root,command[1])
    elif len(command)==2 and command[0]=='merge-logs':merge_logs(root,command[1])
    elif len(command)==2 and command[0]=='receipt':receipt(root,command[1])
    else:raise SystemExit('unknown stage608 command')
