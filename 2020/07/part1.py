#!/usr/bin/python3

from collections import deque

class Bag:
	def __init__(self, color):
		self.color = color
		self.contents = {}
		self.contained_by = set()

	def add_contents(self, num, bag):
		self.contents[bag.color] = (num, bag)
		bag.contained_by.add(self)

	def __repr__(self):
		return "(Bag: %s)" % (self.color)


colors = {}
#with open("test.txt") as f:
with open("input.txt") as f:
	for line in f:
		words = line.strip().split()

		color = ' '.join(words[0:2])
		if color not in colors:
			colors[color] = Bag(color)
		bag = colors[color]

		if words[4] == "no":
			continue
		contents = ' '.join(words[4:])[:-1].split(', ')
		for c in contents:
			parts = c.split()
			c_color = ' '.join(parts[1:3])
			if c_color not in colors:
				colors[c_color] = Bag(c_color)
			bag.add_contents(int(parts[0]), colors[c_color])

could_contain = set()
q = deque((colors['shiny gold'],))
while q:
	bag = q.popleft()
	for container in bag.contained_by:
		if container in could_contain:
			# Already seen this bag color
			continue
		q.append(container)
		could_contain.add(container)

print(len(could_contain))
