from heapq import heappush, heappop
from itertools import count

REMOVED = '<removed-task>'

class PriorityQueue:
	def __init__(self):
		self._pq = []
		self._entry_finder = {}
		self._counter = count()

	def add(self, item, priority=0):
		if item in self._entry_finder:
			self.remove(item)
		c = next(self._counter)
		entry = [priority, c, item]
		self._entry_finder[item] = entry
		heappush(self._pq, entry)

	def remove(self, item):
		entry = self._entry_finder.pop(item)
		entry[-1] = REMOVED

	def pop(self):
		while self._pq:
			priority, c, item = heappop(self._pq)
			if item is not REMOVED:
				del self._entry_finder[item]
				return (priority, item)
		raise KeyError("pop from an empty PriorityQueue")

	def __bool__(self):
		return bool(self._pq)
