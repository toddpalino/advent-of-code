#!/usr/bin/python3

import time
from collections import deque
from map import build_map

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	home = build_map(f.read().strip())

# Figure out the shortest path to every room
rooms = {home.room_id: 0}
visited = set()
queue = deque([home])
while queue:
	room = queue.popleft()
	for next_room, door_id in room.doors():
		if door_id in visited:
			continue
		rooms[next_room.room_id] = rooms[room.room_id] + 1
		visited.add(door_id)
		queue.append(next_room)

over_1000 = 0
longest_path = 0
for dist in rooms.values():
	longest_path = max(longest_path, dist)
	if dist >= 1000:
		over_1000 += 1

print("Longest path: %d" % (longest_path))
print("Paths over 1000: %d" % (over_1000))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
