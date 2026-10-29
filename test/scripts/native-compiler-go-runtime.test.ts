import { describe, expect, it } from "vitest";
import {
  resolveEffectiveMemoryLimitBytes,
  resolveNativeCompilerGoEnv,
  withNativeCompilerGoEnv,
} from "../../scripts/lib/native-compiler-go-runtime.mts";

const GIB = 1024 ** 3;

function reader(files: Record<string, string>, total = 16 * GIB) {
  return {
    readFile: (file: string) => {
      if (!(file in files)) {
        throw new Error(`ENOENT ${file}`);
      }
      return files[file];
    },
    totalMemoryBytes: () => total,
  };
}

describe("native compiler Go runtime policy", () => {
  it("takes the smallest cgroup v2 ancestor limit", () => {
    expect(
      resolveEffectiveMemoryLimitBytes(
        reader({
          "/proc/self/cgroup": "0::/a.slice/b.service\n",
          "/sys/fs/cgroup/a.slice/memory.max": `${4 * GIB}\n`,
          "/sys/fs/cgroup/a.slice/b.service/memory.max": "max\n",
        }),
      ),
    ).toBe(4 * GIB);
  });

  it("reads a container root limit and falls back to physical memory", () => {
    expect(
      resolveEffectiveMemoryLimitBytes(
        reader({ "/proc/self/cgroup": "0::/\n", "/sys/fs/cgroup/memory.max": `${4 * GIB}` }),
      ),
    ).toBe(4 * GIB);
    expect(resolveEffectiveMemoryLimitBytes(reader({}, 2 * GIB))).toBe(2 * GIB);
  });

  it("bounds the Go heap below the 4 GiB lease and keeps explicit values", () => {
    expect(resolveNativeCompilerGoEnv({}, 4 * GIB)).toEqual({ GOMEMLIMIT: "2867MiB" });
    expect(resolveNativeCompilerGoEnv({}, 256 * 1024 ** 2)).toEqual({ GOMEMLIMIT: "512MiB" });
    expect(resolveNativeCompilerGoEnv({ GOMEMLIMIT: "3GiB" }, 4 * GIB)).toEqual({});
  });

  it("applies the policy only for the compiler lifetime, including failures", async () => {
    const env: Record<string, string | undefined> = { GOGC: "100" };
    const seen = await withNativeCompilerGoEnv(async () => env.GOMEMLIMIT, env, 4 * GIB);
    expect(seen).toBe("2867MiB");
    expect(env).toEqual({ GOGC: "100" });
    await expect(
      withNativeCompilerGoEnv(
        async () => {
          throw new Error("compile failed");
        },
        env,
        4 * GIB,
      ),
    ).rejects.toThrow("compile failed");
    expect(env).toEqual({ GOGC: "100" });
    const explicit = { GOMEMLIMIT: "1GiB" };
    await withNativeCompilerGoEnv(async () => undefined, explicit, 4 * GIB);
    expect(explicit).toEqual({ GOMEMLIMIT: "1GiB" });
  });
});
