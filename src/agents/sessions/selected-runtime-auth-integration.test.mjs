import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { registerHooks, stripTypeScriptTypes } from "node:module";
import { describe, it } from "node:test";

// Execute the unchanged source owners, with all unrelated runtime dependencies
// denied. No installed package, credential directory, provider or service loads.
const root = new URL("../../", import.meta.url);
const allowed = new Set([
  "agents/sessions/auth-storage.ts",
  "agents/sessions/auth-storage-error.ts",
  "agents/sessions/agent-session-base.ts",
  "agents/sessions/selected-runtime-auth-read.ts",
  "agents/embedded-agent-runner/active-run-projections.ts",
  "agents/embedded-agent-runner/run-state.ts",
  "agents/embedded-agent-runner/run/auth-controller.ts",
  "agents/provider-secret-egress.ts",
  "agents/provider-request-config.ts",
  "secrets/sentinel.ts",
  "logging/secret-redaction-registry.ts",
  "shared/global-singleton.ts",
  "shared/regexp.ts",
  "infra/map-size.ts",
].map(path => new URL(path, root).href));
const sources = new Map();
const denied = new Map();
const syntheticDependencies = new Map();
globalThis[Symbol.for("strict542.syntheticDependencies")] = syntheticDependencies;
registerHooks({
  resolve(specifier, context, next) {
    if (!allowed.has(context.parentURL)) return next(specifier, context);
    if (specifier.startsWith("node:") && specifier !== "node:fs") {
      return next(specifier, context);
    }
    const target = new URL(specifier.replace(/\.js$/, ".ts"), context.parentURL).href;
    if (allowed.has(target)) return { url: target, shortCircuit: true };
    const url = `denied:${encodeURIComponent(context.parentURL + ":" + specifier)}`;
    const source = sources.get(context.parentURL);
    const names = new Set();
    for (const match of source.matchAll(/import\s+([\s\S]*?)\s+from\s+["']([^"']+)["'];/g)) {
      if (match[2] !== specifier) continue;
      const members = match[1].match(/\{([\s\S]*?)\}/)?.[1] ?? "";
      for (const member of members.split(",")) {
        const name = member.trim().split(/\s+as\s+/)[0];
        if (name) names.add(name);
      }
    }
    const fail = `function denied() { throw new Error(${JSON.stringify("Forbidden runtime dependency: " + specifier)}); }`;
    // These import-time registrations are unrelated to auth availability. They
    // cannot supply credentials, identity or successful provider observations.
    const definitions = [...names].map(name => {
      if (name === "createSubsystemLogger") return `export const ${name} = () => new Proxy({}, { get: () => denied });`;
      if (name === "registerAgentEventLifecycleRotationHandler") return `export const ${name} = () => undefined;`;
      return `export const ${name} = (...args) => {
        const fn = globalThis[Symbol.for("strict542.syntheticDependencies")].get(${JSON.stringify(specifier + ":" + name)});
        return fn ? fn(...args) : denied();
      };`;
    });
    denied.set(url, `${fail}\nexport default new Proxy(denied, { get: () => denied });\n${definitions.join("\n")}`);
    return { url, shortCircuit: true };
  },
  load(url, context, next) {
    if (denied.has(url)) return { format: "module", source: denied.get(url), shortCircuit: true };
    if (!allowed.has(url)) return next(url, context);
    // The remote source-only transfer excludes directories named secrets. The
    // export may relocate this single tracked source file, with its git SHA256
    // verified by the runner. Resolution still uses its canonical source URL.
    const input = url === new URL("secrets/sentinel.ts", root).href && process.env.STRICT542_SENTINEL_SOURCE
      ? new URL(process.env.STRICT542_SENTINEL_SOURCE, root)
      : new URL(url);
    const source = stripTypeScriptTypes(readFileSync(input, "utf8"), { mode: "transform" });
    sources.set(url, source);
    return { format: "module", source, shortCircuit: true };
  },
});

const { AuthStorage } = await import("./auth-storage.ts");
const { AgentSessionBase } = await import("./agent-session-base.ts");
const { sealSecretSentinel, resolveSecretSentinel } = await import("../../secrets/sentinel.ts");
const { readGlobalSingleton } = await import("../../shared/global-singleton.ts");
const { captureActiveEmbeddedSessionRuntimeAuth } = await import("../embedded-agent-runner/active-run-projections.ts");
const state = await import("../embedded-agent-runner/run-state.ts");
const { createEmbeddedRunAuthController } = await import("../embedded-agent-runner/run/auth-controller.ts");
const { attachModelProviderRequestTransport } = await import("../provider-request-config.ts");

function fixture() {
  let reads = 0;
  const storage = AuthStorage.fromStorage({
    read() { reads++; return "{}"; },
    withLock() { throw new Error("Forbidden credential write"); },
    withLockAsync() { throw new Error("Forbidden credential write"); },
    assertProviderReady() { throw new Error("Forbidden credential resolution"); },
  });
  assert.equal(reads, 1); // Synthetic constructor admission, before any read lease.
  const model = { provider: "anthropic", id: "synthetic-model", api: "anthropic-messages", baseUrl: "https://example.invalid" };
  const selection = { modelId: model.id, api: model.api, baseUrl: model.baseUrl, mode: "oauth", expiresAt: Date.now() + 60000 };
  const key = sealSecretSentinel("synthetic-memory-key", { label: "synthetic-owner-test" });
  storage.setRuntimeApiKey(model.provider, key, selection);
  const session = new AgentSessionBase({
    agent: { state: { model }, abort() {} },
    sessionManager: { getSessionId: () => "synthetic-session" },
    modelRegistry: { authStorage: storage },
    settingsManager: {}, resourceLoader: {}, cwd: "/synthetic",
    cleanupProviderSessionResourcesOnDispose: false,
  });
  session.currentExtensionRunner = { invalidate() {} };
  return { storage, model, selection, key, session, assertNoReads: () => assert.equal(reads, 1) };
}

describe("actual selected memory source owners", () => {
  it("preserves ordinary egress redaction refresh while the new decoder stays read-only", () => {
    const f = fixture();
    sealSecretSentinel("synthetic-other-key", { label: "synthetic-other-owner" });
    const redaction = readGlobalSingleton(Symbol.for("openclaw.secretRedactionRegistry"));
    const before = [...redaction.registeredValues.keys()];
    assert.equal(resolveSecretSentinel(f.key), "synthetic-memory-key");
    const after = [...redaction.registeredValues.keys()];
    assert.notDeepEqual(after, before);
    assert.equal(after.at(-1), "synthetic-memory-key");
  });

  it("records the controller's committed route after preparation and refresh overlays", async () => {
    const f = fixture();
    let endpoint = "https://prepared.invalid";
    let preparationCalls = 0;
    let preparedRequest;
    // These are explicit synthetic WRITE-side dependencies. Read leases must
    // never invoke them; none supplies native identity or quota availability.
    syntheticDependencies.set("../../model-auth.js:getApiKeyForModelCore", async () => ({ apiKey: "synthetic-source-key", mode: "oauth" }));
    syntheticDependencies.set("../../../plugins/provider-runtime.js:prepareProviderRuntimeAuth", async () => {
      preparationCalls++;
      return { apiKey: "synthetic-prepared-key", baseUrl: endpoint, expiresAt: Date.now() + 60000, request: preparedRequest };
    });
    syntheticDependencies.set("../../provider-runtime-auth-protection.js:protectPreparedProviderRuntimeAuth", ({ preparedAuth }) => preparedAuth);
    syntheticDependencies.set("./provider-attribution.js:resolveProviderRequestCapabilities", () => ({ endpointClass: "custom", attributionHeaders: {} }));
    syntheticDependencies.set("@openclaw/normalization-core/string-coerce:normalizeLowercaseStringOrEmpty", value => typeof value === "string" ? value.toLowerCase() : "");
    syntheticDependencies.set("../../embedded-agent-helpers.js:isFailoverErrorMessage", () => true);
    syntheticDependencies.set("../../embedded-agent-helpers.js:classifyFailoverReason", () => "auth");
    const authState = {
      models: { runtime: f.model, effective: f.model },
      runtimeAuthRefreshCancelled: true, profileIndex: 0,
    };
    const controller = createEmbeddedRunAuthController({
      config: {}, agentDir: "/synthetic", workspaceDir: "/synthetic",
      authStore: {}, authStorage: f.storage, profileCandidates: [undefined],
      provider: f.model.provider, modelId: f.model.id, state: authState,
      log: { debug() {}, warn() {}, error() {} },
    });
    try {
      await controller.applyAuthProfileCandidate();
      assert.equal(preparationCalls, 1);
      // The old session model must refuse while transport points elsewhere.
      assert.equal(f.session.captureRuntimeAuthRead(), undefined);
      f.session.agent.state.model = authState.models.runtime;
      const lease = f.session.captureRuntimeAuthRead();
      assert.equal(lease.apiKey, "synthetic-prepared-key");
      lease.assertCurrent();
      assert.equal(preparationCalls, 1);
      endpoint = "https://refreshed.invalid";
      assert.equal(await controller.maybeRefreshRuntimeAuthForAuthError("synthetic-auth-error", false), true);
      assert.equal(preparationCalls, 2);
      assert.throws(() => lease.assertCurrent(), /no longer current/);
      assert.equal(f.session.captureRuntimeAuthRead(), undefined);
      f.session.agent.state.model = authState.models.runtime;
      const refreshed = f.session.captureRuntimeAuthRead();
      assert.equal(refreshed.apiKey, "synthetic-prepared-key");
      refreshed.assertCurrent();
      assert.equal(preparationCalls, 2);
      for (const request of [
        { auth: { mode: "authorization-bearer", token: "synthetic-other-token" } },
        { headers: { "x-api-key": "synthetic-other-header" } },
      ]) {
        preparedRequest = request;
        await controller.applyAuthProfileCandidate();
        f.session.agent.state.model = authState.models.runtime;
        assert.equal(f.session.captureRuntimeAuthRead(), undefined);
      }
      f.assertNoReads();
    } finally {
      controller.stopRuntimeAuthRefreshTimer();
      syntheticDependencies.clear();
    }
  });

  it("refuses model headers and owner-attached transport overrides on capture and completion", () => {
    const f = fixture();
    const lease = f.session.captureRuntimeAuthRead();
    f.model.headers = { "x-api-key": "synthetic-header" };
    assert.equal(f.session.captureRuntimeAuthRead(), undefined);
    assert.throws(() => lease.assertCurrent(), /no longer current/);
    delete f.model.headers;
    f.session.agent.state.model = attachModelProviderRequestTransport(f.model, {
      auth: { mode: "authorization-bearer", token: "synthetic-other-token" },
    });
    assert.equal(f.session.captureRuntimeAuthRead(), undefined);
    f.assertNoReads();
  });

  it("reads the concrete session and decodes only its already selected memory credential", () => {
    const f = fixture();
    sealSecretSentinel("synthetic-other-key", { label: "synthetic-other-owner" });
    const redaction = readGlobalSingleton(Symbol.for("openclaw.secretRedactionRegistry"));
    const before = [...redaction.registeredValues.keys()];
    const revision = redaction.registryRevision;
    const lease = f.session.captureRuntimeAuthRead();
    assert.equal(lease.apiKey, "synthetic-memory-key");
    assert.equal(lease.provider, f.model.provider);
    assert.equal(lease.model, f.model.id);
    lease.assertCurrent();
    assert.deepEqual([...redaction.registeredValues.keys()], before);
    assert.equal(redaction.registryRevision, revision);
    f.assertNoReads();
  });

  for (const mutate of [
    f => f.storage.setRuntimeApiKey(f.model.provider, f.key, f.selection),
    f => f.storage.removeRuntimeApiKey(f.model.provider),
    f => f.storage.setFallbackResolver(() => { throw new Error("Forbidden fallback"); }),
    f => { f.session.agent.state.model = { ...f.model }; },
    f => f.session.dispose(),
  ]) {
    it("invalidates an existing lease through the actual owner mutation", () => {
      const f = fixture();
      const lease = f.session.captureRuntimeAuthRead();
      mutate(f);
      assert.throws(() => lease.assertCurrent(), /no longer current/);
      f.assertNoReads();
    });
  }

  it("refuses a key without producer selection and never resolves a stored or fallback key", () => {
    const f = fixture();
    f.storage.setRuntimeApiKey(f.model.provider, f.key);
    assert.equal(f.session.captureRuntimeAuthRead(), undefined);
    f.storage.removeRuntimeApiKey(f.model.provider);
    assert.equal(f.session.captureRuntimeAuthRead(), undefined);
    f.assertNoReads();
  });

  it("invalidates on an auth reload and refuses instead of selecting storage credentials", () => {
    const f = fixture();
    const lease = f.session.captureRuntimeAuthRead();
    f.storage.reload(); // Explicit synthetic writer action, never invoked by a read.
    assert.throws(() => lease.assertCurrent(), /no longer current/);
    assert.equal(f.session.captureRuntimeAuthRead(), undefined);
  });

  it("rejects an undecodable process-local sentinel without credential fallback", () => {
    const f = fixture();
    const first = "oc-sent-v2.".length;
    const corrupt = f.key.slice(0, first) + (f.key[first] === "A" ? "B" : "A") + f.key.slice(first + 1);
    f.storage.setRuntimeApiKey(f.model.provider, corrupt, f.selection);
    assert.equal(f.session.captureRuntimeAuthRead(), undefined);
    f.assertNoReads();
  });

  it("fences the exact active-run registration and rejects its replacement", () => {
    const f = fixture();
    const sessionKey = "synthetic-session-key";
    const sessionId = f.session.sessionId;
    const handle = { runId: "synthetic-run", captureRuntimeAuthRead: () => f.session.captureRuntimeAuthRead() };
    const registration = { sessionKey, sessionId };
    const { ACTIVE_EMBEDDED_RUNS: runs, ACTIVE_EMBEDDED_RUNS_BY_RUN_ID: byRun, ACTIVE_EMBEDDED_RUN_REGISTRATIONS: registrations, ACTIVE_EMBEDDED_RUN_SESSION_IDS_BY_KEY: byKey } = state;
    try {
      assert.equal(captureActiveEmbeddedSessionRuntimeAuth(sessionKey), undefined);
      runs.set(sessionId, handle);
      byRun.set(handle.runId, handle);
      byKey.set(sessionKey, sessionId);
      registrations.set(handle, registration);
      const lease = captureActiveEmbeddedSessionRuntimeAuth(sessionKey);
      assert.equal(lease.apiKey, "synthetic-memory-key");
      registrations.set(handle, { ...registration });
      assert.throws(() => lease.assertCurrent(), /no longer current/);
      registrations.set(handle, registration);
      runs.delete(sessionId);
      assert.throws(() => lease.assertCurrent(), /no longer current/);
      assert.equal(captureActiveEmbeddedSessionRuntimeAuth(sessionKey), undefined);
      f.assertNoReads();
    } finally {
      runs.delete(sessionId);
      byRun.delete(handle.runId);
      byKey.delete(sessionKey);
      registrations.delete(handle);
    }
  });
});
