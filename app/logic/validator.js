// [주석단위]_Part_00100_validator
// 단순 예시: 워크스페이스의 모든 블록을 순회하며 핀 번호가 음수인지 검사
function validateWorkspace(workspace) {
  const issues = [];
  const blocks = workspace.getAllBlocks(false);
  blocks.forEach(block => {
    if (block.type === 'io_digital_write') {
      const pinBlock = block.getInputTargetBlock('PIN');
      if (pinBlock && pinBlock.type === 'math_number') {
        const val = Number(pinBlock.getFieldValue('NUM'));
        if (val < 0) {
          issues.push({id: block.id, message: '핀 번호는 음수가 될 수 없습니다.'});
        }
      }
    }
  });
  return issues;
}

export { validateWorkspace };
