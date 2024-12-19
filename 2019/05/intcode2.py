def get_parameter(mem, loc, param_num, modes):
	value = mem[loc]
	mode = modes[param_num-1] if len(modes) >= param_num else '0'
	if mode == '0':
		return mem[value]
	elif mode == '1':
		return value
	else:
		raise ValueError(f"Invalid mode for parameter {param_num} - {mode}")

def execute(mem, inputs=[]):
	outputs = []

	ip = 0
	while mem[ip] != 99:
		# Defaults for opcode and parameter modes (0 - position)
		opcode = mem[ip]
		pmode = []

		if opcode > 100:
			# Opcode contains parameter modes
			opcode_str = str(mem[ip])
			opcode = int(opcode_str[-2:])
			pmode = opcode_str[:-2][::-1]

		if opcode == 1:
			# Add
			p1 = get_parameter(mem, ip + 1, 1, pmode)
			p2 = get_parameter(mem, ip + 2, 2, pmode)
			p3 = mem[ip+3]
			mem[p3] = p1 + p2
			ip += 4
		elif opcode == 2:
			# Multiply
			p1 = get_parameter(mem, ip + 1, 1, pmode)
			p2 = get_parameter(mem, ip + 2, 2, pmode)
			p3 = mem[ip+3]
			mem[p3] = p1 * p2
			ip += 4
		elif opcode == 3:
			# Input
			p1 = mem[ip+1]
			mem[p1] = inputs.pop()
			ip += 2
		elif opcode == 4:
			# Output
			p1 = get_parameter(mem, ip + 1, 1, pmode)
			outputs.append(p1)
			ip += 2
		elif opcode == 5:
			# Jump if true
			p1 = get_parameter(mem, ip + 1, 1, pmode)
			p2 = get_parameter(mem, ip + 2, 2, pmode)
			if p1 != 0:
				ip = p2
			else:
				ip += 3
		elif opcode == 6:
			# Jump if false
			p1 = get_parameter(mem, ip + 1, 1, pmode)
			p2 = get_parameter(mem, ip + 2, 2, pmode)
			if p1 == 0:
				ip = p2
			else:
				ip += 3
		elif opcode == 7:
			# Less than
			p1 = get_parameter(mem, ip + 1, 1, pmode)
			p2 = get_parameter(mem, ip + 2, 2, pmode)
			p3 = mem[ip+3]
			mem[p3] = 1 if p1 < p2 else 0
			ip += 4
		elif opcode == 8:
			# Equals
			p1 = get_parameter(mem, ip + 1, 1, pmode)
			p2 = get_parameter(mem, ip + 2, 2, pmode)
			p3 = mem[ip+3]
			mem[p3] = 1 if p1 == p2 else 0
			ip += 4
		else:
			raise ValueError("Unknown opcode at ip=%d: %d" % (ip, mem[ip]))
	return outputs
