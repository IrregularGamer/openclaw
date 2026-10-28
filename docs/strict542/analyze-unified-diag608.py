import collections,hashlib,json,sys
from pathlib import Path
root=Path(sys.argv[1]);out={'files':{}}
for p in sorted(root.rglob('*')):
 if p.is_file():
  with p.open('rb') as f: digest=hashlib.file_digest(f,'sha256').hexdigest()
  out['files'][str(p.relative_to(root))]={'bytes':p.stat().st_size,'sha256':digest}
samples=[]
with (root/'samples.jsonl').open() as f:
 for line in f:samples.append(json.loads(line))
out['observed_samples']=len(samples)
out['sample_span_seconds']=samples[-1]['at']-samples[0]['at']
out['cgroup_first']=samples[0]['cgroup'];out['cgroup_last']=samples[-1]['cgroup']
processes={}
for sample in samples:
 for p in sample['processes']:
  rec=processes.setdefault(p['pid'],{'name':p['name'],'first':sample['at'],'last':sample['at'],'first_ticks':p['utime']+p['stime'],'last_ticks':p['utime']+p['stime'],'peak_rss_pages':0,'states':collections.Counter(),'waits':collections.Counter()})
  rec['last']=sample['at'];rec['last_ticks']=p['utime']+p['stime'];rec['peak_rss_pages']=max(rec['peak_rss_pages'],p['rss_pages']);rec['states'][p['state']]+=1;rec['waits'][p['wchan']]+=1
for p in processes.values():p['cpu_ticks_delta']=p['last_ticks']-p['first_ticks']
out['processes']=processes
leaf=collections.Counter();inclusive=collections.Counter();out['profiles']=[]
for p in sorted(root.rglob('*.cpuprofile')):
 if p.stat().st_size>20*1024*1024:raise ValueError('unexpected profile size')
 d=json.loads(p.read_text());nodes={x['id']:x for x in d['nodes']};parents={c:x['id'] for x in d['nodes'] for c in x.get('children',[])}
 ids=d.get('samples',[]);deltas=d.get('timeDeltas',[])
 if len(ids)!=len(deltas):raise ValueError('profile sample/delta mismatch')
 def label(node):
  f=node['callFrame'];return (f['functionName'],f['url'],f['lineNumber'])
 for node,delta in zip(ids,deltas):
  leaf[label(nodes[node])]+=delta
  seen=set()
  while node in nodes:
   frame=label(nodes[node])
   if frame not in seen:inclusive[frame]+=delta;seen.add(frame)
   node=parents.get(node)
 out['profiles'].append({'path':str(p.relative_to(root)),'samples':len(ids),'startTime':d['startTime'],'endTime':d['endTime']})
for name,counter in [('self_microseconds',leaf),('inclusive_microseconds',inclusive)]:out[name]=[{'frame':k,'value':v} for k,v in counter.most_common(35)]
print(json.dumps(out,indent=2,sort_keys=True))
