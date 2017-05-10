#!/usr/bin/python

from math import sqrt

def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

def presents_for_house(house):
    return sum(factors(house), 0) * 10

target_house_num = int(raw_input("Target House: "))
factors_for_target = factors(target_house_num)
presents_for_target = sum(factors_for_target, 0) * 10
print "TARGET HOUSE {0} - {1}: {2} presents".format(target_house_num, len(factors_for_target), presents_for_target)

for i in range(2, target_house_num, 2):
    factors_for_i = factors(i)
    presents = sum(factors_for_i, 0) * 10
    if i % 10000 == 0:
        print "HOUSE {0} - {1}: {2} presents".format(i, len(factors_for_i), presents)
    if presents >= presents_for_target:
        print "FOUND HOUSE {0} - {1}: {2} presents".format(i, len(factors_for_i), presents)
        break
