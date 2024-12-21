import numpy as np
from itertools import product
from math import gcd

def reduce_vector(x, y):
	d = gcd(x, y)
	return x // d, y // d

# Convert an x, y vector into a 0-360 degree angle
def convert_vector(x, y):
	return np.mod(np.degrees(np.arctan2(y, x)) + 90, 360)

class Monitoring:
	def __init__(self, filename):
		self._asteroids = {}
		with open(filename, 'r') as f:
			for y, line in enumerate(f):
				for x, c in enumerate(line.strip()):
					if c == '#':
						self._asteroids[(x, y)] = {}
		self._len_x = x + 1
		self._len_y = y + 1
		self._best_location = None
		self._best_count = 0
		self._destruction_order = []

	def get_asteroids(self, location):
		lx, ly = location

		# Build a list of vectors for lines from our location. The 0s are a special case where we will add them separate
		vectors = {reduce_vector(x, y): [] for x, y in product(range(-lx, self._len_x-lx),
		                                                       range(-ly, self._len_y-ly)) if x != 0 or y != 0}
		vectors[(0, 1)] = []
		vectors[(0, -1)] = []
		vectors[(1, 0)] = []
		vectors[(-1, 0)] = []

		# Walk out each vector collecting asteroids until we go off grid
		for vector in vectors.keys():
			i = 1
			while True:
				nx, ny = lx + (i * vector[0]), ly + (i * vector[1])
				if (nx, ny) in self._asteroids:
					vectors[vector].append((nx, ny))
				if not (0 <= nx < self._len_x and 0 <= ny < self._len_y):
					break
				i += 1
		self._asteroids[location] = vectors

	def count_visible_asteroids(self, location):
		if len(self._asteroids[location]) == 0:
			self.get_asteroids(location)
		return sum(1 for asteroid_list in self._asteroids[location].values() if len(asteroid_list) > 0)

	def find_best_location(self):
		if self._best_location is None:
			self._best_count = 0
			for asteroid in self._asteroids:
				count = self.count_visible_asteroids(asteroid)
				if count > self._best_count:
					self._best_count = count
					self._best_location = asteroid
		return self._best_location, self._best_count

	def destroy_asteroids(self):
		if self._best_location is None:
			self.find_best_location()

		# Sort the vectors as angles. This gives us a clockwise rotation starting at 0 (up)
		vector_order = sorted(self._asteroids[self._best_location].keys(), key=lambda k: convert_vector(*k))
		vectors = self._asteroids[self._best_location]

		while True:
			for vector in vector_order:
				if len(self._destruction_order) == len(self._asteroids) - 1:
					# No more asteroids
					return
				if len(vectors[vector]) > 0:
					asteroid = vectors[vector].pop(0)
					self._destruction_order.append(asteroid)

	def get_destroyed_asteroid(self, num):
		if len(self._destruction_order) == 0:
			self.destroy_asteroids()
		return self._destruction_order[num-1]