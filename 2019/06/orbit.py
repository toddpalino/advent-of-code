from collections import deque
from priorityq import PriorityQueue


class Orbit:
	def __init__(self, name, orbits_around=None):
		self.name = name
		self.orbits_around = orbits_around
		if self.orbits_around is not None:
			self.orbits_around.add_orbiter(self)
		self.orbiters = []

	def add_orbiter(self, orbiter):
		self.orbiters.append(orbiter)
		orbiter.orbits_around = self

	def count_indirect_orbits(self):
		if self.orbits_around is None:
			return 0
		count = 0
		ptr = self.orbits_around
		while ptr.orbits_around is not None:
			ptr = ptr.orbits_around
			count += 1
		return count

	def count_direct_orbits(self):
		return 0 if self.orbits_around is None else 1

	def count_orbits(self):
		return self.count_indirect_orbits() + self.count_direct_orbits()

	def count_transfers(self, tgt):
		visited = set()
		pq = PriorityQueue()
		pq.add(self.orbits_around, 0)

		while pq:
			try:
				count, obj = pq.pop()
			except KeyError:
				# Empty queue
				break

			if obj == tgt:
				return count
			visited.add(obj)

			if obj.orbits_around is not None and obj.orbits_around not in visited:
				pq.add(obj.orbits_around, count + 1)
			for child  in obj.orbiters:
				if child not in visited:
					pq.add(child, count + 1)