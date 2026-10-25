import assert from "node:assert/strict";
import { describe, it } from "node:test";
import {
  captureSelectedRuntimeAuthRead,
  captureSelectedSessionRuntimeAuthRead,
} from "./selected-runtime-auth-read.ts";

// Synthetic state is explicit and mutable. Both production predicates run;
// there is no fixture callback that unconditionally grants availability.
function fixture() {
  let now = 1000;
  const model = { provider: "anthropic", id: "claude-test", api: "anthropic-messages", baseUrl: "https://example.invalid" };
  const session = { generation: {}, sessionId: "synthetic-session", disposed: false, model };
  const auth = {
    generation: {},
    provider: "anthropic",
    model,
    selection: { modelId: model.id, api: model.api, baseUrl: model.baseUrl, mode: "oauth", expiresAt: 2000 },
    apiKey: "synthetic-existing-memory-key",
  };
  const captureAuth = () => captureSelectedRuntimeAuthRead(() => auth, () => now);
  const capture = () => captureSelectedSessionRuntimeAuthRead(() => session, captureAuth);
  return { auth, session, captureAuth, capture, setNow(value) { now = value; } };
}

describe("selected existing memory auth read", () => {
  it("accepts the exact active OAuth model and finite unexpired selected credential", () => {
    const f = fixture();
    const lease = f.capture();
    assert.equal(lease.provider, "anthropic");
    assert.equal(lease.model, "claude-test");
    assert.equal(lease.mode, "oauth");
    assert.equal(lease.apiKey, "synthetic-existing-memory-key");
    lease.assertCurrent();
  });

  it("accepts explicit API-key selection without an expiry", () => {
    const f = fixture();
    f.auth.selection.mode = "api-key";
    delete f.auth.selection.expiresAt;
    assert.equal(f.capture().mode, "api-key");
  });

  for (const mode of [undefined, "", "token", "aws-sdk", "native", "configured"]) {
    it(`refuses unsupported or absent selected mode ${String(mode)}`, () => {
      const f = fixture();
      f.auth.selection.mode = mode;
      assert.equal(f.capture(), undefined);
    });
  }

  for (const expiresAt of [undefined, null, NaN, Infinity, -Infinity, 999, 1000]) {
    it(`refuses OAuth with unusable expiry ${String(expiresAt)}`, () => {
      const f = fixture();
      f.auth.selection.expiresAt = expiresAt;
      assert.equal(f.capture(), undefined);
    });
  }

  for (const apiKey of [undefined, "", "  ", "__aws_sdk_auth__"]) {
    it(`refuses missing or placeholder memory selection ${String(apiKey)}`, () => {
      const f = fixture();
      f.auth.apiKey = apiKey;
      assert.equal(f.capture(), undefined);
    });
  }

  it("refuses an override that was not installed by the model/auth selector", () => {
    const f = fixture();
    delete f.auth.selection;
    assert.equal(f.capture(), undefined);
  });

  for (const field of ["modelId", "api", "baseUrl"]) {
    it(`refuses a selected ${field} from a different route`, () => {
      const f = fixture();
      f.auth.selection[field] = "other-route";
      assert.equal(f.capture(), undefined);
    });
  }

  it("expires before the before/after acceptance check without a refresh", () => {
    const f = fixture();
    const lease = f.capture();
    f.setNow(2000);
    assert.throws(() => lease.assertCurrent(), /no longer current/);
    assert.equal(f.capture(), undefined);
  });

  for (const mutate of [
    f => { f.auth.generation = {}; },
    f => { f.auth.apiKey = "replacement-memory-key"; },
    f => { f.auth.provider = "other-provider"; },
    f => { f.auth.selection = { ...f.auth.selection }; },
    f => { f.auth.selection.mode = "token"; },
    f => { f.auth.selection.expiresAt += 100; },
    f => { f.auth.selection.modelId = "other-model"; },
    f => { delete f.auth.selection; },
  ]) {
    it("invalidates after the existing auth owner or selection changes", () => {
      const f = fixture();
      const lease = f.capture();
      mutate(f);
      assert.throws(() => lease.assertCurrent(), /no longer current/);
    });
  }

  for (const mutate of [
    f => { f.session.generation = {}; },
    f => { f.session.sessionId = "replacement-session"; },
    f => { f.session.model = { ...f.session.model }; },
    f => { f.session.disposed = true; },
    f => { f.session.model.provider = "other-provider"; },
    f => { f.session.model.id = "other-model"; },
    f => { f.session.model.api = "other-api"; },
    f => { f.session.model.baseUrl = "https://other.invalid"; },
  ]) {
    it("invalidates after session disposal, replacement or actual route changes", () => {
      const f = fixture();
      const lease = f.capture();
      mutate(f);
      assert.throws(() => lease.assertCurrent(), /no longer current/);
    });
  }

  for (const mutate of [
    f => { f.session.disposed = true; },
    f => { f.session.sessionId = ""; },
    f => { delete f.session.model; },
  ]) {
    it("refuses absent, disposed or unidentified concrete sessions", () => {
      const f = fixture();
      mutate(f);
      assert.equal(f.capture(), undefined);
    });
  }

  it("invalidates an ABA auth replacement even with identical final key bytes", () => {
    const f = fixture();
    const lease = f.capture();
    const original = f.auth.apiKey;
    f.auth.apiKey = "replacement";
    f.auth.generation = {};
    f.auth.apiKey = original;
    assert.throws(() => lease.assertCurrent(), /no longer current/);
  });

  it("invalidates a route round trip recorded by the actual model mutation epoch", () => {
    const f = fixture();
    const lease = f.capture();
    f.session.generation = {};
    assert.throws(() => lease.assertCurrent(), /no longer current/);
  });

  it("rechecks after auth capture before returning a session lease", () => {
    const f = fixture();
    assert.throws(() => captureSelectedSessionRuntimeAuthRead(() => f.session, () => {
      const auth = f.captureAuth();
      f.session.disposed = true;
      return auth;
    }), /no longer current/);
  });
});
