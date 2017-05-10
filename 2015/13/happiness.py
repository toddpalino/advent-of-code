#!/usr/bin/python

import itertools
import operator

people = {}

class Person:
    def __init__(self, name):
        self.name = name
        self.deltas = {}

def get_arrangements():
    arrangements = {}
    for arrangement in itertools.permutations(people.keys()):
        diff = [0 for i in range(len(people))]
        c = len(arrangement)
        for i, person in enumerate(arrangement):
            diff[i] = people[person].deltas[arrangement[(i+1) % c]] + people[person].deltas[arrangement[(i-1) % c]]
        arrangements[arrangement] = sum(diff, 0)

    return arrangements

with open('deltas') as f:
    for line in f:
        parts = line.strip().split(' ')

        person = people.get(parts[0], Person(parts[0]))
        people[parts[0]] = person

        neighbor_name = parts[10][:-1]
        neighbor = people.get(neighbor_name, Person(neighbor_name))
        people[neighbor_name] = neighbor

        person.deltas[neighbor_name] = int(parts[3]) if parts[2] == 'gain' else -int(parts[3])

arrangements = get_arrangements()
arrangements = sorted(arrangements.items(), key=operator.itemgetter(1))
print "{0} - {1}".format(arrangements[0][0], arrangements[0][1])
print "{0} - {1}".format(arrangements[-1][0], arrangements[-1][1])

print "---"

me = Person('Todd')
for person in people:
    people[person].deltas['Todd'] = 0
    me.deltas[person] = 0
people['Todd'] = me

arrangements = get_arrangements()
arrangements = sorted(arrangements.items(), key=operator.itemgetter(1))
print "{0} - {1}".format(arrangements[0][0], arrangements[0][1])
print "{0} - {1}".format(arrangements[-1][0], arrangements[-1][1])
