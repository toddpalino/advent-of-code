#!/usr/bin/python

class Disc:
    def __init__(self, size, position):
        self.size = size
        self.start = position

    def position_at(self, time_unit):
        return (self.start + time_unit) % self.size

discs_sample = [
    Disc(5, 4),
    Disc(2, 1)
]
discs_step1 = [
    Disc(7, 0),
    Disc(13, 0),
    Disc(3, 2),
    Disc(5, 2),
    Disc(17, 0),
    Disc(19, 7),
]
discs_step2 = [
    Disc(7, 0),
    Disc(13, 0),
    Disc(3, 2),
    Disc(5, 2),
    Disc(17, 0),
    Disc(19, 7),
    Disc(11, 0),
]

def find_drop(discs):
    time_step = 0
    positions = None

    while True:
        positions = [disc.position_at(time_step + 1 + i) for i, disc in enumerate(discs)]
        if max(positions) == 0:
            break
        if time_step % 1000 == 0:
            print "TIME: {0} {1}".format(time_step, positions)
        time_step += 1
    print "TIME: {0} {1}".format(time_step, positions)

#find_drop(discs_sample)
#find_drop(discs_step1)
find_drop(discs_step2)
