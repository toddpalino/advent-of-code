#!/usr/bin/python

houses = {}

fh = open('instructions')
steps = list(fh.read().strip())
fh.close()

x = 0
y = 0
houses[(x, y)] = houses.get((x, y), 0) + 1
for step, move in enumerate(steps):
    if move == '^':
        y += 1
    elif move == 'v':
        y -= 1
    elif move == '<':
        x -= 1
    elif move == '>':
        x += 1
    houses[(x, y)] = houses.get((x, y), 0) + 1

multiple = 0
for presents in houses:
    if presents > 1:
        multiple += 1

print "MULTIPLE: {0}".format(multiple)
