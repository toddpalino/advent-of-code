#!/usr/bin/python3

visited = set()
accumulator = 0

# Format will be a list of tuples - (op, arg)
instructions = []

#with open("test.txt") as f:
with open("input.txt") as f:
	for line in f:
		parts = line.strip().split()
		instructions.append((parts[0], int(parts[1])))

i = 0
while i not in visited:
	visited.add(i)
	op = instructions[i][0]
	arg = instructions[i][1]

	if op == 'nop':
		i += 1
	elif op == 'acc':
		accumulator += arg
		i += 1
	elif op == 'jmp':
		i += arg

print(accumulator)
