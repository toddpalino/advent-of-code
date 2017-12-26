#!/usr/bin/python

import sys

# Rules
writeValue = {
	'A': [1, 0],
	'B': [0, 0],
	'C': [1, 1],
	'D': [1, 0],
	'E': [1, 1],
	'F': [1, 1]
}
movePtr = {
	'A': [1, 1],
	'B': [-1, 1],
	'C': [1, 1],
	'D': [-1, -1],
	'E': [1, -1],
	'F': [1, 1],
}
newState = {
	'A': ['B', 'C'],
	'B': ['A', 'D'],
	'C': ['D', 'A'],
	'D': ['E', 'D'],
	'E': ['F', 'B'],
	'F': ['A', 'E']
}

diagnosticAt = 12368930
state = 'A'
positions = {}
ptr = 0

counter = 0
while counter < diagnosticAt:
	val = positions.get(ptr, 0)
	positions[ptr] = writeValue[state][val]
	ptr += movePtr[state][val]
	state = newState[state][val]
	counter += 1

	if counter % 1000000 == 0:
		sys.stdout.write('.')
		sys.stdout.flush()

print("\nCHECKSUM: {}".format(sum(positions.values())))
