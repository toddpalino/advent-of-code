#!/usr/bin/python

instructions = []
with open("input", "r") as f:
	for line in f:
		instructions.append(line.strip().split(' '))

# Test input
test = [
	['snd', '1'],
	['snd', '2'],
	['snd', 'p'],
	['rcv', 'a'],
	['rcv', 'b'],
	['rcv', 'c'],
	['rcv', 'd']
]
#instructions = test

def get_value_or_register(val, registers):
	try:
		return int(val)
	except ValueError:
		return registers.get(val, 0)


num_instructions = len(instructions)
registers = [{'p': 0}, {'p': 1}]
queues = [[], []]
ptrs = [0, 0]
sends = [0, 0]

def run_until_stopped(my_id):
	other_id = (my_id + 1) % 2

	c = 0
	while (ptrs[my_id] >= 0) and (ptrs[my_id] < num_instructions):
		cmd = instructions[ptrs[my_id]]
		incr = 1

		if cmd[0] == 'snd':
			queues[other_id].append(get_value_or_register(cmd[1], registers[my_id]))
			sends[my_id] = sends[my_id] + 1
		elif cmd[0] == 'set':
			registers[my_id][cmd[1]] = get_value_or_register(cmd[2], registers[my_id])
		elif cmd[0] == 'add':
			reg = get_value_or_register(cmd[1], registers[my_id])
			registers[my_id][cmd[1]] = reg + get_value_or_register(cmd[2], registers[my_id])
		elif cmd[0] == 'mul':
			reg = get_value_or_register(cmd[1], registers[my_id])
			registers[my_id][cmd[1]] = reg * get_value_or_register(cmd[2], registers[my_id])
		elif cmd[0] == 'mod':
			reg = get_value_or_register(cmd[1], registers[my_id])
			registers[my_id][cmd[1]] = reg % get_value_or_register(cmd[2], registers[my_id])
		elif cmd[0] == 'rcv':
			if len(queues[my_id]) > 0:
				registers[my_id][cmd[1]] = queues[my_id].pop(0)
			else:
				break
		elif cmd[0] == 'jgz':
			if get_value_or_register(cmd[1], registers[my_id]) > 0:
				incr = get_value_or_register(cmd[2], registers[my_id])
		ptrs[my_id] = ptrs[my_id] + incr
		c += 1

	return c


while True:
	someone_moved = False
	for i in [0, 1]:
		c = run_until_stopped(i)
		if c > 0:
			someone_moved = True
	if not someone_moved:
		break

print("PGM 1 Sends: {0}".format(sends[1]))
