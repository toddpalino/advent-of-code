def execute(mem):
	ip = 0
	while mem[ip] != 99:
		if mem[ip] == 1:
			mem[mem[ip+3]] = mem[mem[ip+1]] + mem[mem[ip+2]]
			ip += 4
		elif mem[ip] == 2:
			mem[mem[ip+3]] = mem[mem[ip+1]] * mem[mem[ip+2]]
			ip += 4
		else:
			raise ValueError("Unknown opcode at ip=%d: %d" % (ip, mem[ip]))
	return mem
