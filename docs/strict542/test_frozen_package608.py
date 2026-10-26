"""Lock/fallback refusal tests; no package manager, network or build runs."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


class FrozenPackage(unittest.TestCase):
    def setUp(self):
        path=Path(__file__).with_name('frozen-package608.py')
        self.assertTrue(path.is_file(),'fixed frozen-package guard is not implemented')
        spec=importlib.util.spec_from_file_location('frozen608',path)
        self.guard=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.guard)
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        self.pins={}
        for name in ['pnpm-lock.yaml','pnpm-workspace.yaml','.npmrc']:
            raw=('original '+name+'\n').encode();(self.root/name).write_bytes(raw)
            self.pins[name]=hashlib.sha256(raw).hexdigest()
        self.patch=patch.object(self.guard,'PINS',self.pins);self.patch.start();self.addCleanup(self.patch.stop)
        self.out=self.root/'result598-build';self.out.mkdir()
        self.runtime=self.out/'runtime';self.runtime.mkdir()
        (self.runtime/'pnpm-lock.yaml').write_text('dedicated frozen target lock\n')
        (self.out/'deploy.log').write_text('Done with pnpm v12.5.1\n')

    def test_original_source_or_config_drift_refuses(self):
        for name in self.pins:
            p=self.root/name;raw=p.read_bytes();p.write_bytes(raw+b'drift')
            with self.assertRaisesRegex(ValueError,'original package input drift'):
                self.guard.preflight(self.root,{})
            p.write_bytes(raw)
        self.guard.preflight(self.root,{})

    def test_caller_package_policy_refuses_even_empty(self):
        for key in ['npm_config_force_legacy_deploy','NPM_CONFIG_LOCKFILE_DIR','npm_config_shared_workspace_lockfile','PNPM_CONFIG_FORCE_LEGACY_DEPLOY','NPM_CONFIG_USERCONFIG','npm_config_forceLegacyDeploy','npm_config_sharedWorkspaceLockfile']:
            with self.subTest(key=key),self.assertRaisesRegex(ValueError,'inherited package policy'):
                self.guard.preflight(self.root,{key:''})

    def test_lifecycle_cooldown_and_lock_trust_overlays_refuse(self):
        for key in ['PNPM_CONFIG_ALLOW_BUILDS','PNPM_CONFIG_DANGEROUSLY_ALLOW_ALL_BUILDS',
                    'PNPM_CONFIG_PNPMFILE','PNPM_CONFIG_GLOBAL_PNPMFILE','PNPM_CONFIG_SCRIPT_SHELL',
                    'PNPM_CONFIG_NODE_OPTIONS','PNPM_CONFIG_MINIMUM_RELEASE_AGE',
                    'PNPM_CONFIG_MINIMUM_RELEASE_AGE_STRICT','PNPM_CONFIG_MINIMUM_RELEASE_AGE_EXCLUDE',
                    'PNPM_CONFIG_TRUST_LOCKFILE','PNPM_CONFIG_TRUST_POLICY','NPM_CONFIG_WORKSPACE_DIR',
                    'npm_config_minimumReleaseAge','PNPM_CONFIG_FUTURE_POLICY']:
            with self.subTest(key=key),self.assertRaisesRegex(ValueError,'inherited package policy'):
                self.guard.preflight(self.root,{key:''})

    def test_success_records_both_lock_identities_and_exclusive_receipt(self):
        value=self.guard.receipt(self.root,{})
        self.assertEqual(value['source_lock_sha256'],self.pins['pnpm-lock.yaml'])
        self.assertEqual(value['target_lock_sha256'],hashlib.sha256((self.runtime/'pnpm-lock.yaml').read_bytes()).hexdigest())
        self.assertEqual(value['kind'],'FROZEN_DEPLOY_INPUTS_VERIFIED_NOT_APPLICATION_AUTHORITY')
        self.assertEqual(json.loads((self.out/'package-receipt.json').read_bytes()),value)
        with self.assertRaises(FileExistsError):self.guard.receipt(self.root,{})

    def test_legacy_fallback_or_postphase_drift_never_emits_receipt(self):
        log=self.out/'deploy.log'
        for warning in ['Shared lockfile not found. Falling back to installing without a lockfile.',
                        'The lockfile does not contain the workspace. Falling back to installing without it.',
                        'Shared workspace lockfile detected but configuration forces legacy deploy implementation.']:
            log.write_text(warning+'\nDone\n')
            with self.assertRaisesRegex(ValueError,'legacy/fallback'):
                self.guard.receipt(self.root,{})
            self.assertFalse((self.out/'package-receipt.json').exists())
        log.write_text('Done\n');(self.root/'pnpm-lock.yaml').write_text('changed after build')
        with self.assertRaises(ValueError):self.guard.receipt(self.root,{})
        self.assertFalse((self.out/'package-receipt.json').exists())

    def test_missing_or_redirected_target_lock_refuses(self):
        lock=self.runtime/'pnpm-lock.yaml';lock.unlink()
        with self.assertRaises(ValueError):self.guard.receipt(self.root,{})
        lock.symlink_to(self.root/'pnpm-lock.yaml')
        with self.assertRaisesRegex(ValueError,'private regular'):
            self.guard.receipt(self.root,{})
        self.assertFalse((self.out/'package-receipt.json').exists())

if __name__=='__main__':unittest.main()
