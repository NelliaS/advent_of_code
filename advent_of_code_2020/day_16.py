import math
import re
from itertools import chain


def extract_data():
    with open('day_16.txt') as f:
        fields_data, ticket_data, nearby_tickets_data = f.read().split('\n\n')

        my_ticket = tuple([int(number) for number in ticket_data.split('\n')[1].split(',')])
        nearby_tickets = []
        for ticket in nearby_tickets_data.rstrip().split('\n')[1:]:
            nearby_tickets.append(tuple([int(number) for number in ticket.split(',')]))

        fields = {}
        for entry in fields_data.split('\n'):
            field, values = entry.split(': ')
            numbers = [int(number) for number in re.findall('[0-9]+', values)]
            fields[field] = [*range(numbers[0], numbers[1] + 1)] + [*range(numbers[2], numbers[3] + 1)]

    return fields, my_ticket, nearby_tickets


def part1(fields, nearby_tickets):
    # calculate which numbers are invalid (doesn't belong to any range of field)
    invalid_numbers = {*range(0, 1000)}
    for numbers in fields.values():
        invalid_numbers = invalid_numbers.difference(numbers)

    # filter out invalid tickets and calculate error score
    valid_tickets = []
    error_score = 0
    for ticket in nearby_tickets:
        ticket_errors = [number for number in ticket if number in invalid_numbers]
        if ticket_errors:
            error_score += sum(ticket_errors)
        else:
            valid_tickets.append(ticket)
    return valid_tickets, error_score


def part2(fields, nearby_tickets, my_ticket):
    valid_tickets = part1(fields, nearby_tickets)[0]
    match_fields = {field_name: [*range(0, len(my_ticket))] for field_name in fields.keys()}

    # filter out indexes which are invalid for given field
    for i in range(len(my_ticket)):
        for field_name, valid_values in fields.items():
            for number in [ticket[i] for ticket in valid_tickets]:
                if number not in valid_values:
                    match_fields[field_name].remove(i)
                    break

    # reduce until one index is left for every field
    while len(list(chain.from_iterable(match_fields.values()))) != 20:
        for field_name, possible_values in match_fields.items():
            if len(possible_values) != 1:
                continue
            value = possible_values[0]
            for key, all_values in match_fields.items():
                if key != field_name and value in all_values:
                    match_fields[key].remove(value)

    return math.prod([my_ticket[value[0]] for key, value in match_fields.items() if key.startswith('departure')])


fields, my_ticket, nearby_tickets = extract_data()
print(f'Result of part 1: "{part1(fields, nearby_tickets)[1]}"')
print(f'Result of part 2: "{part2(fields, nearby_tickets, my_ticket)}"')
