#!/usr/bin/env python3
"""Fixed source-only package checks; launches no command and never applies."""
import hashlib
import json
import os
from pathlib import Path
import stat
import sys

PINS={
    'pnpm-lock.yaml':'091ede3cb510110ed2b1ca8858100066add16cb3b91bcd0ff097d89f75035751',
    'pnpm-workspace.yaml':'5e672012b9678d1d40ec40e9fdff43283b7c4f947052cc24168b88d1f51ec872',
    '.npmrc':'f1d021e2abdf8817d83e35feb1f5d604e8c985aa0553bec3d417cf6f93e9c09c',
}
FALLBACK=('falling back to installing without','forces legacy deploy implementation')

def regular(path):
    try:info=path.lstat()
    except FileNotFoundError:raise ValueError('missing package input: '+str(path)) from None
    if not stat.S_ISREG(info.st_mode) or info.st_nlink!=1:
        raise ValueError('package input must be private regular file: '+str(path))
    return path

def digest(path):
    with regular(path).open('rb') as stream:return hashlib.file_digest(stream,'sha256').hexdigest()

def preflight(root,env):
    for key in env:
        normalized=key.casefold().replace('-','_')
        if normalized=='pnpm_workspace_dir' or normalized.startswith(('npm_config_','pnpm_config_')):
            raise ValueError('inherited package policy: '+key)
    for name,expected in PINS.items():
        if digest(root/name)!=expected:raise ValueError('original package input drift: '+name)

def receipt(root,env):
    preflight(root,env)
    out=root/'result598-build';runtime=out/'runtime'
    for directory in (out,runtime):
        if directory.is_symlink() or not directory.is_dir():
            raise ValueError('real package output directory required')
    log=regular(out/'deploy.log')
    if log.stat().st_size==0:raise ValueError('missing deploy log')
    with log.open() as stream:
        for line in stream:
            if any(warning in line.casefold() for warning in FALLBACK):
                raise ValueError('legacy/fallback package execution refuses receipt')
    value={'kind':'FROZEN_DEPLOY_INPUTS_VERIFIED_NOT_APPLICATION_AUTHORITY',
           'pnpm_version':'12.5.1','pnpm_source_commit':'859a9cfe39f2afd0c4198f14ca7ef628ee1de70e',
           'source_inputs_sha256':dict(PINS),'source_lock_sha256':PINS['pnpm-lock.yaml'],
           'target_lock_sha256':digest(runtime/'pnpm-lock.yaml'),'deploy_log_sha256':digest(log),
           'command':['pnpm','--filter','openclaw','--prod','deploy','result598-build/runtime'],
           'policy':'reviewed original shared lock; dedicated frozen target; unchanged lifecycle; no legacy fallback'}
    raw=json.dumps(value,sort_keys=True,separators=(',',':'))+'\n'
    with (out/'package-receipt.json').open('x') as stream:stream.write(raw)
    return value

def materialize(root):
    """Break pnpm store hardlinks in the deployed runtime by private exact copies.

    job608 package m674b: pnpm deploy imports files by hardlink, and
    application598 correctly refuses st_nlink>1. Only regular files inside the
    real runtime tree are copied; symlinks are never followed and every copy is
    hash-verified before it atomically replaces its linked original."""
    runtime=root/'result598-build'/'runtime'
    if runtime.is_symlink() or not runtime.is_dir():raise ValueError('real package output directory required')
    count=0;copied=0
    for directory,dirs,files in os.walk(runtime,followlinks=False):
        for name in files:
            count+=1
            if count>300000:raise ValueError('runtime inventory too large')
            path=Path(directory)/name;info=path.lstat()
            if not stat.S_ISREG(info.st_mode) or info.st_nlink==1:continue
            temp=path.with_name('.materialize608-'+name)
            with path.open('rb') as source:raw=source.read()
            fd=os.open(temp,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
            with os.fdopen(fd,'wb') as stream:stream.write(raw)
            os.chmod(temp,stat.S_IMODE(info.st_mode))
            if hashlib.sha256(temp.read_bytes()).digest()!=hashlib.sha256(raw).digest() or temp.lstat().st_nlink!=1:
                raise ValueError('materialized copy mismatch: '+str(path))
            os.replace(temp,path);copied+=1
    return copied

if __name__=='__main__':
    if len(sys.argv)!=2 or sys.argv[1] not in ('preflight','receipt','materialize'):
        raise SystemExit('frozen package guard accepts only preflight, receipt or materialize')
    root=Path.cwd()
    if sys.argv[1]=='preflight':preflight(root,os.environ)
    elif sys.argv[1]=='materialize':print(json.dumps({'materialized':materialize(root)}))
    else:print(json.dumps(receipt(root,os.environ),sort_keys=True))
