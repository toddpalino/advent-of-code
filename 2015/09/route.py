#!/usr/bin/python

import itertools
import operator

locations = {}

class Location:
    def __init__(self, name):
        self.name = name
        self.distances = {}

with open('distances') as f:
    for line in f:
        parts = line.strip().split(' ')
        loc_1 = locations.get(parts[0], Location(parts[0]))
        locations[parts[0]] = loc_1
        loc_2 = locations.get(parts[2], Location(parts[2]))
        locations[parts[2]] = loc_2
        loc_1.distances[parts[2]] = int(parts[4])
        loc_2.distances[parts[0]] = int(parts[4])

paths = {}
for path in itertools.permutations(locations.keys()):
    start = path[0]
    distance = 0
    for location in path[1:]:
        distance += locations[start].distances[location]
        start = location
    paths[path] = distance

distances = sorted(paths.items(), key=operator.itemgetter(1))
print "{0} - {1}".format(distances[0][0], distances[0][1])
print "{0} - {1}".format(distances[-1][0], distances[-1][1])
