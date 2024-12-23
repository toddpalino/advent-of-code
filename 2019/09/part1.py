#!/usr/bin/env python

import time
from aoc.utils.intcode import Intcode, read_intcode_from_file

start_time = time.time()

tests = [
	{'mem': [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99],
	 'output': [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]},
	{'mem': [104,1125899906842624,99], 'output': [1125899906842624]},
]

for i, test in enumerate(tests):
	intcode = Intcode(test['mem'])
	intcode.run()
	outputs = intcode.get_output()
	if outputs != test['output']:
		print(f'Test {i} failed (output expected {test["output"]}, got {outputs})')
		continue
	print(f'Test {i} passed')

intcode = Intcode(read_intcode_from_file('input.txt'), inputs=[1])
intcode.run()
outputs = intcode.get_output()

print(f'BOOST Keycode: {outputs})')

intcode.reset(inputs=[2])
intcode.run()
outputs = intcode.get_output()

print(f'Coordinates: {outputs})')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
