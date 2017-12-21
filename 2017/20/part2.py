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

i = 0
particles = {}
with open("input", "r") as f:
	# p=<-1021,-2406,1428>, v=<11,24,-73>, a=<4,9,0>
	for line in f:
		m = particle_re.match(line)
		if not m:
			print("BAD: " + line)
			continue
		particles[i] = Particle((int(m.group(1)), int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5)), int(m.group(6))), (int(m.group(7)), int(m.group(8)), int(m.group(9))))
		i += 1

# Test input
test_particles = {
	0: Particle((3, 0, 0), (2, 0, 0), (-1, 0, 0)),
	1: Particle((4, 0, 0), (0, 0, 0), (-2, 0, 0))
}
#particles = test_particles

# Step through and check for collisions
for t in range(0, 10000):
	current_positions = {}

	for i in particles:
		pos = particles[i].position(t)
		if pos in current_positions:
			current_positions[pos].append(i)
		else:
			current_positions[pos] = [i]

	for pos in current_positions:
		if len(current_positions[pos]) > 1:
			for i in current_positions[pos]:
				del particles[i]

	if t % 1000 == 0:
		print("PARTICLES (t={0}): {1}".format(t, len(particles)))

print("PARTICLES (t=10000): {0}".format(len(particles)))
