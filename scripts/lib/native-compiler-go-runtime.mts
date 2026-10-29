// Bounds the native TypeScript compiler's Go heap to the build's memory lease.
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

type Env = Record<string, string | undefined>;

const MIB = 1024 ** 2;
/** Share of the effective memory limit given to the Go heap; the rest stays with
 * the Node owner (input snapshot, virtual filesystem, IPC buffers) and the kernel. */
export const NATIVE_COMPILER_GO_MEMORY_SHARE = 0.7;
const MIN_NATIVE_COMPILER_GO_MEMORY_BYTES = 512 * MIB;

type CgroupReader = {
  readFile: (file: string) => string;
  totalMemoryBytes: () => number;
};

const defaultReader: CgroupReader = {
  readFile: (file) => fs.readFileSync(file, "utf8"),
  totalMemoryBytes: () => os.totalmem(),
};

function readLimit(reader: CgroupReader, file: string) {
  try {
    const value = reader.readFile(file).trim();
    return /^\d+$/u.test(value) ? Number(value) : undefined;
  } catch {
    return undefined;
  }
}

/** Smallest memory.max over this process's cgroup v2 ancestry, else physical memory. */
export function resolveEffectiveMemoryLimitBytes(reader: CgroupReader = defaultReader) {
  const limits = [reader.totalMemoryBytes()];
  let own: string | undefined;
  try {
    own = /^0::(\/.*)$/mu.exec(reader.readFile("/proc/self/cgroup"))?.[1];
  } catch {
    own = undefined;
  }
  // Containers usually expose their own cgroup as the mount root.
  const rootLimit = readLimit(reader, "/sys/fs/cgroup/memory.max");
  if (rootLimit !== undefined) {
    limits.push(rootLimit);
  }
  for (let dir = own; dir && dir !== "/"; dir = path.posix.dirname(dir)) {
    const limit = readLimit(reader, path.posix.join("/sys/fs/cgroup", dir, "memory.max"));
    if (limit !== undefined) {
      limits.push(limit);
    }
  }
  return Math.min(...limits.filter((limit) => Number.isFinite(limit) && limit > 0));
}

/**
 * Go defaults to GOGC=100 without a memory limit, so a whole-program checker
 * whose live graph is near half the lease grows its heap to the cgroup cap and
 * thrashes in kernel reclaim. A soft GOMEMLIMIT makes the collector run before
 * that point. Only the collector schedule changes: roots, options and every
 * diagnostic query are untouched. Explicit caller values always win.
 */
export function resolveNativeCompilerGoEnv(
  env: Env,
  effectiveLimitBytes: number = resolveEffectiveMemoryLimitBytes(),
): Env {
  if (env.GOMEMLIMIT) {
    return {};
  }
  const bytes = Math.max(
    MIN_NATIVE_COMPILER_GO_MEMORY_BYTES,
    Math.floor((effectiveLimitBytes * NATIVE_COMPILER_GO_MEMORY_SHARE) / MIB) * MIB,
  );
  return { GOMEMLIMIT: `${bytes / MIB}MiB` };
}

/** Run with the Go policy in process.env; the pinned API client spawns tsgo lazily
 * without an env option, so the child inherits process.env at its first request. */
export async function withNativeCompilerGoEnv<T>(
  run: () => Promise<T>,
  env: Env = process.env,
  effectiveLimitBytes?: number,
): Promise<T> {
  const policy = resolveNativeCompilerGoEnv(env, effectiveLimitBytes);
  const previous = Object.fromEntries(Object.keys(policy).map((key) => [key, env[key]]));
  Object.assign(env, policy);
  try {
    return await run();
  } finally {
    for (const [key, value] of Object.entries(previous)) {
      if (value === undefined) {
        delete env[key];
      } else {
        env[key] = value;
      }
    }
  }
}
