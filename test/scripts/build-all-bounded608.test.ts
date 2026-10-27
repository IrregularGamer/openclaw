import {describe,it,expect} from 'vitest';
import {parseBuildAllArgs,resolveBuildAllSteps,resolveBuildAllTsdownPlan} from '../../scripts/build-all.mts';
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {spawnSync} from 'node:child_process';
import {fixture} from '../../docs/strict542/native-compiler608-fixture.mjs';
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
    try {
      // Vitest uses threads: isolate cwd in a synchronous, joined child instead
      // of changing the process shared by unrelated tests.
      const result=spawnSync(process.execPath,['--import',path.resolve('scripts/tsx.mjs'),'--input-type=module','-e',`
        import assert from 'node:assert/strict';
        import fs from 'node:fs';
        import {resolveBuildAllTsdownPlan} from ${JSON.stringify(pathToFileURL(path.resolve('scripts/build-all.mts')).href)};
        import {resolveNativeBoundedTsdownPlan608} from ${JSON.stringify(pathToFileURL(path.resolve('scripts/tsdown-build.mts')).href)};
        import {nativeCompiler608} from ${JSON.stringify(pathToFileURL(path.resolve('scripts/lib/native-compiler608.mjs')).href)};
        const memory=${JSON.stringify(memory)};
        const env={...nativeCompiler608(process.cwd(),{required:true}).env};
        const plan=resolveBuildAllTsdownPlan('boundedPackage',env,memory);
        assert.equal(plan.heapShortfall,null);
        assert.match(plan.env.NODE_OPTIONS,/--max-old-space-size=3328/);
        assert.equal(plan.env.NAPI_RS_NATIVE_LIBRARY_PATH,env.NAPI_RS_NATIVE_LIBRARY_PATH);
        assert.equal(plan.env.OPENCLAW_BUILD_CACHE,'0');
        for (const control of ['OPENCLAW_TSDOWN_MAX_OLD_SPACE_MB','OPENCLAW_DOCKER_BUILD_TSDOWN_MAX_OLD_SPACE_MB'])
          assert.throws(()=>resolveNativeBoundedTsdownPlan608({...memory,env:{...env,[control]:'8192'}}),/heap override/);
        assert.throws(()=>resolveNativeBoundedTsdownPlan608({...memory,env,resolvedMaxOldSpaceMb:8192}),/heap override/);
        fs.appendFileSync(env.NAPI_RS_NATIVE_LIBRARY_PATH,'changed');
        assert.throws(()=>resolveBuildAllTsdownPlan('boundedPackage',env,memory),/addon mismatch/);
      `],{cwd:root,encoding:'utf8',timeout:30_000});
      expect(result.error,result.stderr).toBeUndefined();
      expect(result.status,result.stderr).toBe(0);
    } finally {for(const clean of cleanups) clean();}
  });
  it('cannot turn boundedPackage into runtime-only output',()=>{
    expect(()=>resolveBuildAllSteps('boundedPackage',{OPENCLAW_RUN_NODE_SKIP_DTS_BUILD:'1'})).toThrow(/complete typed/);
  });
});
