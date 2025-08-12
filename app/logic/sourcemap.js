// [주석단위]_Part_00100_sourcemap
function createSourceMap(code) {
  const map = {};
  const lines = code.split('\n');
  lines.forEach((line, idx) => {
    const m = line.match(/\[BL:([a-z0-9_-]+)\]/i);
    if (m) {
      const id = m[1];
      if (!map[id]) map[id] = [];
      map[id].push(idx + 1); // 1-based
    }
  });
  return map;
}

export { createSourceMap };
