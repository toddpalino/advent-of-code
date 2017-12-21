#!/export/apps/python/3.5/bin/python3.5

import collections

def permute(programs, instructions):
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
	return programs


instructions = None
original_programs = 'abcdefghijklmnop'
with open("input", "r") as f:
	instructions = f.read().split(',')

# Test input
#original_programs = 'abcde'
#instructions = ['s1', 'x3/4', 'pe/b']

total_rounds = 1000000000
num_programs = len(original_programs)
programs = collections.deque(original_programs)

programs = permute(programs, instructions)
print("ROUND 1: {0}".format(''.join(programs)))

# Figure out the moves required to get to this state
moves = [0] * num_programs
for i in range(num_programs):
	moves[i] = programs.index(original_programs[i])

# Do that 999999999 more times
repeat_after = 0
for c in range(total_rounds - 1):
	programs = permute(programs, instructions)

	# Check if/when we get back to starting positions
	if ''.join(programs) == original_programs:
		repeat_after = c + 2
		break

# Shortcut!
print("\nFound loop after round {0}".format(repeat_after))
print("Skipping {0} rounds and performing the last {1}\n".format((total_rounds // repeat_after) * repeat_after, total_rounds % repeat_after))
for i in range(total_rounds % repeat_after):
	programs = permute(programs, instructions)

print("ROUND 1b: {0}".format(''.join(programs)))
