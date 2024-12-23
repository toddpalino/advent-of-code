#!/usr/bin/python3

from itertools import combinations
import re

def shortest_path(nodes, start, end):
	visited = {start: 0}
	queue = [start]
	while queue:
		current = queue.pop(0)
		if current == end:
			return visited[end]
		for next in nodes[current]['tunnels']:
			if next not in visited:
				visited[next] = visited[current] + 1
				queue.append(next)

valve_re = re.compile("Valve ([A-Z]+) has flow rate=(\d+); tunnel(s?) lead(s?) to valve(s?) ([A-Z ,]+)")

valves = {}
with open("input.txt") as f:
	for line in f:
		m = valve_re.match(line)
		valves[m.group(1)] = {
			'flow': int(m.group(2)),
			'open': False,
			'tunnels': m.group(6).split(', ')
		}

targets = [valve for valve, data in valves.items() if data['flow'] > 0]
nodes = targets.copy()
nodes.append('AA')
paths = {k: {} for k in nodes}

for leg in combinations(nodes, 2):
	cost = shortest_path(valves, leg[0], leg[1])
	paths[leg[0]][leg[1]] = cost
	paths[leg[1]][leg[0]] = cost

# node visited, me, elephant, time left me, time left ele, total flow
queue = [[targets.copy(), 'AA', 'AA', 26, 26, 0]]
completed = []

while queue:
	path = queue.pop(0)
	next_1 = path[0].pop()
	next_2 = path[0].pop()
	left_me = path[3] - (paths[path[1]][next_me] + 1)

	print(path)
	did_something = False
	for next_me in paths[path[1]].keys():
		if next_me in path[0]:
			continue

		for next_ele in paths[path[2]].keys():
			if (next_me == next_ele and left_me > 0) or next_ele in path[0]:
				continue
			left_ele = path[4] - (paths[path[2]][next_ele] + 1)

			total_flow = path[5]
			if left_me > 0:
				total_flow += left_me * valves[next_me]['flow']
			if left_ele > 0:
				total_flow += left_ele * valves[next_ele]['flow']

			if left_me < 2 and left_ele < 2:
				completed.append(total_flow)
			else:
				new_visited = path[0].copy()
				new_visited.extend([next_me, next_ele])
				queue.append([new_visited, next_me, next_ele, left_me, left_ele, total_flow])
			did_something = True
	if not did_something:
		completed.append(path[5])

print(max(completed))
