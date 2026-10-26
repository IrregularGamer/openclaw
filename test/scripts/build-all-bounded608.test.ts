import {describe,it,expect} from 'vitest';
import {resolveBuildAllSteps,resolveBuildAllTsdownPlan} from '../../scripts/build-all.mts';
import {BOUNDED_COMPILER_ENV} from '../../scripts/lib/bounded-package608.mjs';

const stages: Record<string,string> = {'tsdown-ai':'ai','tsdown-packages':'packages','tsdown-unified':'unified'};

describe('complete typed bounded package scheduling',()=>{
  it('retains every canonical package phase in exactly the same order',()=>{
    const original=resolveBuildAllSteps('package',{});
    const bounded=resolveBuildAllSteps('boundedPackage',{});
    expect(bounded.map(step=>step.label)).toEqual(original.map(step=>step.label));
    for (const [index,step] of original.entries()) {
      const actual=bounded[index];
      expect(actual.cache).toBeUndefined();
      if (['tsdown-ai','tsdown-packages','tsdown-unified'].includes(step.label)) {
        expect(actual.args).toEqual(['--import','tsx','scripts/tsdown-bounded608.mts',
          stages[step.label]]);
        expect(actual.env).toMatchObject(BOUNDED_COMPILER_ENV);
      } else {
        expect(actual).toEqual({...step,cache:undefined});
      }
    }
  });
  it('retains fatal full-graph admission under the advertised 2 GiB budget',()=>{
    const plan=resolveBuildAllTsdownPlan('boundedPackage',{}, {platform:'linux',availableMemoryBytes:16*1024**3,procMemTotalBytes:16*1024**3,cgroupMemoryLimitBytes:2*1024**3});
    expect(plan.heapShortfall?.fatal).toBe(true);
    expect(plan.heapShortfall?.message).toContain('4352MB');
  });
  it('cannot turn boundedPackage into runtime-only output',()=>{
    expect(()=>resolveBuildAllSteps('boundedPackage',{OPENCLAW_RUN_NODE_SKIP_DTS_BUILD:'1'})).toThrow(/complete typed/);
  });
});
