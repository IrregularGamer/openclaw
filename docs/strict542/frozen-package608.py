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
POLICY={'force_legacy_deploy','shared_workspace_lockfile','lockfile','lockfile_dir',
        'userconfig','globalconfig','ignore_scripts','ignore_pnpmfile','node_linker',
        'package_import_method','prod','production','dev','optional','force'}
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
        if normalized=='pnpm_workspace_dir' or any(
            normalized.startswith(prefix) and normalized[len(prefix):] in POLICY
            for prefix in ('npm_config_','pnpm_config_')):
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

if __name__=='__main__':
    if len(sys.argv)!=2 or sys.argv[1] not in ('preflight','receipt'):
        raise SystemExit('frozen package guard accepts only preflight or receipt')
    root=Path.cwd()
    if sys.argv[1]=='preflight':preflight(root,os.environ)
    else:print(json.dumps(receipt(root,os.environ),sort_keys=True))
