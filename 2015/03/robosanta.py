#!/usr/bin/python

houses = {}

fh = open('instructions')
steps = list(fh.read().strip())
fh.close()

santa = [[0, 0], [0, 0]]
houses[(santa[0][0], santa[0][1])] = houses.get((santa[0][0], santa[0][1]), 0) + 1

for step, move in enumerate(steps):
    idx = step % 2
    if move == '^':
        santa[idx][1] += 1
    elif move == 'v':
        santa[idx][1] -= 1
    elif move == '<':
        santa[idx][0] -= 1
    elif move == '>':
        santa[idx][0] += 1

    houses[(santa[idx][0], santa[idx][1])] = houses.get((santa[idx][0], santa[idx][1]), 0) + 1

multiple = 0
for presents in houses:
    if presents > 1:
        multiple += 1

print "MULTIPLE: {0}".format(multiple)
