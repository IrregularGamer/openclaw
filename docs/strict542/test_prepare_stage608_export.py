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


if __name__ == '__main__':
    unittest.main()
