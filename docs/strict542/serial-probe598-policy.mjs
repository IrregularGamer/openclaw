// Diagnostic scheduling policy only; never an application/build receipt.
export function admitProbe(capacity, env, existingOutput) {
  if (capacity.unresolved || !Number.isFinite(capacity.capacityBytes) ||
      capacity.capacityBytes <= 0 || capacity.capacityBytes > 2*1024**3 ||
      !Number.isFinite(capacity.limitBytes) || capacity.limitBytes <= 0 ||
      capacity.limitBytes > capacity.capacityBytes)
    throw new Error('probe requires observed capacity no larger than admitted2GiB');
  if (existingOutput) throw new Error('probe requires a fresh disposable source export');
  for (const key of Object.keys(env)) {
    if (key === 'NODE_OPTIONS' || key === 'NODE_PATH' || /^(OPENCLAW_|TSDOWN_|TSX_)/u.test(key))
      throw new Error(`probe refuses compiler environment control: ${key}`);
  }
}
