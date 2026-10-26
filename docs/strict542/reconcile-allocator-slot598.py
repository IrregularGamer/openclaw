#!/usr/bin/env python3
"""Dispose job598's isolated slot after the interrupted 00:49Z allocator run, under its runner lock.
Successor of reconcile-isolated-slot598.py: also admits the killed run's leftover source/
only when its sole result files equal the copies already recovered locally.
This is not installation, lease revocation or a scanner/budget override.
"""
import hashlib
import json
import os
from pathlib import Path
import select
import shlex
import subprocess

SLOT = 'tmp-export598-config-isolation-98c59c32'
OUT = Path('/home/deploy/agentq/runs/598/allocator-reconciliation')
# Exact bytes recovered by jailed rsync before cleanup (probe.log, tests.log).
RECOVERED = {'result598-isolated': {'probe.log': 'b91e20b881005041c28aeb83d591bfe495987fc900c466f53bf233aae3b6419c'},
             'strict542-checks': {'tests.log': '1b30cadedb5297c05084baf6e684058d2444d12c2877eaef0dca065d0e50a743'}}
for d, files in RECOVERED.items():
    for n, h in files.items():
        assert hashlib.sha256((OUT/d/n).read_bytes()).hexdigest() == h, 'local recovery missing'
expected = hashlib.sha256(os.environ['AGENTQ_LEASE_ID'].encode()).hexdigest()
# Only the lease digest crosses the administrative channel; never the token.
remote = r'''
import sys,os,json,hashlib,signal
from pathlib import Path
sys.path.insert(0,'/usr/local/lib/offload-safety')
from leases import LeaseStore
from remote_watch import DockerEngine
os.environ.update(XDG_RUNTIME_DIR='/run/user/1001',DOCKER_HOST='unix:///run/user/1001/docker.sock')
signal.alarm(120)
store=LeaseStore();base=Path('/srv/offload/work/tmp-export598-config-isolation-98c59c32')
expected=EXPECTED
with store.runner_slot():
 live=lambda:sorted(hashlib.sha256(p.stem.encode()).hexdigest() for p in store.root.glob('*.json') if store.valid(p.stem))
 leases=live()
 # Fresh session: no offload run yet, so zero live leases (original stricter rule) or only ours.
 assert leases in ([],[expected]), 'unknown lease owner'
 assert not DockerEngine().containers(), 'active managed runner'
 assert base.is_dir() and not base.is_symlink(), 'untrusted slot'
 assert {p.name for p in base.iterdir()}=={'.pnpm-store','export-manifest.json','source598.tar','successor598.tar','native598.tar','run598.sh','source'}, 'unexpected input/result'
 assert not (base/'result598').exists() and not (base/'source').is_symlink(), 'unrecovered result'
 assert not (base/'source/isolated-probe598.json').exists(), 'unrecovered probe json'
 for d,files in RECOVERED.items():
  p=base/'source'/d
  assert p.is_dir() and not p.is_symlink() and {x.name for x in p.iterdir()}==set(files), 'unexpected result file'
  for n,h in files.items(): assert hashlib.sha256((p/n).read_bytes()).hexdigest()==h, 'result differs from recovery'
 assert not (base/'.pnpm-store').is_symlink(), 'redirected store'
 print(json.dumps({'phase':'LOCK_HELD_READY','runner_lock_available':True,'managed_running_containers':0,'live_lease_sha256':leases,'slot':base.name}),flush=True)
 assert sys.stdin.readline()=='VERIFY\n', 'cleanup controller lost'
 assert not base.exists() and not base.is_symlink(), 'cleanup incomplete'
 assert live()==leases and not DockerEngine().containers(), 'concurrent runner/lease'
 print(json.dumps({'phase':'LOCK_HELD_VERIFIED_ABSENT','absent':True,'slot':base.name}),flush=True)
'''.replace('EXPECTED',repr(expected)).replace('RECOVERED',repr(RECOVERED))

def receive(child):
    if not select.select([child.stdout],[],[],60)[0]:
        raise RuntimeError('finite lock/verification response timeout')
    line=child.stdout.readline()
    if not line: raise RuntimeError('remote guard refused or disconnected')
    return json.loads(line)

# Preconditions: exact independently reviewed inputs/outcomes are retained locally;
# no offload or rsync command is running and the sole queue worker owns this lease.
child=subprocess.Popen(['ssh','friend-vps','sudo -n -u offload python3 -u -c '+shlex.quote(remote)],
    stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
try:
    ready=receive(child)
    assert ready['phase']=='LOCK_HELD_READY'
    OUT.mkdir(exist_ok=True)
    (OUT/'immediate-idle.json').write_text(json.dumps(ready,sort_keys=True)+'\n')
    subprocess.run(['ssh','offload','clean',SLOT],check=True,timeout=60)
    child.stdin.write('VERIFY\n');child.stdin.flush()
    post=receive(child)
    assert post['phase']=='LOCK_HELD_VERIFIED_ABSENT' and post['absent'] is True
    (OUT/'post-clean.json').write_text(json.dumps(post,sort_keys=True)+'\n')
    assert child.wait(timeout=10)==0
    print(json.dumps(post))
finally:
    child.stdin.close()
    if child.poll() is None:
        child.terminate()
        try: child.wait(timeout=10)
        except subprocess.TimeoutExpired: child.kill();child.wait(timeout=5)
