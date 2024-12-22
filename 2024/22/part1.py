#!/usr/bin/env python

import time

def next_number(num, iterations=1):
	next_num = num
	for _ in range(iterations):
		next_num = (next_num ^ (next_num * 64)) % 16777216
		next_num = (next_num ^ (next_num // 32)) % 16777216
		next_num = (next_num ^ (next_num * 2048)) % 16777216
	return next_num


tests = [
	{'seed': 123, 'iterations': 1, 'result': 15887950},
	{'seed': 15887950, 'iterations': 1, 'result': 16495136},
	{'seed': 16495136, 'iterations': 1, 'result': 527345},
	{'seed': 527345, 'iterations': 1, 'result': 704524},
	{'seed': 704524, 'iterations': 1, 'result': 1553684},
	{'seed': 1553684, 'iterations': 1, 'result': 12683156},
	{'seed': 12683156, 'iterations': 1, 'result': 11100544},
	{'seed': 11100544, 'iterations': 1, 'result': 12249484},
	{'seed': 12249484, 'iterations': 1, 'result': 7753432},
	{'seed': 7753432, 'iterations': 1, 'result': 5908254},
	{'seed': 1, 'iterations': 2000, 'result': 8685429},
	{'seed': 10, 'iterations': 2000, 'result': 4700978},
	{'seed': 100, 'iterations': 2000, 'result': 15273692},
	{'seed': 2024, 'iterations': 2000, 'result': 8667524},
]

for i, test in enumerate(tests):
	val = next_number(test['seed'], iterations=test['iterations'])
	if val == test['result']:
		print(f'Test {i} passed')
	else:
		print(f'Test {i} failed (expected {test["result"]}, got {val})')

start_time = time.time()

with open("input.txt", 'r') as f:
	seeds = [int(line.strip()) for line in f]

print(f'Sum of 2000th numbers: {sum(next_number(num, iterations=2000) for num in seeds)}')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
