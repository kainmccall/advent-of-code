import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day20"
run_part_1 = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.loadtxt(filename, dtype=int)
#print(data)

# (number, original index)

numbers = []

for i in range(0, len(data)):
    tup = (data[i], i)
    numbers.append(tup)


decrypt_key = np.int64(811589153)

numbers_2 = []
for i in range(len(numbers)):
    tup = (np.int64(numbers[i][0] * decrypt_key), numbers[i][1])
    numbers_2.append(tup)

# ~~~~~~~~~~Part 1~~~~~~~~~~~

def move_number(num_list, index):
    current_index = next((i for i, v in enumerate(num_list) if v[1] == index), None)
    current_val = num_list[current_index][0]
    new_index = current_index + num_list[current_index][0]
    #print(new_index)
    if current_val != 0:
        if new_index == 0:
            mover = num_list.pop(current_index)
            num_list.append(mover)
        # elif new_index > 0:
        #     num_list.insert(int((new_index % len(num_list)) + (new_index // len(num_list))), num_list.pop(current_index))
        else:
            mover = num_list.pop(current_index)
            # num_list.insert(len(num_list) + new_index, mover)
            num_list.insert(int((len(num_list) + new_index) % len(num_list)), mover)
    # print(num_list)
    return num_list

def mix(num_list):
    for i in range(0, len(num_list)):
        num_list = move_number(num_list, i)
    #print(num_list)
    return num_list

def decode(num_list):
    current_zero_position = next((i for i, v in enumerate(num_list) if v[0] == 0), None)
    print('Current Zero Index: ' + str(current_zero_position))
    c1 = num_list[(current_zero_position + 1000) % len(num_list)][0]
    print("c1: " + str(c1))
    c2 = num_list[(current_zero_position + 2000) % len(num_list)][0]
    print("c2: " + str(c2))
    c3 = num_list[(current_zero_position + 3000) % len(num_list)][0]
    print("c3: " + str(c3))
    coordinate_sum = c1 + c2 + c3
    return coordinate_sum

if run_part_1:
    mix(numbers)
    print('PART 1: Sum of c1, c2, and c3: ' + str(decode(numbers)))
    print('\n')


# ~~~~~~~~~~Part 2~~~~~~~~~~~


for i in range(0, 10):
    mix(numbers_2)
# mix(numbers_2)

print('PART 2: Sum of c1, c2, and c3: ' + str(decode(numbers_2)))