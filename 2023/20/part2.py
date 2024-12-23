#!/usr/bin/python3

from collections import deque

# We will define a high pulse as True, and low pulse as False
# For the flip-flop, the state is False if it is off, and True if it is on

modules = {'rx': {'destinations': []}}
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

# Post-process to set the conjunction inputs
for name in modules.keys():
	module = modules[name]
	for destination in module['destinations']:
		if 'inputs' in modules[destination]:
			modules[destination]['inputs'][name] = False

# Run cycles and determine when the qf module will send a low pulse (when all inputs are high)
# This happens in the cycle where all 4 of its inputs (pg, sp, sv, qs) send a high signal to it
inputs = {'pg': 0, 'sp': 0, 'sv': 0, 'qs': 0}

count = 0
while True:
	queue = deque([('button', 'broadcaster', False)])
	count += 1

	while queue:
		(source, target, pulse) = queue.popleft()
		module = modules[target]
		send = pulse

		if target == 'gf' and pulse:
			inputs[source] = count
		if all(inputs.values()):
			break

		if target == 'rx' and not pulse:
			break

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

	if all(inputs.values()):
		break

product = 1
for val in inputs.values():
	product *= val

print(inputs)
print(product)
