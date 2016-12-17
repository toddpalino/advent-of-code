#!/usr/bin/python

import re

nice_re = re.compile(r'(?!.*(ab|cd|pq|xy).*)(?=.*[aeiou].*[aeiou].*[aeiou].*).*([a-z])\2.*')
naughty_strings = []
nice_strings = []

with open('strings') as f:
    for line in f:
        if nice_re.match(line):
            nice_strings.append(line.strip())
        else:
            naughty_strings.append(line.strip())
        
print "NICE: {0}".format(len(nice_strings))
print "NAUGHTY: {0}".format(len(naughty_strings))
