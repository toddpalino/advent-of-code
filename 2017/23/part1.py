#!/usr/bin/python

instructions = []
with open("input", "r") as f:
	for line in f:
		instructions.append(line.strip().split(' '))

registers = {}
def get_value_or_register(val):
	try:
		return int(val)
	except ValueError:
		return registers.get(val, 0)

num_instructions = len(instructions)
last_frequency = None
ptr = 0

mulCounter = 0
while (ptr >= 0) and (ptr < num_instructions):
	cmd = instructions[ptr]
	incr = 1

	if cmd[0] == 'set':
		registers[cmd[1]] = get_value_or_register(cmd[2])
	elif cmd[0] == 'sub':
		regX = get_value_or_register(cmd[1])
		registers[cmd[1]] = regX - get_value_or_register(cmd[2])
	elif cmd[0] == 'mul':
		regX = get_value_or_register(cmd[1])
		registers[cmd[1]] = regX * get_value_or_register(cmd[2])
		mulCounter += 1
	elif cmd[0] == 'jnz':
		if get_value_or_register(cmd[1]) != 0:
			incr = get_value_or_register(cmd[2])
	ptr += incr

print("MUL: {0}".format(mulCounter))
