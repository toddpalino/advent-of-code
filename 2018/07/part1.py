#!/usr/bin/env python3

def available(prereqs):
	steps = set()
	for step in prereqs:
		if prereqs[step] == set():
			steps.add(step)
	return steps


prerequisites = {}
with open('input', 'r') as f:
	for line in f:
		words = line.split(' ')
		if words[1] not in prerequisites:
			prerequisites[words[1]] = set()
		if words[7] not in prerequisites:
			prerequisites[words[7]] = set()
		prerequisites[words[7]].add(words[1])

order = ''
while True:
	can_do = available(prerequisites)
	if len(can_do) == 0:
		break
	next_step = sorted(can_do)[0]
	order += next_step

	prerequisites.pop(next_step, None)
	for step in prerequisites:
		prerequisites[step].discard(next_step)

print(order)
