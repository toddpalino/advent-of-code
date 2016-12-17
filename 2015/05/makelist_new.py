#!/usr/bin/python

# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

import re

nice_re = re.compile(r'(?=.*([a-z][a-z]).*\1).*([a-z])[a-z]\2.*')
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
