#!/usr/bin/env python

import time
from itertools import permutations
from intcode2 import Intcode

def determine_sequence(program):
	amps = [Intcode(program.copy()) for _ in range(5)]
	max_sequence = None
	max_signal = 0

	for sequence in permutations(range(5)):
		signal = 0
		for i, phase in enumerate(sequence):
			intcode = amps[i]
			intcode.reset(inputs=[phase, signal])
			intcode.run()
			outputs = intcode.get_output()
			signal = outputs[0]
		if signal > max_signal:
			max_signal = signal
			max_sequence = sequence
	return max_sequence, max_signal

start_time = time.time()

tests = [
	{'mem': [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], 'sequence': (4,3,2,1,0), 'output': 43210},
	{'mem': [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0],
	 'sequence': (0,1,2,3,4), 'output': 54321},
	{'mem': [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0],
	 'sequence': (1,0,4,3,2), 'output': 65210},
]

for i, test in enumerate(tests):
	sequence, signal = determine_sequence(test['mem'])
	if sequence != test['sequence']:
		print(f'Test {i} failed (sequence expected {test["sequence"]}, got {sequence})')
		continue
	if signal != test['output']:
		print(f'Test {i} failed (signal expected {test["output"]}, got {signal})')
		continue
	print(f'Test {i} passed')

with open('input.txt', 'r') as f:
	mem = [int(x) for x in f.read().strip().split(',')]

sequence, signal = determine_sequence(mem)
print(f'Maximum signal: {signal} (sequence {sequence})')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
