
with open('day_13.txt') as f:
    array = f.read().split('\n')
    arrival_time = int(array[0])
    schedule = array[1].split(',')


# PART 1

def choose_bus(arrival_time, buses):
    '''
    Look for searched bus through addition of time.
    Return earliest bus, for which division of time and its number will be zero.
    '''
    departure_time = arrival_time
    while True:
        for ID in buses:
            if departure_time % ID == 0:
                bus_chosen = ID
                return bus_chosen, departure_time
        departure_time += 1


def find_closest_bus(arrival_time, buses):
    '''
    Buses are numbered. They take loop, leaving at times multiplied by their number.
    Find closest bus, after arrival_time.
    Return number of earliest bus you can take to the airport multiplied by number of waited minutes.
    '''
    buses = []
    [buses.append(int(x)) for x in schedule if x != 'x']
    bus_chosen, departure_time = choose_bus(arrival_time, buses)
    waiting = departure_time - arrival_time
    return waiting * bus_chosen


print(find_closest_bus(arrival_time, schedule))     # part 1