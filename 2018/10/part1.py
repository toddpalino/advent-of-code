#!/usr/bin/env python3

import curses
import re
import time

class Particle:
	def __init__(self, x, y, vx, vy):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy

		self.last_x = x
		self.last_y = y

	def move(self, steps=1):
		self.last_x = self.x
		self.last_y = self.y
		self.x += self.vx * steps
		self.y += self.vy * steps


def spread(particles):
	min_x = min(p.x for p in particles)
	min_y = min(p.y for p in particles)
	max_x = max(p.x for p in particles)
	max_y = max(p.y for p in particles)
	return (max_x - min_x, max_y - min_y)


# position=< 52099, -30992> velocity=<-5,  3>
particle_re = re.compile('^.*<\s*([-\d]+),\s*([-\d]+)>.*<\s*([-\d]+),\s*([-\d]+)>\s*$')

particles = []
with open('input', 'r') as f:
	for line in f:
		m = particle_re.match(line)
		if m:
			particles.append(Particle(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))))

canvas = spread(particles)
last_canvas = (canvas[0] + 1, canvas[1] + 1)
t = 0

# Advance until the points are as close to each other as possible
while canvas[0] < last_canvas[0] and canvas[1] < last_canvas[1]:
	for particle in particles:
		particle.move()
	t += 1

	last_canvas = canvas
	canvas = spread(particles)

# The canvas at t-1 (last_* values) is what we want

# Use the minimum x and y values as offsets to paint the screen
offset_x = -min(p.last_x for p in particles)
offset_y = -min(p.last_y for p in particles)

scr = curses.initscr()
scr.clear()

for x in range(last_canvas[0]):
	for y in range(last_canvas[1]):
		scr.addstr(y, x, '.')

for particle in particles:
	scr.addstr(particle.last_y + offset_y, particle.last_x + offset_x, '#')

scr.addstr(last_canvas[1] + 2, 0, "Time: {}".format(t-1))
scr.refresh()

scr.getkey()
curses.endwin()

