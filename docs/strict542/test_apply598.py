"""Isolated disk-application refusal tests; no root/service/native operations."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec=importlib.util.spec_from_file_location('apply598',Path(__file__).with_name('apply598.py'))
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)

class Application(unittest.TestCase):
    def test_new_release_parent_directories(self):
        with tempfile.TemporaryDirectory() as root:
            target=Path(root)/'opt'/'openclaw-strict542'/'598'/'runtime'
            try:
                a.parents(target)
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

if __name__ == '__main__':unittest.main()
