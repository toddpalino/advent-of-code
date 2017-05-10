#!/usr/bin/python

import itertools

capacities = []
with open('capacities') as f:
    for line in f:
        capacities.append(int(line.strip()))

capacities.sort(reverse=True)
print "TOTAL CONTAINERS: {0}".format(len(capacities))

total_combinations = 0
for i in range(len(capacities)):
    combinations = 0
    for combo in itertools.combinations(capacities, i+1):
        if sum(combo, 0) == 150:
            combinations += 1

    print "COMBINATIONS ({0}): {1}".format(i, combinations)
    total_combinations += combinations

print "TOTAL COMBINATIONS: {0}".format(total_combinations)
