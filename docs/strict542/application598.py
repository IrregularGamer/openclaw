#!/usr/bin/env python3
"""Canonical secretless release receipts and action PREPARATION; never applies."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat

NATIVE_SHA = 'bca40971a35d160ad87b5d18fd1cc7f7730a7f90d2bb5b8480f3d7d79d11c182'
PREFIX = '/opt/openclaw-strict542/598'
TARGETS = {
    'runtime': PREFIX + '/runtime',
    'maintenance.py': PREFIX + '/native/maintenance.py',
    'native_owner_server542.py': '/usr/local/libexec/agentq-safety/native_owner_server542.py',
    'root_owner_supervisor542.py': '/usr/local/libexec/agentq-safety/root_owner_supervisor542.py',
    'strict542-owner.service': '/etc/systemd/system/strict542-owner.service',
    '90-strict542-598.conf': '/home/deploy/.config/systemd/user/openclaw-gateway.service.d/90-strict542-598.conf',
}
GUARDS = {
    '/home/deploy/.config/systemd/user/openclaw-gateway.service',
    '/home/deploy/.config/systemd/user/openclaw-gateway.service.d/60-stop-budget.conf',
    '/home/deploy/.config/systemd/user/openclaw-gateway.service.d/70-heap-cap.conf',
    '/usr/local/libexec/agentq-safety/control.py',
    '/usr/local/libexec/agentq-safety/maintenance.py',
    '/home/deploy/.local/lib/node_modules/openclaw/package.json',
    '/home/deploy/.local/lib/node_modules/openclaw/dist/index.js',
}
CHECKS = {'gateway-scoped', 'native-owner', 'supervisor-ipc', 'cancellation-settlement', 'application-preparation'}

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode() + b'\n'

def digest(value):
    return sha(canonical(value))

def require(condition, reason):
    if not condition:
        raise ValueError(reason)

def hexid(value, length=64):
    return isinstance(value, str) and re.fullmatch('[0-9a-f]{%d}' % length, value) is not None

def read_json(path):
    require(path.stat().st_size <= 64*1024*1024, 'oversized JSON')
    return json.loads(path.read_bytes())

def file_hash(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

def safe_name(name):
    lower = name.lower()
    return not (lower.startswith('.env') or lower in {
        '.git', '.openclaw', 'auth.json', 'auth-profiles.json', 'credentials.json',
        'openclaw.json', 'sessions.json', 'id_rsa', 'id_ed25519', 'cookiejar',
    } or lower.endswith(('.db', '.sqlite', '.sqlite3', '.pem', '.key')))

def inventory(root):
    require(root.is_dir() and not root.is_symlink(), 'runtime must be a real directory')
    require(stat.S_IMODE(root.stat().st_mode) == 0o755, 'runtime root must have exact0755 mode')
    root = root.resolve()
    entries = []
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root).as_posix()
        require(all(safe_name(part) for part in Path(relative).parts), 'forbidden secret/state name: ' + relative)
        info = path.lstat()
        mode = stat.S_IMODE(info.st_mode)
        require(stat.S_ISLNK(info.st_mode) or not mode & 0o7022, 'special or writable-by-group/other mode: ' + relative)
        entry = {'path': relative, 'mode': mode}
        if stat.S_ISLNK(info.st_mode):
            # Symlink permission bits are conventionally0777 and do not grant
            # write access. Their target must exist and remain in this tree.
            target = os.readlink(path)
            require(not os.path.isabs(target), 'absolute symlink')
            try:
                resolved = path.resolve(strict=True)
            except (OSError, RuntimeError) as exc:
                raise ValueError('broken/cyclic symlink') from exc
            require(resolved.is_relative_to(root), 'escaping symlink')
            entry.update(kind='symlink', target=target)
        elif stat.S_ISREG(info.st_mode):
            require(info.st_nlink == 1, 'hardlink refused: ' + relative)
            entry.update(kind='file', size=info.st_size, sha256=file_hash(path))
        elif stat.S_ISDIR(info.st_mode):
            entry.update(kind='directory')
        else:
            raise ValueError('special file refused: ' + relative)
        entries.append(entry)
        require(len(entries) <= 300000, 'runtime inventory too large')
    return entries

def evidence_shape(evidence, allow_fixture=False):
    require(isinstance(evidence, dict), 'invalid execution evidence')
    fixture = evidence.get('fixture', False)
    require(not fixture or allow_fixture, 'fixture evidence cannot claim a build')
    require(hexid(evidence.get('source_commit'),40) and hexid(evidence.get('source_export_sha256')), 'missing exact source/export identity')
    require(type(evidence.get('build_exit')) is int and evidence['build_exit'] == 0
            and type(evidence.get('test_exit')) is int and evidence['test_exit'] == 0, 'build/tests did not pass')
    require(evidence.get('execution') == 'admitted-offload' and isinstance(evidence.get('remote_run_id'), str)
            and evidence['remote_run_id'], 'missing admitted remote execution receipt')
    toolchain = evidence.get('toolchain', {})
    require(set(toolchain) == {'node','pnpm','python'} and all(isinstance(x,str) and x for x in toolchain.values()), 'incomplete toolchain')
    require(toolchain['pnpm'] == '12.5.1', 'unreviewed pnpm toolchain')
    match = re.fullmatch(r'v?(\d+)\.(\d+)\.(\d+)',toolchain['node'])
    require(match is not None and ((int(match[1]) == 24 and int(match[2]) >= 16)
            or (int(match[1]) == 26 and int(match[2]) >= 1) or int(match[1]) > 26), 'unsupported Node version')
    if not fixture:
        require(CHECKS <= set(evidence.get('checks', [])), 'missing relevant check evidence')
    return fixture

def validate_evidence(evidence, lockfile, build_log, test_log, allow_fixture=False):
    fixture = evidence_shape(evidence, allow_fixture)
    require(evidence.get('lockfile_sha256') == file_hash(lockfile), 'lockfile hash mismatch')
    require(build_log.is_file() and test_log.is_file() and build_log.stat().st_size and test_log.stat().st_size, 'empty/missing logs')
    require(evidence.get('build_log_sha256') == file_hash(build_log)
            and evidence.get('test_log_sha256') == file_hash(test_log), 'execution log digest mismatch')
    return fixture

def make_tree(runtime, lockfile, evidence_path, build_log, test_log, allow_fixture=False):
    evidence = read_json(evidence_path)
    fixture = validate_evidence(evidence, lockfile, build_log, test_log, allow_fixture)
    require((runtime/'dist/index.js').is_file() and (runtime/'package.json').is_file(), 'missing application build')
    require((runtime/'node_modules').is_dir() and any((runtime/'node_modules').iterdir()), 'missing production dependencies')
    entries = inventory(runtime)
    return {'schema': 'strict542-release598-v1', 'status': 'FIXTURE_ONLY' if fixture else 'BUILT',
            'execution_evidence': evidence, 'execution_evidence_sha256': digest(evidence),
            'root_mode':0o755, 'entries': entries, 'tree_sha256': digest(entries)}

def check_tree(receipt, runtime, allow_fixture=False):
    require(receipt.get('schema') == 'strict542-release598-v1', 'unknown tree schema')
    require(receipt.get('status') == 'BUILT' or (allow_fixture and receipt.get('status') == 'FIXTURE_ONLY'), 'tree is not a real built receipt')
    evidence_shape(receipt.get('execution_evidence'),allow_fixture)
    require(receipt.get('execution_evidence_sha256') == digest(receipt.get('execution_evidence')), 'execution evidence drift')
    require(receipt.get('root_mode') == 0o755, 'runtime root mode drift')
    require(receipt.get('tree_sha256') == digest(receipt.get('entries')), 'tree receipt drift')
    require(receipt.get('entries') == inventory(runtime), 'runtime changed since build receipt')
    return receipt

def metadata(value):
    require(isinstance(value,dict) and all(type(value.get(key)) is int and value[key] >= 0
            for key in ('mode','uid','gid','mtime_ns','ctime_ns'))
            and hexid(value.get('xattrs_sha256')), 'missing complete original metadata')
    return value

def baseline_inventory(baseline):
    require(set(baseline.get('targets',{})) == set(TARGETS.values()), 'baseline target inventory mismatch')
    require(hexid(baseline.get('seal_sha256')), 'missing original complete seal hash')
    require(isinstance(baseline.get('boot_id'), str) and baseline['boot_id'], 'missing original boot identity')
    metadata(baseline.get('seal_metadata'))
    require(isinstance(baseline.get('observed_guards'),dict) and set(baseline['observed_guards']) == GUARDS, 'missing exact unchanged original gateway/native guards')
    for path,guard in baseline['observed_guards'].items():
        require(path.startswith('/') and hexid(guard.get('sha256')), 'invalid original guard identity')
        metadata(guard.get('metadata'))
    for target, old in baseline['targets'].items():
        require(isinstance(old,dict) and old.get('state') in ('absent','present'), 'invalid original target state')
        if old['state'] == 'present':
            require(old.get('kind') == 'file' and hexid(old.get('sha256')) and type(old.get('mode')) is int
                    and type(old.get('uid')) is int and type(old.get('gid')) is int, 'missing original bytes/metadata')
            metadata(old.get('metadata'))
    require(baseline['targets'][TARGETS['runtime']]['state'] == 'absent', 'new release598 runtime must be absent')
    return baseline

def make_action(tree, stage, baseline):
    check_tree(tree,stage/'runtime')
    baseline_inventory(baseline)
    changes=[]
    for name,target in TARGETS.items():
        path=stage/name
        if name == 'runtime':
            new={'kind':'directory-tree','sha256':tree['tree_sha256'],'mode':0o755,'uid':0,'gid':0}
        else:
            require(path.is_file() and not path.is_symlink(), 'missing fixed staged file: '+name)
            new={'kind':'file','sha256':file_hash(path),'mode':0o644,'uid':0,'gid':0}
            if name == 'maintenance.py':require(new['sha256'] == NATIVE_SHA,'native source pin mismatch')
            if name == '90-strict542-598.conf':new.update(uid=1000,gid=1000)
        changes.append({'source':name,'target':target,'old':baseline['targets'][target],'new':new})
    payload={'schema':'strict542-action598-v1','source_commit':tree['execution_evidence']['source_commit'],
        'tree_receipt_sha256':digest(tree),'baseline':baseline,'changes':changes,
        'required_reviews':['source','action','privilege-policy'],
        'requirements':['original-full-seal-valid','native-admission-lock','natural-settled-no-worker-gap',
            'genuine-foreground-nonqueue-HQ','finite-dual-clock-window','fresh-post-restart-owner-binding',
            'fresh-post-restart-accepted-run-ack','original-predicates-unchanged','independent-loaded-generation-check'],
        'rollback':'Before gateway restart only: restore exact exclusive old-byte/full-metadata backups and remove only recorded-new absent targets under original lock/guards. After restart or partial seal/native action: refuse automatic rollback; independently review reconciliation and fresh HQ binding. Never replay historical installers.',
        'seal_policy':'Validate original complete seal and metadata first; never amend unrelated entries. Any exact new sealed target requires separate privilege/seal-policy review and exact old/new amendment. Preserve original whole seal, metadata/xattrs and hash; full seal must validate after application.'}
    payload['unchanged_guard_backup_inventory']=[{'target':path,'original':baseline['observed_guards'][path], 'backup_name':'guard-'+str(index)} for index,path in enumerate(sorted(GUARDS))]
    identity=digest(payload)
    payload['exclusive_backup_root']='/var/backups/strict542-598/'+identity
    payload['backup_inventory']=[{'target':change['target'],'original':change['old'],
        'backup_name':str(index),'preserve':['bytes','mode','uid','gid','xattrs','timestamps']} for index,change in enumerate(changes)]
    payload['backup_inventory'].append({'target':'/var/lib/agentq-safety/validation.json','sha256':baseline['seal_sha256'],
        'backup_name':'original-full-seal','preserve':['bytes','mode','uid','gid','xattrs','timestamps']})
    return {'action':payload,'action_sha256':digest(payload)}

def validate_action(action, tree, stage, reviews):
    require(action.get('action_sha256') == digest(action.get('action')), 'action digest drift')
    rebuilt=make_action(tree,stage,action['action']['baseline'])
    require(action == rebuilt, 'action or staged inventory drift')
    require(isinstance(reviews,list), 'review list required')
    for scope in ('source','action','privilege-policy'):
        matching=[r for r in reviews if r.get('scope') == scope]
        require(len(matching) == 1,'exact single independent '+scope+' review required')
        r=matching[0]
        require(r.get('verdict') == 'APPROVE' and r.get('action_sha256') == action['action_sha256']
                and r.get('tree_receipt_sha256') == digest(tree)
                and r.get('source_commit') == action['action']['source_commit'], 'review binding mismatch')
        require(isinstance(r.get('author'),str) and isinstance(r.get('reviewer'),str)
                and r['author'] and r['reviewer'] and r['author'] != r['reviewer'], 'independent reviewer required')
        require(hexid(r.get('review_receipt_sha256')), 'missing exact external review receipt digest')
    return {'status':'PREPARED_REVIEWED_NOT_APPLIED','action_sha256':action['action_sha256']}

def emit(path,value):
    # Exclusive output prevents accidental replacement of reviewed receipts.
    with path.open('xb') as stream:stream.write(canonical(value))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    tree=sub.add_parser('tree')
    for name in ('runtime','lockfile','build-evidence','build-log','test-log','output'):tree.add_argument('--'+name,type=Path,required=True)
    action=sub.add_parser('action')
    for name in ('tree','stage','baseline','output'):action.add_argument('--'+name,type=Path,required=True)
    validate=sub.add_parser('validate')
    for name in ('tree','stage','action','reviews'):validate.add_argument('--'+name,type=Path,required=True)
    args=parser.parse_args()
    try:
        if args.command == 'tree':emit(args.output,make_tree(args.runtime,args.lockfile,args.build_evidence,args.build_log,args.test_log))
        elif args.command == 'action':emit(args.output,make_action(read_json(args.tree),args.stage,read_json(args.baseline)))
        else:print(canonical(validate_action(read_json(args.action),read_json(args.tree),args.stage,read_json(args.reviews))).decode(),end='')
    except (ValueError,OSError,KeyError,TypeError) as exc:parser.exit(2,'REFUSED: '+str(exc)+'\n')

if __name__ == '__main__':main()
