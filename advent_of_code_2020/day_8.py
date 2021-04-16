instr = []

with open('day_8.txt') as f:
    arrays = []
    for line in f:
        text, value = line.rstrip().split()
        instr.append((text, value))


def identify_infinite_loop(instr):
    '''
    Identify the value of accumulator before program starts an infinite loop
    (executes same instruction for 2nd time).
    Input is array of tuples, first in tuple, there is is operation (acc, jmp, nop) and second is number.
    Operation "nop" - does nothing.
    Operation "acc" - add or reduce accumulator value by given number.
    Operation "jmp" - when positive: skips some instructions, eg. (jmp, 2) skip one following instruction,
                    - when negative: goes back in instructions, eg. (jmp, -2) goes two instructions back.
    Returns True, when an infinite loop is present.
    Returns False, if program hasn't an infinite loop.
    '''
    accum = 0           # accumulator starts at 0
    used = []           # indexes of already used instructions
    current_index = 0
    try:
        while current_index not in used:
            operation, number = instr[current_index]
            used.append(current_index)
            if operation == 'nop':
                current_index += 1
            elif operation == 'acc':
                accum += int(number)
                current_index += 1
            else:                           # jmp
                current_index += int(number)
        return (True, accum)      # the value of accumulator before infinite loop starts
    except IndexError:
        return (False, accum)


def infinite_or_not(instr):
    '''
    Return False if there is infinite loop present in instructions,
    else return value of accumulator before program termination
    '''
    infinite, accum = identify_infinite_loop(instr)
    if infinite:
        return False
    else:
        return accum


def prevent_infinite(instr):
    '''
    Try to swap operations "nop" and "jmp" to find a way how to prevent infinite loop.
    Return value of accumulator before program termination.
    '''
    while True:
        for i, instruction in enumerate(instr):
            operation, number = instruction
            if operation == 'nop':
                changed_instr = instr[:i] + [('jmp', number)] + instr[i+1:]
                accum = infinite_or_not(changed_instr)
                if accum:
                    return accum
            if operation == 'jmp':
                changed_instr = instr[:i] + [('nop', number)] + instr[i+1:]
                accum = infinite_or_not(changed_instr)
                if accum:
                    return accum


print(identify_infinite_loop(instr)[1])         # part 1
print(prevent_infinite(instr))                  # part 2