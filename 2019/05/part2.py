#!/usr/bin/env python

import time
from intcode2 import execute

fn = "input.txt"

start_time = time.time()

tests = [
	{'mem': [3,9,8,9,10,9,4,9,99,-1,8], 'input': [8], 'outputs': [1]},
	{'mem': [3,9,8,9,10,9,4,9,99,-1,8], 'input': [3], 'outputs': [0]},
	{'mem': [3,9,7,9,10,9,4,9,99,-1,8], 'input': [4], 'outputs': [1]},
	{'mem': [3,9,7,9,10,9,4,9,99,-1,8], 'input': [9], 'outputs': [0]},
	{'mem': [3,3,1108,-1,8,3,4,3,99], 'input': [8], 'outputs': [1]},
	{'mem': [3,3,1108,-1,8,3,4,3,99], 'input': [1], 'outputs': [0]},
	{'mem': [3,3,1107,-1,8,3,4,3,99], 'input': [4], 'outputs': [1]},
	{'mem': [3, 3, 1107, -1, 8, 3, 4, 3, 99], 'input': [9], 'outputs': [0]},
	{'mem': [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 'input': [0], 'outputs': [0]},
	{'mem': [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 'input': [2], 'outputs': [1]},
	{'mem': [3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 'input': [0], 'outputs': [0]},
	{'mem': [3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 'input': [7], 'outputs': [1]},
	{'mem': [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
             1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
             999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 'input': [5], 'outputs': [999]},
	{'mem': [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
             1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
             999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 'input': [8], 'outputs': [1000]},
	{'mem': [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
             1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
             999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], 'input': [9], 'outputs': [1001]},
]

for i, test in enumerate(tests):
	mem = test['mem']
	outputs = execute(mem, inputs=test['input'])
	if outputs != test['outputs']:
		print(f'Test {i} failed (outputs expected {test["outputs"]}, got {outputs})')
	else:
		print(f'Test {i} passed')

with open(fn, 'r') as f:
	nums = [int(x) for x in f.read().strip().split(',')]

outputs = execute(nums, inputs=[5])
print(f'Output: {outputs}')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
