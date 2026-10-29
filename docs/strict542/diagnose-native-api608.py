#!/usr/bin/env python3
"""Finite external API observer for the unchanged, reviewed a39a unified-0.

Only an admitted committed secretless export may execute this fixed entry point.
Timeout is diagnostic evidence, never checkpoint or installation authority.
"""
import hashlib
import json
import os
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
    'native-api-phases608.mjs': 'f50191444745bf8710fe513b66d36a2cfb16b50f9427d5875bb1aba8a68be87d',
    'install-native-api-phases608.mjs': '87fb06525b6baa62adf05a8308f5281271659a952422126582c1d14b7c307d83',
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


def collect(command, output, limit=1500):
    """Bound the whole setup/probe tree; forward cancellation and settle it."""
    cancelled = []
    child = None
    phase_stream = None

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
            if phase_stream is not None:
                forward_events(phase_stream)
            return child.returncode, (128 + cancelled[0] if cancelled else None)
    finally:
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
    rc, cancelled = collect(['sh', 'native-api-inner608.sh'], result/'runner.log')
    outcome = Path('result608-unified-0')
    if outcome.exists():
        outcome.rename(result/'unified-0')
    receipt = {'kind': 'DIAGNOSTIC_ONLY_NOT_BUILD_RECEIPT608',
               'source_commit': FREEZE, 'source_export_sha256': COMMON,
               'command_exit': rc, 'collection_exit': cancelled or (0 if rc in (0, 124) else rc),
               'cancelled_signal': cancelled - 128 if cancelled else None,
               'elapsed_seconds': time.monotonic()-started,
               'setup_and_probe_limit_seconds': 1500, 'compiler_limit_seconds': 900,
               'preload_smoke_limit_seconds': 30,
               'application_authority': False, 'accepted_checkpoint': False,
               'run_id': manifest['run_id']}
    (result/'diagnostic.json').write_text(json.dumps(receipt, sort_keys=True, indent=2)+'\n')
    print(json.dumps(receipt), flush=True)
    raise SystemExit(receipt['collection_exit'])


if __name__ == '__main__':
    main()
