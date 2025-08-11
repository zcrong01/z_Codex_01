// [주석단위]_Part_00100_blocks
Blockly.Blocks['arduino_setup_loop'] = {
  init: function() {
    this.appendDummyInput().appendField('setup / loop');
    this.appendStatementInput('SETUP').appendField('setup');
    this.appendStatementInput('LOOP').appendField('loop');
    this.setColour('#7950f2');
  }
};

Blockly.Blocks['io_digital_write'] = {
  init: function() {
    this.appendDummyInput().appendField('digitalWrite');
    this.appendValueInput('PIN').setCheck('Number').appendField('PIN');
    this.appendDummyInput().appendField('을')
        .appendField(new Blockly.FieldDropdown([["HIGH","HIGH"],["LOW","LOW"]]), 'VAL');
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour('#228be6');
  }
};

Blockly.Blocks['base_delay'] = {
  init: function() {
    this.appendDummyInput().appendField('delay');
    this.appendValueInput('MS').setCheck('Number').appendField('ms');
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour('#40c057');
  }
};
