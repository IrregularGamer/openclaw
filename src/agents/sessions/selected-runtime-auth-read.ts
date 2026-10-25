import type { RuntimeApiKeyReadSelection } from "./auth-storage-types.js";

export type SelectedRuntimeAuthReadSnapshot = {
  generation: object;
  provider: string;
  model: { id: string; api?: string; baseUrl?: string };
  selection?: RuntimeApiKeyReadSelection;
  apiKey?: string;
};

export type SelectedRuntimeAuthReadLease = {
  readonly apiKey: string;
  readonly mode: "api-key" | "oauth";
  readonly expiresAt?: number;
  assertCurrent(): void;
};

/** Pure validation of facts supplied directly by the existing in-memory auth owner. */
export function captureSelectedRuntimeAuthRead(
  readCurrent: () => SelectedRuntimeAuthReadSnapshot,
  nowMs: () => number = Date.now,
): SelectedRuntimeAuthReadLease | undefined {
  const observed = readCurrent();
  const { apiKey, selection, generation, provider } = observed;
  const model = { ...observed.model };
  const hasUsableExpiry = () =>
    selection?.expiresAt !== undefined &&
    Number.isFinite(selection.expiresAt) &&
    selection.expiresAt > nowMs();
  if (
    !apiKey?.trim() ||
    apiKey === "__aws_sdk_auth__" ||
    !selection ||
    (selection.mode !== "api-key" && selection.mode !== "oauth") ||
    (selection.mode === "oauth" && !hasUsableExpiry()) ||
    (selection.expiresAt !== undefined && !hasUsableExpiry()) ||
    selection.modelId !== model.id ||
    selection.api !== model.api ||
    selection.baseUrl !== model.baseUrl
  ) {
    return undefined;
  }
  const selectedFacts = { ...selection };
  const assertCurrent = () => {
    const current = readCurrent();
    if (
      current.generation !== generation ||
      current.apiKey !== apiKey ||
      current.provider !== provider ||
      current.selection !== selection ||
      selection.mode !== selectedFacts.mode ||
      selection.modelId !== selectedFacts.modelId ||
      selection.api !== selectedFacts.api ||
      selection.baseUrl !== selectedFacts.baseUrl ||
      selection.expiresAt !== selectedFacts.expiresAt ||
      current.model.id !== model.id ||
      current.model.api !== model.api ||
      current.model.baseUrl !== model.baseUrl ||
      (selection.expiresAt !== undefined && !hasUsableExpiry())
    ) {
      throw new Error("Selected runtime authentication is no longer current.");
    }
  };
  assertCurrent();
  return { apiKey, mode: selection.mode, expiresAt: selection.expiresAt, assertCurrent };
}

export type SelectedSessionRuntimeAuthSnapshot = {
  generation: object;
  sessionId: string;
  disposed: boolean;
  model?: { provider: string; id: string; api?: string; baseUrl?: string };
};

/** The concrete session remains the model owner throughout the auth read. */
export function captureSelectedSessionRuntimeAuthRead(
  readCurrent: () => SelectedSessionRuntimeAuthSnapshot,
  readAuth: (
    model: NonNullable<SelectedSessionRuntimeAuthSnapshot["model"]>,
  ) => SelectedRuntimeAuthReadLease | undefined,
) {
  const observed = readCurrent();
  const { generation, sessionId, model } = observed;
  if (observed.disposed || !sessionId || !model) {
    return undefined;
  }
  const route = { provider: model.provider, id: model.id, api: model.api, baseUrl: model.baseUrl };
  const auth = readAuth(model);
  if (!auth) {
    return undefined;
  }
  const assertCurrent = () => {
    auth.assertCurrent();
    const current = readCurrent();
    if (
      current.disposed ||
      current.generation !== generation ||
      current.sessionId !== sessionId ||
      current.model !== model ||
      model.provider !== route.provider ||
      model.id !== route.id ||
      model.api !== route.api ||
      model.baseUrl !== route.baseUrl
    ) {
      throw new Error("Selected session route is no longer current.");
    }
  };
  assertCurrent();
  return {
    provider: route.provider,
    model: route.id,
    api: route.api,
    baseUrl: route.baseUrl,
    ...auth,
    assertCurrent,
  };
}
