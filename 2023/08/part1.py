#!/usr/bin/python3

nodes = {}
moves = None

with open("input.txt") as f:
	for line in f:
		if moves is None:
			moves = [0 if c == 'L' else 1 for c in line[0:-1]]
			continue
		if len(line) == 1:
			continue
		nodes[line[0:3]] = (line[7:10], line[12:15])

len_moves = len(moves)
ptr = 0
loops = 0
current = 'AAA'
target = 'ZZZ'
while True:
	current = nodes[current][moves[ptr]]
	ptr += 1
	if ptr == len_moves:
		ptr = 0
		loops += 1
	if current == target:
		break

total_moves = (loops * len_moves) + ptr
print(len_moves)
print(total_moves)
