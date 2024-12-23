#!/usr/bin/python3

import time

t1 = time.process_time()

paths = []
nodes = {}
moves = None

with open("input.txt") as f:
	for line in f:
		if moves is None:
			moves = [0 if c == 'L' else 1 for c in line[0:-1]]
			continue
		if len(line) == 1:
			continue

		n = line[0:3]
		nodes[n] = (line[7:10], line[12:15])
		if n[2] == 'A':
			paths.append(n)

# Observation: start/end pairs are unique and consistent
# Observation: the path is always a whole number of loops, and that number is prime
# Observation: Start -> End is the same number of loops as End -> End again

len_paths = len(paths)
len_moves = len(moves)
loops = [0 for i in range(len_paths)]

for i in range(len_paths):
	current = paths[i]

	while True:
		for ptr in range(len_moves):
			current = nodes[current][moves[ptr]]
		loops[i] += 1
		if current[2] == 'Z':
			break

steps = len_moves
for loop in loops:
	steps *= loop

t2 = time.process_time()

print(steps)
print("Time: %f" % (t2 - t1))
