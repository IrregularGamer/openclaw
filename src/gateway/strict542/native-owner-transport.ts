import { spawn as nodeSpawn } from "node:child_process";

// Fixed root-native read prepared in docs/strict542/native-owner-read.patch. It
// calls the EXISTING Native510.owner_check (Preservation.owner + gateway
// MainPID) with caller=True; this module never evaluates ownership itself.
// The command is only usable after a separately authorized installation of
// that native operation and its fixed sudoers rule. Until then the read
// refuses as native_unavailable and usage.preflight stays UNKNOWN.
export const NATIVE_OWNER542_ARGV = Object.freeze([
  "/usr/bin/sudo",
  "-n",
  "/usr/bin/python3",
  "/usr/local/libexec/agentq-safety/control.py",
  "owner542-read",
] as const);

export const HQ542_SESSION_KEY = "agent:claw:telegram:group:-5217857869";

const STDOUT_LIMIT = 4096;
// The native side receives an earlier deadline so it finishes (or refuses) with
// time left for this process to observe settlement before the shared deadline.
export const NATIVE_RESERVE_NS = 1_500_000_000n;
// SIGTERM is delivered at the native deadline; SIGKILL follows at this margin.
const KILL_RESERVE_NS = 500_000_000n;

export type NativeOwner542 = {
  name: "Pinch";
  session: string;
  pid: number;
  start: string;
};

export type NativeOwnerReadFailure =
  | "native_unavailable"
  | "native_refused"
  | "native_malformed"
  | "cancelled"
  | "deadline"
  | "unsettled";

export type NativeOwnerReadResult =
  | { ok: true; owner: NativeOwner542; settledNs: bigint }
  | { ok: false; reason: NativeOwnerReadFailure; settledNs: bigint | null };

type SpawnFn = typeof nodeSpawn;

export function monotonicNs(): bigint {
  // CLOCK_MONOTONIC, the same clock as Python's time.monotonic_ns on Linux.
  return process.hrtime.bigint();
}

/** Strict decode of the native read's single JSON line. */
export function parseNativeOwner542(raw: string): NativeOwner542 | undefined {
  let value: unknown;
  try {
    value = JSON.parse(raw);
  } catch {
    return undefined;
  }
  if (!isExactRecord(value, ["owner", "schemaVersion"]) || value.schemaVersion !== 1) {
    return undefined;
  }
  const owner = value.owner;
  if (
    !isExactRecord(owner, ["name", "pid", "session", "start"]) ||
    owner.name !== "Pinch" ||
    owner.session !== HQ542_SESSION_KEY ||
    !Number.isSafeInteger(owner.pid) ||
    (owner.pid as number) <= 1 ||
    typeof owner.start !== "string" ||
    !/^[0-9]{1,20}$/.test(owner.start)
  ) {
    return undefined;
  }
  return Object.freeze({
    name: "Pinch",
    session: HQ542_SESSION_KEY,
    pid: owner.pid as number,
    start: owner.start,
  });
}

/**
 * Runs the fixed native read once. Resolves only after the child has exited and
 * its stdout closed (settled), or, if settlement is not observed by the shared
 * deadline, resolves "unsettled" which callers must treat as UNKNOWN.
 */
export function readNativeOwner542(params: {
  deadlineNs: bigint;
  signal: AbortSignal;
  argv?: readonly string[];
  spawn?: SpawnFn;
  nowNs?: () => bigint;
}): Promise<NativeOwnerReadResult> {
  const nowNs = params.nowNs ?? monotonicNs;
  const argv = params.argv ?? NATIVE_OWNER542_ARGV;
  const spawn = params.spawn ?? nodeSpawn;
  const { deadlineNs, signal } = params;
  const nativeDeadlineNs = deadlineNs - NATIVE_RESERVE_NS;
  const entered = nowNs();
  if (signal.aborted) {
    return Promise.resolve({ ok: false, reason: "cancelled", settledNs: entered });
  }
  if (nativeDeadlineNs <= entered) {
    return Promise.resolve({ ok: false, reason: "deadline", settledNs: entered });
  }
  return new Promise((resolve) => {
    let stdout = "";
    let failure: NativeOwnerReadFailure | undefined;
    let done = false;
    const timers: NodeJS.Timeout[] = [];
    const finish = (result: NativeOwnerReadResult) => {
      if (done) {
        return;
      }
      done = true;
      for (const timer of timers) {
        clearTimeout(timer);
      }
      signal.removeEventListener("abort", onAbort);
      resolve(result);
    };
    const msUntil = (ns: bigint) => Math.max(0, Number((ns - nowNs()) / 1_000_000n));
    let child: ReturnType<SpawnFn>;
    try {
      child = spawn(argv[0], [...argv.slice(1), "--deadline-ns", nativeDeadlineNs.toString()], {
        stdio: ["ignore", "pipe", "ignore"],
        shell: false,
        detached: false,
        env: { PATH: "/usr/bin:/bin", LANG: "C" },
      });
    } catch {
      finish({ ok: false, reason: "native_unavailable", settledNs: nowNs() });
      return;
    }
    const terminate = (reason: NativeOwnerReadFailure) => {
      failure ??= reason;
      child.kill("SIGTERM");
      timers.push(setTimeout(() => child.kill("SIGKILL"), msUntil(deadlineNs - KILL_RESERVE_NS)));
    };
    function onAbort() {
      terminate("cancelled");
    }
    signal.addEventListener("abort", onAbort, { once: true });
    timers.push(setTimeout(() => terminate("deadline"), msUntil(nativeDeadlineNs)));
    // Never publish after the shared deadline. If the child has not settled the
    // caller still refuses; no result from it can be consumed afterwards.
    timers.push(
      setTimeout(() => finish({ ok: false, reason: "unsettled", settledNs: null }), msUntil(deadlineNs)),
    );
    child.stdout?.setEncoding("utf8");
    child.stdout?.on("data", (chunk: string) => {
      stdout += chunk;
      if (stdout.length > STDOUT_LIMIT) {
        stdout = "";
        terminate("native_malformed");
      }
    });
    child.on("error", (error: NodeJS.ErrnoException) => {
      failure ??= "native_unavailable";
      if (child.pid === undefined) {
        // Spawn itself failed: no process exists to settle.
        finish({ ok: false, reason: failure, settledNs: nowNs() });
      }
      void error;
    });
    child.on("close", (code: number | null) => {
      const settledNs = nowNs();
      if (settledNs >= deadlineNs) {
        finish({ ok: false, reason: "unsettled", settledNs });
        return;
      }
      if (failure) {
        finish({ ok: false, reason: failure, settledNs });
        return;
      }
      if (code !== 0) {
        finish({ ok: false, reason: "native_refused", settledNs });
        return;
      }
      const owner = parseNativeOwner542(stdout.trim());
      finish(
        owner
          ? { ok: true, owner, settledNs }
          : { ok: false, reason: "native_malformed", settledNs },
      );
    });
  });
}

function isExactRecord(value: unknown, keys: readonly string[]): value is Record<string, unknown> {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    return false;
  }
  const actual = Object.keys(value).toSorted();
  return actual.length === keys.length && actual.every((key, index) => key === keys[index]);
}
