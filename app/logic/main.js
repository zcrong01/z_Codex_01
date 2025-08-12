// [주석단위]_Part_00100_main_logic
import { validateWorkspace } from './validator.js';
import { createSourceMap } from './sourcemap.js';
import { mapErrors } from './error_map.js';

window.AppLogic = {
  validateWorkspace,
  createSourceMap,
  mapErrors,
};
