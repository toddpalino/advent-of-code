from collections import defaultdict

NOT_STARTED = 0
PAUSED = 1
HALTED = 2
FAILED = 3

class Intcode:
	def __init__(self, program, inputs=None, pause_on_output=False):
		self._original_mem = program.copy()
		self._pause_on_output = pause_on_output
		self._inputs = [] if inputs is None else inputs

		self._mem = defaultdict(int)
		for i, value in enumerate(self._original_mem):
			self._mem[i] = value

		self._ip = 0
		self._relative_base = 0
		self._outputs = []
		self._state = NOT_STARTED

	def add_input(self, value):
		self._inputs.append(value)

	def get_output(self):
		rv = self._outputs
		self._outputs = []
		return rv

	def reset(self, inputs=None):
		self._mem = defaultdict(int)
		for i, value in enumerate(self._original_mem):
			self._mem[i] = value
		self._ip = 0
		self._relative_base = 0
		self._outputs = []
		self._inputs = [] if inputs is None else inputs
		self._state = NOT_STARTED

	def is_paused(self):
		return self._state == PAUSED

	def is_halted(self):
		return self._state == HALTED

	def _read_opcode(self):
		opcode = self._mem[self._ip]
		self._ip += 1
		if opcode < 100:
			return opcode, []

		# Opcode contains parameter modes
		opcode_str = str(opcode)
		return int(opcode_str[-2:]), list(opcode_str[:-2])

	def _read_parameters(self, num, parameter_modes):
		params = []
		for i in range(num):
			value = self._mem[self._ip]
			self._ip += 1

			mode = parameter_modes.pop() if len(parameter_modes) >= 1 else '0'
			if mode == '0':
				params.append(self._mem[value])
			elif mode == '1':
				params.append(value)
			elif mode == '2':
				params.append(self._mem[value + self._relative_base])
			else:
				raise ValueError(f"Invalid mode for parameter {i} - {mode}")
		return tuple(params) if len(params) > 1 else params[0]

	# Parameters that we write to have a slightly different definition of "position mode".
	# We actually need to return it here like an immediate parameter - i.e. just the value -
	# because we will write to that POSITION
	def _get_write_parameter(self, parameter_modes):
		value = self._mem[self._ip]
		self._ip += 1

		mode = parameter_modes.pop() if len(parameter_modes) >= 1 else '0'
		if mode == '0':
			return value
		elif mode == '2':
			return value + self._relative_base
		else:
			raise ValueError(f"Invalid mode for parameter {i} - {mode}")

	def run(self):
		while self._mem[self._ip] != 99:
			opcode, parameter_modes = self._read_opcode()

			if opcode == 1:
				# Add
				p1, p2 = self._read_parameters(2, parameter_modes)
				p3 = self._get_write_parameter(parameter_modes)
				self._mem[p3] = p1 + p2
			elif opcode == 2:
				# Multiply
				p1, p2 = self._read_parameters(2, parameter_modes)
				p3 = self._get_write_parameter(parameter_modes)
				self._mem[p3] = p1 * p2
			elif opcode == 3:
				# Input
				p1 = self._get_write_parameter(parameter_modes)
				self._mem[p1] = self._inputs.pop(0)
			elif opcode == 4:
				# Output
				p1 = self._read_parameters(1, parameter_modes)
				self._outputs.append(p1)
				if self._pause_on_output:
					self._state = PAUSED
					return
			elif opcode == 5:
				# Jump if true
				p1, p2 = self._read_parameters(2, parameter_modes)
				if p1 != 0:
					self._ip = p2
			elif opcode == 6:
				# Jump if false
				p1, p2 = self._read_parameters(2, parameter_modes)
				if p1 == 0:
					self._ip = p2
			elif opcode == 7:
				# Less than
				p1, p2 = self._read_parameters(2, parameter_modes)
				p3 = self._get_write_parameter(parameter_modes)
				self._mem[p3] = 1 if p1 < p2 else 0
			elif opcode == 8:
				# Equals
				p1, p2 = self._read_parameters(2, parameter_modes)
				p3 = self._get_write_parameter(parameter_modes)
				self._mem[p3] = 1 if p1 == p2 else 0
			elif opcode == 9:
				# Set Relative Base
				p1 = self._read_parameters(1, parameter_modes)
				self._relative_base += p1
			else:
				self._state = FAILED
				raise ValueError("Unknown opcode at ip=%d: %d" % (self._ip, opcode))
		self._state = HALTED