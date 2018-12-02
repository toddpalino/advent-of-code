#!/usr/bin/python

import re

registers = {}
max_register = None
max_value = None

# Read in input
instruction_re = re.compile('^([a-z]+)\s+(inc|dec)\s+([0-9-]+)\s+if\s+([a-z]+)\s+(.*)\s+([0-9-]+)\s*$')
with open("input", "r") as f:
#with open("test_input", "r") as f:
	for line in f:
		m = instruction_re.match(line)
		if not m:
			print("ERR line does not match: {0}".format(line.strip()))
			continue

		# Fetch registers
		tgt = m.group(1)
		tgt_val = registers.get(tgt, 0)
		tst = m.group(4)
		tst_val = registers.get(tst, 0)

		# Set the modifier
		modif = int(m.group(3))
		if m.group(2) == 'dec':
			modif = - modif

		op = m.group(5)
		val = int(m.group(6))
		if op == '>':
			if tst_val > val:
				registers[tgt] = tgt_val + modif
		elif op == '<':
			if tst_val < val:
				registers[tgt] = tgt_val + modif
		elif op == '>=':
			if tst_val >= val:
				registers[tgt] = tgt_val + modif
		elif op == '<=':
			if tst_val <= val:
				registers[tgt] = tgt_val + modif
		elif op == '==':
			if tst_val == val:
				registers[tgt] = tgt_val + modif
		elif op == '!=':
			if tst_val != val:
				registers[tgt] = tgt_val + modif

		tgt_val = registers.get(tgt, 0)
		if (max_register is None) or (tgt_val > max_value):
                	max_register = tgt
                	max_value = tgt_val

print("WORKING MAX: {0} = {1}".format(max_register, max_value))

max_register = None
max_value = -1
for register in registers:
	if (max_register is None) or (registers[register] > max_value):
		max_register = register
		max_value = registers[register]

print("MAX: {0} = {1}".format(max_register, max_value))
