#!/usr/bin/env python3

with open('input', 'r') as f:
	license = [int(num) for num in f.read().split(' ')]

# We're going to go over 1000 layers deep, so a non-recursive may not necessarily be required,
# but it is highly recommended.

# Add the root node as index 0
nodes = [{'children': [], 'metadata': [], 'value': 0}]
task_stack = [{'id': 0, 'parent': None, 'children_left': license[0], 'metadata': license[1]}]

pos = 2
while len(task_stack) > 0:
	task = task_stack[-1]
	task_id = task['id']

	# Done reading children. Read metadata and move on
	if task['children_left'] == 0:
		nodes[task_id]['metadata'] = license[pos:pos+task['metadata']]
		pos = pos + task['metadata']

		# Because metadata is written from the bottom of the tree up, we can calculate node value as we go along
		if len(nodes[task_id]['children']) == 0:
			nodes[task_id]['value'] = sum(nodes[task_id]['metadata'])
		else:
			for child in nodes[task_id]['metadata']:
				if child > 0 and child <= len(nodes[task_id]['children']):
					nodes[task_id]['value'] += nodes[nodes[task_id]['children'][child-1]]['value']

		task_stack.pop()
		continue

	# Read next child
	next_id = len(nodes)
	nodes[task['id']]['children'].append(next_id)
	nodes.append({'children': [], 'metadata': [], 'value': 0})
	task['children_left'] -= 1
	task_stack.append({'id': next_id, 'parent': task['id'], 'children_left': license[pos], 'metadata': license[pos+1]})
	pos += 2

# Sum all metadata
total_metadata = sum(sum(node['metadata']) for node in nodes)

print("Nodes: {}".format(len(nodes)))
print("Total Metadata: {}".format(total_metadata))
print("Node 0 Value: {}".format(nodes[0]['value']))
