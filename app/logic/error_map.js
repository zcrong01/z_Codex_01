// [주석단위]_Part_00100_error_map
// Arduino CLI JSON 로그를 받아 블록 ID 목록을 추출하는 단순 예시
function mapErrors(log, sourceMap) {
  const ids = new Set();
  try {
    const data = JSON.parse(log);
    if (Array.isArray(data)) {
      data.forEach(entry => {
        if (entry['file'] && entry['line']) {
          const line = entry['line'];
          for (const [id, lines] of Object.entries(sourceMap)) {
            if (lines.includes(line)) ids.add(id);
          }
        }
      });
    }
  } catch (e) {
    console.warn('log parse failed', e);
  }
  return Array.from(ids);
}

export { mapErrors };
