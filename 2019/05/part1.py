#!/usr/bin/env python

import time
from intcode2 import execute

fn = "input.txt"

start_time = time.time()

tests = [
	{'mem': [1002,4,3,4,33], 'position': 4, 'value': 99, 'outputs': []},
	{'mem': [1101,100,-1,4,0], 'position': 4, 'value': 99, 'outputs': []}
]

for i, test in enumerate(tests):
	mem = test['mem']
	outputs = execute(mem)
	if outputs != test['outputs']:
		print(f'Test {i} failed (outputs expected {test["outputs"]}, got {outputs})')
		break
	if mem[test['position']] != test['value']:
		print(f'Test {i} failed (position {test["position"]} expected {test['value']}, got {mem[test["position"]]})')
		break
	print(f'Test {i} passed')

with open(fn, 'r') as f:
	nums = [int(x) for x in f.read().strip().split(',')]

outputs = execute(nums, inputs=[1])
print(f'Output: {outputs}')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
