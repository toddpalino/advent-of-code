#!/usr/bin/python3

from itertools import combinations, permutations
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

# nodes in path, time left, total flow
queue = [[['AA'], 30, 0]]

current = 'AA'
completed = []

while queue:
	path = queue.pop(0)
	for next in paths[path[0][-1]].keys():
		if next not in path[0]:
			if (path[1] - paths[path[0][-1]][next]) < 2:
				completed.append(path[2])
			else:
				new_path = path[0].copy()
				new_path.append(next)
				time_left = path[1] - (paths[path[0][-1]][next] + 1)
				queue.append([new_path, time_left, path[2] + (valves[next]['flow'] * time_left)])
		else:
			completed.append(path[2])

print(max(completed))
