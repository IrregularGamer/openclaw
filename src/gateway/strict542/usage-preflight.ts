import type { NativeOwner542, NativeOwnerReadResult } from "./native-owner-transport.js";

// Exact542 strict quota preflight. Point-in-time, read-only and fail-closed:
// anything not proven returns UNKNOWN. Ordinary usage.status is separate and
// unchanged; no cache, last-good, in-flight sharing or ordinary loader is used.

export const PREFLIGHT542_SCHEMA_VERSION = 1;
export const PREFLIGHT542_AGENT_ID = "claw";
export const PREFLIGHT542_SESSION_KEY = "agent:claw:telegram:group:-5217857869";
export const PREFLIGHT542_MAX_DEADLINE_MS = 10_000;
export const PREFLIGHT542_FRESHNESS_MS = 15_000;
const CLOCK_SKEW_TOLERANCE_MS = 1_000;
const PROVIDER_BODY_LIMIT = 65_536;
export const ANTHROPIC_OAUTH_USAGE_URL = "https://api.anthropic.com/api/oauth/usage";
const ANTHROPIC_ROUTE_BASE_URLS = new Set<string | undefined>([
  undefined,
  "https://api.anthropic.com",
  "https://api.anthropic.com/",
]);

const REQUEST_KEYS = ["agentId", "model", "owner", "provider", "requestId", "sessionKey", "timeoutMs"];
const OWNER_KEYS = ["name", "pid", "session", "start"];

export type UsagePreflightRequest = {
  agentId: string;
  sessionKey: string;
  provider: string;
  model: string;
  owner: NativeOwner542;
  requestId: string;
  timeoutMs: number;
};

export type UsagePreflightStatus = "AVAILABLE" | "UNAVAILABLE" | "UNKNOWN";

export type UsagePreflightWindow = { label: string; usedPercent: number; resetAt?: string };

export type UsagePreflightResult = {
  schemaVersion: 1;
  requestId: string;
  agentId: string | null;
  sessionKey: string | null;
  provider: string | null;
  model: string | null;
  owner: NativeOwner542 | null;
  status: UsagePreflightStatus;
  reason: string;
  requestStartedAt: number;
  providerObservedAt: number | null;
  completedAt: number;
  expiresAt: number | null;
  windows: UsagePreflightWindow[];
  source: "provider-live" | null;
  cached: false | null;
  credentialMutation: false | null;
};

/** In-memory selection of the concrete active session (job574 lease). */
export type PreflightSessionLease = {
  readonly provider: string;
  readonly model: string;
  readonly api?: string;
  readonly baseUrl?: string;
  readonly apiKey: string;
  readonly mode: "api-key" | "oauth";
  readonly expiresAt?: number;
  assertCurrent(): void;
};

export type ProviderUsageHttpResult =
  | { ok: true; status: number; body: unknown }
  | { ok: false; reason: "network" | "aborted" | "body_limit" | "malformed_body" };

export type UsagePreflightDeps = {
  /** Monotonic nanoseconds shared with the native read. */
  nowNs: () => bigint;
  /** Wall clock, used only for published timestamps. */
  nowMs: () => number;
  captureSession: (sessionKey: string) => PreflightSessionLease | undefined;
  readNativeOwner: (params: { deadlineNs: bigint; signal: AbortSignal }) => Promise<NativeOwnerReadResult>;
  fetchUsage: (params: { apiKey: string; signal: AbortSignal }) => Promise<ProviderUsageHttpResult>;
};

export function validateUsagePreflightParams(
  params: unknown,
): { ok: true; request: UsagePreflightRequest } | { ok: false; message: string } {
  if (!isExactRecord(params, REQUEST_KEYS)) {
    return { ok: false, message: "usage.preflight requires exactly the exact542 request keys" };
  }
  const { agentId, sessionKey, provider, model, owner, requestId, timeoutMs } = params;
  if (
    typeof agentId !== "string" ||
    typeof sessionKey !== "string" ||
    typeof provider !== "string" ||
    !/^[a-z0-9][a-z0-9._-]{0,63}$/.test(provider) ||
    typeof model !== "string" ||
    !/^[A-Za-z0-9][A-Za-z0-9._:/@-]{0,127}$/.test(model) ||
    typeof requestId !== "string" ||
    !/^[A-Za-z0-9][A-Za-z0-9._:-]{7,127}$/.test(requestId) ||
    !Number.isSafeInteger(timeoutMs) ||
    (timeoutMs as number) < 1_000 ||
    (timeoutMs as number) > PREFLIGHT542_MAX_DEADLINE_MS
  ) {
    return { ok: false, message: "usage.preflight request fields are invalid" };
  }
  if (
    !isExactRecord(owner, OWNER_KEYS) ||
    typeof owner.name !== "string" ||
    typeof owner.session !== "string" ||
    !Number.isSafeInteger(owner.pid) ||
    (owner.pid as number) < 1 ||
    typeof owner.start !== "string" ||
    !/^[0-9]{1,20}$/.test(owner.start)
  ) {
    return { ok: false, message: "usage.preflight owner is invalid" };
  }
  return {
    ok: true,
    request: {
      agentId,
      sessionKey,
      provider,
      model,
      requestId,
      timeoutMs: timeoutMs as number,
      owner: {
        name: owner.name as "Pinch",
        session: owner.session,
        pid: owner.pid as number,
        start: owner.start,
      },
    },
  };
}

/**
 * Runs one strict preflight. `enteredNs` is the handler-entry monotonic time;
 * the single deadline covering identity, auth selection and provider GET
 * starts there. Optional `signal` propagates caller/transport cancellation.
 */
export async function runUsagePreflight(
  request: UsagePreflightRequest,
  deps: UsagePreflightDeps,
  enteredNs: bigint,
  signal?: AbortSignal,
): Promise<UsagePreflightResult> {
  const requestStartedAt = deps.nowMs();
  const deadlineNs = enteredNs + BigInt(request.timeoutMs) * 1_000_000n;
  const controller = new AbortController();
  const onOuterAbort = () => controller.abort();
  signal?.addEventListener("abort", onOuterAbort, { once: true });
  if (signal?.aborted) {
    controller.abort();
  }
  const remainingMs = Number((deadlineNs - deps.nowNs()) / 1_000_000n);
  const timer = setTimeout(() => controller.abort(), Math.max(0, remainingMs));

  const verified: {
    agentId: string | null;
    sessionKey: string | null;
    provider: string | null;
    model: string | null;
    owner: NativeOwner542 | null;
  } = { agentId: null, sessionKey: null, provider: null, model: null, owner: null };
  const unknown = (reason: string): UsagePreflightResult => ({
    schemaVersion: 1,
    requestId: request.requestId,
    ...verified,
    status: "UNKNOWN",
    reason,
    requestStartedAt,
    providerObservedAt: null,
    completedAt: deps.nowMs(),
    expiresAt: null,
    windows: [],
    source: null,
    cached: null,
    credentialMutation: null,
  });
  const expired = () => controller.signal.aborted || deps.nowNs() >= deadlineNs;
  const expiredReason = () => (signal?.aborted ? "cancelled" : "deadline_exceeded");

  try {
    if (expired()) {
      return unknown(expiredReason());
    }
    if (request.agentId !== PREFLIGHT542_AGENT_ID || request.sessionKey !== PREFLIGHT542_SESSION_KEY) {
      return unknown("unknown_agent_session");
    }
    if (
      request.owner.name !== "Pinch" ||
      request.owner.session !== request.sessionKey ||
      request.owner.pid <= 1
    ) {
      return unknown("owner_mismatch");
    }

    // Session route/auth: actual concrete active HQ session, in memory only.
    let lease: PreflightSessionLease | undefined;
    try {
      lease = deps.captureSession(request.sessionKey);
    } catch {
      lease = undefined;
    }
    if (!lease) {
      return unknown("session_auth_unbound");
    }
    if (lease.provider !== request.provider || lease.model !== request.model) {
      return unknown("route_mismatch");
    }
    if (
      lease.provider !== "anthropic" ||
      lease.mode !== "oauth" ||
      lease.api !== "anthropic-messages" ||
      !ANTHROPIC_ROUTE_BASE_URLS.has(lease.baseUrl)
    ) {
      // The selected token is only ever sent to the session's own default
      // Anthropic route.
      // No strict, non-mutating provider quota adapter is proven for this route.
      return unknown("provider_unsupported");
    }
    if (lease.expiresAt === undefined || !(lease.expiresAt > deps.nowMs())) {
      // Expired or unbounded selection: refuse. Nothing here can refresh it.
      return unknown("auth_expired");
    }
    const applicable = applicableWindowKeys(lease.model);
    if (!applicable) {
      return unknown("model_applicability_unknown");
    }

    // Native owner, before. The existing native predicate decides ownership.
    const before = await deps.readNativeOwner({ deadlineNs, signal: controller.signal });
    if (!before.ok) {
      return unknown(expired() ? expiredReason() : `owner_${before.reason}`);
    }
    if (!sameOwner(before.owner, request.owner)) {
      return unknown("owner_mismatch");
    }
    if (expired()) {
      return unknown(expiredReason());
    }
    if (!leaseCurrent(lease)) {
      return unknown("route_auth_changed");
    }

    const response = await deps.fetchUsage({ apiKey: lease.apiKey, signal: controller.signal });
    const providerObservedAt = deps.nowMs();
    if (expired()) {
      return unknown(expiredReason());
    }
    if (!response.ok) {
      return unknown(response.reason === "aborted" ? expiredReason() : `provider_${response.reason}`);
    }
    if (response.status !== 200) {
      return unknown(providerStatusReason(response.status));
    }
    const parsed = parseAnthropicUsageWindows(response.body, applicable);

    // Revalidate route/auth and native owner after the provider read, inside
    // the same deadline.
    if (!leaseCurrent(lease)) {
      return unknown("route_auth_changed");
    }
    const after = await deps.readNativeOwner({ deadlineNs, signal: controller.signal });
    if (!after.ok) {
      return unknown(expired() ? expiredReason() : `owner_${after.reason}`);
    }
    if (!sameOwner(after.owner, before.owner)) {
      return unknown("owner_changed");
    }
    if (!leaseCurrent(lease)) {
      return unknown("route_auth_changed");
    }
    const completedAt = deps.nowMs();
    const completedNs = deps.nowNs();
    if (expired()) {
      return unknown(expiredReason());
    }
    const wallElapsed = completedAt - requestStartedAt;
    const monoElapsed = Number((completedNs - enteredNs) / 1_000_000n);
    if (
      !Number.isFinite(requestStartedAt) ||
      !Number.isFinite(completedAt) ||
      providerObservedAt < requestStartedAt ||
      completedAt < providerObservedAt ||
      Math.abs(wallElapsed - monoElapsed) > CLOCK_SKEW_TOLERANCE_MS
    ) {
      return unknown("clock_anomaly");
    }
    const expiresAt = providerObservedAt + PREFLIGHT542_FRESHNESS_MS;
    if (lease.expiresAt === undefined || lease.expiresAt <= completedAt || completedAt >= expiresAt) {
      return unknown("auth_expired");
    }
    if (parsed.kind === "invalid") {
      return unknown(parsed.reason);
    }
    verified.agentId = request.agentId;
    verified.sessionKey = request.sessionKey;
    verified.provider = lease.provider;
    verified.model = lease.model;
    verified.owner = after.owner;
    const exhausted = parsed.kind === "exhausted";
    return {
      schemaVersion: 1,
      requestId: request.requestId,
      ...verified,
      status: exhausted ? "UNAVAILABLE" : "AVAILABLE",
      reason: exhausted ? "window_exhausted" : "ok",
      requestStartedAt,
      providerObservedAt,
      completedAt,
      expiresAt,
      windows: parsed.windows,
      source: "provider-live",
      cached: false,
      credentialMutation: false,
    };
  } finally {
    clearTimeout(timer);
    signal?.removeEventListener("abort", onOuterAbort);
  }
}

const WINDOW_LABELS: Record<string, string> = {
  five_hour: "5h",
  seven_day: "7d",
  seven_day_opus: "7d-opus",
  seven_day_sonnet: "7d-sonnet",
  seven_day_oauth_apps: "7d-oauth-apps",
};

/** Short/weekly plus the selected model family's weekly window; others UNKNOWN. */
export function applicableWindowKeys(model: string): string[] | undefined {
  const id = model.toLowerCase();
  const opus = id.includes("opus");
  const sonnet = id.includes("sonnet");
  if (opus === sonnet) {
    return undefined;
  }
  return ["five_hour", "seven_day", opus ? "seven_day_opus" : "seven_day_sonnet"];
}

/**
 * Fail-closed parse. Every non-null field must be a recognised window; an
 * unrecognised field may be a restriction, so it is UNKNOWN. Any reported
 * window at or above 100% (applicable or not) is exhaustion and cannot be
 * masked; otherwise every applicable window must be present.
 */
export function parseAnthropicUsageWindows(
  body: unknown,
  applicable: readonly string[],
):
  | { kind: "ok"; windows: UsagePreflightWindow[] }
  | { kind: "exhausted"; windows: UsagePreflightWindow[] }
  | { kind: "invalid"; reason: string } {
  if (!body || typeof body !== "object" || Array.isArray(body)) {
    return { kind: "invalid", reason: "provider_malformed" };
  }
  const reported = new Map<string, UsagePreflightWindow>();
  for (const [key, raw] of Object.entries(body as Record<string, unknown>)) {
    if (raw === null) {
      continue;
    }
    if (!Object.hasOwn(WINDOW_LABELS, key)) {
      return { kind: "invalid", reason: "provider_unrecognized_field" };
    }
    if (typeof raw !== "object" || Array.isArray(raw)) {
      return { kind: "invalid", reason: "window_malformed" };
    }
    const { utilization, resets_at: resetsAt } = raw as Record<string, unknown>;
    if (typeof utilization !== "number" || !Number.isFinite(utilization)) {
      return { kind: "invalid", reason: "window_malformed" };
    }
    if (utilization < 0) {
      return { kind: "invalid", reason: "window_out_of_range" };
    }
    const window: UsagePreflightWindow = { label: WINDOW_LABELS[key], usedPercent: utilization };
    if (resetsAt !== undefined && resetsAt !== null) {
      const parsed = typeof resetsAt === "string" ? Date.parse(resetsAt) : Number.NaN;
      if (!Number.isFinite(parsed)) {
        return { kind: "invalid", reason: "window_malformed" };
      }
      window.resetAt = new Date(parsed).toISOString();
    }
    reported.set(key, window);
  }
  const exhausted = [...reported.values()].filter((window) => window.usedPercent >= 100);
  if (exhausted.length > 0) {
    return { kind: "exhausted", windows: exhausted };
  }
  const windows: UsagePreflightWindow[] = [];
  for (const key of applicable) {
    const window = reported.get(key);
    if (!window) {
      return { kind: "invalid", reason: "window_missing" };
    }
    windows.push(window);
  }
  return { kind: "ok", windows };
}

/** Single GET with the selected in-memory token. No retry, redirect or refresh. */
export async function fetchAnthropicOAuthUsage(params: {
  apiKey: string;
  signal: AbortSignal;
  fetchFn?: typeof fetch;
}): Promise<ProviderUsageHttpResult> {
  const fetchFn = params.fetchFn ?? fetch;
  let response: Response;
  try {
    response = await fetchFn(ANTHROPIC_OAUTH_USAGE_URL, {
      method: "GET",
      headers: {
        accept: "application/json",
        authorization: `Bearer ${params.apiKey}`,
        "anthropic-beta": "oauth-2025-04-20",
      },
      redirect: "error",
      cache: "no-store",
      signal: params.signal,
    });
  } catch {
    return { ok: false, reason: params.signal.aborted ? "aborted" : "network" };
  }
  if (response.status !== 200) {
    // Discard the provider body unread; it is never logged or returned.
    await response.body?.cancel().catch(() => undefined);
    return { ok: true, status: response.status, body: undefined };
  }
  let text = "";
  try {
    const reader = response.body?.getReader();
    const decoder = new TextDecoder();
    let size = 0;
    while (reader) {
      const { done, value } = await reader.read();
      if (done) {
        break;
      }
      size += value.byteLength;
      if (size > PROVIDER_BODY_LIMIT) {
        await reader.cancel().catch(() => undefined);
        return { ok: false, reason: "body_limit" };
      }
      text += decoder.decode(value, { stream: true });
    }
    text += decoder.decode();
  } catch {
    return { ok: false, reason: params.signal.aborted ? "aborted" : "network" };
  }
  try {
    return { ok: true, status: 200, body: JSON.parse(text) };
  } catch {
    return { ok: false, reason: "malformed_body" };
  }
}

function providerStatusReason(status: number): string {
  if (status === 401 || status === 403) {
    return "provider_unauthorized";
  }
  if (status === 429) {
    return "provider_rate_limited";
  }
  if (status >= 500) {
    return "provider_error";
  }
  return "provider_unexpected_status";
}

function leaseCurrent(lease: PreflightSessionLease): boolean {
  try {
    lease.assertCurrent();
    return true;
  } catch {
    return false;
  }
}

function sameOwner(a: NativeOwner542, b: NativeOwner542): boolean {
  return a.name === b.name && a.session === b.session && a.pid === b.pid && a.start === b.start;
}

function isExactRecord(value: unknown, keys: readonly string[]): value is Record<string, unknown> {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    return false;
  }
  const actual = Object.keys(value).toSorted();
  return actual.length === keys.length && actual.every((key, index) => key === keys[index]);
}
