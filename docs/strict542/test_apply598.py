"""Isolated disk-application refusal tests; no root/service/native operations."""
import importlib.util
from pathlib import Path
import tempfile
import os
import sqlite3
import hashlib
import json
from unittest.mock import patch
from types import SimpleNamespace
import unittest

spec=importlib.util.spec_from_file_location('apply598',Path(__file__).with_name('apply598.py'))
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)

class Application(unittest.TestCase):
    def test_new_release_parent_directories(self):
        with tempfile.TemporaryDirectory() as root:
            target=Path(root)/'opt'/'openclaw-strict542'/'598'/'runtime'
            try:
                os.close(a.parents(target))
            except PermissionError as exc:
                self.fail('new fixed release ancestors must be created: '+str(exc))
            self.assertTrue(target.parent.is_dir())
            self.assertFalse(target.exists())
    def test_symlink_ancestor_refuses(self):
        with tempfile.TemporaryDirectory() as root:
            base=Path(root);(base/'real').mkdir();(base/'link').symlink_to(base/'real')
            with self.assertRaises(PermissionError):a.parents(base/'link'/'release'/'runtime')
            self.assertFalse((base/'real'/'release').exists())
    def test_file_ancestor_refuses(self):
        with tempfile.TemporaryDirectory() as root:
            base=Path(root);(base/'file').write_text('fixture')
            with self.assertRaises(PermissionError):a.parents(base/'file'/'runtime')

class GuardedApplication(unittest.TestCase):
    def test_original_seal_accepts_only_exact_existing_link_and_target_bytes(self):
        with tempfile.TemporaryDirectory() as root:
            base=Path(root);target=base/'devstack-source';target.write_bytes(b'sealed source')
            link=base/'devstack';link.symlink_to(target)
            digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
            prep=SimpleNamespace(hexid=lambda h:len(h)==64,file_hash=digest)
            seal={'installed_hashes':{str(link):digest(target)}}
            with patch.object(a,'ORIGINAL_SEAL_LINKS',{str(link):str(target)},create=True):
                a.seal_valid(seal,prep)
                other=base/'other';other.write_bytes(target.read_bytes())
                link.unlink();link.symlink_to(other)
                with self.assertRaisesRegex(PermissionError,'original sealed link drift'):a.seal_valid(seal,prep)
                link.unlink();link.symlink_to(target);target.write_bytes(b'changed')
                with self.assertRaisesRegex(PermissionError,'installed seal drift'):a.seal_valid(seal,prep)
                link.unlink();link.write_bytes(b'sealed source')
                with self.assertRaisesRegex(PermissionError,'original sealed link drift'):a.seal_valid(seal,prep)
            unlisted=base/'new-link';unlisted.symlink_to(target)
            with self.assertRaisesRegex(PermissionError,'installed seal drift'):
                a.seal_valid({'installed_hashes':{str(unlisted):digest(target)}},prep)

    def test_queue_gate_requires_actual_done_build_matching_review_and_exact_result(self):
        with tempfile.TemporaryDirectory() as root,patch.object(a,'DB',Path(root)/'queue.db'):
            result='fixture independently recorded result\nVERDICT: APPROVE'
            digest=lambda raw:hashlib.sha256(raw).hexdigest()
            prep=SimpleNamespace(PREPARATION_JOB_ID=608,sha=digest)
            review={'scope':'automatic-queue','build_job_id':608,'review_job_id':609,'queue_result_sha256':digest(result.encode())}
            with sqlite3.connect(a.DB) as db:
                db.execute('CREATE TABLE jobs(id INTEGER,kind TEXT,status TEXT,parent_id INTEGER,result TEXT)')
                db.executemany('INSERT INTO jobs VALUES(?,?,?,?,?)',[(608,'build','review',605,None),(609,'review','done',608,result)])
            with self.assertRaisesRegex(PermissionError,'actual automatic queue approval'):a.queue_approved([review],prep)
            with sqlite3.connect(a.DB) as db:db.execute("UPDATE jobs SET status='done' WHERE id=608")
            a.queue_approved([review],prep)
            for refused in ('VERDICT: CHANGES', 'VERDICT: CHANGES\nVERDICT: APPROVE', 'no verdict'):
                with sqlite3.connect(a.DB) as db:db.execute('UPDATE jobs SET result=? WHERE id=609',(refused,))
                with self.assertRaisesRegex(PermissionError,'did not approve'):
                    a.queue_approved([{**review,'queue_result_sha256':digest(refused.encode())}],prep)
            with sqlite3.connect(a.DB) as db:db.execute('UPDATE jobs SET result=? WHERE id=609',(result,))
            for key,value in [('build_job_id',598),('review_job_id',999),('queue_result_sha256','f'*64)]:
                with self.assertRaises(PermissionError):a.queue_approved([{**review,key:value}],prep)
            with sqlite3.connect(a.DB) as db:db.execute('UPDATE jobs SET parent_id=598 WHERE id=609')
            with self.assertRaises(PermissionError):a.queue_approved([review],prep)

    def test_intermediate_directory_replacement_cannot_redirect_privileged_write(self):
        with tempfile.TemporaryDirectory() as root:
            base=Path(root);parent=base/'owned';parent.mkdir();outside=base/'outside';outside.mkdir()
            source=base/'source';source.write_text('reviewed bytes');target=parent/'dropin'
            fd=a.parents(target)
            parent.rename(base/'moved');parent.symlink_to(outside)
            with patch.object(a,'parents',return_value=fd):
                a.install_file(source,target,dict(mode=0o644,uid=os.getuid(),gid=os.getgid()))
            self.assertFalse((outside/'dropin').exists())
            self.assertEqual((base/'moved'/'dropin').read_text(),'reviewed bytes')

    def test_unchanged_guard_drift_refuses_final_verification(self):
        guard={'sha256':'synthetic','metadata':{}}
        action={'action':{'baseline':{'observed_guards':{'/guard':guard}}}}
        with patch.object(a,'check_original',side_effect=PermissionError('guard drift')):
            with self.assertRaisesRegex(PermissionError,'guard drift'):a.verify_disk(action,{},None)

    def test_native_quiet_requires_valid_registered_worker(self):
        controller=SimpleNamespace(registry=lambda:{'reconciled':True},valid_registration=lambda value:False)
        loader=SimpleNamespace(exec_module=lambda module:setattr(module,'Controller',lambda **kw:controller))
        with patch.object(a,'protected',side_effect=lambda path:path),patch.object(a.importlib.util,'spec_from_file_location',return_value=SimpleNamespace(loader=loader)),patch.object(a.importlib.util,'module_from_spec',return_value=SimpleNamespace()):
            with self.assertRaisesRegex(PermissionError,'valid settled registration'):a.native_quiet(None)

    def test_native_quiet_refuses_fixture_or_remote_uncertainty(self):
        worker={'job_id':598,'unit':'fixed','attempt':1,'epoch':1,'invocation':'fixed','reconciled':True}
        controller=SimpleNamespace(registry=lambda:worker,valid_registration=lambda value:True)
        loader=SimpleNamespace(exec_module=lambda module:setattr(module,'Controller',lambda **kw:controller))
        native=SimpleNamespace(Native510=lambda c:SimpleNamespace(quiet=lambda identity:False))
        with patch.object(a,'protected',side_effect=lambda path:path),patch.object(a.importlib.util,'spec_from_file_location',return_value=SimpleNamespace(loader=loader)),patch.object(a.importlib.util,'module_from_spec',return_value=SimpleNamespace()),patch.object(a,'native_module',return_value=native):
            with self.assertRaisesRegex(PermissionError,'fixture/remote work unsettled'):a.native_quiet(None)

    def test_absolute_lifetime_interrupts_with_refusal(self):
        with self.assertRaisesRegex(PermissionError,'finite application lifetime'):
            a.expired(14,None)

    def test_previous_application_journal_refuses_replay(self):
        with tempfile.TemporaryDirectory() as root,patch.object(a,'JOURNAL',Path(root)/'journal'):
            a.JOURNAL.write_text('poison')
            with patch.object(a,'initial_checks') as check:
                with self.assertRaisesRegex(PermissionError,'attempted already'):a.apply({}, {}, [], {},None)
                check.assert_not_called()

class RollbackApplication(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.base=Path(self.temp.name)
        self.stage=self.base/'stage';self.stage.mkdir()
        self.backups=self.base/'backups';self.backups.mkdir()
        self.directory=self.backups/('1'*64);self.directory.mkdir()
        self.seal=self.base/'validation.json';self.journal=self.base/'journal.json'
        self.guard=self.base/'guard';self.guard.write_bytes(b'unchanged guard')
        spec=importlib.util.spec_from_file_location('rollback_prep_fixture',Path(__file__).with_name('application598.py'))
        self.prep=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.prep)
        self.original_seal={'installed_hashes':{str(self.guard):self.prep.file_hash(self.guard)},'amendments':[]}
        self.seal.write_bytes(self.prep.canonical(self.original_seal))
        original_seal_metadata=a.metadata(self.seal,self.prep)
        a.backup(self.seal,self.directory/'original-full-seal',self.prep)
        guard={'sha256':self.prep.file_hash(self.guard),'metadata':a.metadata(self.guard,self.prep)}
        a.backup(self.guard,self.directory/'guard-0',self.prep)
        self.targets={name:str(self.base/'targets'/name) for name in ('runtime','native','server','supervisor','unit','dropin')}
        Path(self.targets['runtime']).mkdir(parents=True,mode=0o755)
        (Path(self.targets['runtime'])/'entry').write_bytes(b'exact runtime')
        self.entries=self.prep.inventory(Path(self.targets['runtime']))
        self.tree={'entries':self.entries}
        self.changes=[];inventory=[]
        for index,(name,target) in enumerate(self.targets.items()):
            path=Path(target)
            if name=='runtime':new={'kind':'directory-tree','sha256':self.prep.digest(self.entries),'mode':0o755,'uid':os.getuid(),'gid':os.getgid()}
            else:
                path.write_bytes(('exact '+name).encode());path.chmod(0o644)
                new={'kind':'file','sha256':self.prep.file_hash(path),'mode':0o644,'uid':os.getuid(),'gid':os.getgid()}
            old={'state':'absent'}
            self.changes.append({'source':name,'target':target,'old':old,'new':new})
            item={'target':target,'original':old,'backup_name':str(index),'preserve':['bytes','mode','uid','gid','xattrs','timestamps']}
            inventory.append(item)
            (self.directory/(str(index)+'.ABSENT')).write_bytes(self.prep.canonical(item))
        self.action={'action_sha256':'2'*64,'action':{'changes':self.changes,'exclusive_backup_root':str(self.directory),
            'baseline':{'boot_id':'fixture-boot','seal_sha256':self.prep.file_hash(self.seal),'seal_metadata':original_seal_metadata,'observed_guards':{str(self.guard):guard}},
            'backup_inventory':inventory+[{'target':str(self.seal),'backup_name':'original-full-seal'}],
            'unchanged_guard_backup_inventory':[{'target':str(self.guard),'original':guard,'backup_name':'guard-0'}]}}
        self.ack={'boot_id':'fixture-boot','owner':{'name':'Pinch','session':'genuine-fixture','pid':123,'start':'456'}}
        self.record={'state':'DISK_APPLIED_SERVICES_UNCHANGED','action_sha256':self.action['action_sha256'],
            'backup':str(self.directory),'completed':[item['target'] for item in self.changes],
            'application_owner':{'boot_id':self.ack['boot_id'],'owner':self.ack['owner']}}
        self.journal.write_bytes(self.prep.canonical(self.record))
        self.next_seal={'installed_hashes':dict(self.original_seal['installed_hashes']),'amendments':[{'kind':'strict542-598','action_sha256':self.action['action_sha256']}]}
        self.seal.write_bytes(self.prep.canonical(self.next_seal))
        (self.stage/'validation.next.json').write_bytes(self.prep.canonical(self.next_seal))
        self.patches=[patch.object(a,'STAGE',self.stage),patch.object(a,'SEAL',self.seal),patch.object(a,'JOURNAL',self.journal),
            patch.object(a,'ROOT',self.base),patch.object(a,'BACKUP_ROOT',self.backups,create=True),
            patch.object(a,'protected',side_effect=lambda path:path),patch.object(a,'owner_check'),patch.object(a,'quiet'),
            patch.object(a,'rollback_service_unchanged',create=True),patch.object(a,'verify_disk'),patch.object(a,'next_seal'),
            patch.object(self.prep,'TARGETS',self.targets),patch.object(self.prep,'check_tree',side_effect=self.check_tree)]
        for p in self.patches:p.start();self.addCleanup(p.stop)

    def check_tree(self,tree,runtime):
        self.assertEqual(self.prep.inventory(runtime),self.entries)

    def rollback(self):return a.rollback(self.action,self.tree,[],self.ack,self.prep)

    def test_complete_unchanged_owner_rolls_back_by_quarantining_all_exact_new_targets(self):
        result=self.rollback()
        self.assertEqual(result['state'],'ROLLED_BACK_SERVICES_UNCHANGED')
        self.assertEqual(self.seal.read_bytes(),self.prep.canonical(self.original_seal))
        self.assertTrue(all(not os.path.lexists(target) for target in self.targets.values()))
        quarantine=self.directory/'rollback-quarantine'
        self.assertEqual(sorted(p.name for p in quarantine.iterdir()),[str(i) for i in range(6)])
        self.assertEqual((quarantine/'0'/'entry').read_bytes(),b'exact runtime')
        self.assertEqual((quarantine/'5').read_bytes(),b'exact dropin')
        self.assertEqual(self.prep.file_hash(self.directory/'original-full-seal'),self.action['action']['baseline']['seal_sha256'])
        self.assertEqual(result['restored_seal_metadata']['mtime_ns'],self.action['action']['baseline']['seal_metadata']['mtime_ns'])
        self.assertIn('ctime',result['metadata_limit'])
        with self.assertRaisesRegex(PermissionError,'complete disk application'):self.rollback()

    def test_partial_old_or_postrestart_owner_journals_refuse_without_mutation(self):
        for changed in ({**self.record,'state':'INCOMPLETE_POISON'},
                {k:v for k,v in self.record.items() if k!='application_owner'},
                {**self.record,'application_owner':{'boot_id':'fixture-boot','owner':{**self.ack['owner'],'start':'different'}}},
                {**self.record,'completed':self.record['completed'][:-1]}):
            self.journal.write_bytes(self.prep.canonical(changed))
            with self.assertRaises(PermissionError):self.rollback()
            self.assertTrue(all(os.path.lexists(target) for target in self.targets.values()))
            self.assertFalse((self.directory/'rollback-quarantine').exists())

    def test_nonabsent_baseline_or_changed_backup_or_new_bytes_refuses_before_quarantine(self):
        self.changes[0]['old']={'state':'present'}
        with self.assertRaisesRegex(PermissionError,'originally absent'):self.rollback()
        self.changes[0]['old']={'state':'absent'}
        marker=self.directory/'0.ABSENT';raw=marker.read_bytes();marker.write_bytes(b'changed')
        with self.assertRaisesRegex(PermissionError,'absence backup'):self.rollback()
        marker.write_bytes(raw)
        original=self.directory/'original-full-seal';original.write_bytes(b'changed')
        with self.assertRaisesRegex(PermissionError,'backup'):self.rollback()
        self.assertFalse((self.directory/'rollback-quarantine').exists())

    def test_changed_new_file_or_runtime_refuses_before_first_mutation(self):
        for name in ('native','runtime'):
            path=Path(self.targets[name]);path=path/'entry' if name=='runtime' else path
            raw=path.read_bytes();path.write_bytes(b'changed')
            with self.assertRaises((PermissionError,AssertionError)):self.rollback()
            path.write_bytes(raw)
            self.assertFalse((self.directory/'rollback-quarantine').exists())

    def test_quarantine_failure_poison_survives_and_cannot_be_replayed(self):
        with patch.object(a.os,'rename',side_effect=OSError('cross-device refusal')):
            with self.assertRaisesRegex(OSError,'cross-device'):self.rollback()
        self.assertEqual(json.loads(self.journal.read_bytes())['state'],'ROLLBACK_INCOMPLETE_POISON')
        with self.assertRaisesRegex(PermissionError,'complete disk application'):self.rollback()

    def test_started_root_supervisor_refuses(self):
        # Exercise the real fixed read-only predicate without invoking systemctl
        # or inspecting the installed socket. Fixtures cover prior start, active
        # service, missing status, unreadable manager and stale socket refusal.
        self.patches[8].stop()
        inactive='MainPID=0\nActiveState=inactive\nExecMainStartTimestampMonotonic=0\n'
        with patch.object(a.os.path,'lexists',return_value=False),patch.object(a,'run',return_value=SimpleNamespace(returncode=0,stdout=inactive)) as command:
            a.rollback_service_unchanged()
            self.assertEqual(command.call_args.kwargs['timeout'],5)
            self.assertEqual(command.call_args.args[0][:3],['/usr/bin/systemctl','show','strict542-owner.service'])
        for text,code,socket_present in ((inactive.replace('Monotonic=0','Monotonic=123'),0,False),
                (inactive.replace('MainPID=0','MainPID=12'),0,False),
                (inactive.replace('inactive','active'),0,False),('',0,False),(inactive,1,False),(inactive,0,True)):
            with patch.object(a.os.path,'lexists',return_value=socket_present),patch.object(a,'run',return_value=SimpleNamespace(returncode=code,stdout=text)):
                with self.assertRaisesRegex(PermissionError,'supervisor'):a.rollback_service_unchanged()

if __name__ == '__main__':unittest.main()
