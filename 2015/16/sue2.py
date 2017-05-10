#!/usr/bin/python

sues = {}

class Sue:
    def __init__(self, num, attributes):
        self.num = num
        self.attributes = attributes

with open('attributes') as f:
    for line in f:
        sue, sep, attr_str = line.strip().partition(':')

        attributes = {}
        for attr in attr_str.split(','):
            k, sep, v = attr.strip().partition(': ')
            attributes[k] = int(v)
        sue_id = int(sue.split(' ')[1])
        sues[sue_id] = Sue(sue_id, attributes)

mfcsam = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

for attribute in mfcsam:
    for sue_id in sues.keys():
        if attribute in ['cats', 'trees']:
            if attribute in sues[sue_id].attributes and mfcsam[attribute] >= sues[sue_id].attributes[attribute]:
                del sues[sue_id]
        elif attribute in ['pomeranians', 'goldfish']:
            if attribute in sues[sue_id].attributes and mfcsam[attribute] <= sues[sue_id].attributes[attribute]:
                del sues[sue_id]
        else:
            if attribute in sues[sue_id].attributes and mfcsam[attribute] != sues[sue_id].attributes[attribute]:
                del sues[sue_id]

for sue_id in sues:
    print "Sue {0} - {1}".format(sue_id, sues[sue_id].attributes)
