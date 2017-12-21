#!/usr/bin/python

instructions = []
with open("input", "r") as f:
	for line in f:
		instructions.append(line.strip().split(' '))

# Test input
test = [
	['set', 'a', '1'],
	['add', 'a', '2'],
	['mul', 'a', 'a'],
	['mod', 'a', '5'],
	['snd', 'a'],
	['set', 'a', '0'],
	['rcv', 'a'],
	['jgz', 'a', '-1'],
	['set', 'a', '1'],
	['jgz', 'a', '-2']
]
#instructions = test

registers = {}
def get_value_or_register(val):
	try:
		return int(val)
	except ValueError:
		return registers.get(val, 0)


num_instructions = len(instructions)
last_frequency = None
ptr = 0

while (ptr >= 0) and (ptr < num_instructions):
	cmd = instructions[ptr]
	incr = 1

	if cmd[0] == 'snd':
		last_frequency = get_value_or_register(cmd[1])
	elif cmd[0] == 'set':
		registers[cmd[1]] = get_value_or_register(cmd[2])
	elif cmd[0] == 'add':
		reg = get_value_or_register(cmd[1])
		registers[cmd[1]] = reg + get_value_or_register(cmd[2])
	elif cmd[0] == 'mul':
		reg = get_value_or_register(cmd[1])
		registers[cmd[1]] = reg * get_value_or_register(cmd[2])
	elif cmd[0] == 'mod':
		reg = get_value_or_register(cmd[1])
		registers[cmd[1]] = reg % get_value_or_register(cmd[2])
	elif cmd[0] == 'rcv':
		if get_value_or_register(cmd[1]) != 0:
			print("RECOVER: {0}".format(last_frequency))
			break
	elif cmd[0] == 'jgz':
		if get_value_or_register(cmd[1]) > 0:
			incr = get_value_or_register(cmd[2])
	ptr += incr
