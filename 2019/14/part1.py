#!/usr/bin/env python

import time
from nanofactory import process_reaction_list, tests, get_ore_required, produce_fuel

for i, test in enumerate(tests):
	reactions = process_reaction_list(test['input'])
	ore, stock = get_ore_required(1, 'FUEL', reactions)
	failed = False
	if ore != test['ore']:
		print(f'Test failed, expected ore {test["ore"]}, got {ore}')
		failed = True
	if test['fuel'] is not None:
		fuel = produce_fuel(1000000000000, reactions)
		if fuel != test['fuel']:
			failed = True
			print(f'Test failed, expected fuel {test["fuel"]}, got {fuel}')
	if not failed:
		print(f'Test passed')
print()

start_time = time.time()

with open("input.txt", 'r') as f:
	data = f.read()
reactions = process_reaction_list(data)
ore, stock = get_ore_required(1, 'FUEL', reactions)
print(f'Ore required for 1 FUEL: {ore}')

p1_time = time.time()
print("Part 1 Elapsed time: %f" % (p1_time - start_time))
print()

fuel = produce_fuel(1000000000000, reactions)
print(f'Fuel produced by 1b ORE: {fuel}')
print("Part 2 Elapsed time: %f" % (time.time() - p1_time))
