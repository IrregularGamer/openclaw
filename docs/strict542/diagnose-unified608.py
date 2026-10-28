#!/usr/bin/env python3
"""One finite, source-only diagnostic of the accepted 5f unified-0 boundary.

Run only in a fresh admitted export. Instrumentation is disposable and cannot
produce an accepted checkpoint, package receipt, or installation authority.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

FREEZE = '5f7d810b7f254e4f06dbf7761b557ba90bf1a2b0'
PINS = {
    'native-declaration-emitter.mts': '8e1ba4705f959b85a7330494bc8ad60a0b17a6d059f75feed2e2d5a446c50927',
    'native-typescript-diagnostics.mts': 'b9b5ca10a73e3eb93ebfdc3aa90eeae5b952f615b76851dc5e96b0108a4ed15c',
}

PROFILER = r'''
import { Session as DiagnosticSession608 } from 'node:inspector';
const diagnosticSession608 = new DiagnosticSession608();
diagnosticSession608.connect();
const diagnosticPost608 = (name, args = {}) => new Promise((resolve, reject) => diagnosticSession608.post(name,args,(error,result)=>error?reject(error):resolve(result)));
const diagnosticMark608 = name => console.error(JSON.stringify({kind:'DECLARATION_PHASE608',name,at:Date.now(),cpu:process.cpuUsage(),memory:process.memoryUsage()}));
await diagnosticPost608('Profiler.enable');
await diagnosticPost608('Profiler.setSamplingInterval',{interval:10000});
await diagnosticPost608('Profiler.start');
let diagnosticBusy608 = false, diagnosticIndex608 = 0;
const diagnosticTimer608 = setInterval(async()=>{
 if(diagnosticBusy608)return;diagnosticBusy608=true;
 try { const {profile}=await diagnosticPost608('Profiler.stop');
  fs.writeFileSync(path.join(process.env.STRICT542_DIAGNOSTIC_DIR,`node-${process.pid}-${diagnosticIndex608++}.cpuprofile`),JSON.stringify(profile));
  await diagnosticPost608('Profiler.start');
 }catch(error){console.error('DIAGNOSTIC_PROFILE_ERROR608',String(error));process.exitCode=1;}
 finally {diagnosticBusy608=false;}
},60000);diagnosticTimer608.unref();
diagnosticMark608('module-ready');
'''


def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('diagnostic source boundary changed: ' + old[:80])
    return text.replace(old, new, 1)


def instrument():
    for name, digest in PINS.items():
        file = Path('scripts/lib') / name
        if file.is_symlink() or hashlib.sha256(file.read_bytes()).hexdigest() != digest:
            raise ValueError('diagnostic requires exact original source: ' + name)
    file = Path('scripts/lib/native-declaration-emitter.mts')
    text = file.read_text()
    text = once(text, 'export type NativeDeclaration = {', PROFILER + '\nexport type NativeDeclaration = {')
    pairs = [
        ('const before = snapshot();', 'snapshot-before'),
        ('before.signature(admittedConfig, args, [], stage);', 'signature-before'),
        ('const configured = await api.parseConfigFile(config);', 'parse-config'),
        ('const nativeSnapshot = await api.createSnapshot({', 'create-snapshot'),
        ('const errors = await collectNativeTypeScriptDiagnosticsAsync(project, {', 'diagnostics'),
        ('const result = await project.program.emitToString(EmitOnly.OnlyDts);', 'emit'),
        ('for (const file of await project.program.getSourceFileNames()) {', 'source-files'),
        ('await api.close();', 'api-close'),
        ('const after = snapshot();', 'snapshot-after'),
        ('after.seal(admittedConfig, args, inputs, before, preparationStartedAt, stage, producedFiles);', 'seal-after'),
    ]
    for statement, phase in pairs:
        text = once(text, statement, f"diagnosticMark608('{phase}:enter');\n    " + statement)
    # Marks immediately after the relevant await/statement show real completion.
    for statement, phase in [
        ('before.signature(admittedConfig, args, [], stage);', 'signature-before'),
        ('const configured = await api.parseConfigFile(config);', 'parse-config'),
        ('await api.close();', 'api-close'),
        ('after.seal(admittedConfig, args, inputs, before, preparationStartedAt, stage, producedFiles);', 'seal-after'),
    ]:
        text = once(text, statement, statement + f"\n    diagnosticMark608('{phase}:done');")
    text = once(text, 'const project = nativeSnapshot.getConfiguredProject(config);', "diagnosticMark608('create-snapshot:done');\n    const project = nativeSnapshot.getConfiguredProject(config);")
    text = once(text, 'if (result.emitSkipped || result.diagnostics.length) {', "diagnosticMark608('emit:done');\n      if (result.emitSkipped || result.diagnostics.length) {")
    file.write_text(text)
    file = Path('scripts/lib/native-typescript-diagnostics.mts')
    text = once(file.read_text(), 'diagnostics.push(...(await project.program[query]()));', "console.error('DIAGNOSTIC_QUERY608 enter',query,Date.now());\n    diagnostics.push(...(await project.program[query]()));\n    console.error('DIAGNOSTIC_QUERY608 done',query,Date.now());")
    file.write_text(text)


def sample():
    processes = []
    for entry in Path('/proc').iterdir():
        if not entry.name.isdecimal():
            continue
        try:
            # No command lines or environment: only pid/name/state/CPU/RSS/wait.
            stat = (entry/'stat').read_text()
            tail = stat[stat.rindex(')')+2:].split()
            processes.append({'pid':int(entry.name),'name':stat[stat.index('(')+1:stat.rindex(')')],
                              'state':tail[0],'ppid':int(tail[1]),'utime':int(tail[11]),
                              'stime':int(tail[12]),'rss_pages':int(tail[21]),
                              'wchan':(entry/'wchan').read_text().strip()})
        except (OSError, ValueError, IndexError):
            continue
    counters = {}
    for name in ['cpu.stat','memory.current','memory.peak','memory.events','memory.pressure','cpu.pressure']:
        counters[name] = (Path('/sys/fs/cgroup')/name).read_text()
    return {'at':time.time(),'processes':processes,'cgroup':counters}


def main():
    if sys.argv[1:] == ['instrument']:
        instrument()
        return
    if sys.argv[1:]:
        raise ValueError('no caller-selected diagnostic command')
    manifest = json.loads(Path('export-manifest.json').read_text())
    if manifest['source_commit'] != FREEZE or manifest['stage'] != 'unified-0':
        raise ValueError('diagnostic requires frozen unified-0')
    runner = Path('run608.sh').read_bytes()
    if hashlib.sha256(runner).hexdigest() != manifest['runner_sha256']:
        raise ValueError('runner pin mismatch')
    script = once(runner.decode(), 'sh docs/strict542/run-build-stage608.sh "$STAGE"', 'sh ../diagnostic-build608.sh "$STAGE"')
    script = once(script, 'python3 stage608.py archive-build "$RESULT"', 'echo DIAGNOSTIC_ONLY_NO_CHECKPOINT608')
    script = once(script, 'python3 stage608.py receipt "$RESULT"', 'echo DIAGNOSTIC_ONLY_NO_STAGE_RECEIPT608')
    Path('diagnostic-inner608.sh').write_text(script)
    Path('diagnostic-build608.sh').write_text('''set -eu
export STRICT542_DIAGNOSTIC_DIR="$PWD/../result608-unified-0/profiles"
mkdir "$STRICT542_DIAGNOSTIC_DIR"
python3 ../diagnose-unified608.py instrument
timeout -k 15s 600s sh docs/strict542/run-build-stage608.sh "$1"
''')
    result = Path('diagnostic608')
    result.mkdir()
    started = time.time()
    with (result/'runner.log').open('w') as log, (result/'samples.jsonl').open('w') as stats:
        child = subprocess.Popen(['sh','diagnostic-inner608.sh'],stdout=log,stderr=subprocess.STDOUT)
        while child.poll() is None:
            stats.write(json.dumps(sample(),sort_keys=True)+'\n');stats.flush()
            time.sleep(10)
        rc = child.wait()
    outcome = Path('result608-unified-0')
    if outcome.exists():
        outcome.rename(result/'unified-0')
    receipt = {'kind':'DIAGNOSTIC_ONLY_NOT_BUILD_RECEIPT608','source_commit':FREEZE,
               'source_export_sha256':manifest['source_export_sha256'],'command_exit':rc,
               'elapsed_seconds':time.time()-started,'compiler_wall_limit_seconds':600,
               'purpose':'phase/CPU/wait diagnosis only; no checkpoint/package/install authority'}
    (result/'diagnostic.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt),flush=True)
    # A deliberate finite timeout is evidence. Other failures are real failures.
    if rc not in (0,124):
        raise SystemExit(rc)


if __name__ == '__main__':
    main()
