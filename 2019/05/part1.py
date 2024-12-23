#!/usr/bin/env python

import time
from aoc.utils.intcode import Intcode, read_intcode_from_file

start_time = time.time()

tests = [
	{'mem': [1002,4,3,4,33], 'position': 4, 'value': 99, 'outputs': []},
	{'mem': [1101,100,-1,4,0], 'position': 4, 'value': 99, 'outputs': []}
]

for i, test in enumerate(tests):
	intcode = Intcode(test['mem'])
	intcode.run()
	outputs = intcode.get_output()
	if outputs != test['outputs']:
		print(f'Test {i} failed (outputs expected {test["outputs"]}, got {outputs})')
		break
	if intcode._mem[test['position']] != test['value']:
		print(f'Test {i} failed (position {test["position"]} expected {test['value']}, got {intcode._mem[test["position"]]})')
		break
	print(f'Test {i} passed')

intcode = Intcode(read_intcode_from_file("input.txt"), inputs=[1])
intcode.run()
outputs = intcode.get_output()
print(f'Output: {outputs}')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
