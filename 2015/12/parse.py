#!/usr/bin/python

import collections
import json

def get_sum(data, skip_keys=[]):
    total = 0
    objs = [data]
    skip_set = set(skip_keys)
    while len(objs) > 0:
        obj = objs.pop()
        if isinstance(obj, basestring):
            continue

        if isinstance(obj, dict):
            if skip_set.isdisjoint([item for item in obj.keys() + obj.values() if isinstance(item, basestring)]):
                for k, v in obj.iteritems():
                    objs.append(k)
                    objs.append(v)
            continue

        try:
            for item in obj:
                objs.append(item)
        except TypeError:
            total += obj

    return total

fh = open('doc.json')
raw_data = json.load(fh)
fh.close()

print "TOTAL: {0}".format(get_sum(raw_data))
print "TOTAL: {0} (skip red)".format(get_sum(raw_data, skip_keys=['red']))
