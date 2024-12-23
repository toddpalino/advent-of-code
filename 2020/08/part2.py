#!/usr/bin/python3

from collections import deque

visited = deque()

# Format will be a list of tuples - (op, arg)
instructions = []

#with open("test.txt") as f:
with open("input.txt") as f:
	for line in f:
		parts = line.strip().split()
		instructions.append((parts[0], int(parts[1])))

finished_instruction = len(instructions)

ptr = 0
bad_ptr = None
while ptr != finished_instruction:
	while ptr not in visited:
		if ptr == finished_instruction:
			break

		visited.append(ptr)
		ptr += (instructions[ptr][1] if instructions[ptr][0] == 'jmp' else 1)

	if ptr == finished_instruction:
		break

	# Rewind the instruction stack to before the last tested nop/jmp
	if bad_ptr is not None:
		while (ptr := visited.pop()) != bad_ptr:
			pass

	# Now rewind the stack to find the next previous nop/jmp to test
	while ptr := visited.pop():
		if instructions[ptr][0] == 'jmp':
			# Treat as a nop
			visited.append(ptr)
			bad_ptr = ptr
			ptr += 1
			break
		elif instructions[ptr][0] == 'nop':
			# Treat as a jmp
			visited.append(ptr)
			bad_ptr = ptr
			ptr += instructions[ptr][1]
			break

# Calculate the accumulator afterwards, so we don't have to constantly rewind it
accumulator = sum(instructions[i][1] for i in visited if instructions[i][0] == 'acc')
print(accumulator)
