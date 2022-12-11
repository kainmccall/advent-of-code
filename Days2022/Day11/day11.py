import numpy as np
import Monkey as m
import copy

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day11"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter='\n')

# ~~~~~~~~~~Part 1~~~~~~~~~~~

def print_monkey_items(round_num, monkey_list):
    print("Round " + str(round_num + 1))
    for monk in monkey_list:
        print(monk.items)
    print("------------------")

monkeys = []
test_product = 1
i = 0
while i < len(data):
    monk_num = int(i / 6)
    start_items = [int(x) for x in data[i + 1][16:].split(', ')]
    op_string = data[i + 2][17:]
    test = int(data[i + 3][19:])
    test_product = test_product * test
    if_true = int(data[i + 4][25:])
    if_false = int(data[i + 5][26:])
    new_monkey = m.Monkey(start_items, i, op_string, test, if_true, if_false)
    monkeys.append(new_monkey)
    i += 6

monkeys_2 = copy.deepcopy(monkeys)      # Added for part 2

num_rounds = 20

for round in range(0, num_rounds):
    for monk in range(0, len(monkeys)):
        this_monkey = monkeys[monk]
        for item in range(0, len(this_monkey.items)):
            item_thrown = this_monkey.inspect_throw()
            monkeys[item_thrown[0]].items.append(item_thrown[1])
    #print_monkey_items(round, monkeys)

num_inspects = []
for monk in monkeys:
    num_inspects.append(monk.num_inspects)
num_inspects.sort(reverse=True)

monkey_business = num_inspects[0] * num_inspects[1]

print("Monkey Business: " + str(monkey_business))

# ~~~~~~~~~~Part 2~~~~~~~~~~~

def elim_test_products(monkey_list):
    for monk in monkey_list:
        monk.items = [x % test_product for x in monk.items]

num_rounds_2 = 10000

for round in range(0, num_rounds_2):
    for monk in range(0, len(monkeys_2)):
        this_monkey = monkeys_2[monk]
        for item in range(0, len(this_monkey.items)):
            item_thrown = this_monkey.inspect_throw_2(test_product)
            monkeys_2[item_thrown[0]].items.append(item_thrown[1])
    #print_monkey_items(round, monkeys_2)
    elim_test_products(monkeys_2)

num_inspects_2 = []
for monk in monkeys_2:
    num_inspects_2.append(monk.num_inspects)
num_inspects_2.sort(reverse=True)

monkey_business_2 = num_inspects_2[0] * num_inspects_2[1]

print("Monkey Business, pt. 2: " + str(monkey_business_2))