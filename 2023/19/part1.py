#!/usr/bin/python3

parse_workflows = True
workflows = {}
parts = []

with open("input.txt") as f:
	for line in f:
		if line[:-1] == '':
			parse_workflows = False
			continue
		if parse_workflows:
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
		else:
			parts.append({v[0]: int(v[2:]) for v in line[1:-2].split(',')})

# This eases processing
workflows[None] = None

accept_sum = 0
for part in parts:
	workflow = workflows['in']
	while True:
		accept = None
		for rule in workflow:
			if rule['var'] is None:
				workflow = workflows[rule['next']]
				accept = rule['accept']
				break
			if (rule['lt'] and (part[rule['var']] < rule['val'])) or ((not rule['lt']) and (part[rule['var']] > rule['val'])):
				workflow = workflows[rule['next']]
				accept = rule['accept']
				break

		if accept is not None:
			if accept:
				accept_sum += sum(part.values())
			break

print(accept_sum)
