#!/usr/bin/env python

import time
from asteroids import Monitoring

tests = [
	{'filename': 'test5.txt', 'num': 200, 'asteroid': (8, 2)},
]

for i, test in enumerate(tests):
	station = Monitoring(test['filename'])
	asteroid = station.get_destroyed_asteroid(test['num'])
	failed = False
	if asteroid != test['asteroid']:
		print(f'Test {i} failed: expected asteroid {test["asteroid"]}, got {asteroid}')
		failed = True
	if not failed:
		print(f'Test {i} passed')

start_time = time.time()

station = Monitoring("input.txt")
asteroid = station.get_destroyed_asteroid(200)
print(f'200th asteroid destroyed: {asteroid} ({asteroid[0] * 100 + asteroid[1]})')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
