#!/usr/bin/python3

# Just putting both parts in the same script, because it's trivial
import time

#fn = "test.txt"
fn = "input.txt"

def run(instructions, registers):
	last_instruction = len(instructions) - 1
	ptr = 0
	while ptr <= last_instruction:
		instruction = instructions[ptr]
		op = instruction[0]
		register = instruction[1]
		offset = instruction[2]

		if op == 'hlf':
			registers[register] = registers[register] // 2
		elif op == 'tpl':
			registers[register] = registers[register] * 3
		elif op == 'inc':
			registers[register] = registers[register] + 1
		elif op == 'jmp':
			# Jumps go to the offset before the target, because we're going to increment ptr
			ptr += offset - 1
		elif op == 'jie':
			if registers[register] % 2 == 0:
				ptr += offset - 1
		elif op == 'jio':
			if registers[register] == 1:
				ptr += offset - 1

		ptr += 1

	return registers


instructions = []
with open(fn, 'r') as f:
	for line in f:
		op = line[0:3]
		register = None if op == 'jmp' else line[4]
		register = None
		offset = None
		if op == 'jmp':
			register = None
			offset = int(line[4:])
		else:
			register = line[4]
			offset = int(line[7:]) if len(line) > 7 else None
		instructions.append((op, register, offset))

start_time = time.time()

registers = run(instructions, {'a': 0, 'b': 0})
print("Part 1 Registers: %s" % (registers))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))

print("")

start_time = time.time()

registers = run(instructions, {'a': 1, 'b': 0})
print("Part 2 Registers: %s" % (registers))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
