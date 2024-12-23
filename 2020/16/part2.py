#!/usr/bin/python3

from functools import reduce

fields = {}
my_ticket = []
nearby_tickets = []

#with open("test2.txt") as f:
with open("input.txt") as f:
	parsing_tickets = False

	for line in f:
		ln = line.strip()
		if len(ln) == 0:
			continue

		if 'ticket' in ln:
			parsing_tickets = True
			continue
			
		if parsing_tickets:
			ticket = [int(n) for n in ln.split(',')]
			if not my_ticket:
				my_ticket = ticket
			else:
				nearby_tickets.append(ticket)
			continue

		# Parsing fields
		parts = ln.split(': ')
		ranges = parts[1].split(' or ')
		fields[parts[0]] = [[int(n) for n in r.split('-')] for r in ranges]

# Discard invalid tickets
valid_nearby = [ticket for ticket in nearby_tickets if not any(num >= 0 for num in ticket if all(not r[0] <= num <= r[1] for ranges in fields.values() for r in ranges))]
valid_nearby.append(my_ticket)

# Figure out the potential field mappings
field_ids = {field: [i for i, vals in enumerate(zip(*valid_nearby)) if all(((ranges[0][0] <= val <= ranges[0][1]) or (ranges[1][0] <= val <= ranges[1][1])) for val in vals)] for field, ranges in fields.items()}

# Iterate over the field_ids to reduce each one to one valid field
change = True
while change:
	change = False
	for field, ids in field_ids.items():
		if len(ids) > 1:
			continue
		remove_id = ids[0]
		for r_field, r_ids in field_ids.items():
			if len(r_ids) == 1:
				continue
			try:
				r_ids.remove(remove_id)
				change = True
			except ValueError:
				pass

print(reduce((lambda a, b: a * b), [my_ticket[field_ids[field][0]] for field in field_ids if field.startswith("departure")]))

