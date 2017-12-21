#!/usr/bin/python

import sys

class BufferEntry(object):
	def __init__(self, val, after=None):
		self.value = val

		if after is None:
			self.left = self
			self.right = self
		else:
			self.left = after
			self.right = after.right
			self.left.right = self
			self.right.left = self

	def display(self, highlight=None):
		stop_at = self.value
		if highlight and (highlight == self):
			sys.stdout.write("({0}) ".format(self.value))
		else:
			sys.stdout.write("{0} ".format(self.value))

		ptr = self.right
		while ptr.value != stop_at:
			if highlight and (highlight == ptr):
				sys.stdout.write("({0}) ".format(ptr.value))
			else:
				sys.stdout.write("{0} ".format(ptr.value))
			ptr = ptr.right
		print


# Input
steps = 348

# Test input
#steps = 3

zero_node = BufferEntry(0)

buf = zero_node
for i in range(1, 2018):
	for j in range(steps):
		buf = buf.right
	buf = BufferEntry(i, buf)

print("AFTER 2017: {0}".format(buf.right.value))

for i in range(2018, 50000001):
	for j in range(steps):
		buf = buf.right
	buf = BufferEntry(i, buf)

	if i % 1000000 == 0:
		sys.stdout.write('.')
		sys.stdout.flush()

print("\nAFTER 0: {0}".format(zero_node.right.value))
