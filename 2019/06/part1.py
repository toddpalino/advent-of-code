#!/usr/bin/env python

import time
from orbit import Orbit

#fn = "test.txt"
#fn = "test2.txt"
fn = "input.txt"

start_time = time.time()

# A dict to map names to orbits. Start with the Center of Mass (COM) which orbits around nothing
orbits = {'COM': Orbit('COM')}

with open(fn, 'r') as f:
	for line in f:
		parts = line.strip().split(')')
		if parts[0] not in orbits:
			orbits[parts[0]] = Orbit(parts[0])
		if parts[1] not in orbits:
			orbits[parts[1]] = Orbit(parts[1], orbits[parts[0]])
		else:
			orbits[parts[0]].add_orbiter(orbits[parts[1]])

num_orbits = sum(o.count_orbits() for o in orbits.values())
print(f"Total number of orbits: {num_orbits}")

src = orbits['YOU']
tgt = orbits['SAN'].orbits_around
num_transfers = src.count_transfers(tgt)
print(f"Total number of transfers: {num_transfers}")

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
