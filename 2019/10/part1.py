#!/usr/bin/env python

import time
from asteroids import Monitoring


tests = [
	{'filename': 'test1.txt', 'location': (3, 4), 'count': 8},
	{'filename': 'test2.txt', 'location': (5, 8), 'count': 33},
	{'filename': 'test3.txt', 'location': (1, 2), 'count': 35},
	{'filename': 'test4.txt', 'location': (6, 3), 'count': 41},
	{'filename': 'test5.txt', 'location': (11, 13), 'count': 210},
]

for i, test in enumerate(tests):
	station = Monitoring(test['filename'])
	location, count = station.find_best_location()
	failed = False
	if location != test['location']:
		print(f'Test {i} failed: expected location {test["location"]}, got {location}')
		failed = True
	if count != test['count']:
		print(f'Test {i} failed: expected count {test["count"]}, got {count}')
		failed = True
	if not failed:
		print(f'Test {i} passed')

start_time = time.time()

station = Monitoring("input.txt")
location, count = station.find_best_location()
print(f'Best location: {location} ({count} asteroids)')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
