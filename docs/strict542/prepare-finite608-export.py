#!/usr/bin/env python3
"""Prepare one unused finite-stage export. Never launch, install or change policy.

Base archives are immutable committed secretless exports. Every consumer copies
only exact successful same-source producing outputs, not a checkout or cache.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess


def sha(path):
    with Path(path).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for n in ('base','dest'):ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--commit',required=True)
    ap.add_argument('--stage',required=True)
    ap.add_argument('--result',action='append',default=[],help='required predecessor STAGE=RESULT_DIRECTORY')
    a=ap.parse_args();repo=Path(__file__).resolve().parents[2]
    git=lambda *args:subprocess.check_output(['git','-C',str(repo),*args])
    commit=git('rev-parse',a.commit+'^{commit}').decode().strip()
    # Load the exact committed helper used in the new export, not local edits.
    helper=git('show',commit+':docs/strict542/stage608.py')
    stage={};exec(compile(helper,'committed-stage608.py','exec'),stage)
    if a.stage not in stage['STAGES']:raise ValueError('unknown finite stage')
    base=a.base.resolve();dest=a.dest.resolve()
    if dest.exists():raise ValueError('destination must be new and unused')
    m=json.loads((base/'export-manifest.json').read_text())
    archives={'source598.tar':'base_source_archive_sha256','native598.tar':'native_export_sha256',
              'rolldown608-source.tar.gz':'compiler_upstream_archive_sha256'}
    for name,key in archives.items():
        if sha(base/name)!=m[key]:raise ValueError('base archive digest drift: '+name)
    changed=git('diff','--name-only',m['source_commit'],commit).decode().splitlines()
    paths=sorted(set(m['successor_paths']).union(changed))
    tracked=set(git('ls-tree','-r','--name-only',commit).decode().splitlines())
    if set(paths)-tracked:raise ValueError('overlay cannot silently remove source paths')
    if any(p.startswith('/') or '..' in Path(p).parts or Path(p).name in ('.env','.db') for p in paths):
        raise ValueError('unsupported export source path')
    results={}
    for item in a.result:
        name,value=item.split('=',1)
        if name in results:raise ValueError('duplicate producing result')
        results[name]=Path(value).resolve()
    needed=stage['STAGES'][a.stage]
    if set(results)!=set(needed):raise ValueError('supply exactly required producing results: '+','.join(needed))
    dest.mkdir()
    for name in archives:os.link(base/name,dest/name)
    shutil.copytree(base/'native608-stages',dest/'native608-stages')
    for name,digest in m['native_stage_outputs'].items():
        if sha(dest/'native608-stages'/name)!=digest:raise ValueError('native receipt drift')
    with (dest/'successor598.tar').open('xb') as output:
        subprocess.run(['git','-C',str(repo),'archive',commit,'--',*paths],stdout=output,check=True)
    identity={'base_source_archive_sha256':m['base_source_archive_sha256'],'source_commit':commit,
              'successor_archive_sha256':sha(dest/'successor598.tar')}
    common=hashlib.sha256(json.dumps(identity,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    pins={}
    for name in needed:
        root=results[name]
        if (root/'exit-code.txt').read_text().strip()!='0':raise ValueError('producing run did not exit zero: '+name)
        receipt=root/name/'stage-receipt.json';r=json.loads(receipt.read_text())
        if (r.get('kind')!='JOB608_STAGE_RECEIPT' or r.get('exit_code')!=0 or r.get('stage')!=name or
            r.get('source_commit')!=commit or r.get('source_export_sha256')!=common):
            raise ValueError('foreign or incomplete producing stage: '+name)
        outputs=stage['OUTPUTS'][name]
        if r.get('outputs')!={p:sha(root/p) for p in outputs}:raise ValueError('producing output digest mismatch')
        for path in [*outputs,name+'/stage-receipt.json']:
            source=stage['regular'](root/path);target=dest/'stage608-inputs'/path
            target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target);pins[path]=sha(target)
    (dest/'run608.sh').write_bytes(git('show',commit+':docs/strict542/run-stage608.sh'))
    (dest/'stage608.py').write_bytes(helper)
    m.update(identity,source_export_sha256=common,successor_paths=paths,stage=a.stage,
             stage_inputs=dict(sorted(pins.items())),runner_commit=commit,runner_sha256=sha(dest/'run608.sh'),
             stage_helper_sha256=sha(dest/'stage608.py'),run_id='stage608-'+a.stage+'-'+dest.name,
             execution_state='UNUSED',launch_history='none (fresh finite export)',
             purpose='fixed finite canonical build stage '+a.stage+'; admitted offload only; no application authority')
    (dest/'export-manifest.json').write_text(json.dumps(m,indent=2,sort_keys=True)+'\n')
    subprocess.run(['python3','-I','stage608.py','verify-inputs'],cwd=dest,check=True)
    print(json.dumps({'dest':str(dest),'stage':a.stage,'source_commit':commit,
                      'source_export_sha256':common,'manifest_sha256':sha(dest/'export-manifest.json')}))


if __name__=='__main__':main()
