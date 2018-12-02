#!/usr/bin/python

import re

class Program(object):
	def __init__(self, name, weight, holding=[]):
		self.name = name
		self.weight = weight
		self._holding_raw = holding
		self.children = []
		self.children_weight = 0
		self.parent = None

	def find_holding(self, programs):
		self.children = []
		for program in self._holding_raw:
			child = programs[program]
			self.children.append(child)
			child.parent = self

	def total_weight(self):
		if self.children_weight == 0:
			for child in self.children:
				self.children_weight += child.total_weight()
		return self.children_weight + self.weight


# Read in input
programs = {}
program_re = re.compile('^([a-z]+)\s+\(([0-9]+)\)(\s+->\s+(.*))?\s*$')
with open("input", "r") as f:
	for line in f:
		m = program_re.match(line)
		if not m:
			print("ERR line does not match: {0}".format(line.strip()))
			continue
		if m.group(4) is None:
			programs[m.group(1)] = Program(m.group(1), int(m.group(2)))
		else:
			programs[m.group(1)] = Program(m.group(1), int(m.group(2)), m.group(4).split(', '))

# Test input
test_programs = {
	'pbga': Program('pbga', 66, []),
	'xhth': Program('xhth', 57, []),
	'ebii': Program('ebii', 61, []),
	'havc': Program('havc', 66, []),
	'ktlj': Program('ktlj', 57, []),
	'fwft': Program('fwft', 72, ['ktlj', 'cntj', 'xhth']),
	'qoyq': Program('qoyq', 66, []),
	'padx': Program('padx', 45, ['pbga', 'havc', 'qoyq']),
	'tknk': Program('tknk', 41, ['ugml', 'padx', 'fwft']),
	'jptl': Program('jptl', 61, []),
	'ugml': Program('ugml', 68, ['gyxo', 'ebii', 'jptl']),
	'gyxo': Program('gyxo', 61, []),
	'cntj': Program('cntj', 57, [])
}
#programs = test_programs

for program in programs:
	programs[program].find_holding(programs)

root = None
for program in programs:
	if programs[program].parent is None:
		root = programs[program]
		break
total_weight = root.total_weight()
print("ROOT: {0} ({1})".format(root.name, total_weight))

program = root
problem = None
while True:
	print(program.name)
	weights = [child.total_weight() for child in program.children]
	if len(weights) == 0:
		problem = program
		break

	max_weight = -1
	max_index = None
	children_equal = True
	for child_idx in range(len(weights)):
		if max_index is None:
			max_weight = weights[child_idx]
			max_index = child_idx
			continue
		if weights[child_idx] == max_weight:
			continue
		elif weights[child_idx] > max_weight:
			max_weight = weights[child_idx]
			max_index = child_idx
		children_equal = False

	if not children_equal:
		program = program.children[max_index]
	else:
		problem = program
		break

print("PROBLEM: {0} ({1})".format(problem.name, problem.weight))
print("DIFFERENCE: {0}".format([problem.total_weight() - child.total_weight() for child in problem.parent.children]))
