#!/usr/bin/env python3
"""Unprivileged source staging only; never install, delete, launch or change policy.

This host/return wrapper is supplemental to the frozen gateway build source.
Its own exact committed bytes need independent action review before use.
"""
import argparse,hashlib,json,os,re,shutil,stat
from pathlib import Path

MIB=1024**2
MAX_STORE=4096*MIB
FREE_RESERVE=2048*MIB
PARENT=Path('/srv/encrypted/dev-move-98')
SOURCE='1bed4d1bb53eff145f724cc6a448dc73b3609015'
COMMON='5d7e9d57fb660e2b54f5595e81ddf332027e21b303937c2cd6bc7f718f311263'
BASE_MANIFEST='20111ce5f68e7764e7176a670df6e9097deafa51d02291810bf65dd41c8c7c2d'
CAPS={'native':64*MIB,'checks':16*MIB,'compiler':16*MIB,'runtime':128*MIB,
      **{'unified-'+str(i):32*MIB for i in range(6)},'middle':128*MIB,
      'sdk-0':32*MIB,'sdk-1':32*MIB,'tail':192*MIB,'package':2048*MIB}
ARCHIVES={'source598.tar':'base_source_archive_sha256','native598.tar':'native_export_sha256',
          'rolldown608-source.tar.gz':'compiler_upstream_archive_sha256','successor598.tar':'successor_archive_sha256'}
SMALL_FILES=['run608.sh','stage608.py','export-manifest.json']

def sha(path):
    with Path(path).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()

def real_path(path):
    path=Path(path).absolute()
    if '..' in path.parts or any(p.is_symlink() for p in (path,*path.parents)):
        raise ValueError('source staging path redirect refused')
    return path

def regular(path):
    path=real_path(path)
    if not path.is_file():raise ValueError('regular source input required')
    return path

def forecast(base_archive_bytes):
    # One copied base overlay plus one NEW overlay for each of fifteen stages.
    value={'base_archive_bytes':base_archive_bytes,'overlay_bytes':16*(len(CAPS)+1)*MIB,
           'return_caps_bytes':sum(CAPS.values()),'metadata_and_filesystem_reserve_bytes':128*MIB}
    value['total_bytes']=sum(value.values())
    if value['total_bytes']>MAX_STORE:raise ValueError('aggregate source staging forecast exceeds 4GiB')
    return value

def bytes_used(root,unique=True):
    root=real_path(root);seen=set();total=0
    if not root.is_dir():raise ValueError('real staging directory required')
    for path in root.rglob('*'):
        info=path.lstat()
        if stat.S_ISLNK(info.st_mode):
            if not path.resolve().is_relative_to(root):raise ValueError('escaping staging link')
            total+=info.st_size
        elif stat.S_ISREG(info.st_mode):
            key=(info.st_dev,info.st_ino)
            if not unique or key not in seen:total+=info.st_size;seen.add(key)
        elif not stat.S_ISDIR(info.st_mode):raise ValueError('special staging file refused')
    return total

def cap(stage):
    if stage not in CAPS:raise ValueError('unknown finite stage')
    return CAPS[stage]

def check_room(root,stage,free=None):
    allowance=cap(stage)+16*MIB
    used=bytes_used(root)
    if used+allowance+128*MIB>MAX_STORE:raise ValueError('aggregate staging cap would be exceeded')
    free=shutil.disk_usage(root).free if free is None else free
    if free<FREE_RESERVE+allowance:raise ValueError('encrypted volume free reserve would be exceeded')
    return {'stage':stage,'current_unique_bytes':used,'return_cap_bytes':cap(stage),
            'free_bytes':free,'free_reserve_bytes':FREE_RESERVE,'max_store_bytes':MAX_STORE}

def check_result(result,stage):
    # rsync -az does not preserve hardlinks, so charge every returned file path.
    limit=cap(stage)
    size=bytes_used(result,unique=False)
    if size>limit:raise ValueError('finite stage return cap exceeded')
    return {'stage':stage,'logical_return_bytes':size,'return_cap_bytes':limit}

def copy_base(base,dest,m):
    files={name:m[key] for name,key in ARCHIVES.items()}
    files.update({name:sha(regular(base/name)) for name in SMALL_FILES})
    files.update({'native608-stages/'+name:d for name,d in m['native_stage_outputs'].items()})
    # Validate the complete allowlist first; no arbitrary directory copy or link.
    for name,digest in files.items():
        if name.startswith('/') or '..' in Path(name).parts:raise ValueError('unsafe source input')
        if sha(regular(base/name))!=digest:raise ValueError('base source digest drift: '+name)
    for name,digest in files.items():
        target=dest/name;target.parent.mkdir(parents=True,exist_ok=True)
        with regular(base/name).open('rb') as source,target.open('xb') as output:
            shutil.copyfileobj(source,output,64*1024)
        if sha(target)!=digest:raise ValueError('copied source digest drift: '+name)
    return files

def store_path(root):
    root=real_path(root)
    if root.parent!=PARENT or not re.fullmatch(r'agentq-source608-[a-zA-Z0-9-]{8,64}',root.name):
        raise ValueError('fixed private source staging namespace required')
    info=PARENT.stat()
    if info.st_uid!=os.getuid() or stat.S_IMODE(info.st_mode)!=0o700:
        raise ValueError('existing deploy-private source staging parent required')
    if root.exists():
        info=root.stat()
        if info.st_uid!=os.getuid() or stat.S_IMODE(info.st_mode)!=0o700:
            raise ValueError('private source staging root required')
    return root

def initialize(base,root):
    base=real_path(base);root=store_path(root)
    if root.exists():raise ValueError('source staging root must be new')
    if sha(regular(base/'export-manifest.json'))!=BASE_MANIFEST:
        raise ValueError('exact independently reviewed base manifest required')
    m=json.loads(regular(base/'export-manifest.json').read_text())
    if m['source_commit']!=SOURCE or m['source_export_sha256']!=COMMON or m.get('stage_inputs')!={}:
        raise ValueError('exact frozen secretless base with empty stage inputs required')
    for name,key in [('run608.sh','runner_sha256'),('stage608.py','stage_helper_sha256')]:
        if sha(regular(base/name))!=m[key]:raise ValueError('exact reviewed runner/helper required')
    base_size=sum(regular(base/n).stat().st_size for n in ARCHIVES if n!='successor598.tar')
    plan=forecast(base_size)
    free=shutil.disk_usage(PARENT).free
    if free<MAX_STORE+FREE_RESERVE:raise ValueError('full staging cap plus free reserve unavailable')
    root.mkdir(mode=0o700);dest=root/'base';dest.mkdir(mode=0o700)
    files=copy_base(base,dest,m)
    receipt={'kind':'SOURCE_ONLY_STORAGE608','source_commit':SOURCE,'source_export_sha256':COMMON,
             'original_base':str(base),'copied_inputs_sha256':files,'forecast':plan,
             'max_store_bytes':MAX_STORE,'free_reserve_bytes':FREE_RESERVE,'initial_free_bytes':free,
             'return_caps_bytes':CAPS,'helper_sha256':sha(Path(__file__)),
             'scope':'new private source files only; historical files preserved; no install authority'}
    (root/'storage-receipt.json').write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
    return receipt

def main():
    ap=argparse.ArgumentParser(description=__doc__);sub=ap.add_subparsers(dest='command',required=True)
    init=sub.add_parser('init');init.add_argument('--base',type=Path,required=True);init.add_argument('--root',type=Path,required=True)
    check=sub.add_parser('check');check.add_argument('--root',type=Path,required=True);check.add_argument('--stage',required=True)
    result=sub.add_parser('result');result.add_argument('--result',type=Path,required=True);result.add_argument('--stage',required=True)
    a=ap.parse_args()
    if a.command=='init':value=initialize(a.base,a.root)
    elif a.command=='check':value=check_room(store_path(a.root),a.stage)
    else:value=check_result(a.result,a.stage)
    print(json.dumps(value,sort_keys=True))

if __name__=='__main__':main()
