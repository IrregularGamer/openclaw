// Whole-config isolation preserves the owning config's shared module graph.
export function configCensus(configs) {
  if (!Array.isArray(configs) || configs.length === 0) throw new Error('missing config inventory');
  return configs.map((config, index) => {
    if (!config || config.dts !== false || !config.entry || Array.isArray(config.entry) ||
        typeof config.entry !== 'object' || Object.keys(config.entry).length === 0 ||
        Object.values(config.entry).some(source => typeof source !== 'string'))
      throw new Error('isolation requires explicit runtime-only named entries');
    return {index, name:config.name ?? null, entry:config.entry, outDir:config.outDir ?? 'dist', dts:false};
  });
}
export function selectWholeConfig(configs, indexText, expectedCensus) {
  const census = JSON.stringify(configCensus(configs));
  if (census !== expectedCensus) throw new Error('config census changed');
  if (typeof indexText !== 'string' || !/^(0|[1-9][0-9]*)$/u.test(indexText))
    throw new Error('invalid config index');
  const index = Number(indexText);
  if (!Number.isSafeInteger(index) || index >= configs.length) throw new Error('config index out of range');
  return configs[index];
}
