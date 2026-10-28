#!/usr/bin/env python3
"""Deterministic analysis of the finite observer's printed ps samples only.

Never a build receipt, PID authority, memory-pressure measurement or checkpoint.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROW=re.compile(r'^\s+(\d+)\s+(\d+)\s+(\d+)\s+((?:\d+-)?\d+:\d{2}:\d{2})\s+(\d+)\s+(.+)$')

def cpu_seconds(text):
    days=0
    if '-' in text:
        prefix,text=text.split('-',1);days=int(prefix)
    hours,minutes,seconds=map(int,text.split(':'))
    return days*86400+hours*3600+minutes*60+seconds

def role(command):
    if '/lib/tsc --api --async' in command:return 'native-typescript'
    if '/tsdown/dist/run.mjs' in command:return 'declaration-node'
    if 'scripts/build-checkpoint608-owned.mjs' in command:return 'checkpoint-node'
    if command.startswith('pnpm install '):return 'installer'
    if '/esbuild --service=' in command:return 'esbuild-service'
    return 'other'

def analyze(raw):
    if len(raw)>2*1024*1024:raise ValueError('observer log exceeds finite analysis bound')
    samples=[];current=None;end=None;by={}
    for line in raw.decode('utf8').splitlines():
        start=re.fullmatch(r'SAMPLE608 elapsed=(\d+)s',line)
        finish=re.fullmatch(r'SAMPLE608 end rc=(\d+) elapsed=(\d+)s',line)
        if start:
            elapsed=int(start[1])
            if samples and elapsed<=samples[-1]['elapsed_seconds']:raise ValueError('nonincreasing observer wall clock')
            current={'elapsed_seconds':elapsed,'processes':[]};samples.append(current)
        elif finish:
            if end is not None:raise ValueError('duplicate observer completion')
            end={'command_exit_code':int(finish[1]),'elapsed_seconds':int(finish[2])};current=None
        elif current is not None and (match:=ROW.fullmatch(line)):
            pid,ppid,age,cpu,rss,command=match.groups()
            item={'pid':int(pid),'ppid':int(ppid),'age_seconds':int(age),'cpu_seconds':cpu_seconds(cpu),
                  'rss_bytes':int(rss)*1024,'role':role(command),'printed_command_prefix':command}
            current['processes'].append(item)
            key=(item['pid'],item['role'])
            by.setdefault(key,[]).append({'sample_elapsed_seconds':current['elapsed_seconds'],**item})
    totals=[]
    for (pid,kind),rows in sorted(by.items()):
        if kind=='other':continue
        first,last=rows[0],rows[-1]
        if any(b['cpu_seconds']<a['cpu_seconds'] or b['age_seconds']<a['age_seconds'] for a,b in zip(rows,rows[1:])):
            raise ValueError('printed process identity/counter discontinuity')
        totals.append({'pid':pid,'role':kind,'observations':len(rows),
                       'first_sample_seconds':first['sample_elapsed_seconds'],
                       'last_sample_seconds':last['sample_elapsed_seconds'],
                       'first_cpu_seconds':first['cpu_seconds'],'last_cpu_seconds':last['cpu_seconds'],
                       'observed_cpu_delta_seconds':last['cpu_seconds']-first['cpu_seconds'],
                       'largest_sampled_rss_bytes':max(row['rss_bytes'] for row in rows)})
    return {'kind':'DIAGNOSTIC_PS_SAMPLES_ONLY_NOT_ACCEPTANCE608',
            'raw_log_sha256':hashlib.sha256(raw).hexdigest(),'raw_log_bytes':len(raw),
            'sample_count':len(samples),'end':end,'process_summaries':totals,'samples':samples,
            'limits':['Printed top processes only; CPU/RSS between samples is unobserved.',
                      'Printed PID continuity is not native ownership or kernel start identity.',
                      'RSS is sampled per-process; no cgroup pressure/OOM history is established.',
                      'CPU progress identifies active work, not the exact native API query or full timeout cause.']}

if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('usage: analyze-unified608-samples.py observer.log')
    with Path(sys.argv[1]).open('rb') as stream:raw=stream.read(2*1024*1024+1)
    print(json.dumps(analyze(raw),indent=2,sort_keys=True))
