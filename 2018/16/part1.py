#!/usr/bin/env python3

from itertools import islice

samples = []

# Before: [0, 3, 3, 0]
# 5 0 2 1
# After:  [0, 0, 3, 0]

with open('samples', 'r') as f:
	try:
		while True:
			data =  islice(f, 0, 4)

			before = next(data)
			op = [int(x) for x in next(data).split(' ')]
			after = next(data)
			junk = next(data)

			samples.append({
				'before': [int(x) for x in before[9:-2].split(', ')],
				'opcode': op[0],
				'args': op[1:3],
				'output': op[3],
				'after': [int(x) for x in after[9:-2].split(', ')],
				'behaves': set()
			})
	except StopIteration:
		pass

funcs = {
	'addr': lambda a, b, register: register[a] + register[b],
	'addi': lambda a, b, register: register[a] + b,
	'mulr': lambda a, b, register: register[a] * register[b],
	'muli': lambda a, b, register: register[a] * b,
	'banr': lambda a, b, register: register[a] & register[b],
	'bani': lambda a, b, register: register[a] & b,
	'borr': lambda a, b, register: register[a] | register[b],
	'bori': lambda a, b, register: register[a] | b,
	'setr': lambda a, b, register: register[a],
	'seti': lambda a, b, register: a,
	'gtir': lambda a, b, register: 1 if a > register[b] else 0,
	'gtri': lambda a, b, register: 1 if register[a] > b else 0,
	'gtrr': lambda a, b, register: 1 if register[a] > register[b] else 0,
	'eqir': lambda a, b, register: 1 if a == register[b] else 0,
	'eqri': lambda a, b, register: 1 if register[a] == b else 0,
	'eqrr': lambda a, b, register: 1 if register[a] == register[b] else 0
}

# Count how many behave like 3 or more opcode
count = 0
opcode = [set(funcs.keys()) for i in range(16)]

for sample in samples:
	for name, op in funcs.items():
		try:
			c = op(sample['args'][0], sample['args'][1], sample['before'])

			# Check the after registers
			if sample['after'][sample['output']] != c:
				continue
			for i in range(4):
				if (i != sample['output']) and (sample['before'][i] != sample['after'][i]):
					raise ValueError

			sample['behaves'].add(name)
		except IndexError:
			# Bad register reference - move on
			pass
		except ValueError:
			# After registers don't match - move on
			pass

	opcode[sample['opcode']] &= sample['behaves']
	if len(sample['behaves']) >= 3:
		count += 1

print("Samples with more than 3 opcodes: {} / {}".format(count, len(samples)))

# Figure out which opcode matches to which function
while any(len(codes) > 1 for codes in opcode):
	for i, codes in enumerate(opcode):
		if len(opcode[i]) == 1:
			for j, tcodes in enumerate(opcode):
				if j == i:
					continue
				opcode[j] -= opcode[i]
opcode = [list(codes)[0] for codes in opcode]

# Run the test program
register = [0, 0, 0, 0]
with open('test_program', 'r') as f:
	for line in f:
		op = [int(x) for x in line.split(' ')]
		register[op[3]] = funcs[opcode[op[0]]](op[1], op[2], register)
print(register)
