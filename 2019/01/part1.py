#!/usr/bin/env python

import time

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	masses = [int(ln) for ln in f]

def fuel_required(mass, part2=False):
	module_fuel = (mass // 3) - 2
	if part2:
		if module_fuel <= 0:
			return 0
		module_fuel += fuel_required(module_fuel, part2=part2)
	return module_fuel

print("Fuel required: %d" % (sum(fuel_required(mass) for mass in masses)))

print("Actual fuel required: %d" % (sum(fuel_required(mass, part2=True) for mass in masses)))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
