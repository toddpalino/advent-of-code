def combo_operand(x, regs):
	if x <= 3:
		return x
	if x == 4:
		return regs['a']
	if x == 5:
		return regs['b']
	if x == 6:
		return regs['c']
	if x == 7:
		raise ValueError("combo operand 7 is not valid")

def run_program(program, registers):
	len_program = len(program)
	output = []
	ip = 0

	while ip < len_program:
		opcode = program[ip]
		operand = program[ip+1]
		if opcode == 0:
			registers['a'] = registers['a'] // (2**combo_operand(operand, registers))
		if opcode == 1:
			registers['b'] = registers['b'] ^ operand
		if opcode == 2:
			registers['b'] = combo_operand(operand, registers) % 8
		if opcode == 3:
			if registers['a'] != 0:
				ip = operand
				continue
		if opcode == 4:
			registers['b'] = registers['b'] ^ registers['c']
		if opcode == 5:
			output.append(combo_operand(operand, registers) % 8)
		if opcode == 6:
			registers['b'] = registers['a'] // (2 ** combo_operand(operand, registers))
		if opcode == 7:
			registers['c'] = registers['a'] // (2 ** combo_operand(operand, registers))

		ip += 2
	return output
