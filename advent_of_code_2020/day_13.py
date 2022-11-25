import math

with open('day_13.txt') as f:
    array = f.read().split('\n')
    arrival_time = int(array[0])
    schedule = array[1].split(',')


def find_closest_bus(arrival_time, schedule):
    """
    Look for searched bus through addition of time.
    Return earliest bus, for which division of time and its number will be zero.
    """
    buses = [int(x) for x in schedule if x != 'x']
    departure_time = arrival_time
    while True:
        for bus_id in buses:
            if departure_time % bus_id == 0:
                return (departure_time - arrival_time) * bus_id
        departure_time += 1


# Previous - extremely slow solution, even though optimized as well as I could

# def find_timestamp_of_schedule(schedule):
#     template = [(int(bus), schedule.index(bus)) for bus in schedule if bus != 'x']
#     chosen_bus, time_to_sync = max(template)
#     departures = {bus: departure - time_to_sync for bus, departure in template if bus != chosen_bus}
#     divisor_rules = {
#         19: ['+', 2],
#         17: ['-', 5],
#         23: ['+', 7],
#         13: ['+', 4],
#         29: ['+', 3],
#         37: ['-', 11],
#         41: ['-', 4],
#         379: ['-', 341],
#     }
#
#     for timestamp in count(99999999999708, step=chosen_bus):
#         for bus_id, diff in departures.items():
#             timestamp_to_check = str(timestamp + diff)
#             operation, multiply_by = divisor_rules[bus_id]
#             n1, n2 = int(timestamp_to_check[:-1]), int(timestamp_to_check[-1]) * multiply_by
#             result = n1 + n2 if operation == '+' else n1 - n2
#             if not result % bus_id == 0:
#                 break
#             else:
#                 if bus_id == 19:  # last on the list
#                     return timestamp + min(departures.values())


def find_timestamp_of_schedule(schedule):
    """
    We are looking for number, which can be divided by product of bus ids to give result timestamp as a remainder.
    Such number is sum of multiplications of partial product * remainder * modular multiplicative inverse

    Heavily based on Elvin Lee solution, check it out:
        https://github.com/elvinyhlee/advent-of-code-2020-python/blob/master/day13.py
    """
    template = [(int(bus_id), int(bus_id) - schedule.index(bus_id)) for bus_id in schedule if bus_id != 'x']
    product = math.prod([bus_id for bus_id, _ in template])
    number = 0
    for bus_id, remainder in template:
        partial_product = product // bus_id
        number += partial_product * remainder * pow(partial_product, -1, bus_id)

    return number % product


print(f'Result of part 1: "{find_closest_bus(arrival_time, schedule)}"')
print(f'Result of part 2: "{find_timestamp_of_schedule(schedule)}"')
