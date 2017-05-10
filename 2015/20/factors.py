#!/usr/bin/python

from math import sqrt

def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

def presents_for_house(house):
    return sum(factors(house), 0) * 10

target_house_num = int(raw_input("Target House: "))
presents_for_target = presents_for_house(target_house_num)
print "TARGET HOUSE: {0} presents".format(presents_for_target)
print factors(target_house_num)
