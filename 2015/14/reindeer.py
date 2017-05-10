#!/usr/bin/python

import operator

reindeer = []

class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.last_distance = 0

    def fly(self, seconds):
        block_time = self.fly_time + self.rest_time
        blocks = seconds / block_time
        remainder = min(self.fly_time, seconds % block_time)
        self.last_distance = (blocks * self.speed * self.fly_time) + (self.speed * remainder)

def winner_at_time(reindeer, t):
    for r in reindeer:
        r.fly(t)
    results = sorted(reindeer, key=lambda r: r.last_distance, reverse = True)
    return results[0]

total_time = int(raw_input("Length of race: "))

with open('reindeer') as f:
    for line in f:
        parts = line.strip().split(' ')
        reindeer.append(Reindeer(parts[0], int(parts[3]), int(parts[6]), int(parts[13])))

winner = winner_at_time(reindeer, total_time)
print "WINNER: {0} ({1})".format(winner.name, winner.last_distance)

points = {r.name: 0 for r in reindeer}
for t in range(1, total_time+1):
    intermediate = winner_at_time(reindeer, t)
    points[intermediate.name] = points[intermediate.name] + 1

results = sorted(points.items(), key=operator.itemgetter(1), reverse=True)
print "POINTS WINNER: {0} ({1})".format(results[0][0], results[0][1])
