#!/usr/bin/python3

mask = [None] * 36
mem = {}

#with open("test.txt") as f:
with open("input.txt") as f:
	for line in f:
		if line.startswith("mask"):
			# Keep the 1 and 0 as strings because we will do string manipulation
			mask = [None if c == 'X' else c for c in line[7:-1]]
			continue
		if line.startswith("mem"):
			parts = line.split(' = ')
			loc = int(parts[0][4:-1])

			# Convert the value to store to a 36-bit binary string (as list)
			val = list(format(int(parts[1]), '036b'))

			# Apply the mask to the binary string
			for i in range(36):
				if mask[i] is not None:
					val[i] = mask[i]

			# Write the value to the memory location
			mem[loc] = int(''.join(val), 2)

print(sum(mem.values()))

