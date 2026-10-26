// Select one complete original typed configuration. Never repartition its graph.
import configs from './tsdown.config.ts';
import { selectTypedWholeConfig } from './scripts/lib/bounded-package608.mjs';
export default selectTypedWholeConfig(configs, process.env.OPENCLAW_608_CONFIG_INDEX,
  process.env.OPENCLAW_608_CONFIG_CENSUS);
