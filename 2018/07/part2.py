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

t = 0
workers = [
	{'task': None, 'finish_at': 0},
	{'task': None, 'finish_at': 0},
	{'task': None, 'finish_at': 0},
	{'task': None, 'finish_at': 0},
	{'task': None, 'finish_at': 0}
]

while True:
	if len(prerequisites) == 0 and not any([w['task'] for w in workers]):
		break

	# Finish tasks first
	for worker in workers:
		if worker['task'] is None:
			continue

		if worker['finish_at'] == t:
			for step in prerequisites:
				prerequisites[step].discard(worker['task'])
			worker['task'] = None
			worker['finish_at'] = 0

	# Assign available tasks
	can_do = available(prerequisites)
	for step in sorted(can_do):
		# Find a worker
		for worker in workers:
			if worker['task'] is None:
				worker['task'] = step
				worker['finish_at'] = t + ord(step) - 4
				prerequisites.pop(step, None)
				break
		else:
			# No workers available, so don't bother anymore
			break

	t += 1

print("Elapsed: {} seconds".format(t-1))
