#!/usr/bin/python

class Program(object):
	def __init__(self, id_str, siblings=[]):
		self._id = int(id_str)
		self._siblings = [int(x) for x in siblings]
		self.siblings = {}

	def id(self):
		return self._id

	def connect(self, programs):
		self.siblings = {}
		for sibling in self._siblings:
			self.siblings[sibling] = programs[sibling]

	def group(self):
		seen = {self._id: True}
		stack = [self]
		while len(stack) > 0:
			ptr = stack.pop(0)
			for sibling_id in ptr.siblings:
				if sibling_id not in seen:
					seen[sibling_id] = True
					stack.append(ptr.siblings[sibling_id])
		return seen.keys()


programs = {}
with open("input", "r") as f:
	for line in f:
		parts = line.strip().split(' ', 2)
		programs[int(parts[0])] = Program(parts[0], parts[2].split(', '))

for program_id in programs:
	programs[program_id].connect(programs)

group_0 = programs[0].group()
print("GROUP 0: {0} members".format(len(group_0)))

groups = []
pids_left = programs.keys()
while len(pids_left) > 0:
	pid = pids_left.pop(0)
	group = programs[pid].group()
	print("GROUP {0}: {1} members".format(pid, len(group)))
	groups.append(pid)
	for member in group:
		try:
			pids_left.remove(member)
		except ValueError:
			pass

print("TOTAL GROUPS: {0}".format(len(groups)))
