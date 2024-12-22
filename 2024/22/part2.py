#!/usr/bin/env python

import time
from collections import deque
from itertools import product


def get_best_sequence(buyers):
	len_buyers = len(buyers)

	# Rather than record the entire list of 2000 changes, we're going to create a lookup table of sequences
	# to banana totals as we go through. This will allow us to just find the max in the next step
	lookup = {}

	# We don't need to store prices or changes - we can just generate them as we go through
	for buyer in range(len_buyers):
		# We only need to store the last 4 change values
		sequence = deque(maxlen=4)

		# Generate the first 3 numbers (after the seed) to prime our deques
		last_price = buyers[buyer] % 10
		next_num = buyers[buyer]
		for i in range(3):
			# In part 1 this was in a method to avoid repetition. Here, we want to save time from method calls
			next_num = (next_num ^ (next_num * 64)) % 16777216
			next_num = (next_num ^ (next_num // 32)) % 16777216
			next_num = (next_num ^ (next_num * 2048)) % 16777216
			next_price = next_num % 10
			sequence.append(next_price - last_price)
			last_price = next_price

		# Now go through the rest of the prices
		for i in range(3, 2000):
			next_num = (next_num ^ (next_num * 64)) % 16777216
			next_num = (next_num ^ (next_num // 32)) % 16777216
			next_num = (next_num ^ (next_num * 2048)) % 16777216
			next_price = next_num % 10
			sequence.append(next_price - last_price)
			t = tuple(sequence)
			if t not in lookup:
				lookup[t] = {}
			if buyer not in lookup[t]:
				lookup[t][buyer] = next_price
			last_price = next_price

	# Now just find the sequence with the max value
	best_sequence = max(lookup, key=lambda seq: sum(lookup[seq].values()))
	return best_sequence, sum(lookup[best_sequence].values())

tests = [
	{'buyers': [1, 2, 3, 2024], 'sequence': (-2, 1, -1, 3), 'bananas': 23},
]

for i, test in enumerate(tests):
	sequence, bananas = get_best_sequence(test['buyers'])
	failed = False
	if sequence != test['sequence']:
		print(f'Test {i} failed (expected sequence {test["sequence"]}, got {sequence})')
		failed = True
	if bananas != test['bananas']:
		print(f'Test {i} failed (expected bananas {test["bananas"]}, got {bananas})')
		failed = True
	if not failed:
		print(f'Test {i} passed')

start_time = time.time()

with open("input.txt", 'r') as f:
	seeds = [int(line.strip()) for line in f]

sequence, bananas = get_best_sequence(seeds)
print(f"Sequence: {sequence} gets {bananas} bananas")

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
