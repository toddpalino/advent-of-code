#!/usr/bin/python

import re
import sys

def list_aba(str):
    possibles = set()
    for i in range(len(str)):
        substr = str[i:i+3]
        if len(substr) < 3:
            break
        if (substr[0] == substr[2]) and (substr[0] != substr[1]):
            possibles.add(substr)
    return possibles

substr_re = re.compile("[a-z]+")

ssl_support = []
for ln in sys.stdin.readlines():
    aba_set = set()
    bab_set = set()
    for i, sub_ip in enumerate(substr_re.findall(ln)):
        if i % 2 == 0:
            aba_set |= list_aba(sub_ip)
        else:
            bab_set |= list_aba(sub_ip)

    for aba in aba_set:
        bab = aba[1] + aba[0] + aba[1]
        if bab in bab_set:
            ssl_support.append(ln.strip())
            break

print "---"
print "\n".join(ssl_support)
print len(ssl_support)
