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

	def num_bags(self):
		# Always start with this bag itself
		count = 1
		for color, t in self.contents.items():
			count += t[0] * t[1].num_bags()
		return count

	def __repr__(self):
		return "(Bag: %s)" % (self.color)


colors = {}
#with open("test2.txt") as f:
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

bag = colors['shiny gold']
print(bag.num_bags() - 1)
