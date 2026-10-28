"""Bounded read-only acceptance and retained evidence for the current runtime stage."""
import gzip,hashlib,json,shutil,tarfile
from pathlib import Path
ROOT=Path('/home/deploy/agentq/tmp/export608-stage-runtime-owned-next')
DOC=Path('/home/deploy/agentq/tmp/source552/docs/strict542')
RUN=Path('/home/deploy/agentq/runs/608')
PREFIX='job608-stage-runtime-owned-'
def sha(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def emit(p,x):p.write_text(json.dumps(x,sort_keys=True,indent=2)+'\n')
def compressed(src,name):
    dest=DOC/(PREFIX+name+'.gz')
    with src.open('rb') as source,dest.open('wb') as target,gzip.GzipFile(fileobj=target,mode='wb',filename='',mtime=0) as z:
        shutil.copyfileobj(source,z,1<<20)
    with gzip.open(dest,'rb') as f: expanded=hashlib.file_digest(f,'sha256').hexdigest()
    assert expanded==sha(src)
    return {'sha256':sha(dest),'expanded_sha256':expanded,'expanded_bytes':src.stat().st_size}
m=json.loads((ROOT/'export-manifest.json').read_text());r=ROOT/'result608-runtime'
assert sha(ROOT/'export-manifest.json')=='cf8907d39394721c84a496cd9aed4d52f33f4bf335335cf91a7a03252329cd80'
assert m['source_commit']=='5f7d810b7f254e4f06dbf7761b557ba90bf1a2b0'
assert m['source_export_sha256']=='76b4b47a0e5c3e0a157f75ff1b76d60753c8acdbf5f76bc495668dd985d70f64'
assert (RUN/'stage-runtime-owned-offload.rc').read_bytes()==b'0\n'
assert (r/'exit-code.txt').read_bytes()==b'0\n'
receipt=json.loads((r/'runtime/stage-receipt.json').read_text())
for key in ['source_commit','source_export_sha256','stage','stage_inputs','run_id']:assert receipt[key]==m[key],key
assert receipt['kind']=='JOB608_STAGE_RECEIPT' and receipt['exit_code']==0
assert receipt['manifest_sha256']==sha(ROOT/'export-manifest.json')
assert set(receipt['outputs'])=={'runtime/checkpoint.tar','runtime/build.log'}
files={str(p.relative_to(r)):sha(p) for p in r.rglob('*') if p.is_file() and not p.is_symlink()}
assert not any(p.is_symlink() for p in r.rglob('*'))
assert set(files)=={'runtime/checkpoint.tar','runtime/build.log','runtime/stage-receipt.json','exit-code.txt','strict542-checks/pnpm-path.txt'},set(files)
for name,digest in receipt['outputs'].items():assert files[name]==digest,name
with tarfile.open(r/'runtime/checkpoint.tar','r:') as t:
    entries=t.getmembers(); names=[e.name.rstrip('/') for e in entries]
    assert len(names)==len(set(names))
    assert set(names)>={'runtime','runtime/data','runtime/receipt.json'}
    assert all(n in {'runtime','runtime/data','runtime/receipt.json'} or n.startswith('runtime/data/') for n in names)
    inner=json.load(t.extractfile('runtime/receipt.json'))
    assert inner['schema']=='strict542-build-checkpoint608-v1' and inner['status']=='CHECKPOINT_NOT_BUILT' and inner['stage']=='runtime'
    identity=inner['identity']; assert identity['sourceCommit']==m['source_commit'] and identity['sourceExportSha256']==m['source_export_sha256']
    assert identity['nativeCompileSha256']==m['stage_inputs']['native/receipt.json']
    assert identity['nativeLibtestsSha256']==m['stage_inputs']['native/libtests-receipt.json']
    assert identity['nativeAddonSha256']==m['stage_inputs']['native/rolldown-binding.linux-x64-gnu.node']
    assert inner['ancestors']==[]
    assert [x['label'] for x in inner['phases']]==['clean:dist','plugins:assets:build','tsdown-ai','tsdown-packages','tsdown-unified']
    assert all(x['status']=='ran' and isinstance(x['durationMs'],(int,float)) and x['durationMs']>=0 for x in inner['phases'])
    actual={}
    for entry in entries:
        name=entry.name.rstrip('/')
        if not name.startswith('runtime/data/'):continue
        relative=name[len('runtime/data/'):]
        assert relative and not relative.startswith('/') and '..' not in Path(relative).parts
        item={'mode':entry.mode&0o7777}
        if entry.isdir():item['kind']='directory'
        elif entry.issym():item.update(kind='link',target=entry.linkname)
        else:
            assert entry.isfile() and not entry.islnk(),name
            with t.extractfile(entry) as f:item.update(kind='file',sha256=hashlib.file_digest(f,'sha256').hexdigest())
        actual[relative]=item
    assert actual==inner['outputs'],'checkpoint exact inventory mismatch'
for source,suffix in [(ROOT/'export-manifest.json','manifest.json'),(r/'runtime/stage-receipt.json','receipt.json'),(RUN/'stage-runtime-owned-offload.rc','offload.rc')]:shutil.copyfile(source,DOC/(PREFIX+suffix))
emit(DOC/(PREFIX+'checkpoint-receipt.json'),inner)
z={PREFIX+n+'.gz':compressed(p,n) for p,n in [(r/'runtime/build.log','build.log'),(RUN/'stage-runtime-owned-offload.log','offload.log')]}
value={'scope':'ACTUAL_RUNTIME_CHECKPOINT_ONLY_NOT_COMPLETE_GATEWAY_BUILD_PACKAGE_OR_APPLICATION','export':str(ROOT),'source_commit':m['source_commit'],'source_export_sha256':m['source_export_sha256'],'actual_offload_exit':0,'result_exit':0,'receipt_sha256':sha(r/'runtime/stage-receipt.json'),'receipt':receipt,'all_returned_files_sha256':files,'returned_bytes':sum(p.stat().st_size for p in r.rglob('*') if p.is_file()),'checkpoint_inventory_entries':len(actual),'checkpoint_inventory_kinds':{kind:sum(x['kind']==kind for x in actual.values()) for kind in ['directory','file','link']},'checkpoint_phases':inner['phases'],'checkpoint_identity':identity,'compressed_evidence':z,'remaining':'NEW current unified0..5/middle/sdk0..1/tail/package; final artifact/source/action/privilege/seal/REAL automatic queue reviews.595 MUST NOT APPLY'}
emit(DOC/(PREFIX+'verification.json'),value)
print(json.dumps({k:value[k] for k in ['receipt_sha256','returned_bytes','checkpoint_inventory_entries','checkpoint_inventory_kinds','checkpoint_phases']}))
