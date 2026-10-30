"""Small local filesystem checks; no build, services, or remote inputs."""
import errno
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import sys
import unittest
from unittest.mock import patch

HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location('prepare608', HERE / 'prepare-stage608-export.py')
prepare = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prepare)


class LinkInputTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=HERE)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.src = self.root / 'producer'
        self.src.write_bytes(b'accepted checkpoint\n')
        self.digest = hashlib.sha256(self.src.read_bytes()).hexdigest()
        self.dst = self.root / 'consumer'

    def test_hardlink_preserves_producer_inode_bytes_and_mode(self):
        before = self.src.stat()
        self.assertEqual(prepare.link_input(self.src, self.dst, self.digest), self.digest)
        after = self.src.stat()
        self.assertEqual(self.src.read_bytes(), b'accepted checkpoint\n')
        self.assertEqual((before.st_dev, before.st_ino, before.st_mode, before.st_mtime_ns),
                         (after.st_dev, after.st_ino, after.st_mode, after.st_mtime_ns))
        self.assertEqual((after.st_dev, after.st_ino),
                         (self.dst.stat().st_dev, self.dst.stat().st_ino))

    def test_bad_digest_refused_before_link(self):
        with self.assertRaisesRegex(ValueError, 'digest'):
            prepare.link_input(self.src, self.dst, '0' * 64)
        self.assertFalse(self.dst.exists())

    def test_source_and_parent_symlinks_refused(self):
        alias = self.root / 'alias'
        alias.symlink_to(self.src)
        parent = self.root / 'parent'
        parent.symlink_to(self.root, target_is_directory=True)
        for src in (alias, parent / 'producer'):
            with self.subTest(src=src), self.assertRaisesRegex(ValueError, 'symlink'):
                prepare.link_input(src, self.dst, self.digest)
        self.assertFalse(self.dst.exists())

    def test_existing_destination_and_destination_symlink_parent_refused(self):
        self.dst.write_bytes(b'keep')
        with self.assertRaises(FileExistsError):
            prepare.link_input(self.src, self.dst, self.digest)
        self.assertEqual(self.dst.read_bytes(), b'keep')
        alias = self.root / 'alias'
        alias.symlink_to(self.root, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'symlink'):
            prepare.link_input(self.src, alias / 'new', self.digest)

    def test_cross_device_error_never_falls_back_to_copy(self):
        with patch.object(prepare.os, 'link', side_effect=OSError(errno.EXDEV, 'cross-device')):
            with self.assertRaisesRegex(ValueError, 'same filesystem'):
                prepare.link_input(self.src, self.dst, self.digest)
        self.assertFalse(self.dst.exists())
        self.assertEqual(prepare.sha(self.src), self.digest)

    def test_parent_traversal_refused(self):
        with self.assertRaisesRegex(ValueError, 'traversal'):
            prepare.link_input(self.root / '..' / self.root.name / 'producer', self.dst, self.digest)

    def test_new_export_replaces_inherited_runner_and_helper_identity(self):
        base=self.root/'base';base.mkdir();dest=self.root/'export'
        m={'source_commit':'old','successor_paths':[], 'native_stage_outputs':{},
           'run_id':'old-run','purpose':'test','runner_commit':'stale',
           'stage_helper_sha256':'stale'}
        for name,key in [('source598.tar','base_source_archive_sha256'),('native598.tar','native_export_sha256'),
                         ('rolldown608-source.tar.gz','compiler_upstream_archive_sha256')]:
            (base/name).write_bytes(name.encode());m[key]=prepare.sha(base/name)
        (base/'native608-stages').mkdir();(base/'export-manifest.json').write_text(json.dumps(m))
        helper=(HERE/'stage608.py').read_bytes();runner=b'#!/bin/sh\nexit 0\n'
        def git(*args):
            if args[0]=='rev-parse':return b'new-commit\n'
            if args[0] in ('diff','ls-tree'):return b''
            if args[0]=='show':return helper if args[1].endswith('/stage608.py') else runner
            raise AssertionError(args)
        def archive(*args,**kwargs):kwargs['stdout'].write(b'committed overlay')
        with patch.object(prepare,'git',side_effect=git),patch.object(prepare.subprocess,'run',side_effect=archive),\
             patch.object(sys,'argv',['prepare','--base',str(base),'--dest',str(dest),'--commit','new','--stage','native']):
            prepare.main()
        result=json.loads((dest/'export-manifest.json').read_text())
        self.assertEqual(result['runner_commit'],'new-commit')
        self.assertEqual(result['runner_sha256'],prepare.sha(dest/'run608.sh'))
        self.assertEqual(result['stage_helper_sha256'],prepare.sha(dest/'stage608.py'))



class InputLineageTest(unittest.TestCase):
    """Decision662 Option B: package-only reviewed lineage; default binding unchanged."""
    A,C='a'*40,'c'*40

    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(dir=HERE);self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        import stage608 as st;self.st=st
        base=self.base=self.root/'base';base.mkdir()
        addon=b'addon';compile_bytes=json.dumps({'addon_sha256':hashlib.sha256(addon).hexdigest()}).encode();lib=b'{"lib":1}'
        self.files={'native/receipt.json':compile_bytes,'native/libtests-receipt.json':lib,'native/'+st.ADDON:addon,
                    'checks/tests.log':b'c\n','checks/installed.json':b'{}','compiler/tests.log':b'k\n',
                    'tail/checkpoint.tar.gz':b'tar','tail/build.log':b'b\n'}
        h=lambda b:hashlib.sha256(b).hexdigest()
        m={'source_commit':'old','successor_paths':[],'run_id':'old-run','purpose':'p','runner_commit':'s','stage_helper_sha256':'s',
           'native_stage_outputs':{'compile/receipt.json':h(compile_bytes),'libtests/receipt.json':h(lib)}}
        for name,key in [('source598.tar','base_source_archive_sha256'),('native598.tar','native_export_sha256'),
                         ('rolldown608-source.tar.gz','compiler_upstream_archive_sha256')]:
            (base/name).write_bytes(name.encode());m[key]=prepare.sha(base/name)
        for k,b in [('compile/receipt.json',compile_bytes),('libtests/receipt.json',lib)]:
            (base/'native608-stages'/k).parent.mkdir(parents=True,exist_ok=True);(base/'native608-stages'/k).write_bytes(b)
        (base/'export-manifest.json').write_text(json.dumps(m))
        ident={'base_source_archive_sha256':m['base_source_archive_sha256'],'source_commit':self.C,'successor_archive_sha256':h(b'committed overlay')}
        self.c_export=h(json.dumps(ident,sort_keys=True,separators=(',',':')).encode());self.a_export='e'*64
        self.diff=['docs/strict542/build598.sh','docs/strict542/frozen-package608.py','docs/strict542/job608-x/evidence.md']
        self.ancestor=0

    def producer(self,stage,commit):
        d=self.root/('result-'+stage);export=self.c_export if commit==self.C else self.a_export
        outs={o:hashlib.sha256(self.files[o]).hexdigest() for o in self.st.OUTPUTS[stage]}
        for o in self.st.OUTPUTS[stage]:(d/o).parent.mkdir(parents=True,exist_ok=True);(d/o).write_bytes(self.files[o])
        (d/stage/'stage-receipt.json').write_text(json.dumps({'kind':'JOB608_STAGE_RECEIPT','stage':stage,'exit_code':0,
            'source_commit':commit,'source_export_sha256':export,'outputs':outs}))
        (d/'exit-code.txt').write_text('0\n');return d

    def run_prepare(self,commits,stage='package',lineage=True):
        dest=self.root/'export';helper=(HERE/'stage608.py').read_bytes()
        def git(*args):
            if args[0]=='rev-parse':return (self.A if args[1].startswith('anc') else self.C).encode()+b'\n'
            if args[0]=='diff':return ('\n'.join(self.diff)+'\n').encode() if args[2]==self.A else b''
            if args[0]=='ls-tree':return b''
            if args[0]=='show':return helper if args[1].endswith('/stage608.py') else b'#!/bin/sh\n'
            raise AssertionError(args)
        class R:returncode=0
        def run(cmd,**kw):
            if 'stdout' in kw:kw['stdout'].write(b'committed overlay');return R()
            assert cmd[3:5]==['merge-base','--is-ancestor'],cmd;r=R();r.returncode=self.ancestor;return r
        argv=['prepare','--base',str(self.base),'--dest',str(dest),'--commit','new','--stage',stage]
        argv+=sum((['--input',str(self.producer(n,c))] for n,c in commits.items()),[])
        if lineage:argv+=['--lineage-ancestor','anc']
        with patch.object(prepare,'git',side_effect=git),patch.object(prepare.subprocess,'run',side_effect=run),patch.object(sys,'argv',argv):
            prepare.main()
        return dest

    def b246(self):return {'native':self.A,'checks':self.C,'compiler':self.A,'tail':self.A}

    def test_accepts_exact_b246_case_and_remote_verify_agrees(self):
        dest=self.run_prepare(self.b246());m=json.loads((dest/'export-manifest.json').read_text())
        lin=m['input_lineage'];self.assertEqual((lin['ancestor_commit'],lin['ancestor_source_export_sha256']),(self.A,self.a_export))
        self.assertEqual(sorted(lin['stages']),['compiler','native','tail']);self.assertEqual(lin['changed_paths'],sorted(self.diff))
        self.assertEqual(lin['receipt_sha256']['tail'],m['stage_inputs']['tail/stage-receipt.json'])
        self.st.verify_inputs(dest)

    def test_refuses_non_ancestor(self):
        self.ancestor=1
        with self.assertRaisesRegex(AssertionError,'not an ancestor'):self.run_prepare(self.b246())

    def test_refuses_non_allowlisted_changed_path(self):
        self.diff.append('docs/strict542/run-stage608.sh')
        with self.assertRaisesRegex(AssertionError,'not allowed'):self.run_prepare(self.b246())

    def test_refuses_checks_receipt_from_ancestor(self):
        with self.assertRaisesRegex(AssertionError,'may not use input lineage'):self.run_prepare({**self.b246(),'checks':self.A})

    def test_default_binding_still_refuses_ancestor_receipts(self):
        with self.assertRaises(AssertionError):self.run_prepare(self.b246(),lineage=False)

    def test_lineage_is_package_only(self):
        with self.assertRaisesRegex(AssertionError,'package-only'):self.run_prepare({'native':self.A},stage='compiler')

    def test_remote_verify_refuses_tampered_lineage_record(self):
        dest=self.run_prepare(self.b246());p=dest/'export-manifest.json'
        for tamper in [lambda l:l['changed_paths'].append('docs/strict542/run-stage608.sh'),lambda l:l['stages'].append('checks'),
                       lambda l:l['receipt_sha256'].update(tail='0'*64),lambda l:l['stages'].remove('tail'),
                       lambda l:l.update(ancestor_commit=self.C)]:
            m=json.loads(p.read_text());saved=json.dumps(m);tamper(m['input_lineage']);p.write_text(json.dumps(m))
            with self.assertRaisesRegex(ValueError,'lineage|producing stage receipt'):self.st.verify_inputs(dest)
            p.write_text(saved)
        self.st.verify_inputs(dest)


if __name__ == '__main__':
    unittest.main()
