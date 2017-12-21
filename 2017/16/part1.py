#!/export/apps/python/3.5/bin/python3.5

import collections

instructions = None
original_programs = 'abcdefghijklmnop'
with open("input", "r") as f:
	instructions = f.read().split(',')

# Test input
#original_programs = 'abcde'
#instructions = ['s1', 'x3/4', 'pe/b']

num_programs = len(original_programs)
programs = collections.deque(original_programs)

for instruction in instructions:
	if instruction[0] == 's':
		programs.rotate(int(instruction[1:]))
	elif instruction[0] == 'x':
		parts = instruction[1:].split('/')
		programs[int(parts[0])], programs[int(parts[1])] = programs[int(parts[1])], programs[int(parts[0])]
	elif instruction[0] == 'p':
		parts = instruction[1:].split('/')
		idx_a = programs.index(parts[0])
		idx_b = programs.index(parts[1])
		programs[idx_a], programs[idx_b] = programs[idx_b], programs[idx_a]

program_list = list(programs)
print("ROUND 1: {0}".format(''.join(program_list)))

# Figure out the moves required to get to this state
moves = [0] * num_programs
for i in range(num_programs):
	moves[i] = program_list.index(original_programs[i])

# Do that 999999999 more times
for c in range(999999999):
	start_str = ''.join(program_list)
	for i in range(num_programs):
		program_list[moves[i]] = start_str[i]

print("ROUND 1b: {0}".format(''.join(program_list)))
