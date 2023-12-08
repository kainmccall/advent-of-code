import numpy as np
import math
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
run_part_1 = False
filename = "day8"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    if run_part_1:
        filename = filename + "test.txt"
    else:
        filename = filename + "testb.txt"

else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter="\n")
steps = data[0]
network = {}
for i in range(1, len(data), 1):
    instruction = data[i][0:3]
    left = data[i][7:10]
    right = data[i][12:15]
    network[instruction] = [left, right]

# ~~~~~~~~~~Part 1~~~~~~~~~~~
if run_part_1:
    current_location = "AAA"
    atZZZ = False
    num_steps = 0
    while not atZZZ:
        left_right = 0
        if steps[num_steps % len(steps)] == "R":
            left_right = 1
        current_location = network[current_location][left_right]
        num_steps += 1
        if current_location == "ZZZ":
            atZZZ = True

    print("Number of Steps to Reach ZZZ: " + str(num_steps))



# ~~~~~~~~~~Part 2~~~~~~~~~~~
else:
    start_positions = []
    for key in network.keys():
        if str(key)[-1] == "A":
            start_positions.append(key)
    num_steps_to_z = []
    for i in range(len(start_positions)):
        current_location = start_positions[i]
        atZ = False
        num_steps = 0
        while not atZ:
            left_right = 0
            if steps[num_steps % len(steps)] == "R":
                left_right = 1
            num_steps += 1
            current_location = network[current_location][left_right]
            if current_location[-1] == "Z":
                atZ = True
        num_steps_to_z.append(num_steps)
    #   Unfortunately, I can't get math.lcm() to work with a list as its argument, so now I'm using eval() because why not?
    num_steps_to_z_str = str(num_steps_to_z[0])
    for i in range(1, len(num_steps_to_z), 1):
        num_steps_to_z_str += ", " + str(num_steps_to_z[i])
    total_steps = eval("math.lcm(" + num_steps_to_z_str + ")")
    print("Part 2 Number of Steps Needed: " + str(total_steps))