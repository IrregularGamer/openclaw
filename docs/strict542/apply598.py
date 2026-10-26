#!/usr/bin/env python3
"""Fixed reviewed strict542 application. SOURCE ONLY; never manages services."""
import argparse
import base64
import fcntl
import importlib.util
import json
import os
import re
from pathlib import Path
import shutil
import signal
import sqlite3
import stat
import subprocess
import sys
import time
from types import ModuleType, SimpleNamespace

STAGE = Path('/var/lib/agentq-safety/strict542-598-input')
ROOT = Path('/var/lib/agentq-safety')
SEAL = ROOT/'validation.json'
JOURNAL = ROOT/'strict542-598-application.json'
LOCK = ROOT/'admission.lock'
DB = Path('/home/deploy/agentq/state/agentq.db')
BOOT = Path('/proc/sys/kernel/random/boot_id')

def preparation():
    path=STAGE/'application598.py'
    protected(path)
    spec=importlib.util.spec_from_file_location('strict542_preparation598',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def expired(signum,frame):
    raise PermissionError('finite application lifetime expired; preserve poison/backups')

def require(value,reason):
    if not value:raise PermissionError(reason)

def protected(path):
    for part in (path,*path.parents):
        info=part.lstat()
        require(not part.is_symlink() and info.st_uid == 0 and not info.st_mode & 0o022,'root protected path required: '+str(part))
    return path

def read(path):
    protected(path)
    require(path.stat().st_size <= 64*1024*1024,'oversized receipt')
    return json.loads(path.read_bytes())

def xattrs(path):
    return {name:base64.b64encode(os.getxattr(path,name,follow_symlinks=False)).decode()
            for name in sorted(os.listxattr(path,follow_symlinks=False))}

def metadata(path,prep):
    info=path.lstat()
    return dict(mode=stat.S_IMODE(info.st_mode),uid=info.st_uid,gid=info.st_gid,
        mtime_ns=info.st_mtime_ns,ctime_ns=info.st_ctime_ns,xattrs_sha256=prep.digest(xattrs(path)))

def check_original(path,old,prep):
    if old['state'] == 'absent':
        require(not os.path.lexists(path),'original absent target exists: '+str(path));return
    require(path.is_file() and not path.is_symlink(),'original target type drift')
    require(prep.file_hash(path) == old['sha256'] and metadata(path,prep) == old['metadata'],'original bytes/metadata drift: '+str(path))

def run(argv,**kwargs):
    return subprocess.run(argv,**kwargs,env={'PATH':'/usr/bin:/bin','LANG':'C'},check=False)

def native_module(prep):
    native_path=protected(STAGE/'maintenance.py');raw=native_path.read_bytes()
    require(prep.sha(raw) == prep.NATIVE_SHA,'native owner pin changed')
    native=ModuleType('strict542_application_native');native.__file__=str(native_path)
    exec(compile(raw,str(native_path),'exec'),native.__dict__)
    return native

def owner_check(ack,action,prep):
    require(set(ack) == {'scope','owner','boot_id','created_wall','expires_wall','created_mono','expires_mono','action_sha256'},'HQ acknowledgement schema')
    require(ack['scope'] == 'strict542-gateway-install598' and ack['action_sha256'] == action['action_sha256'],'HQ acknowledgement action mismatch')
    wall=time.time();mono=time.monotonic()
    require(ack['boot_id'] == BOOT.read_text().strip(),'HQ acknowledgement boot changed')
    for current,start,end in ((wall,ack['created_wall'],ack['expires_wall']),(mono,ack['created_mono'],ack['expires_mono'])):
        require(type(start) in (int,float) and type(end) in (int,float) and start <= current < end and 0 < end-start <= 900,'HQ finite window expired/invalid')
    native=native_module(prep)
    adapter=native.Native510(SimpleNamespace(root=native.ROOT,runner=run))
    # Existing predicates, caller cgroup and MainPID are unchanged and repeated.
    adapter.owner_check(ack['owner'],caller=True)
    adapter.owner_check(ack['owner'],caller=True)

def native_quiet(prep):
    # Use the installed, seal-checked controller and exact native owner for
    # broker fixture inventory and repeated stopped+revoked remote proof.
    # Controller import/initialization performs no actions. No stop/resume,
    # lease creation, container launch, or alternate owner predicate exists.
    spec=importlib.util.spec_from_file_location('strict542_installed_control',protected(Path('/usr/local/libexec/agentq-safety/control.py')))
    control=importlib.util.module_from_spec(spec);spec.loader.exec_module(control)
    controller=control.Controller(runner=run)
    worker=controller.registry()
    require(controller.valid_registration(worker),'valid settled registration required')
    identity={key:worker.get(key) for key in ('job_id','unit','attempt','epoch','invocation')}
    require(native_module(prep).Native510(controller).quiet(identity),'native registered/fixture/remote work unsettled')

def quiet(prep):
    native_quiet(prep)
    registration=ROOT/'worker.json'
    if registration.exists():
        require(read(registration).get('reconciled') is True,'registered worker unsettled')
    with sqlite3.connect('file:'+str(DB)+'?mode=ro',uri=True,timeout=2) as db:
        require(db.execute("SELECT 1 FROM jobs WHERE status='running' LIMIT 1").fetchone() is None,'running queue job')
    result=run(['/usr/bin/systemctl','list-units','--all','--plain','--no-pager','--no-legend','agentq-exec-*','agentq-check-*'],capture_output=True,text=True,timeout=5)
    require(result.returncode == 0,'worker inventory unavailable')
    for line in result.stdout.splitlines():
        columns=line.split()
        require(len(columns)>=4 and columns[2] in {'inactive','failed'},'live worker/fixture unit')
    for name in ('maintenance-transaction.json','scheduler-request.json'):
        require(not (ROOT/name).exists(),'pending native action requires reconciliation: '+name)

def seal_valid(seal,prep):
    hashes=seal.get('installed_hashes')
    require(isinstance(hashes,dict) and hashes,'missing original full seal')
    for path,expected in hashes.items():
        target=Path(path)
        require(target.is_absolute() and target.is_file() and not target.is_symlink()
            and prep.hexid(expected) and prep.file_hash(target) == expected,'existing installed seal drift: '+path)

def next_seal(old,new,action,reviews,prep):
    payload=action['action'];allowed={change['target']:change['new']['sha256'] for change in payload['changes'] if change['source'] != 'runtime'}
    runtime=prep.TARGETS['runtime'];entries={entry['path']:entry for entry in read(STAGE/'tree.json')['entries']}
    for name in ('package.json','dist/index.js'):
        require(entries.get(name,{}).get('kind') == 'file','runtime seal entry missing')
        allowed[runtime+'/'+name]=entries[name]['sha256']
    expected=json.loads(json.dumps(old));expected['installed_hashes'].update(allowed)
    expected.setdefault('amendments',[]).append({'kind':'strict542-598','action_sha256':action['action_sha256']})
    require(new == expected,'next seal must be exact additive fixed-target amendment')
    policy=[review for review in reviews if review.get('scope') == 'seal']
    require(len(policy) == 1 and policy[0].get('next_seal_sha256') == prep.file_hash(STAGE/'validation.next.json'),'independent exact next-seal policy review missing')

def queue_approved(reviews,prep):
    # Read the actual queue's settled facts; an APPROVE598 label is not a review.
    review=[r for r in reviews if r.get('scope') == 'automatic-queue']
    require(len(review) == 1,'exact automatic queue review required')
    review=review[0]
    require(review.get('build_job_id') == prep.PREPARATION_JOB_ID,'queue preparation identity mismatch')
    with sqlite3.connect('file:'+str(DB)+'?mode=ro',uri=True,timeout=2) as db:
        build=db.execute('SELECT kind,status FROM jobs WHERE id=?',(prep.PREPARATION_JOB_ID,)).fetchone()
        actual=db.execute('SELECT kind,status,parent_id,result FROM jobs WHERE id=?',(review.get('review_job_id'),)).fetchone()
    require(build == ('build','done') and actual is not None
            and actual[:3] == ('review','done',prep.PREPARATION_JOB_ID)
            and isinstance(actual[3],str)
            and prep.sha(actual[3].encode()) == review.get('queue_result_sha256'),
            'actual automatic queue approval is missing or differs')
    # Match the first verdict exactly as agentq's review transition does. Ancestor
    # builds may become done after a successor, so done alone is not approval.
    verdict=re.search(r'VERDICT:\s*(APPROVE|CHANGES)',actual[3])
    require(verdict is not None and verdict.group(1) == 'APPROVE',
            'actual automatic queue review did not approve this build')

def load(prep):
    action=read(STAGE/'action.json');tree=read(STAGE/'tree.json');reviews=read(STAGE/'reviews.json')
    prep.validate_action(action,tree,STAGE,reviews)
    queue_approved(reviews,prep)
    ack=read(STAGE/'hq-ack.json');owner_check(ack,action,prep)
    signal.setitimer(signal.ITIMER_REAL,min(ack['expires_wall']-time.time(),ack['expires_mono']-time.monotonic(),900))
    return action,tree,reviews,ack

def initial_checks(prep,action,reviews):
    baseline=action['action']['baseline']
    require(BOOT.read_text().strip() == baseline['boot_id'],'baseline boot drift')
    require(prep.file_hash(protected(SEAL)) == baseline['seal_sha256'] and metadata(SEAL,prep) == baseline['seal_metadata'],'original complete seal/metadata drift')
    seal=read(SEAL);seal_valid(seal,prep)
    for path,guard in baseline['observed_guards'].items():
        check_original(Path(path),dict(state='present',kind='file',sha256=guard['sha256'],metadata=guard['metadata']),prep)
    for change in action['action']['changes']:check_original(Path(change['target']),change['old'],prep)
    quiet(prep);new=read(STAGE/'validation.next.json');next_seal(seal,new,action,reviews,prep)
    return seal,new

def fsync_dir(path):
    fd=os.open(path,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW)
    try:os.fsync(fd)
    finally:os.close(fd)

def write_exclusive(path,raw,mode=0o600):
    fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,mode)
    with os.fdopen(fd,'wb') as stream:stream.write(raw);stream.flush();os.fsync(stream.fileno())
    fsync_dir(path.parent)

def checkpoint(record,prep):
    # Fixed private journal, poison survives any failure; never delete/replay.
    temp=JOURNAL.with_suffix('.next')
    write_exclusive(temp,prep.canonical(record));os.replace(temp,JOURNAL);fsync_dir(ROOT)

def backup(path,destination,prep):
    shutil.copy2(path,destination,follow_symlinks=False)
    info=path.lstat();os.chown(destination,info.st_uid,info.st_gid,follow_symlinks=False)
    for name in os.listxattr(path,follow_symlinks=False):os.setxattr(destination,name,os.getxattr(path,name,follow_symlinks=False),follow_symlinks=False)
    require(prep.file_hash(path) == prep.file_hash(destination),'backup byte mismatch')
    require(xattrs(path) == xattrs(destination),'backup xattr mismatch')
    with destination.open('rb') as stream:os.fsync(stream.fileno())
    write_exclusive(destination.with_name(destination.name+'.metadata.json'),prep.canonical({'original':metadata(path,prep),'xattrs':xattrs(path)}))

def parents(path):
    # Pin EVERY component with openat(O_NOFOLLOW), including deploy-owned
    # ancestors. The returned descriptor, never a re-resolved pathname, is
    # used for privileged rename. Concurrent replacement can only orphan it.
    fd=os.open('/',os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW)
    try:
        for name in path.parent.parts[1:]:
            try:child=os.open(name,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=fd)
            except FileNotFoundError:
                os.mkdir(name,mode=0o755,dir_fd=fd)
                child=os.open(name,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=fd)
            except OSError as exc:raise PermissionError('unsafe target ancestor') from exc
            os.close(fd);fd=child
        return fd
    except BaseException:
        os.close(fd);raise

def install_file(source,target,new):
    fd=parents(target)
    temp='.'+target.name+'.strict542-598'
    try:
        out=os.open(temp,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,new['mode'],dir_fd=fd)
        with os.fdopen(out,'wb') as stream:
            with source.open('rb') as incoming:shutil.copyfileobj(incoming,stream,1024*1024)
            os.fchmod(stream.fileno(),new['mode']);os.fchown(stream.fileno(),new['uid'],new['gid']);stream.flush();os.fsync(stream.fileno())
        os.replace(temp,target.name,src_dir_fd=fd,dst_dir_fd=fd);os.fsync(fd)
    finally:os.close(fd)

def verify_guards(action,prep):
    for path,guard in action['action']['baseline']['observed_guards'].items():
        check_original(Path(path),dict(state='present',kind='file',sha256=guard['sha256'],metadata=guard['metadata']),prep)

def verify_disk(action,tree,prep):
    verify_guards(action,prep)
    for change in action['action']['changes']:
        target=Path(change['target']);new=change['new']
        if change['source'] == 'runtime':
            prep.check_tree(tree,target)
            for path in (target,*target.rglob('*')):
                info=path.lstat();require(info.st_uid == 0 and info.st_gid == 0,'runtime root ownership drift')
        else:
            info=target.lstat()
            require(not target.is_symlink() and prep.file_hash(target) == new['sha256'] and
                (stat.S_IMODE(info.st_mode),info.st_uid,info.st_gid) == (new['mode'],new['uid'],new['gid']),'installed target drift')
    require(prep.file_hash(SEAL) == prep.file_hash(STAGE/'validation.next.json'),'installed full seal differs')
    seal_valid(read(SEAL),prep)

def apply(action,tree,reviews,ack,prep):
    require(not os.path.lexists(JOURNAL),'application attempted already; independent reconciliation required')
    initial_checks(prep,action,reviews)
    directory=Path(action['action']['exclusive_backup_root'])
    require(directory.parent == Path('/var/backups/strict542-598') and prep.hexid(directory.name),'fixed exclusive backup root required')
    directory.parent.mkdir(mode=0o700,exist_ok=True);protected(directory.parent);directory.mkdir(mode=0o700)
    record={'state':'INCOMPLETE_POISON','action_sha256':action['action_sha256'],'backup':str(directory),'completed':[]}
    write_exclusive(JOURNAL,prep.canonical(record))
    backup(SEAL,directory/'original-full-seal',prep)
    for item in action['action']['backup_inventory']:
        if item['target'] == str(SEAL):continue
        target=Path(item['target']);dest=directory/item['backup_name']
        if item['original']['state'] == 'absent':write_exclusive(dest.with_suffix('.ABSENT'),prep.canonical(item))
        else:backup(target,dest,prep)
    for item in action['action']['unchanged_guard_backup_inventory']:backup(Path(item['target']),directory/item['backup_name'],prep)
    fsync_dir(directory)
    # Backups/reads may take time. Recheck genuine owner, clocks, original full
    # state and settlement before first mutation and before each fixed write.
    initial_checks(prep,action,reviews)
    for change in action['action']['changes']:
        owner_check(ack,action,prep);quiet(prep);source=STAGE/change['source'];target=Path(change['target'])
        if change['source'] == 'runtime':
            ancestor_fd=parents(target);os.close(ancestor_fd)
            # Runtime path has exclusively root-owned ancestors, unlike dropin.
            protected(target.parent);shutil.copytree(source,target,symlinks=True)
            for path in (target,*target.rglob('*')):os.chown(path,0,0,follow_symlinks=False)
            prep.check_tree(tree,target);fsync_dir(target.parent)
        else:install_file(source,target,change['new'])
        record['completed'].append(change['target']);checkpoint(record,prep)
    owner_check(ack,action,prep);quiet(prep)
    # This exact next ledger was independently reviewed; helper creates none.
    verify_guards(action,prep)
    info=SEAL.stat();install_file(STAGE/'validation.next.json',SEAL,dict(mode=stat.S_IMODE(info.st_mode),uid=info.st_uid,gid=info.st_gid))
    verify_disk(action,tree,prep)
    record['state']='DISK_APPLIED_SERVICES_UNCHANGED';checkpoint(record,prep)
    return record

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('command',choices=('preflight','apply','verify'));args=parser.parse_args()
    try:
        require(os.geteuid() == 0,'root required')
        signal.signal(signal.SIGALRM,expired);signal.setitimer(signal.ITIMER_REAL,900)
        protected(STAGE)
        prep=preparation();protected(LOCK)
        with LOCK.open('r+') as stream:
            fcntl.flock(stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
            action,tree,reviews,ack=load(prep)
            if args.command == 'verify':
                require(read(JOURNAL).get('state') == 'DISK_APPLIED_SERVICES_UNCHANGED','not a complete disk application')
                quiet(prep);verify_disk(action,tree,prep);print('DISK_VERIFIED_ONLY; no restart, loaded generation, fresh postrestart HQ or accepted-run proof')
            elif args.command == 'preflight':
                require(not os.path.lexists(JOURNAL),'previous attempt requires independent reconciliation')
                initial_checks(prep,action,reviews);print('PREFLIGHT_ONLY; no installation')
            else:print(prep.canonical(apply(action,tree,reviews,ack,prep)).decode(),end='')
    except (OSError,ValueError,KeyError,TypeError,PermissionError) as exc:parser.exit(2,'REFUSED; preserve journal/backups: '+str(exc)+'\n')

if __name__ == '__main__':main()
