#!/usr/bin/env python3

import time
from functools import reduce
from math import sqrt

#fn = "test.txt"
fn = "input.txt"

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

def factors(n):
	step = 2 if n%2 else 1
	return set(reduce(list.__add__,
	           ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

def execute_program(instructions, register):
	ip = 0
	while 0 <= ip < len_instructions:
		op, a, b, output = instructions[ip]

		# Write the current IP to the IP register
		if ip_register is not None:
			register[ip_register] = ip

		# There is a loop that starts if we reach IP=18 which will increment register 5 until 256
		# that number is greater than register 2
		# Shortcut it by setting the registers as they will be when it finishes
		if ip == 18:
			register[1] = register[2] // 256
			register[5] = (register[1] + 1) * 256
			register[4] = 19
			print("Reached ip=18, loop skipped => %s" % (register))
			ip = 20
			continue

		# IP=28 is the halt decision. We halt if register 3 equals register 0
		# If we reach IP=28, print out a message about what number would cause us to exit and then break
		if ip == 28:
			print("Reached ip=28, r0=%d required to exit" % (register[3]))
			break

		# Execute the instruction
		register[output] = funcs[op](a, b, register)

		# Read the IP back from the IP register
		if ip_register is not None:
			ip = register[ip_register]

		# Increment the IP
		ip += 1


	return register

def print_registers(register):
	print("Registers: %s" % (' '.join(f"{k}={register[k]}" for k in range(6))))


start_time = time.time()

ip_register = None
instructions = []

with open(fn, 'r') as f:
	for line in f:
		if line.startswith('#ip'):
			ip_register = int(line[4:])
			continue
		op = line[0:4]
		args = line[5:].strip().split()
		instructions.append((op, int(args[0]), int(args[1]), int(args[2])))
len_instructions = len(instructions)

register = [0, 0, 0, 0, 0, 0]
register = execute_program(instructions, register)

print_registers(register)

print("Elapsed time: %f" % (time.time() - start_time))

