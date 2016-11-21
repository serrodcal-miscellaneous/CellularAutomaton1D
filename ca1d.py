import sys

RULE = int(sys.argv[1])

MAX_TIME = int(sys.argv[2])
HALF_SIZE = MAX_TIME
index = range(-HALF_SIZE, HALF_SIZE+1)

# initial condition
cells = {i: '0' for i in index}
cells[0] = '1'
# padding on both ends
cells[-HALF_SIZE-1] = '0'
cells[ HALF_SIZE+1] = '0'

#Parsing RULE to binary
BINARY_RULE = format(RULE, '08b')

keys_sorted = ["111","110","101", "100", "011", "010", "001", "000"]

new_state = {"111": '0', "110": '0', "101": '0', "100": '0', "011": '0', "010": '0', "001": '0', "000": '0'}

position = 0

#Fill new_satate dict with rule in binary
for key in keys_sorted:
    new_state[key] = BINARY_RULE[position]
    position += 1

for time in range(0, MAX_TIME):
    # print current state
    for i in index:
        if cells[i] == '1':
            sys.stdout.write(u'\u2588')
        else:
            sys.stdout.write(' ')
    sys.stdout.write('\n')
    # evolve
    patterns = {i: cells[i-1] + cells[i] + cells[i+1] for i in
                index}
    cells = {i: new_state[patterns[i]] for i in index}
    cells[-HALF_SIZE-1] = '0'
    cells[ HALF_SIZE+1] = '0'