#!/usr/bin/python

class Node(object):
	def __init__(self, pins, partsLeft, left=None, strength=0, length=0):
		self.pins = pins
		self.partsLeft = partsLeft
		self.left = left
		self.right = []
		self.strength = strength
		self.length = length

	def makeNext(self):
		self.right = []
		for part in self.partsLeft:
			if self.pins in part.ports:
				newPartsLeft = self.partsLeft[:]
				newPartsLeft.remove(part)
				self.right.append(Node(part.ports[1] if part.ports[0] == self.pins else part.ports[0], newPartsLeft, left=self, strength=self.strength+sum(part.ports), length=self.length+1))


class Part(object):
	def __init__(self, ports):
		self.used = False
		self.ports = [int(port) for port in ports]


parts = []
with open("input", "r") as f:
	for line in f:
		part = Part(line.strip().split('/'))
		parts.append(part)

# Test input
testParts = [
	Part(['0', '2']),
	Part(['2', '2']),
	Part(['2', '3']),
	Part(['3', '4']),
	Part(['3', '5']),
	Part(['0', '1']),
	Part(['10', '1']),
	Part(['9', '10'])
]
#parts = testParts

# Make all bridges
zero = Node(0, parts)
nextNode = [zero]
while len(nextNode) > 0:
	node = nextNode.pop()
	node.makeNext()
	nextNode.extend(node.right)

maxStrengthNode = None
maxLengthNode = None
maxLength = 0
nextNode = [zero]
while len(nextNode) > 0:
	node = nextNode.pop()
	if maxStrengthNode is None or node.strength > maxStrengthNode.strength:
		maxStrengthNode = node
	if maxLengthNode is None or node.length > maxLengthNode.length or (node.length == maxLengthNode.length and node.strength > maxLengthNode.strength):
		maxLengthNode = node
	nextNode.extend(node.right)

print("MAX STRENGTH: {}".format(maxStrengthNode.strength))
print("MAX LENGTH: {} (strength={})".format(maxLengthNode.length, maxLengthNode.strength))
