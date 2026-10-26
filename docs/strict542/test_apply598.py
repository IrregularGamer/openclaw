"""Isolated disk-application refusal tests; no root/service/native operations."""
import importlib.util
from pathlib import Path
import tempfile
import os
import sqlite3
import hashlib
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

if __name__ == '__main__':unittest.main()
