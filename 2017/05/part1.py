#!/usr/bin/python

# Read in input
instructions = []
with open("input", "r") as f:
	for line in f:
		instructions.append(int(line.strip()))

# Test input
# instructions = [0, 3, 0, 1, -3]

max_i = len(instructions)
i = 0
c = 0
while True:
	if (i < 0) or (i >= max_i):
		break
	next_i = i + instructions[i]
	instructions[i] = instructions[i] + 1
	i = next_i
	c += 1

print("Count: {0}".format(c))
