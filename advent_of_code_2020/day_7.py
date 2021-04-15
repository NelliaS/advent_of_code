dictionary = {}

with open('day_7.txt') as f:
    for line in f:
        key = ' '.join(line.split()[0:2])
        value_str = ' '.join(line.split()[4:]).replace(' bags', '').replace(' bag', '').rstrip('.')
        value = []
        for bag in value_str.split(', '):
            if bag == 'no other':
                pass
            else:
                bag = bag.split()
                bag = bag[0], ' '.join(bag[1:])
                value.append(bag)
        dictionary.setdefault(key, value)


def shiny_bags(dictionary):
    '''How many colors can, eventually, contain at least one shiny gold bag?'''
    keys = ['shiny gold']
    new = []
    all_colors = []
    while keys:  # until there is another key, which eventually contain shiny gold bag
        for key, value in dictionary.items():
            for tuple in value:
                if tuple[1] in keys:  # contains bag, which contains shiny gold bag
                    new.append(key)
                    all_colors.append(key)
        keys = new
        new = []
    return len(set(all_colors))            # filter off duplicates


def shiny_bag_require(dictionary):
    ''' How many individual bags are required inside single shiny gold bag? '''
    count = -1
    tuple_number_color = [('1', 'shiny gold')]
    while tuple_number_color:
        one_cycle = []
        for number, color in tuple_number_color:
            for i in range(int(number)):
                count += 1
                one_cycle += dictionary[color]
        tuple_number_color = one_cycle
    return count


print(shiny_bags(dictionary))           # part 1
print(shiny_bag_require(dictionary))    # part 2