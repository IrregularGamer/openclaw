#!/usr/bin/env python3
"""Finite external API observer for the unchanged, reviewed a39a unified-0.

Only an admitted committed secretless export may execute this fixed entry point.
Timeout is diagnostic evidence, never checkpoint or installation authority.
"""
import hashlib
import importlib.util
import json
import os
import re
from pathlib import Path
import signal
import subprocess
import sys
import time

FREEZE = 'a39ad5ee95609193502850d0dbb87b5dcbb5e3e3'
COMMON = 'd28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62'
RUNNER = 'e2ed7e1337f5d0564b56e61174d0837440655cd38f75416608bff3de82780605'
BUILD = 'e6c1270bf3e41e53e80f904fcf054df0636966e4b5f75c46ffaf890243ca326c'
HELPER = 'a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4'
OBSERVERS = {
    'diagnose-unified608.py': 'e9054f13c3b94e0813c825d3318e3da5e14beb40a37947be0cfd7ae6b22d7aa8',
    'native-api-phases608.mjs': 'f50191444745bf8710fe513b66d36a2cfb16b50f9427d5875bb1aba8a68be87d',
    'install-native-api-phases608.mjs': '7802d135ffeee9bedcc802cb47e46beba09db63a49ef5e3c8c2635f23ec50916',
    'native-api-cpu-profile608.mjs': '6278df90a9eaab783a6cc3b2fffcfd660d63c511888d80cf7c4e4356d82d488f',
}


def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('diagnostic boundary changed')
    return text.replace(old, new, 1)


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def external_runner(text):
    text = once(text, 'sh docs/strict542/run-build-stage608.sh "$STAGE"',
                'sh ../native-api-build608.sh "$STAGE"')
    text = once(text, 'python3 stage608.py archive-build "$RESULT"',
                'echo DIAGNOSTIC_ONLY_NO_CHECKPOINT608')
    return once(text, 'python3 stage608.py receipt "$RESULT"',
                'echo DIAGNOSTIC_ONLY_NO_STAGE_RECEIPT608')


def external_build(text):
    # Retain the original frozen install, both preflights and all owner entry
    # predicates. Only the final fixed Node entry gains an external preload.
    original = 'node --import ./scripts/tsx.mjs scripts/build-checkpoint608-owned.mjs "$STAGE"'
    replacement = '''timeout -k 15s 30s node --import ../install-native-api-phases608.mjs --input-type=module -e 'console.error("NATIVE_API_PRELOAD_SMOKE608")'
timeout -k 15s 900s node --import ../install-native-api-phases608.mjs --import ./scripts/tsx.mjs scripts/build-checkpoint608-owned.mjs "$STAGE"'''
    return once(text, original, replacement)


def validate():
    manifest = json.loads(Path('export-manifest.json').read_text())
    if (manifest['source_commit'], manifest['source_export_sha256'], manifest['stage']) != (FREEZE, COMMON, 'unified-0'):
        raise ValueError('requires exact unchanged a39a unified-0 export')
    if manifest['runner_sha256'] != RUNNER or digest('run608.sh') != RUNNER:
        raise ValueError('runner pin mismatch')
    if digest('stage608.py') != HELPER:
        raise ValueError('stage helper pin mismatch')
    for name, expected in OBSERVERS.items():
        if Path(name).is_symlink() or digest(name) != expected:
            raise ValueError('observer pin mismatch')
    return manifest


def resource_sampler():
    # validate() pins this external module first. Import only its maintained
    # read-only sample function; its historical profiler/main never executes.
    spec = importlib.util.spec_from_file_location('resource_sampler608', Path('diagnose-unified608.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.sample


def verify_cpu_profile(result):
    """Accept only finalized bounded profile bytes, never compiler success."""
    result = Path(result)
    directory = result/'cpu-profile'
    if result.is_symlink() or directory.is_symlink() or not directory.is_dir():
        raise ValueError('CPU profile directory refused')
    if directory.stat().st_mode & 0o777 != 0o700:
        raise ValueError('CPU profile directory mode refused')
    receipt_file = directory/'receipt.json'
    if (receipt_file.is_symlink() or not receipt_file.is_file()
            or receipt_file.stat().st_size > 2048 or receipt_file.stat().st_nlink != 1
            or receipt_file.stat().st_mode & 0o777 != 0o600):
        raise ValueError('CPU profile receipt refused')
    receipt = json.loads(receipt_file.read_text())
    if (not isinstance(receipt, dict)
            or set(receipt) != {'kind', 'complete', 'profile', 'sha256', 'bytes', 'limit_ms', 'max_profile_bytes'}
            or receipt['kind'] != 'NATIVE_CPU_PROFILE_RECEIPT608' or receipt['complete'] is not True
            or type(receipt['limit_ms']) is not int or type(receipt['max_profile_bytes']) is not int
            or receipt['limit_ms'] != 120000 or receipt['max_profile_bytes'] != 8388608
            or type(receipt['bytes']) is not int or not 0 < receipt['bytes'] <= 8388608
            or not isinstance(receipt['profile'], str)
            or re.fullmatch(r'\d+-\d+-cpuprofile\.pb\.gz', receipt['profile']) is None
            or not isinstance(receipt['sha256'], str)
            or re.fullmatch(r'[0-9a-f]{64}', receipt['sha256']) is None):
        raise ValueError('CPU profile receipt fields refused')
    profile = directory/receipt['profile']
    if (set(p.name for p in directory.iterdir()) != {'receipt.json', receipt['profile']}
            or profile.is_symlink() or not profile.is_file() or profile.stat().st_nlink != 1
            or profile.stat().st_size != receipt['bytes'] or digest(profile) != receipt['sha256']):
        raise ValueError('CPU profile bytes or inventory refused')
    log = result/'unified-0/unified-0/build.log'
    if log.is_symlink() or not log.is_file() or log.stat().st_size > 4*1024*1024:
        raise ValueError('CPU profile phase log refused')
    global_entered = False
    with log.open() as stream:
        for line in stream:
            if len(line) > 65536 or 'NATIVE_CPU_PROFILE_REFUSED608' in line:
                raise ValueError('CPU profile refusal recorded')
            try:
                event = json.loads(line)
            except ValueError:
                continue
            if not isinstance(event, dict):
                continue
            if event.get('kind') == 'NATIVE_CPU_PROFILE608' and event.get('phase') == 'refused':
                raise ValueError('CPU profile refusal recorded')
            if (event.get('kind'), event.get('method'), event.get('phase')) == (
                    'NATIVE_API_PHASE608', 'Program.getGlobalDiagnostics', 'start'):
                global_entered = True
    if not global_entered:
        raise ValueError('CPU profile lacks actual global entry')
    return receipt


def live_group(group):
    """Exclude zombies: only live processes can still execute or hold IPC."""
    live = []
    for path in Path('/proc').glob('[0-9]*/stat'):
        try:
            fields = path.read_text().rsplit(')', 1)[1].split()
            if int(fields[2]) == group and fields[0] not in ('Z', 'X'):
                live.append(int(path.parent.name))
        except (OSError, ValueError, IndexError):
            continue
    return live


def settle_group(group):
    # GNU timeout can exit while a TERM-ignoring grandchild remains. Do not
    # confuse its leader's wait status with process-tree settlement.
    if live_group(group):
        try:
            os.killpg(group, signal.SIGKILL)
        except ProcessLookupError:
            pass
        deadline = time.monotonic() + 5
        while live_group(group):
            if time.monotonic() >= deadline:
                raise RuntimeError('diagnostic process group failed settlement')
            time.sleep(0.05)


def forward_events(stream):
    # Only observer records; never echo arbitrary build output, arguments,
    # environment or source diagnostics into the offload progress channel.
    while True:
        line = stream.readline(4096)
        if not line:
            break
        if line.strip() == 'NATIVE_API_PRELOAD_SMOKE608':
            print('NATIVE_API_PRELOAD_SMOKE608', flush=True)
        elif line.startswith('{') and len(line) < 4096:
            try:
                event = json.loads(line)
            except ValueError:
                continue
            allowed = {'kind', 'pid', 'method', 'phase', 'status', 'duration_ms', 'monotonic_ms'}
            methods = {'API.parseConfigFile', 'API.createSnapshot', 'API.close'} | {
                'Program.' + name for name in ('getConfigFileParsingDiagnostics', 'getProgramDiagnostics',
                'getGlobalDiagnostics', 'getSyntacticDiagnostics', 'getBindDiagnostics',
                'getSemanticDiagnostics', 'emitToString', 'getSourceFileNames')}
            if (set(event) <= allowed and event.get('kind') == 'NATIVE_API_PHASE608'
                    and event.get('method') in methods and event.get('phase') in ('start', 'end')
                    and event.get('status') in (None, 'returned', 'failed')
                    and all(type(event.get(key)) in (int, float, type(None))
                            for key in ('pid', 'duration_ms', 'monotonic_ms'))):
                print(json.dumps(event, sort_keys=True), flush=True)


def collect(command, output, limit=1500, sample_fn=None):
    """Bound the whole setup/probe tree; forward cancellation and settle it."""
    cancelled = []
    child = None
    phase_stream = None
    stats = Path(output).with_name('samples.jsonl').open('x') if sample_fn else None
    next_sample = 0

    def record_sample():
        try:
            value = sample_fn()
        except Exception as error:
            # Record incomplete observation without printing exception details.
            value = {'sampling_error': type(error).__name__}
        stats.write(json.dumps(value, sort_keys=True)+'\n')
        stats.flush()

    def forward(signum, frame):
        cancelled.append(signum)
        if child is not None and child.poll() is None:
            try:
                os.killpg(child.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass

    previous = {sig: signal.signal(sig, forward) for sig in (signal.SIGTERM, signal.SIGINT)}
    try:
        with Path(output).open('w') as log:
            child = subprocess.Popen(['timeout', '-k', '15s', str(limit)+'s', *command],
                                     stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            while child.poll() is None:
                if stats is not None and time.monotonic() >= next_sample:
                    record_sample()
                    next_sample = time.monotonic() + 10
                phase_log = Path('result608-unified-0/unified-0/build.log')
                if phase_stream is None and phase_log.is_file():
                    phase_stream = phase_log.open()
                if phase_stream is not None:
                    forward_events(phase_stream)
                try:
                    child.wait(timeout=0.2)
                except subprocess.TimeoutExpired:
                    if cancelled:
                        try:
                            child.wait(timeout=15)
                        except subprocess.TimeoutExpired:
                            os.killpg(child.pid, signal.SIGKILL)
                            child.wait()
            settle_group(child.pid)
            if stats is not None:
                record_sample()  # Post-settlement sample; active samples precede it.
            if phase_stream is not None:
                forward_events(phase_stream)
            return child.returncode, (128 + cancelled[0] if cancelled else None)
    finally:
        if stats is not None:
            stats.close()
        if phase_stream is not None:
            phase_stream.close()
        for sig, handler in previous.items():
            signal.signal(sig, handler)


def main():
    if sys.argv[1:]:
        raise ValueError('no caller-selected diagnostic command')
    manifest = validate()
    result = Path('native-api608')
    result.mkdir()  # Refuse reuse or overwrite of any earlier diagnostic.
    Path('native-api-inner608.sh').write_text(external_runner(Path('run608.sh').read_text()))
    # This fixed helper verifies the frozen source script AFTER extraction,
    # before executing its otherwise unchanged install/preflight sequence.
    Path('native-api-build608.sh').write_text('''set -eu
[ "$#" = 1 ] && [ "$1" = unified-0 ]
python3 - <<'PINNED_BUILD'
import hashlib,importlib.util
from pathlib import Path
p=Path('docs/strict542/run-build-stage608.sh')
assert not p.is_symlink()
assert hashlib.sha256(p.read_bytes()).hexdigest()==''' + repr(BUILD) + '''
spec=importlib.util.spec_from_file_location('observer_launcher','../diagnose-native-api608.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
Path('../native-api-launch608.sh').write_text(module.external_build(p.read_text()))
PINNED_BUILD
sh ../native-api-launch608.sh "$1"
''')
    started = time.monotonic()
    rc, cancelled = collect(['sh', 'native-api-inner608.sh'], result/'runner.log', sample_fn=resource_sampler())
    samples = [json.loads(line) for line in (result/'samples.jsonl').read_text().splitlines()]
    sampling_errors = sum('sampling_error' in sample for sample in samples) or (0 if samples else 1)
    outcome = Path('result608-unified-0')
    if outcome.exists():
        outcome.rename(result/'unified-0')
    profile_receipt, profile_error = None, None
    try:
        profile_receipt = verify_cpu_profile(result)
    except Exception as error:
        profile_error = type(error).__name__  # Never publish arbitrary failure details.
    receipt = {'kind': 'DIAGNOSTIC_ONLY_NOT_BUILD_RECEIPT608',
               'source_commit': FREEZE, 'source_export_sha256': COMMON,
               'command_exit': rc, 'collection_exit': cancelled or (0 if rc in (0, 124) else rc),
               'cancelled_signal': cancelled - 128 if cancelled else None,
               'elapsed_seconds': time.monotonic()-started,
               'setup_and_probe_limit_seconds': 1500, 'compiler_limit_seconds': 900,
               'preload_smoke_limit_seconds': 30,
               'resource_samples': len(samples), 'resource_sampling_errors': sampling_errors,
               'cpu_profile': profile_receipt, 'cpu_profile_error': profile_error,
               'application_authority': False, 'accepted_checkpoint': False,
               'run_id': manifest['run_id']}
    if (sampling_errors or profile_error) and receipt['collection_exit'] == 0:
        receipt['collection_exit'] = 7
    (result/'diagnostic.json').write_text(json.dumps(receipt, sort_keys=True, indent=2)+'\n')
    print(json.dumps(receipt), flush=True)
    raise SystemExit(receipt['collection_exit'])


if __name__ == '__main__':
    main()
