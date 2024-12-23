#!/usr/bin/env python

import time
from planets import simulate, calculate_energy, tests, planets


for i, test in enumerate(tests):
	failed = False
	simulate(test['planets'], iterations=test['iterations'])
	energy = calculate_energy(test['planets'])
	for p in range(4):
		if test['planets'][p]['position'] != test['expects'][p]['position']:
			failed = True
			print(f'Test {i}: Planet {p} position mismatch (expected {test['expects'][p]['position']}, got {test['planets'][p]['position']})')
		if test['planets'][p]['velocity'] != test['expects'][p]['velocity']:
			failed = True
			print(f'Test {i}: Planet {p} velocity mismatch (expected {test['expects'][p]['velocity']}, got {test['planets'][p]['velocity']})')
	if energy != test['energy']:
		failed = True
		print(f'Test {i}: System energy mismatch (expected {test['energy']}, got {energy})')
	if not failed:
		print(f'Test {i} passed')

start_time = time.time()

simulate(planets, iterations=1000)
energy = calculate_energy(planets)
print(f'Total System Energy: {energy}')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
