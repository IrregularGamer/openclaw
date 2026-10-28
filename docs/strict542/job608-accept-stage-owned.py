"""Bounded read-only acceptance of one actual frozen 5f7d810b build stage (unified-N/sdk-N/middle/tail).
Usage: accept-stage-owned.py STAGE EXPORT_DIR LOGTAG. Never extracts; streams every archive member."""
import gzip,hashlib,json,shutil,sys,tarfile
from pathlib import Path
stage,ROOT,tag=sys.argv[1],Path(sys.argv[2]),sys.argv[3]
DOC=Path('/home/deploy/agentq/tmp/source552/docs/strict542');RUN=Path('/home/deploy/agentq/runs/608')
PREFIX='job608-stage-%s-owned-'%tag
def sha(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def emit(p,x):p.write_text(json.dumps(x,sort_keys=True,indent=2)+'\n')
def compressed(src,name):
    dest=DOC/(PREFIX+name+'.gz')
    with src.open('rb') as s,dest.open('wb') as t,gzip.GzipFile(fileobj=t,mode='wb',filename='',mtime=0) as z:shutil.copyfileobj(s,z,1<<20)
    with gzip.open(dest,'rb') as f:e=hashlib.file_digest(f,'sha256').hexdigest()
    assert e==sha(src);return {'sha256':sha(dest),'expanded_sha256':e,'expanded_bytes':src.stat().st_size}
sys.path.insert(0,str(ROOT));import stage608
name=stage608.checkpoint_path(stage);sidecar=name+'.build608.json' if stage.startswith(('unified-','sdk-')) else None
m=json.loads((ROOT/'export-manifest.json').read_text());r=ROOT/('result608-'+stage)
assert m['stage']==stage and m['source_commit']=='5f7d810b7f254e4f06dbf7761b557ba90bf1a2b0'
rc=RUN/('stage-%s-owned-offload.rc'%tag);log=RUN/('stage-%s-owned-offload.log'%tag)
assert rc.read_bytes()==b'0\n' and (r/'exit-code.txt').read_bytes()==b'0\n'
receipt=json.loads((r/stage/'stage-receipt.json').read_text())
for k in ['source_commit','source_export_sha256','stage','stage_inputs','run_id']:assert receipt[k]==m[k],k
assert receipt['kind']=='JOB608_STAGE_RECEIPT' and receipt['exit_code']==0 and receipt['manifest_sha256']==sha(ROOT/'export-manifest.json')
assert set(receipt['outputs'])=={stage+'/checkpoint.tar',stage+'/build.log'}
assert not any(p.is_symlink() for p in r.rglob('*'))
files={str(p.relative_to(r)):sha(p) for p in r.rglob('*') if p.is_file()}
for n,d in receipt['outputs'].items():assert files[n]==d,n
with tarfile.open(r/stage/'checkpoint.tar','r:') as t:
    entries=t.getmembers();names=[e.name.rstrip('/') for e in entries];assert len(names)==len(set(names))
    assert all(n==name or n==sidecar or n.startswith(name+'/') for n in names) and name in names and (not sidecar or sidecar in names)
    assert not any(e.mode&0o7000 or e.islnk() for e in entries)
    inner=json.load(t.extractfile(name+'/receipt.json'));binding=json.load(t.extractfile(sidecar)) if sidecar else None
    assert inner['schema']=='strict542-build-checkpoint608-v1' and inner['stage']==stage,(inner.get('schema'),inner.get('stage'))
    ident=inner['identity'];assert ident['sourceCommit']==m['source_commit'] and ident['sourceExportSha256']==m['source_export_sha256']
    assert all(x['status']=='ran' for x in inner['phases']),inner['phases']
    actual={}
    for e in entries:
        n=e.name.rstrip('/')
        if not n.startswith(name+'/data/'):continue
        rel=n[len(name+'/data/'):];assert rel and '..' not in Path(rel).parts
        it={'mode':e.mode&0o7777}
        if e.isdir():it['kind']='directory'
        elif e.issym():it.update(kind='link',target=e.linkname)
        else:
            with t.extractfile(e) as f:it.update(kind='file',sha256=hashlib.file_digest(f,'sha256').hexdigest())
        actual[rel]=it
    assert actual==inner['outputs'],'checkpoint exact inventory mismatch'
for s,suf in [(ROOT/'export-manifest.json','manifest.json'),(r/stage/'stage-receipt.json','receipt.json'),(rc,'offload.rc')]:shutil.copyfile(s,DOC/(PREFIX+suf))
emit(DOC/(PREFIX+'checkpoint-receipt.json'),{'inner':inner,'binding':binding})
z={PREFIX+n+'.gz':compressed(p,n) for p,n in [(r/stage/'build.log','build.log'),(log,'offload.log')]}
v={'scope':'ACTUAL_%s_CHECKPOINT_ONLY_NOT_COMPLETE_BUILD_PACKAGE_OR_APPLICATION'%stage.upper(),'stage':stage,'export':str(ROOT),'source_commit':m['source_commit'],'source_export_sha256':m['source_export_sha256'],'receipt_sha256':sha(r/stage/'stage-receipt.json'),'receipt':receipt,'all_returned_files_sha256':files,'checkpoint_inventory_entries':len(actual),'checkpoint_phases':inner['phases'],'checkpoint_ancestors':inner.get('ancestors'),'compressed_evidence':z,'remaining':'595 MUST NOT APPLY'}
emit(DOC/(PREFIX+'verification.json'),v)
print(json.dumps({k:v[k] for k in ['receipt_sha256','checkpoint_inventory_entries','checkpoint_phases','checkpoint_ancestors']}))
