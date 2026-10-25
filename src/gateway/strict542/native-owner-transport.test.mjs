import assert from "node:assert/strict";
import { mkdtempSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { describe, it } from "node:test";
import {
  HQ542_SESSION_KEY,
  NATIVE_OWNER542_ARGV,
  NATIVE_RESERVE_NS,
  monotonicNs,
  parseNativeOwner542,
  readNativeOwner542,
} from "./native-owner-transport.ts";

// Synthetic native children only. The production argv is never executed here.
const dir = mkdtempSync(join(tmpdir(), "native542-"));
const owner = { name: "Pinch", session: HQ542_SESSION_KEY, pid: 4242, start: "123456" };
function child(name, body) {
  const path = join(dir, `${name}.mjs`);
  writeFileSync(path, body);
  return [process.execPath, path];
}
const ok = child(
  "ok",
  `const i = process.argv.indexOf("--deadline-ns");
   process.stdout.write(JSON.stringify({ schemaVersion: 1, owner: ${JSON.stringify(owner)} }));
   if (i < 0 || !/^[0-9]+$/.test(process.argv[i + 1])) process.exit(9);`,
);
const refuse = child("refuse", `process.stdout.write('{"status":"UNKNOWN"}'); process.exit(75);`);
const garbage = child("garbage", `process.stdout.write("not json");`);
const wrongOwner = child(
  "wrong",
  `process.stdout.write(JSON.stringify({ schemaVersion: 1, owner: { ...${JSON.stringify(owner)}, name: "Rook" } }));`,
);
const flood = child("flood", `process.stdout.write("x".repeat(10000)); setTimeout(() => {}, 60000);`);
// Cooperative native: SIGTERM is its cancellation acknowledgement, exit 75.
const slowCooperative = child(
  "slow",
  `process.on("SIGTERM", () => process.exit(75)); setTimeout(() => {}, 60000); process.stdout.write("");`,
);
// Uncooperative native ignores SIGTERM; only SIGKILL settles it.
const stubborn = child("stubborn", `process.on("SIGTERM", () => {}); setTimeout(() => {}, 60000);`);

const alive = (pid) => {
  try {
    process.kill(pid, 0);
    return true;
  } catch {
    return false;
  }
};
async function trackedRead(argv, ms, signal = new AbortController().signal) {
  const { spawn } = await import("node:child_process");
  let proc;
  const deadlineNs = monotonicNs() + BigInt(ms) * 1_000_000n;
  const result = await readNativeOwner542({
    deadlineNs,
    signal,
    argv,
    spawn: (...args) => (proc = spawn(...args)),
  });
  return { result, deadlineNs, proc };
}

describe("native owner542 transport", () => {
  it("keeps the fixed production argv immutable and shell-free", () => {
    assert.ok(Object.isFrozen(NATIVE_OWNER542_ARGV));
    assert.deepEqual(NATIVE_OWNER542_ARGV, [
      "/usr/bin/sudo",
      "-n",
      "/usr/bin/python3",
      "/usr/local/libexec/agentq-safety/control.py",
      "owner542-read",
    ]);
  });

  it("returns the settled native owner and passes an earlier native deadline", async () => {
    const { result, deadlineNs, proc } = await trackedRead(ok, 5000);
    assert.equal(result.ok, true);
    assert.deepEqual(result.owner, owner);
    assert.ok(result.settledNs < deadlineNs);
    const argv = proc.spawnargs;
    assert.equal(argv.at(-2), "--deadline-ns");
    assert.equal(BigInt(argv.at(-1)), deadlineNs - NATIVE_RESERVE_NS);
    assert.equal(proc.exitCode, 0);
  });

  it("refuses native refusal, malformed output, non-Pinch owner and oversize output", async () => {
    assert.equal((await trackedRead(refuse, 5000)).result.reason, "native_refused");
    assert.equal((await trackedRead(garbage, 5000)).result.reason, "native_malformed");
    assert.equal((await trackedRead(wrongOwner, 5000)).result.reason, "native_malformed");
    const big = await trackedRead(flood, 5000);
    assert.equal(big.result.reason, "native_malformed");
    assert.equal(alive(big.proc.pid), false);
  });

  it("strictly decodes owner records", () => {
    const line = (o, extra = {}) => JSON.stringify({ schemaVersion: 1, owner: o, ...extra });
    assert.deepEqual(parseNativeOwner542(line(owner)), owner);
    assert.equal(parseNativeOwner542(line({ ...owner, pid: 1 })), undefined);
    assert.equal(parseNativeOwner542(line({ ...owner, pid: "4242" })), undefined);
    assert.equal(parseNativeOwner542(line({ ...owner, start: "12a" })), undefined);
    assert.equal(parseNativeOwner542(line({ ...owner, session: "agent:claw:main" })), undefined);
    assert.equal(parseNativeOwner542(line({ ...owner, extra: 1 })), undefined);
    assert.equal(parseNativeOwner542(line(owner, { status: "ok" })), undefined);
  });

  it("refuses an unavailable native command without settling late", async () => {
    const { result, deadlineNs } = await trackedRead(["/nonexistent/strict542-native"], 5000);
    assert.equal(result.ok, false);
    assert.equal(result.reason, "native_unavailable");
    assert.ok(result.settledNs < deadlineNs);
  });

  it("propagates cancellation and settles the acknowledged child before the deadline", async () => {
    const controller = new AbortController();
    const started = monotonicNs();
    setTimeout(() => controller.abort(), 200);
    const { result, deadlineNs, proc } = await trackedRead(slowCooperative, 10000, controller.signal);
    assert.equal(result.reason, "cancelled");
    assert.ok(result.settledNs < deadlineNs);
    assert.ok(result.settledNs - started < 2_000_000_000n);
    assert.equal(alive(proc.pid), false);
    assert.equal(proc.exitCode, 75);
  });

  it("refuses an already-cancelled request without spawning", async () => {
    const controller = new AbortController();
    controller.abort();
    let spawned = 0;
    const result = await readNativeOwner542({
      deadlineNs: monotonicNs() + 5_000_000_000n,
      signal: controller.signal,
      argv: ok,
      spawn: () => {
        spawned += 1;
        throw new Error("must not spawn");
      },
    });
    assert.equal(result.reason, "cancelled");
    assert.equal(spawned, 0);
  });

  it("terminates at the native deadline and settles inside the shared deadline", async () => {
    const { result, deadlineNs, proc } = await trackedRead(slowCooperative, 2500);
    assert.equal(result.reason, "deadline");
    assert.ok(result.settledNs < deadlineNs);
    assert.equal(alive(proc.pid), false);
  });

  it("escalates to SIGKILL for an uncooperative child and still settles in time", async () => {
    const { result, deadlineNs, proc } = await trackedRead(stubborn, 2500);
    assert.equal(result.reason, "deadline");
    assert.ok(result.settledNs < deadlineNs);
    assert.equal(proc.signalCode, "SIGKILL");
    assert.equal(alive(proc.pid), false);
  });

  it("refuses a deadline without room for native settlement", async () => {
    let spawned = 0;
    const result = await readNativeOwner542({
      deadlineNs: monotonicNs() + NATIVE_RESERVE_NS - 1n,
      signal: new AbortController().signal,
      argv: ok,
      spawn: () => {
        spawned += 1;
        throw new Error("must not spawn");
      },
    });
    assert.equal(result.reason, "deadline");
    assert.equal(spawned, 0);
  });

});
