#!/usr/bin/env python3
"""Prepare, never launch, a fresh UNUSED INC-261027-18 stage export at a new
committed source, reusing a prior stage export's digest-verified archives."""
import argparse,hashlib,json,os,shutil,subprocess
from pathlib import Path
REPO=Path('/home/deploy/agentq/tmp/source552')
git=lambda *a:subprocess.check_output(['git','-C',str(REPO),*a])
def sha(p):
    # INC-261028-08: stream; read_bytes() on the 690MB source598.tar OOM-killed the 1GiB worker slice
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('--base',type=Path,required=True);ap.add_argument('--commit',required=True)
ap.add_argument('--stage',required=True)
# INC-261027-18 continuation: result608-<stage> dirs of accepted producing stages, staged and pinned as exact stage inputs
ap.add_argument('--input',type=Path,action='append',default=[]);ap.add_argument('--dest',type=Path,required=True)
a=ap.parse_args();base=a.base.resolve();dest=a.dest.resolve()
assert not dest.exists(),'destination must be NEW'
m=json.loads((base/'export-manifest.json').read_text())
keys={'source598.tar':'base_source_archive_sha256','native598.tar':'native_export_sha256','rolldown608-source.tar.gz':'compiler_upstream_archive_sha256'}
for n,k in keys.items(): assert sha(base/n)==m[k],n
for n,d in m['native_stage_outputs'].items(): assert sha(base/'native608-stages'/n)==d,n
commit=git('rev-parse',a.commit+'^{commit}').decode().strip()
changed=git('diff','--name-only',m['source_commit'],commit).decode().splitlines()
tree=set(git('ls-tree','-r','--name-only',commit).decode().splitlines())
paths=sorted(set(m['successor_paths']).union(changed));assert not set(paths)-tree,set(paths)-tree
assert all(not p.startswith('/') and '..' not in Path(p).parts and Path(p).name not in {'.env','.db'} for p in paths)
dest.mkdir()
for n in keys: os.link(base/n,dest/n)
shutil.copytree(base/'native608-stages',dest/'native608-stages')
with (dest/'successor598.tar').open('wb') as s: subprocess.run(['git','-C',str(REPO),'archive',commit,'--',*paths],stdout=s,check=True)
(dest/'run608.sh').write_bytes(git('show',commit+':docs/strict542/run-stage608.sh'))
(dest/'stage608.py').write_bytes(git('show',commit+':docs/strict542/stage608.py'))
ident={'base_source_archive_sha256':m['base_source_archive_sha256'],'source_commit':commit,'successor_archive_sha256':sha(dest/'successor598.tar')}
prev=sha(base/'export-manifest.json');m.update(ident)
m.update(stage=a.stage,execution_state='UNUSED',run_id='stage608-%s-%s'%(a.stage,dest.name.rsplit('-',1)[-1]),
 runner_sha256=sha(dest/'run608.sh'),successor_paths=paths,predecessor_manifest_sha256=prev,
 source_export_sha256=hashlib.sha256(json.dumps(ident,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 predecessor_package_attempt=m['run_id']+' (superseded by source '+commit[:8]+')')
if a.stage=='native': m['purpose']=m['purpose'].replace('stage checks: verified archives + scoped gateway/supervisor-IPC/cancellation tests + frozen install + installed tooling checks (120000ms/case, maxConcurrency=1); 4g/1CPU, outer wall <=24','stage native: verified archives + reviewed 2400s native rebuild returning pinned receipts/addon; 4g/1CPU, outer wall <=24')
NATIVE_PURPOSE='stage native: verified archives + reviewed 2400s native rebuild returning pinned receipts/addon; 4g/1CPU, outer wall <=24'
CHECKS_PURPOSE='stage checks: verified archives + scoped gateway/supervisor-IPC/cancellation tests + frozen install + installed tooling checks (120000ms/case, maxConcurrency=1); 4g/1CPU, outer wall <=24'
if a.stage=='checks': m['purpose']=m['purpose'].replace(NATIVE_PURPOSE,CHECKS_PURPOSE)
(dest/'export-manifest.json').write_text(json.dumps(m,indent=2,sort_keys=True)+'\n')
import importlib.util
spec=importlib.util.spec_from_file_location('stage608',dest/'stage608.py');st=importlib.util.module_from_spec(spec);spec.loader.exec_module(st)
assert a.stage in st.STAGES,'unknown stage'
needed=st.STAGES[a.stage];by={}
for r in a.input:
    rr=r.resolve();assert (rr/'exit-code.txt').read_text().strip()=='0',rr
    for n in needed:
        if (rr/n/'stage-receipt.json').is_file():assert n not in by,'duplicate input stage '+n;by[n]=rr
assert set(by)==set(needed),('stage inputs missing',set(needed)-set(by))
pins={}
for n in needed:
    rec=json.loads((by[n]/n/'stage-receipt.json').read_text())
    assert rec['exit_code']==0 and rec['source_commit']==commit and rec['source_export_sha256']==m['source_export_sha256'],n
    for o in [n+'/stage-receipt.json']+st.OUTPUTS[n]:
        src=by[n]/o;assert src.is_file() and not src.is_symlink(),o
        t=dest/'stage608-inputs'/o;t.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,t);pins[o]=sha(t)
    assert rec['outputs']=={o:pins[o] for o in st.OUTPUTS[n]},n
m['stage_inputs']=pins
(dest/'export-manifest.json').write_text(json.dumps(m,indent=2,sort_keys=True)+'\n')
print(json.dumps({'dest':str(dest),'stage':a.stage,'source_commit':commit,'manifest_sha256':sha(dest/'export-manifest.json')}))
