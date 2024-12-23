#!/usr/bin/python3

pairs = []
with open('input.txt') as f:
	for line in f:
		elves = line.strip().split(',')
		e1 = elves[0].split('-')
		e2 = elves[1].split('-')
		pairs.append((
			(int(e1[0]), int(e1[1])),
			(int(e2[0]), int(e2[1]))
		))

count = 0
for pair in pairs:
	if ((pair[0][0] <= pair[1][0]) and (pair[0][1] >= pair[1][1]) or (pair[0][0] >= pair[1][0]) and (pair[0][1] <= pair[1][1])):
		count += 1

print(count)
