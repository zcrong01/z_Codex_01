// [주석단위]_Part_00100_generator
Blockly.Arduino = new Blockly.Generator('Arduino');

Blockly.Arduino.addReservedWords('setup,loop');

Blockly.Arduino['arduino_setup_loop'] = function(block) {
  const setupCode = Blockly.Arduino.statementToCode(block, 'SETUP');
  const loopCode = Blockly.Arduino.statementToCode(block, 'LOOP');
  return `void setup() {\n${setupCode}}\n\nvoid loop() {\n${loopCode}}\n`;
};

Blockly.Arduino['io_digital_write'] = function(block) {
  const pin = Blockly.Arduino.valueToCode(block, 'PIN', Blockly.Arduino.ORDER_ATOMIC) || '13';
  const val = block.getFieldValue('VAL') || 'HIGH';
  return `digitalWrite(${pin}, ${val});\n`;
};

Blockly.Arduino['base_delay'] = function(block) {
  const ms = Blockly.Arduino.valueToCode(block, 'MS', Blockly.Arduino.ORDER_ATOMIC) || '1000';
  return `delay(${ms});\n`;
};

Blockly.Arduino.statementToCode = function(block, name) {
  const target = block.getInputTargetBlock(name);
  let code = '';
  let current = target;
  while (current) {
    let line = Blockly.Arduino.blockToCode(current);
    if (Array.isArray(line)) line = line[0];
    code += line || '';
    current = current.getNextBlock();
  }
  return code;
};
