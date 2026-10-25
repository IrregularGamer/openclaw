import { randomUUID } from "node:crypto";
import { lstatSync } from "node:fs";
import { createConnection } from "node:net";
import { dirname } from "node:path";

// Only a separately provisioned root endpoint may serve this path. No request
// launches sudo, a native CLI, or any process. Missing endpoint means UNKNOWN.
export const NATIVE_OWNER542_SOCKET = "/run/agentq-safety/owner542.sock";
export const HQ542_SESSION_KEY = "agent:claw:telegram:group:-5217857869";
export const NATIVE_RESERVE_NS = 150_000_000n;
export type NativeOwner542 = { name: "Pinch"; session: string; pid: number; start: string };
export type NativeOwnerReadFailure = "native_unavailable" | "native_refused" | "native_malformed" | "cancelled" | "deadline" | "unsettled";
export type NativeOwnerReadResult =
  | { ok: true; owner: NativeOwner542; settledNs: bigint }
  | { ok: false; reason: NativeOwnerReadFailure; settledNs: bigint | null };
export function monotonicNs(): bigint { return process.hrtime.bigint(); }

// A root-created endpoint beneath root-owned nonwritable parents is the root
// authority, just as with other privileged Unix services. No caller path exists.
function trustedEndpoint(): boolean {
  try {
    let path = NATIVE_OWNER542_SOCKET;
    let socket = true;
    for (;;) {
      const info = lstatSync(path);
      if (info.uid !== 0 || info.isSymbolicLink() ||
          (socket ? !info.isSocket() || (info.mode & 0o007) !== 0
                  : !info.isDirectory() || (info.mode & 0o022) !== 0)) return false;
      if (path === "/") return true;
      path = dirname(path);
      socket = false;
    }
  } catch { return false; }
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

/** One IPC request, one explicit native settlement receipt, one shared deadline. */
export function readNativeOwner542(params: {
  deadlineNs: bigint; signal: AbortSignal;
}): Promise<NativeOwnerReadResult> {
  const { deadlineNs, signal } = params;
  const entered = monotonicNs();
  if (signal.aborted) return Promise.resolve({ ok: false, reason: "cancelled", settledNs: entered });
  if (deadlineNs <= entered || deadlineNs - entered > 10_000_000_000n)
    return Promise.resolve({ ok: false, reason: "deadline", settledNs: entered });
  if (!trustedEndpoint()) return Promise.resolve({ ok: false, reason: "native_unavailable", settledNs: entered });
  return new Promise(resolve => {
    const requestId = randomUUID();
    const socket = createConnection(NATIVE_OWNER542_SOCKET);
    let pending = "";
    let malformed = false;
    let done = false;
    let requested = false;
    let cancelled = false;
    let cancelReason: "cancelled" | "deadline" = "cancelled";
    let receipt: NativeOwnerReadResult | undefined;
    const msUntil = (ns: bigint) => Math.max(0, Number((ns - monotonicNs()) / 1_000_000n));
    const finish = (value: NativeOwnerReadResult) => {
      if (done) return;
      done = true;
      clearTimeout(deadlineTimer); clearTimeout(cancelTimer);
      signal.removeEventListener("abort", onAbort);
      socket.destroy();
      resolve(value);
    };
    const cancel = (reason: "cancelled" | "deadline") => {
      cancelReason = reason;
      if (cancelled) return;
      cancelled = true;
      if (requested) socket.write(JSON.stringify({ operation: "cancel", requestId }) + "\n");
    };
    const onAbort = () => cancel("cancelled");
    const deadlineTimer = setTimeout(() => finish({ ok: false, reason: "unsettled", settledNs: null }), msUntil(deadlineNs));
    const cancelTimer = setTimeout(() => cancel("deadline"), msUntil(deadlineNs - NATIVE_RESERVE_NS));
    signal.addEventListener("abort", onAbort, { once: true });
    socket.on("connect", () => {
      if (cancelled || signal.aborted || monotonicNs() >= deadlineNs - NATIVE_RESERVE_NS) {
        finish({ ok: false, reason: signal.aborted ? "cancelled" : "deadline", settledNs: monotonicNs() });
        return;
      }
      requested = true;
      socket.write(JSON.stringify({ schemaVersion: 1, operation: "operator-read", requestId, deadlineNs: deadlineNs.toString() }) + "\n");
    });
    socket.setEncoding("utf8");
    socket.on("data", (chunk: string) => {
      if (malformed) return;
      pending += chunk;
      if (pending.length > 4096) { pending = ""; malformed = true; cancel("cancelled"); return; }
      if (!pending.endsWith("\n")) return;
      try {
        const value: unknown = JSON.parse(pending);
        if (!isExactRecord(value, ["cancelled", "owner", "reason", "requestId", "schemaVersion", "settled"]) ||
            value.schemaVersion !== 1 || value.requestId !== requestId || value.settled !== true ||
            typeof value.cancelled !== "boolean") { cancel("cancelled"); return; }
        const settledNs = monotonicNs();
        if (settledNs >= deadlineNs) return;
        if (cancelled || signal.aborted) {
          // Success racing cancellation is never accepted as cancellation ACK.
          if (value.cancelled !== true || value.owner !== null || value.reason !== "cancelled") return;
          receipt = { ok: false, reason: cancelReason, settledNs };
        } else if (value.cancelled === true || value.reason !== null) {
          if (value.owner !== null || !["cancelled", "deadline", "native_refused"].includes(value.reason as string)) return;
          receipt = { ok: false, reason: value.reason as NativeOwnerReadFailure, settledNs };
        } else {
          const owner = parseNativeOwner542(JSON.stringify({ schemaVersion: 1, owner: value.owner }));
          if (!owner) { cancel("cancelled"); return; }
          receipt = { ok: true, owner, settledNs };
        }
      } catch { cancel("cancelled"); }
    });
    socket.on("end", () => {
      if (receipt && !(receipt.ok && (cancelled || signal.aborted)) && monotonicNs() < deadlineNs) finish(receipt);
      else finish({ ok: false, reason: "unsettled", settledNs: null });
    });
    socket.on("error", () => finish({ ok: false, reason: requested ? "unsettled" : "native_unavailable", settledNs: requested ? null : monotonicNs() }));
    socket.on("close", () => { if (!done) finish({ ok: false, reason: "unsettled", settledNs: null }); });
    if (signal.aborted) onAbort();
  });
}

function isExactRecord(value: unknown, keys: readonly string[]): value is Record<string, unknown> {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    return false;
  }
  const actual = Object.keys(value).toSorted();
  return actual.length === keys.length && actual.every((key, index) => key === keys[index]);
}
