import assert from "node:assert/strict";
import { chmodSync, mkdtempSync, readFileSync, rmSync } from "node:fs";
import { registerHooks, stripTypeScriptTypes } from "node:module";
import { createServer } from "node:net";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { after, test } from "node:test";

// Only endpoint pathname/metadata change. Production protocol uses real IPC.
const dir = mkdtempSync(join(tmpdir(), "native542-"));
const endpoint = join(dir, "owner.sock");
const target = new URL("./native-owner-transport.ts", import.meta.url).href;
registerHooks({ resolve(specifier, context, next) {
  if (context.parentURL === target && specifier === "node:child_process") throw new Error("Forbidden native execution in source tests");
  return next(specifier, context);
}, load(url, context, next) {
  if (url !== target) return next(url, context);
  let source = readFileSync(new URL(url), "utf8");
  source = source.replace('"/run/agentq-safety/owner542.sock"', JSON.stringify(endpoint));
  source = source.replace('info.uid !== 0', '![0, process.getuid()].includes(info.uid)');
  source = source.replace('info.mode & 0o022', 'info.mode & 0o000'); // synthetic /tmp parent only
  return { format: "module", shortCircuit: true, source: stripTypeScriptTypes(source) };
} });
const { readNativeOwner542, monotonicNs, parseNativeOwner542, HQ542_SESSION_KEY } = await import(target);
after(() => rmSync(dir, { recursive: true, force: true }));
const owner = { name: "Pinch", session: HQ542_SESSION_KEY, pid: 4242, start: "123456" };
async function exercise(reply, { cancel = false, ms = 700 } = {}) {
  const sockets = new Set();
  const server = createServer(socket => {
    sockets.add(socket);
    socket.on("close", () => sockets.delete(socket));
    let pending = "";
    socket.on("error", () => {});
    socket.on("data", bytes => {
      pending += bytes;
      while (pending.includes("\n")) {
        const end = pending.indexOf("\n");
        const request = JSON.parse(pending.slice(0, end));
        pending = pending.slice(end + 1);
        reply(socket, request);
      }
    });
  });
  await new Promise(resolve => server.listen(endpoint, resolve));
  chmodSync(endpoint, 0o600);
  const controller = new AbortController();
  const timer = cancel ? setTimeout(() => controller.abort(), 80) : undefined;
  try {
    return await readNativeOwner542({ deadlineNs: monotonicNs() + BigInt(ms) * 1_000_000n, signal: controller.signal });
  } finally {
    clearTimeout(timer);
    for (const socket of sockets) socket.destroy();
    await new Promise(resolve => server.close(resolve));
  }
}
const settled = (socket, req, extra = {}) => socket.end(JSON.stringify({
  schemaVersion: 1, requestId: req.requestId, settled: true,
  cancelled: false, reason: null, owner, ...extra,
}) + "\n");

test("accepts exact native result only with settled acknowledgement", async () => {
  const result = await exercise((socket, req) => settled(socket, req));
  assert.equal(result.ok, true);
  assert.deepEqual(result.owner, owner);
});
test("cancellation waits for explicit native settled acknowledgement", async () => {
  let acknowledged = false;
  const result = await exercise((socket, req) => {
    if (req.operation === "cancel") {
      acknowledged = true;
      settled(socket, req, { cancelled: true, reason: "cancelled", owner: null });
    }
  }, { cancel: true });
  assert.equal(acknowledged, true);
  assert.equal(result.reason, "cancelled");
  assert.notEqual(result.settledNs, null);
});
test("EOF without settlement refuses", async () => {
  assert.equal((await exercise(socket => socket.end())).reason, "unsettled");
});
test("cancellation without native acknowledgement refuses by shared deadline", async () => {
  const start = monotonicNs();
  const result = await exercise(() => {}, { cancel: true, ms: 250 });
  assert.equal(result.reason, "unsettled");
  assert.equal(result.settledNs, null);
  assert.ok(monotonicNs() - start < 1_000_000_000n);
});
test("wrong correlation, nonsettled, malformed owner and oversize refuse", async () => {
  for (const extra of [{ requestId: "wrong" }, { settled: false }, { owner: { ...owner, pid: 1 } }]) {
    assert.equal((await exercise((socket, req) => settled(socket, req, extra))).ok, false);
  }
  assert.equal((await exercise(socket => socket.end("x".repeat(5000)))).ok, false);
});
test("deadline above 10 seconds and already cancelled refuse before connection", async () => {
  const c = new AbortController();
  assert.equal((await readNativeOwner542({ deadlineNs: monotonicNs() + 11_000_000_000n, signal: c.signal })).ok, false);
  c.abort();
  assert.equal((await readNativeOwner542({ deadlineNs: monotonicNs() + 1_000_000_000n, signal: c.signal })).reason, "cancelled");
});
test("native owner decoder refuses caller echoes and extra fields", () => {
  assert.deepEqual(parseNativeOwner542(JSON.stringify({ schemaVersion: 1, owner })), owner);
  assert.equal(parseNativeOwner542(JSON.stringify({ schemaVersion: 1, owner, available: true })), undefined);
});
