# This is a generic implementation of Dijkstra's shortest path algorithm. It provides for both scoring and
# path determination, and lets me plug in logic for determining what directions are available. We're going
# to start basic and add functionality later as we need it

from itertools import product
from aoc.utils.priorityq import PriorityQueue

# This is a common helper function to find locations on a grid. By default, it will replace
# the location, once found, with a '.'. replace can be set to None for no replacement, or
# any other character needed
def find_location(grid, letter, replace='.'):
	for x, y in product(range(len(grid[0])), range(len(grid))):
		if grid[y][x] == letter:
			if replace is not None:
				grid[y][x] = replace
			return x, y

# Most of the time, our grids have '.' as a valid path and '#' as a wall. This provides an iterator
# that will yield those choices along with the score to add for moving to each one
def _choices_at(grid, item, letter='.'):
	x, y = item
	for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
		if not ((0 <= nx < len(grid[0])) and (0 <= ny < len(grid))):
			continue
		if grid[ny][nx] != '.':
			continue
		yield (nx, ny), 1

class PathFinder:
	def __init__(self, grid, start, func_choices_at=None):
		self._grid = grid
		self._start = start
		self.scores = {self._start: 0}
		self._prev = {}
		self._run_complete = False

		# Pluggable methods
		self._choices_at = func_choices_at if func_choices_at is not None else _choices_at

	def run(self):
		visited = set()
		queue = PriorityQueue()
		queue.add(self._start, 0)
		while queue:
			try:
				score, item = queue.pop()
			except KeyError:
				# Empty queue
				break
			visited.add(item)

			# Find blocks we can move to
			for next_item, next_score in self._choices_at(grid=self._grid, item=item):
				if next_item in visited:
					continue

				next_score += score
				if next_item not in self.scores or next_score < self.scores[next_item]:
					self.scores[next_item] = next_score
					self._prev[next_item] = item
				queue.add(next_item, next_score)
		self._run_complete = True

	def get_score(self, end):
		if not self._run_complete:
			self.run()
		return self.scores[end] if end in self.scores else None

	def get_path(self, end):
		if not self._run_complete:
			self.run()
		if end not in self._prev:
			return None
		path = [end]
		loc = end
		while loc != self._start:
			loc = self._prev[loc]
			path.append(loc)
		return path[::-1]

	def print(self, with_path_to=None):
		path = self.get_path(end=with_path_to) if with_path_to is not None else None
		for y, row in enumerate(self._grid):
			for x, c in enumerate(row):
				if (x, y) == self._start:
					c = 'S'
				elif path is not None and (x, y) in path:
					c = 'E' if (x, y) == with_path_to else 'O'
				print(c, end='')
			print()
