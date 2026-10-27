import {describe,it,expect} from 'vitest';
import {parseBuildAllArgs,resolveBuildAllSteps,resolveBuildAllTsdownPlan} from '../../scripts/build-all.mts';
import fs from 'node:fs';
import {fixture} from '../../docs/strict542/native-compiler608-fixture.mjs';
import {nativeCompiler608} from '../../scripts/lib/native-compiler608.mjs';
import {resolveNativeBoundedTsdownPlan608} from '../../scripts/tsdown-build.mts';
import {BOUNDED_COMPILER_ENV} from '../../scripts/lib/bounded-package608.mjs';

const stages: Record<string,string> = {'tsdown-ai':'ai','tsdown-packages':'packages','tsdown-unified':'unified'};

describe('complete typed bounded package scheduling',()=>{
  it('standalone package builder uses the actual positional profile interface',()=>{
    const script=fs.readFileSync('docs/strict542/build598.sh','utf8');
    const line=script.split('\n').find(line=>line.startsWith('node --import ./scripts/tsx.mjs scripts/build-all.mts '));
    expect(line).toBeDefined();
    const args=line!.split(' ').slice(4);
    expect(parseBuildAllArgs(args).profile).toBe('boundedPackage');
  });
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
  it('requires actual native bytes, derives bounded heap and retains ordinary full/package guard',()=>{
    const memory={platform:'linux' as const,availableMemoryBytes:16*1024**3,procMemTotalBytes:16*1024**3,cgroupMemoryLimitBytes:4*1024**3};
    for (const profile of ['full','package']) {
      const stock=resolveBuildAllTsdownPlan(profile,{},memory);
      expect(stock.heapShortfall?.fatal).toBe(true);
      expect(stock.heapShortfall?.message).toContain('4352MB');
    }
    expect(()=>resolveBuildAllTsdownPlan('boundedPackage',{},memory)).toThrow(/required native compiler/);
    const cleanups: (()=>void)[]=[];
    const root=fixture({after:(fn:()=>void)=>cleanups.push(fn)});
    const cwd=process.cwd();
    try {
      process.chdir(root);
      const env={...nativeCompiler608(root,{required:true}).env};
      const plan=resolveBuildAllTsdownPlan('boundedPackage',env,memory);
      expect(plan.heapShortfall).toBeNull();
      expect(plan.env.NODE_OPTIONS).toContain('--max-old-space-size=3328');
      expect(plan.env.NAPI_RS_NATIVE_LIBRARY_PATH).toEqual(env.NAPI_RS_NATIVE_LIBRARY_PATH);
      expect(plan.env.OPENCLAW_BUILD_CACHE).toBe('0');
      for (const control of ['OPENCLAW_TSDOWN_MAX_OLD_SPACE_MB','OPENCLAW_DOCKER_BUILD_TSDOWN_MAX_OLD_SPACE_MB'])
        expect(()=>resolveNativeBoundedTsdownPlan608({...memory,env:{...env,[control]:'8192'}})).toThrow(/heap override/);
      expect(()=>resolveNativeBoundedTsdownPlan608({...memory,env,resolvedMaxOldSpaceMb:8192})).toThrow(/heap override/);
      fs.appendFileSync(env.NAPI_RS_NATIVE_LIBRARY_PATH,'changed');
      expect(()=>resolveBuildAllTsdownPlan('boundedPackage',env,memory)).toThrow(/addon mismatch/);
    } finally {process.chdir(cwd);for(const clean of cleanups) clean();}
  });
  it('cannot turn boundedPackage into runtime-only output',()=>{
    expect(()=>resolveBuildAllSteps('boundedPackage',{OPENCLAW_RUN_NODE_SKIP_DTS_BUILD:'1'})).toThrow(/complete typed/);
  });
});
