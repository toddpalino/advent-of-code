#!/usr/bin/env python

import time
from itertools import permutations
from aoc.utils.intcode import Intcode, read_intcode_from_file

def determine_sequence(program):
	amps = [Intcode(program.copy(), pause_on_output=True) for _ in range(5)]
	max_sequence = None
	max_signal = 0

	for sequence in permutations(range(5, 10)):
		signal = 0
		iter = 0
		while True:
			iter += 1
			for i, phase in enumerate(sequence):
				amp = amps[i]
				if not amp.is_paused():
					amp.reset(inputs=[phase])
				amp.add_input(signal)
				amp.run()
				outputs = amp.get_output()
				if amp.is_paused():
					signal = outputs[0]
			if all(amp.is_halted() for amp in amps):
				break
		if signal > max_signal:
			max_signal = signal
			max_sequence = sequence
	return max_sequence, max_signal

start_time = time.time()

tests = [
	{'mem': [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5],
	 'sequence': (9,8,7,6,5), 'output': 139629729},
	{'mem': [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,
	         55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10],
	 'sequence': (9,7,8,5,6), 'output': 18216},
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

sequence, signal = determine_sequence(read_intcode_from_file("input.txt"))
print(f'Maximum signal: {signal} (sequence {sequence})')

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
