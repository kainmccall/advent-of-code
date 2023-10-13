import numpy as np
import Monkey as m
import sys

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = True        # Set to True when testing; set to False for actual problem
filename = "day21"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test-noah.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter='\n')

monkeys_1 = {}
for ln in data:
    monk = m.Monkey(ln)
    name = monk.name
    monkeys_1[name] = monk

# ~~~~~~~~~~Part 1~~~~~~~~~~~

print('Part 1: ' + str(monkeys_1['root'].get_value(monkeys_1)))

# ~~~~~~~~~~Part 2~~~~~~~~~~~

#sys.setrecursionlimit(1000000000)

monkeys_2 = {}
for ln in data:
    monk = m.Monkey(ln)
    name = monk.name
    if name == 'root':
        monkey_a = monk.value_tup[0]
        monkey_b = monk.value_tup[2]
    elif name == 'humn':
        monk.value_tup = (0, '+', 0)
        monk.value = 0
        monk.is_num = True
        monkeys_2[name] = monk
    else:
        monkeys_2[name] = monk

for monk in monkeys_2.keys():
    monkeys_2[monk].populate_inverses(monkeys_2)

monkeys_2['humn'].is_num = False

dependency = [False]
dep_branch = ''
monkeys_2[monkey_a].find_dependent(monkeys_2, 'humn', dependency, dep_branch)
# print("BRANCH: " + dep_branch)
# print(dependency)
if dependency[0]:
    #print('a')
    target = monkey_a
    equal_val = monkeys_2[monkey_b].get_value(monkeys_2, set_value=True)
    print(equal_val)
    monkeys_2[monkey_a].is_num = True
    monkeys_2[monkey_a].value = equal_val
else:
    #print('b')
    target = monkey_b
    equal_val = monkeys_2[monkey_a].get_value(monkeys_2, set_value=True)
    print(equal_val)
    monkeys_2[monkey_b].is_num = True
    monkeys_2[monkey_b].value = equal_val


for m in monkeys_2.keys():
    dep = [False]
    monkeys_2[m].find_dependent(monkeys_2, 'humn', dep, '')
    if not dep[0]:
        monkeys_2[m].get_value(monkeys_2, set_value=True)

human_num = monkeys_2['humn'].get_value_from_inverse(monkeys_2, set_value=True)
print('Part 2: ' + str(human_num))