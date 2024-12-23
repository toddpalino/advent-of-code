#!/usr/bin/python3

#with open("test.txt") as f:
with open("input.txt") as f:
	ts = int(f.readline())
	buses = [int(bus_id) for bus_id in f.readline().split(',') if bus_id != 'x']

min_wait = None
min_bus_id = None
for bus_id in buses:
	wait_time = (((ts // bus_id) + 1) * bus_id) - ts
	if min_wait is None or min_wait > wait_time:	
		min_wait = wait_time
		min_bus_id = bus_id

print("Bus ID: %d" % (min_bus_id))
print("Wait Time: %d" % (min_wait))
print(min_bus_id * min_wait)
