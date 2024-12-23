#!/usr/bin/python3

from collections import deque

# We will define a high pulse as True, and low pulse as False
# For the flip-flop, the state is False if it is off, and True if it is on

modules = {}
with open("input.txt") as f:
	for line in f:
		ptr = line.index(' -> ')
		name = 'broadcaster'
		if line[0] == '%':
			name = line[1:ptr]
			modules[name] = {'state': False}
		elif line[0] == '&':
			name = line[1:ptr]
			modules[name] = {'inputs': {}}
		else:
			modules[name] = {}

		modules[name]['destinations'] = line[ptr+4:-1].split(', ')

# Post-process to set the conjunction inputs and catch untyped modules
for name in list(modules.keys()):
	module = modules[name]
	for destination in module['destinations']:
		if destination not in modules:
			# Untyped module - Treat it as a sink with no outputs
			modules[destination] = {'destinations': []}
		if 'inputs' in modules[destination]:
			modules[destination]['inputs'][name] = False

presses = []
for _ in range(1000):
	count = {True: 0, False: 0}
	queue = deque([('button', 'broadcaster', False)])
	while queue:
		(source, target, pulse) = queue.popleft()
		count[pulse] += 1
		module = modules[target]
		send = pulse

		if 'state' in module:
			# Flip-flop
			if pulse:
				continue
			send = not module['state']
			module['state'] = not module['state']
		elif 'inputs' in module:
			# Conjunction
			module['inputs'][source] = pulse
			send = not all(module['inputs'].values())

		for destination in module['destinations']:
			queue.append((target, destination, send))

	presses.append(count)

low_count = sum(count[False] for count in presses)
high_count = sum(count[True] for count in presses)
print("low=%d high=%d product=%d" % (low_count, high_count, low_count * high_count))
