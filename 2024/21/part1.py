#!/usr/bin/env python

import time
from keypads import get_optimized_command_length, expand_numeric_command, calculate_complexity

def get_sequence_complexity(numeric_codes, depth):
	total_complexity = 0
	total_length = 0
	for code in numeric_codes:
		commands = expand_numeric_command(code)
		seq_len = sum(get_optimized_command_length(command, depth) for command in commands)
		total_complexity += calculate_complexity(code, seq_len)
		total_length += seq_len
	return total_complexity, total_length

tests = [
	{'code': '029A', 'length': 68, 'complexity': 68 * 29, 'num_directional_bots': 2},
	{'code': '980A', 'length': 60, 'complexity': 60 * 980, 'num_directional_bots': 2},
	{'code': '179A', 'length': 68, 'complexity': 68 * 179, 'num_directional_bots': 2},
	{'code': '456A', 'length': 64, 'complexity': 64 * 456, 'num_directional_bots': 2},
	{'code': '379A', 'length': 64, 'complexity': 64 * 379, 'num_directional_bots': 2},
]

for i, test in enumerate(tests):
	score, sequence_length = get_sequence_complexity([test['code']], test['num_directional_bots'])
	failed = False
	if sequence_length != test['length']:
		print(f'Test {i} failed (expected sequence length {test["length"]}, got {sequence_length})')
		failed = True
	if score != test['complexity']:
		print(f'Test {i} failed (expected complexity {test['complexity']}, got {score})')
		failed = True
	if not failed:
		print(f'Test {i} passed')

# This bot count is the number of directional keypad bots (not numeric)
part1_bots = 2
part2_bots = 25
codes = ['286A', '974A', '189A', '802A', '805A']

start_time = time.time()
score, sequence_length = get_sequence_complexity(codes, part1_bots)
print(f'Part 1 - Total complexity: {score}')
print(f'Part 1 - Sequence Length: {sequence_length}')
print(f'Part 1 time: {time.time() - start_time}')

start_time = time.time()
score, sequence_length = get_sequence_complexity(codes, part2_bots)
print(f'Part 2 - Total complexity: {score}')
print(f'Part 2 - Sequence Length: {sequence_length}')
print(f'Overall time: {time.time() - start_time}')

