#!/usr/bin/python

from copy import deepcopy

def steps_away(current_steps):
	# Clone the dict so we don't change it
	steps = deepcopy(current_steps)

	# ne + sw = 0
	if steps['ne'] >= steps['sw']:
		steps['ne'] = steps['ne'] - steps['sw']
		steps['sw'] = 0
	else:
		steps['sw'] = steps['sw'] - steps['ne']
		steps['ne'] = 0

	# nw + se = 0
	if steps['nw'] >= steps['se']:
		steps['nw'] = steps['nw'] - steps['se']
		steps['se'] = 0
	else:
		steps['se'] = steps['se'] - steps['nw']
		steps['nw'] = 0

	# n + s = 0
	if steps['n'] >= steps['s']:
		steps['n'] = steps['n'] - steps['s']
		steps['s'] = 0
	else:
		steps['s'] = steps['s'] - steps['n']
		steps['n'] = 0

	# ne + nw is just n
	if steps['ne'] >= steps['nw']:
		steps['n'] = steps['n'] + steps['nw']
		steps['ne'] = steps['ne'] - steps['nw']
		steps['nw'] = 0
	else:
		steps['n'] = steps['n'] + steps['ne']
		steps['nw'] = steps['nw'] - steps['ne']
		steps['ne'] = 0

	# se + sw is just s
	if steps['se'] >= steps['sw']:
		steps['s'] = steps['s'] + steps['sw']
		steps['se'] = steps['se'] - steps['sw']
		steps['sw'] = 0
	else:
		steps['s'] = steps['s'] + steps['se']
		steps['sw'] = steps['sw'] - steps['se']
		steps['se'] = 0

	# n + sw = nw
	if steps['n'] >= steps['sw']:
		steps['nw'] = steps['nw'] + steps['sw']
		steps['n'] = steps['n'] - steps['sw']
		steps['sw'] = 0
	else:
		steps['nw'] = steps['nw'] + steps['n']
		steps['sw'] = steps['sw'] - steps['n']
		steps['n'] = 0

	# n + se = ne
	if steps['n'] >= steps['se']:
		steps['ne'] = steps['ne'] + steps['se']
		steps['n'] = steps['n'] - steps['se']
		steps['se'] = 0
	else:
		steps['ne'] = steps['ne'] + steps['n']
		steps['se'] = steps['se'] - steps['n']
		steps['n'] = 0

	# s + nw = sw
	if steps['s'] >= steps['nw']:
		steps['sw'] = steps['sw'] + steps['nw']
		steps['s'] = steps['s'] - steps['nw']
		steps['nw'] = 0
	else:
		steps['sw'] = steps['sw'] + steps['s']
		steps['nw'] = steps['nw'] - steps['s']
		steps['s'] = 0

	# s + ne = se
	if steps['s'] >= steps['ne']:
		steps['se'] = steps['se'] + steps['ne']
		steps['s'] = steps['s'] - steps['ne']
		steps['ne'] = 0
	else:
		steps['se'] = steps['se'] + steps['s']
		steps['ne'] = steps['ne'] - steps['s']
		steps['s'] = 0

	return sum(steps.values())

directions = []
with open("input", "r") as f:
	directions = f.read().strip().split(',')

steps = {
	'ne': 0,
	'n': 0,
	'nw': 0,
	'sw': 0,
	's': 0,
	'se': 0
}

max_distance = 0
for direction in directions:
	steps[direction] = steps[direction] + 1
	current_steps_away = steps_away(steps)
	if current_steps_away > max_distance:
		max_distance = current_steps_away

print("STEPS: {0}".format(steps_away(steps)))
print("MAX: {0}".format(max_distance))
