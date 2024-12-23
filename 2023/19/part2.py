#!/usr/bin/python3

def decompose_workflow(workflow, conditions):
	accepted_conditions = []
	for rule in workflow:
		new_conditions = conditions.copy()
		if rule['var'] is not None:
			new_conditions.append((rule['var'], rule['lt'], rule['val']))
			conditions.append((rule['var'], not rule['lt'], rule['val'] + (-1 if rule['lt'] else 1)))
		if rule['accept'] is None:
			accepted_conditions.extend(decompose_workflow(workflows[rule['next']], new_conditions.copy()))
		elif rule['accept']:
			accepted_conditions.append(new_conditions.copy())
	return accepted_conditions

workflows = {}
with open("input.txt") as f:
	for line in f:
		if line[:-1] == '':
			break

		n = line.index('{')
		wf_name = line[0:n]
		raw_rules = line[n+1:-2].split(',')
		last_rule = raw_rules.pop()

		rules = []
		for rule in raw_rules:
			ptr_colon = rule.index(':')
			rules.append({
				'var': rule[0],
				'lt': rule[1] == '<',
				'val': int(rule[2:ptr_colon]),
				'accept': None,
				'next': rule[ptr_colon+1:]
			})
		rules.append({'var': None, 'accept': None, 'next': last_rule})

		# Clean the rule targets
		for rule in rules:
			if rule['next'] == 'A':
				rule['accept'] = True
				rule['next'] = None
			elif rule['next'] == 'R':
				rule['accept'] = False
				rule['next'] = None

		workflows[wf_name] = rules

accepted_conditions = decompose_workflow(workflows['in'], [])

accepted_count = 0
for conditions in accepted_conditions:
	# Bounds will be exclusive
	bounds = {'x': [0, 4001], 'm': [0, 4001],'a': [0, 4001],'s': [0, 4001]}
	for rule in conditions:
		if rule[1]:
			bounds[rule[0]][1] = min(bounds[rule[0]][1], rule[2])
		else:
			bounds[rule[0]][0] = max(bounds[rule[0]][0], rule[2])

	accepted_count += (bounds['x'][1] - bounds['x'][0] - 1) * (bounds['m'][1] - bounds['m'][0] - 1) * (bounds['a'][1] - bounds['a'][0] - 1) * (bounds['s'][1] - bounds['s'][0] - 1)

print(accepted_count)
