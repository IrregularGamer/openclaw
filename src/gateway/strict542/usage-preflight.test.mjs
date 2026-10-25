import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { describe, it } from "node:test";
import {
  captureSelectedRuntimeAuthRead,
  captureSelectedSessionRuntimeAuthRead,
} from "../../agents/sessions/selected-runtime-auth-read.ts";
import {
  PREFLIGHT542_SESSION_KEY,
  fetchAnthropicOAuthUsage,
  runUsagePreflight,
  validateUsagePreflightParams,
} from "./usage-preflight.ts";

const SECRET = "synthetic-existing-memory-token";
const owner = { name: "Pinch", session: PREFLIGHT542_SESSION_KEY, pid: 4242, start: "123456" };
const MODEL = "claude-opus-test";

function request(overrides = {}) {
  return {
    agentId: "claw",
    sessionKey: PREFLIGHT542_SESSION_KEY,
    provider: "anthropic",
    model: MODEL,
    owner: { ...owner },
    requestId: "probe-0001-strict542",
    timeoutMs: 10000,
    ...overrides,
  };
}
const fullBody = () => ({
  five_hour: { utilization: 12.5, resets_at: "2026-10-25T15:00:00Z" },
  seven_day: { utilization: 40, resets_at: "2026-10-30T00:00:00Z" },
  seven_day_opus: { utilization: 55, resets_at: null },
  seven_day_sonnet: { utilization: 3 },
});

/**
 * Fake clock plus the REAL job574 session/auth lease predicates over mutable
 * synthetic in-memory state. Native and provider transports are synthetic.
 */
function fixture(options = {}) {
  let ns = 1_000_000_000_000n;
  let ms = 1_800_000_000_000;
  const advance = (delta) => {
    ns += BigInt(delta) * 1_000_000n;
    ms += delta;
  };
  const model = { provider: "anthropic", id: MODEL, api: "anthropic-messages", baseUrl: "https://api.anthropic.com" };
  const session = { generation: {}, sessionId: "synthetic-session", disposed: false, model };
  const auth = {
    generation: {},
    provider: "anthropic",
    model,
    selection: { modelId: model.id, api: model.api, baseUrl: model.baseUrl, mode: "oauth", expiresAt: ms + 3_600_000 },
    apiKey: SECRET,
  };
  const calls = { native: [], fetch: [], capture: 0, refresh: 0, writes: 0, sends: 0 };
  const state = {
    nativeResults: options.nativeResults ?? [],
    fetchImpl:
      options.fetchImpl ??
      (async () => {
        advance(150);
        return { ok: true, status: 200, body: fullBody() };
      }),
  };
  const deps = {
    nowNs: () => ns,
    nowMs: () => ms,
    captureSession: (key) => {
      calls.capture += 1;
      if (key !== PREFLIGHT542_SESSION_KEY) {
        return undefined;
      }
      return captureSelectedSessionRuntimeAuthRead(
        () => session,
        () => captureSelectedRuntimeAuthRead(() => auth, () => ms),
      );
    },
    readNativeOwner: async ({ deadlineNs, signal }) => {
      calls.native.push({ deadlineNs, aborted: signal.aborted });
      advance(40);
      const next = state.nativeResults.shift();
      return next ?? { ok: true, owner: { ...owner }, settledNs: ns };
    },
    fetchUsage: async (params) => {
      calls.fetch.push({ apiKey: params.apiKey, signal: params.signal });
      return state.fetchImpl(params, { advance, session, auth });
    },
  };
  return { deps, calls, state, session, auth, advance, enteredNs: () => ns, now: () => ms };
}
const run = (f, req = request(), signal) => runUsagePreflight(req, f.deps, f.enteredNs(), signal);
const noSecret = (result) => assert.ok(!JSON.stringify(result).includes(SECRET));

describe("usage.preflight exact542 request schema", () => {
  it("accepts exactly the exact542 keys", () => {
    assert.equal(validateUsagePreflightParams(request()).ok, true);
  });
  it("refuses extra, missing and malformed keys", () => {
    assert.equal(validateUsagePreflightParams({ ...request(), extra: 1 }).ok, false);
    const missing = request();
    delete missing.requestId;
    assert.equal(validateUsagePreflightParams(missing).ok, false);
    assert.equal(validateUsagePreflightParams(request({ timeoutMs: 10001 })).ok, false);
    assert.equal(validateUsagePreflightParams(request({ timeoutMs: 999 })).ok, false);
    assert.equal(validateUsagePreflightParams(request({ timeoutMs: 1.5 })).ok, false);
    assert.equal(validateUsagePreflightParams(request({ requestId: "x" })).ok, false);
    assert.equal(validateUsagePreflightParams(request({ owner: { ...owner, extra: true } })).ok, false);
    assert.equal(validateUsagePreflightParams(request({ owner: { ...owner, pid: "4242" } })).ok, false);
    assert.equal(validateUsagePreflightParams(request({ owner: { ...owner, start: "x" } })).ok, false);
    assert.equal(validateUsagePreflightParams(null).ok, false);
    assert.equal(validateUsagePreflightParams([]).ok, false);
  });
});

describe("usage.preflight acceptance", () => {
  it("returns verified fresh AVAILABLE windows for the actual active route", async () => {
    const f = fixture();
    const started = f.now();
    const result = await run(f);
    assert.equal(result.status, "AVAILABLE");
    assert.equal(result.reason, "ok");
    assert.deepEqual(
      {
        agentId: result.agentId,
        sessionKey: result.sessionKey,
        provider: result.provider,
        model: result.model,
        owner: result.owner,
      },
      { agentId: "claw", sessionKey: PREFLIGHT542_SESSION_KEY, provider: "anthropic", model: MODEL, owner },
    );
    assert.deepEqual(result.windows, [
      { label: "5h", usedPercent: 12.5, resetAt: "2026-10-25T15:00:00.000Z" },
      { label: "7d", usedPercent: 40, resetAt: "2026-10-30T00:00:00.000Z" },
      { label: "7d-opus", usedPercent: 55 },
    ]);
    assert.equal(result.source, "provider-live");
    assert.equal(result.cached, false);
    assert.equal(result.credentialMutation, false);
    assert.equal(result.requestStartedAt, started);
    assert.equal(result.expiresAt, result.providerObservedAt + 15000);
    assert.ok(result.completedAt < result.expiresAt);
    // Native before and after share the single handler-entry deadline.
    assert.equal(f.calls.native.length, 2);
    assert.equal(f.calls.native[0].deadlineNs, f.calls.native[1].deadlineNs);
    assert.equal(f.calls.fetch.length, 1);
    assert.equal(f.calls.fetch[0].apiKey, SECRET);
    assert.equal(f.calls.refresh + f.calls.writes + f.calls.sends, 0);
    noSecret(result);
  });

  it("never serves cache or historical success", async () => {
    const f = fixture();
    assert.equal((await run(f)).status, "AVAILABLE");
    f.state.fetchImpl = async () => ({ ok: false, reason: "network" });
    const second = await run(f);
    assert.equal(second.status, "UNKNOWN");
    assert.equal(second.reason, "provider_network");
    assert.equal(f.calls.fetch.length, 2);
  });
});

describe("usage.preflight identity and route refusals", () => {
  const cases = [
    ["unknown agent", (f) => run(f, request({ agentId: "main" })), "unknown_agent_session"],
    ["wrong HQ session", (f) => run(f, request({ sessionKey: "agent:claw:main" })), "unknown_agent_session"],
    ["wrong owner name", (f) => run(f, request({ owner: { ...owner, name: "Rook" } })), "owner_mismatch"],
    ["PID1 placeholder", (f) => run(f, request({ owner: { ...owner, pid: 1 } })), "owner_mismatch"],
    ["PID reuse (start differs)", (f) => run(f, request({ owner: { ...owner, start: "999" } })), "owner_mismatch"],
    ["model drift", (f) => run(f, request({ model: "claude-sonnet-test" })), "route_mismatch"],
    ["provider drift", (f) => run(f, request({ provider: "openai" })), "route_mismatch"],
  ];
  for (const [name, call, reason] of cases) {
    it(`refuses ${name}`, async () => {
      const f = fixture();
      const result = await call(f);
      assert.equal(result.status, "UNKNOWN");
      assert.equal(result.reason, reason);
      assert.equal(result.owner, null);
      assert.equal(result.source, null);
      assert.equal(f.calls.fetch.length, 0);
      noSecret(result);
    });
  }

  it("refuses an idle/unbound session", async () => {
    const f = fixture();
    f.session.disposed = true;
    const result = await run(f);
    assert.equal(result.reason, "session_auth_unbound");
    assert.equal(f.calls.native.length + f.calls.fetch.length, 0);
  });

  it("refuses ambiguous or missing in-memory auth", async () => {
    const f = fixture();
    f.auth.apiKey = undefined;
    assert.equal((await run(f)).reason, "session_auth_unbound");
    const g = fixture();
    g.deps.captureSession = () => {
      throw new Error("ambiguous transport credentials");
    };
    assert.equal((await run(g)).reason, "session_auth_unbound");
    assert.equal(f.calls.fetch.length + g.calls.fetch.length, 0);
  });

  it("refuses expired auth with zero provider, refresh or write calls", async () => {
    const f = fixture();
    f.auth.selection.expiresAt = f.now() + 10;
    f.advance(20);
    const result = await run(f);
    assert.equal(result.status, "UNKNOWN");
    assert.equal(f.calls.fetch.length, 0);
    assert.equal(f.calls.refresh + f.calls.writes, 0);
  });

  it("never sends the token to a non-default or non-Anthropic route", async () => {
    for (const patch of [{ baseUrl: "https://proxy.example.invalid" }, { api: "openai-completions" }]) {
      const f = fixture();
      f.session.model = { ...f.session.model, ...patch };
      f.auth.model = f.session.model;
      f.auth.selection = { ...f.auth.selection, ...patch };
      const result = await run(f);
      assert.equal(result.reason, "provider_unsupported");
      assert.equal(f.calls.fetch.length + f.calls.native.length, 0);
    }
  });

  it("refuses API-key auth and models without known window applicability", async () => {
    const f = fixture();
    f.auth.selection = { ...f.auth.selection, mode: "api-key", expiresAt: undefined };
    assert.equal((await run(f)).reason, "provider_unsupported");
    const g = fixture();
    g.session.model = { ...g.session.model, id: "claude-haiku-test" };
    g.auth.model = g.session.model;
    g.auth.selection = { ...g.auth.selection, modelId: "claude-haiku-test" };
    assert.equal((await run(g, request({ model: "claude-haiku-test" }))).reason, "model_applicability_unknown");
  });

  it("refuses native owner refusal, unavailability and owner change after the read", async () => {
    for (const reason of ["native_refused", "native_unavailable", "unsettled"]) {
      const f = fixture({ nativeResults: [{ ok: false, reason, settledNs: null }] });
      const result = await run(f);
      assert.equal(result.reason, `owner_${reason}`);
      assert.equal(f.calls.fetch.length, 0);
    }
    const g = fixture({
      nativeResults: [
        { ok: true, owner: { ...owner }, settledNs: 0n },
        { ok: true, owner: { ...owner, pid: 5151 }, settledNs: 0n },
      ],
    });
    const changed = await run(g);
    assert.equal(changed.reason, "owner_changed");
    assert.equal(changed.windows.length, 0);
  });

  it("refuses auth/account or model replacement observed after the provider GET", async () => {
    const f = fixture({
      fetchImpl: async (_params, { auth }) => {
        auth.selection = { ...auth.selection };
        return { ok: true, status: 200, body: fullBody() };
      },
    });
    assert.equal((await run(f)).reason, "route_auth_changed");
    const g = fixture({
      fetchImpl: async (_params, { session }) => {
        session.model = { ...session.model };
        return { ok: true, status: 200, body: fullBody() };
      },
    });
    assert.equal((await run(g)).reason, "route_auth_changed");
  });
});

describe("usage.preflight provider window refusals", () => {
  const withBody = (body) =>
    fixture({ fetchImpl: async () => ({ ok: true, status: 200, body }) });
  it("refuses empty, partial, malformed, nonfinite and out-of-range windows", async () => {
    const partial = fullBody();
    delete partial.seven_day_opus;
    const cases = [
      [{}, "window_missing"],
      [[], "provider_malformed"],
      [partial, "window_missing"],
      [{ ...fullBody(), seven_day: { utilization: "40" } }, "window_malformed"],
      [{ ...fullBody(), seven_day: { utilization: Number.NaN } }, "window_malformed"],
      [{ ...fullBody(), seven_day: { utilization: Number.POSITIVE_INFINITY } }, "window_malformed"],
      [{ ...fullBody(), extra_usage: { is_enabled: true } }, "provider_unrecognized_field"],
      [{ ...fullBody(), restriction: "blocked" }, "provider_unrecognized_field"],
      [{ ...fullBody(), seven_day_oauth_apps: { utilization: Number.NaN } }, "window_malformed"],
      [{ ...fullBody(), five_hour: { utilization: -1 } }, "window_out_of_range"],
      [{ ...fullBody(), five_hour: { utilization: 5, resets_at: "soon" } }, "window_malformed"],
    ];
    for (const [body, reason] of cases) {
      const result = await run(withBody(body));
      assert.equal(result.status, "UNKNOWN", reason);
      assert.equal(result.reason, reason);
      assert.deepEqual(result.windows, []);
    }
  });

  it("reports UNAVAILABLE for any exhausted applicable window, including above 100%", async () => {
    for (const utilization of [100, 101, 250]) {
      const result = await run(withBody({ ...fullBody(), seven_day_opus: { utilization } }));
      assert.equal(result.status, "UNAVAILABLE");
      assert.equal(result.reason, "window_exhausted");
      assert.deepEqual(result.windows, [{ label: "7d-opus", usedPercent: utilization }]);
      assert.equal(result.source, "provider-live");
    }
  });

  it("reports UNAVAILABLE for exhausted non-applicable or unlisted-but-known windows", async () => {
    for (const key of ["seven_day_sonnet", "seven_day_oauth_apps"]) {
      const result = await run(withBody({ ...fullBody(), [key]: { utilization: 100 } }));
      assert.equal(result.status, "UNAVAILABLE", key);
    }
  });

  it("reports UNAVAILABLE when an exhausted window accompanies a missing one", async () => {
    const body = { ...fullBody(), five_hour: { utilization: 100 } };
    delete body.seven_day_opus;
    assert.equal((await run(withBody(body))).status, "UNAVAILABLE");
  });

  it("does not let non-applicable windows mask exhaustion or a missing window", async () => {
    const exhausted = { ...fullBody(), five_hour: { utilization: 100 }, seven_day_sonnet: { utilization: 0 } };
    assert.equal((await run(withBody(exhausted))).status, "UNAVAILABLE");
    const masked = fullBody();
    delete masked.seven_day_opus;
    masked.seven_day_sonnet = { utilization: 0 };
    assert.equal((await run(withBody(masked))).reason, "window_missing");
  });

  it("refuses 401/403/429/5xx, unexpected status, network failure and body errors", async () => {
    const statuses = [
      [401, "provider_unauthorized"],
      [403, "provider_unauthorized"],
      [429, "provider_rate_limited"],
      [500, "provider_error"],
      [503, "provider_error"],
      [302, "provider_unexpected_status"],
    ];
    for (const [status, reason] of statuses) {
      const f = fixture({ fetchImpl: async () => ({ ok: true, status, body: undefined }) });
      const result = await run(f);
      assert.equal(result.reason, reason);
      noSecret(result);
    }
    for (const reason of ["network", "body_limit", "malformed_body"]) {
      const f = fixture({ fetchImpl: async () => ({ ok: false, reason }) });
      assert.equal((await run(f)).reason, `provider_${reason}`);
    }
  });
});

describe("usage.preflight deadline, cancellation and clocks", () => {
  it("refuses a late provider response after the shared deadline", async () => {
    const f = fixture({
      fetchImpl: async (_p, { advance }) => {
        advance(10_500);
        return { ok: true, status: 200, body: fullBody() };
      },
    });
    const result = await run(f);
    assert.equal(result.reason, "deadline_exceeded");
    assert.equal(f.calls.native.length, 1);
  });

  it("aborts a hanging provider GET at the real deadline with no later publication", async () => {
    const f = fixture();
    f.deps.nowNs = () => process.hrtime.bigint();
    let observedAbort = false;
    f.state.fetchImpl = ({ signal }) =>
      new Promise((resolve) => {
        signal.addEventListener("abort", () => {
          observedAbort = true;
          resolve({ ok: false, reason: "aborted" });
        });
      });
    const start = process.hrtime.bigint();
    const result = await runUsagePreflight(request({ timeoutMs: 1000 }), f.deps, start);
    const elapsedMs = Number((process.hrtime.bigint() - start) / 1_000_000n);
    assert.equal(result.reason, "deadline_exceeded");
    assert.equal(observedAbort, true);
    assert.ok(elapsedMs < 1500, `elapsed ${elapsedMs}`);
  });

  it("propagates caller cancellation to the provider transport", async () => {
    const f = fixture();
    const controller = new AbortController();
    f.state.fetchImpl = ({ signal }) =>
      new Promise((resolve) => {
        signal.addEventListener("abort", () => resolve({ ok: false, reason: "aborted" }));
        setTimeout(() => controller.abort(), 10);
      });
    const result = await run(f, request(), controller.signal);
    assert.equal(result.reason, "cancelled");
    assert.equal(f.calls.native.length, 1);
  });

  it("refuses an already-cancelled request without native or provider work", async () => {
    const f = fixture();
    const controller = new AbortController();
    controller.abort();
    const result = await run(f, request(), controller.signal);
    assert.equal(result.reason, "cancelled");
    assert.equal(f.calls.native.length + f.calls.fetch.length + f.calls.capture, 0);
  });

  it("refuses wall-clock anomalies", async () => {
    for (const jump of [-5_000, 5_000]) {
      const f = fixture();
      let ms = f.now();
      f.deps.nowMs = () => ms;
      f.state.fetchImpl = async () => {
        ms += jump;
        return { ok: true, status: 200, body: fullBody() };
      };
      const result = await run(f);
      assert.equal(result.reason, "clock_anomaly");
      assert.equal(result.source, null);
    }
  });
});

describe("strict Anthropic usage GET", () => {
  it("sends one GET with no redirect, cache or retry and hides error bodies", async () => {
    const seen = [];
    const fetchFn = async (url, init) => {
      seen.push({ url, init });
      return new Response("secret provider body", { status: 429 });
    };
    const signal = new AbortController().signal;
    const result = await fetchAnthropicOAuthUsage({ apiKey: SECRET, signal, fetchFn });
    assert.deepEqual(result, { ok: true, status: 429, body: undefined });
    assert.equal(seen.length, 1);
    assert.equal(seen[0].url, "https://api.anthropic.com/api/oauth/usage");
    assert.equal(seen[0].init.method, "GET");
    assert.equal(seen[0].init.redirect, "error");
    assert.equal(seen[0].init.cache, "no-store");
    assert.equal(seen[0].init.signal, signal);
  });
  it("parses JSON, bounds the body and maps aborts", async () => {
    const ok = await fetchAnthropicOAuthUsage({
      apiKey: SECRET,
      signal: new AbortController().signal,
      fetchFn: async () => new Response(JSON.stringify(fullBody()), { status: 200 }),
    });
    assert.deepEqual(ok, { ok: true, status: 200, body: fullBody() });
    const big = await fetchAnthropicOAuthUsage({
      apiKey: SECRET,
      signal: new AbortController().signal,
      fetchFn: async () => new Response("x".repeat(70_000), { status: 200 }),
    });
    assert.deepEqual(big, { ok: false, reason: "body_limit" });
    const controller = new AbortController();
    controller.abort();
    const aborted = await fetchAnthropicOAuthUsage({
      apiKey: SECRET,
      signal: controller.signal,
      fetchFn: async (_u, init) => {
        init.signal.throwIfAborted();
        return new Response("{}");
      },
    });
    assert.deepEqual(aborted, { ok: false, reason: "aborted" });
  });
});

describe("gateway registration", () => {
  const usage = readFileSync(new URL("../server-methods/usage.ts", import.meta.url), "utf8");
  const descriptors = readFileSync(new URL("../methods/core-descriptors.ts", import.meta.url), "utf8");
  it("registers usage.preflight as an operator.read method and keeps usage.status", () => {
    assert.ok(descriptors.includes('["usage.preflight", "usage", "operator.read", "2026.9"]'));
    assert.ok(descriptors.includes('["usage.status", "usage", "operator.read", "<=2026.7"]'));
  });
  it("leaves the usage.status handler byte-identical", () => {
    const block = usage.match(/^ {2}"usage\.status": async[\s\S]*?^ {2}\},\n/m)[0];
    assert.equal(
      createHash("sha256").update(block).digest("hex"),
      "4d8d78f8d8504d043c478d5b9da266ab77ed2e21cc38532fee7900dc0107421a",
    );
  });
  it("binds preflight only to the strict dependencies and refuses unauthenticated clients", () => {
    const block = usage.match(/^ {2}"usage\.preflight": async[\s\S]*?^ {2}\},\n/m)[0];
    assert.ok(block.includes("const enteredNs = monotonicNs();"));
    assert.ok(block.indexOf("monotonicNs()") < block.indexOf("validateUsagePreflightParams"));
    assert.ok(block.includes("!client?.connect"));
    assert.ok(block.includes("      callerSignal,\n    );"), "handler forwards caller cancellation");
    assert.ok(block.includes("AbortSignal.any([signal, client.connectionSignal])"), "disconnect and request cancellation both bind");
    assert.ok(block.includes('typeof hasCurrentClientAuthority !== "function"'), "authority guard is mandatory");
    assert.equal(block.match(/!hasCurrentClientAuthority\(\)/g).length, 2);
    assert.ok(block.includes("ErrorCodes.FORBIDDEN"));
    assert.ok(block.includes("captureSession: captureActiveEmbeddedSessionRuntimeAuth"));
    assert.ok(block.includes("readNativeOwner: readNativeOwner542"));
    assert.ok(block.includes("fetchUsage: fetchAnthropicOAuthUsage"));
    assert.ok(!/loadUsageStatus|loadProviderUsageSummary|Cached|ensureAuthProfileStore/.test(block));
  });
});
