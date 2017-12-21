#!/usr/bin/python

from __future__ import division
import re

def displacement(t, vi, vf):
	return ((vi + vf) / 2) * t

def velocity(t, vi, a):
	return vi + (a * t)

class Particle(object):
	def __init__(self, position, velocity, acceleration):
		self.initial_position = position
		self.initial_velocity = velocity
		self.acceleration = acceleration

	def velocity(self, t):
		x = velocity(t, self.initial_velocity[0], self.acceleration[0])
		y = velocity(t, self.initial_velocity[1], self.acceleration[1])
		z = velocity(t, self.initial_velocity[2], self.acceleration[2])
		return (x, y, z)

	def position(self, t):
		# We can't use acceleration directly, because we have to update velocity FIRST
		vf = self.velocity(t+1)

		x = self.initial_position[0] + displacement(t, self.initial_velocity[0], vf[0])
		y = self.initial_position[1] + displacement(t, self.initial_velocity[1], vf[1])
		z = self.initial_position[2] + displacement(t, self.initial_velocity[2], vf[2])
		return (int(x), int(y), int(z))

particle_re = re.compile('p=<([0-9-]+),([0-9-]+),([0-9-]+)>, v=<([0-9-]+),([0-9-]+),([0-9-]+)>, a=<([0-9-]+),([0-9-]+),([0-9-]+)>')

particles = []
with open("input", "r") as f:
	# p=<-1021,-2406,1428>, v=<11,24,-73>, a=<4,9,0>
	for line in f:
		m = particle_re.match(line)
		if not m:
			print("BAD: " + line)
			continue
		particles.append(Particle((int(m.group(1)), int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5)), int(m.group(6))), (int(m.group(7)), int(m.group(8)), int(m.group(9)))))

# Test input
test_particles = [
	Particle((3, 0, 0), (2, 0, 0), (-1, 0, 0)),
	Particle((4, 0, 0), (0, 0, 0), (-2, 0, 0))
]
#particles = test_particles

# Check at a bunch of points
for t in range(0, 1000000000, 100000000):
	min_distance = 0
	min_idx = None

	for i in range(len(particles)):
		pos = particles[i].position(t)
		distance = abs(pos[0]) + abs(pos[1]) + abs(pos[2])

		if min_idx is None or distance < min_distance:
			min_idx = i
			min_distance = distance

	print("CLOSEST (t={0}): {1} (d={2})".format(t, min_idx, min_distance))
