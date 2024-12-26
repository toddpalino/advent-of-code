import operator
from functools import total_ordering


@total_ordering
class Wire:
	def __init__(self, name, wire_value=None):
		self.name = name
		if wire_value is not None:
			self.set_letter = name[0]
			self.bit_position = int(name[1:])
		else:
			self.set_letter = None
			self.bit_position = int(name[1:]) if name[0] == 'z' else None
		self.wire_value = wire_value
		self.value_from = None
		self._calculated_value = None
		self._calculated_value = wire_value if wire_value is not None else None
		self._component_wires = [self]
		self._swapped_with = None

	def get_value(self):
		if self.wire_value is None and self._calculated_value is None:
			self._calculated_value, upstream_wires = self.value_from.get_gate_value()
			self._component_wires.extend(upstream_wires)
		return self._calculated_value

	def get_value_with_gates(self):
		if self.wire_value is None and self._calculated_value is None:
			self._calculated_value, upstream_wires = self.value_from.get_gate_value()
			self._component_wires.extend(upstream_wires)
		return self._calculated_value, self._component_wires

	# Filter output wires from the list of component names
	def get_output_wire_names(self):
		if self.wire_value is None and self._calculated_value is None:
			self.get_value()
		return set(wire.name for wire in self._component_wires if wire.wire_value is None)

	# Filter only the wires that have initial values from the list of component names
	def get_source_wire_names(self):
		if self.wire_value is None and self._calculated_value is None:
			self.get_value()
		return set(wire.name for wire in self._component_wires if wire.wire_value is not None)

	def uses_component(self, other):
		if self.wire_value is None and self._calculated_value is None:
			self.get_value()
		return other in self._component_wires

	def swap_with(self, other):
		if self._swapped_with is not None:
			raise Exception('Cannot swap output that is already swapped')
		self._swapped_with = other
		other._swapped_with = self
		self.value_from, other.value_from = other.value_from, self.value_from

	def unswap(self):
		if self._swapped_with is None:
			raise Exception('Cannot unswap without a swap with')
		self.value_from, self._swapped_with.value_from = self._swapped_with.value_from, self.value_from
		self._swapped_with._swapped_with = None
		self._swapped_with = None

	def is_swapped(self):
		return self._swapped_with is not None

	def clear(self):
		self._calculated_value = self.wire_value if self.wire_value is not None else None
		self._component_wires = [self]

	def __eq__(self, other):
		return self.name == other.name

	def __lt__(self, other):
		return self.name < other.name


class Gate:
	def __init__(self, input1, input2, output, op):
		self.w1 = input1
		self.w2 = input2
		self.output = output
		output.value_from = self
		self.op_name = op
		self.op = operator.and_ if op == 'AND' else (operator.or_ if op == 'OR' else operator.xor)
		self._calculated_value = None
		self._component_wires = None

	def get_gate_value(self):
		if self._calculated_value is None:
			w1_value, w1_wires = self.w1.get_value_with_gates()
			w2_value, w2_wires = self.w2.get_value_with_gates()
			self._calculated_value = self.op(w1_value, w2_value)
			self._component_wires = w1_wires + w2_wires
		return self._calculated_value, self._component_wires

	def clear(self):
		self._calculated_value = None
		self._component_wires = None


def read_input(filename):
	wires = {}
	gates = []
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip()
			if ':' in line:
				# Wire
				name, val = line.split(': ')
				wires[name] = Wire(name, wire_value=val=='1')
			elif '->' in line:
				# Gate
				w1, op, w2, _, w3 = line.split(' ')
				if w1 not in wires:
					wires[w1] = Wire(w1)
				if w2 not in wires:
					wires[w2] = Wire(w2)
				if w3 not in wires:
					wires[w3] = Wire(w3)
				gates.append(Gate(wires[w1], wires[w2], wires[w3], op))
	return wires, gates

def get_wire_set(wires, letter):
	wire_set = [wire for name, wire in wires.items() if name[0] == letter]
	wire_set.sort(reverse=True)
	return wire_set

# Note - this assumes that the list of names provided is in reverse order (MSB first)
def get_wire_set_value(wires):
	val = 0
	for w in wires:
		val = (val << 1) | w.get_value()
	return val

def set_wire_set_value(wires, val):
	s = bin(val)[2:][::-1]
	len_s = len(s)
	if len_s > len(wires):
		raise Exception('Number too large for wire set')

	# Clear (False) or set True) the wire values
	for wire in wires:
		if wire.bit_position < len_s:
			wire.wire_value = s[wire.bit_position] == '1'
		else:
			wire.wire_value = False

def clear(wires, gates):
	for wire in wires.values():
		wire.clear()
	for gate in gates:
		gate.clear()

def get_bad_bit(wires, gates, wire_sets, lsb, msb):
	bad_bit = None
	good_wires = set()
	for i in range(lsb, msb):
		# We need to test 7 cases per bit: 0+0, and then 0+1, 1+0, and 1+1 with and without carry from the last bit
		for j, t in enumerate(((0, 0), (0, 2**i), (2**i, 0), (2**i, 2**i), (2**(i-1), 2**i + 2**(i-1)),
		                       (2**i + 2**(i-1), 2**(i-1)), (2**i + 2**(i-1), 2**i + 2**(i-1)))):
			if i == 0 and j >= 3:
				break
			set_wire_set_value(wire_sets['x'], t[0])
			set_wire_set_value(wire_sets['y'], t[1])
			expected = sum(t)
			clear(wires, gates)
			z = get_wire_set_value(wire_sets['z'])
			if expected != z:
				return bin(expected ^ z)[2:][::-1].index('1'), good_wires

		# We're good up to this point, so save all the wires we used earlier
		good_wires |= wires["z{:02}".format(i)].get_output_wire_names()
	return bad_bit, good_wires

# There are some rules for a z wire (output) in an adder:
#   It can never connect to an AND gate
#   It can only connect to an OR gate if it is the MSB (45)
#   It can only connect to a gate that directly uses x/y if it is bit 0
def is_valid_z_wire(wire, max_bit_position):
	if wire.value_from.op_name == 'AND':
		return False
	if wire.value_from.op_name == 'OR':
		return wire.bit_position == max_bit_position
	if wire.value_from.w1.name[0] in ('x', 'y'):
		return wire.bit_position == 0
	return True

def find_bad_gates(wires, gates, wire_sets, all_wire_names, good_wires=None, last_bad_bit=-1):
	new_good_wires = good_wires.copy() if good_wires is not None else set()

	# Find the least significant bad bit
	bad_bit, add_good_wires = get_bad_bit(wires, gates, wire_sets, last_bad_bit + 1, len(wire_sets['x']))
	if bad_bit is None:
		# No bad bits. Looks like we're done!
		return True
	if sum(1 for wire in wires.values() if wire.is_swapped()) >= 8:
		# We can't have more than 4 pairs of swapped outputs
		return False
	new_good_wires |= add_good_wires

	# Get the z wire for the bad bit
	z_wire = wires["z{:02d}".format(bad_bit)]
	bad_z_bit = z_wire.get_value()

	# Check if the z wire follows the rules first. If not, we know that's the wire that needs to be swapped
	possible_w1 = []
	if not is_valid_z_wire(z_wire, len(wire_sets['z']) - 1):
		possible_w1.append(z_wire)
	else:
		# The swap is an internal wire. We only have one of these, so we're just going to test everything
		for n1 in z_wire.get_output_wire_names():
			w1 = wires[n1]
			if n1 in new_good_wires or w1.is_swapped():
				continue
			possible_w1.append(w1)

	# Now get the possible things to swap with. Don't touch any of the gates involved in bits prior to the bad one
	test_swaps = set()
	for w1 in possible_w1:
		for n2 in all_wire_names:
			w2 = wires[n2]
			if w1 == w2 or n2 in new_good_wires or w2.is_swapped():
				continue
			if w1.name[0] == 'z' and not is_valid_z_wire(w2, len(wire_sets['z']) - 1):
				continue
			if w2.name[0] == 'z' and not is_valid_z_wire(w1, len(wire_sets['z']) - 1):
				continue
			if max(wires[n].bit_position for n in w2.get_source_wire_names()) > bad_bit:
				# We don't want to swap if it would cause us to use a more significant source bit
				continue
			if w2.uses_component(w1) or w1.uses_component(w2):
				# We can't create a feedback loop
				continue
			test_swaps.add((w1.name, w2.name))

	# Save the state of x/y that we are testing under, because it could change when we recurse
	x = get_wire_set_value(wire_sets['x'])
	y = get_wire_set_value(wire_sets['y'])

	for w1_name, w2_name in test_swaps:
		w1, w2 = wires[w1_name], wires[w2_name]

		# Swap the two outputs and assure x/y are our test values (state can change after the first time through)
		w1.swap_with(w2)
		set_wire_set_value(wire_sets['x'], x)
		set_wire_set_value(wire_sets['y'], y)
		clear(wires, gates)

		if bad_z_bit != z_wire.get_value():
			if find_bad_gates(wires, gates, wire_sets, all_wire_names, good_wires=new_good_wires, last_bad_bit=bad_bit):
				return True

		# Un-swap the pair we just tested
		w1.unswap()
		clear(wires, gates)

	return False
