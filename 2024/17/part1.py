#!/usr/bin/env python

import time
from chrono import run_program

start_time = time.time()

# Tests from the puzzle description
tests = [
	{'program': "0,1,5,4,3,0", 'registers': {'a': 729, 'b': 0, 'c': 0}, 'output': [4,6,3,5,6,3,5,2,1,0]},
	{'program': "5,0,5,1,5,4", 'registers': {'a': 10, 'b': 0, 'c': 0}, 'output': [0,1,2]},
	{'program': "0,1,5,4,3,0", 'registers': {'a': 2024, 'b': 0, 'c': 0}, 'output': [4,2,5,6,7,7,7,7,3,1,0]},
]

for i, test in enumerate(tests):
	program = [int(x) for x in test['program'].split(',')]
	if run_program(program, test['registers']) == test['output']:
		print(f"Test {i} passed")
	else:
		print(f"Test {i} failed")

# My puzzle input
prog_str = "2,4,1,6,7,5,4,4,1,7,0,3,5,5,3,0"

program = [int(x) for x in prog_str.split(',')]
output = run_program(program, {'a': 37293246, 'b': 0, 'c': 0})
print("Output: ", ','.join(map(str, output)))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
