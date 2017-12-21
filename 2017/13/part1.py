#!/usr/bin/python

class Layer(object):
	def __init__(self, depth, range):
		self._depth = depth
		self._range = range

	def caught(self, t):
		return t % ((self._range - 1) * 2) == 0

	def severity(self):
		return self._depth * self._range


input = {}
with open("input", "r") as f:
	for line in f:
		parts = line.strip().split(': ')
		input[int(parts[0])] = int(parts[1])

# Test input
#input = {0: 3, 1: 2, 4: 4, 6: 4}

max_layer = max(input.keys()) + 1
layers = [None] * (max_layer)
for layer_num in input:
	layers[layer_num] = Layer(layer_num, input[layer_num])


def trip(delay=0):
	severity = 0
	caught = False
	for pos in range(max_layer):
		if layers[pos] is None:
			continue
		if layers[pos].caught(pos + delay):
			caught = True
			severity += layers[pos].severity()
	return (caught, severity)


caught, severity = trip()
print("SEVERITY: {0}".format(severity))

delay = 1
while True:
	caught, severity = trip(delay)
	if not caught:
		break
	delay += 1

print("DELAY: {0}".format(delay))
