import numpy as np
import copy

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "2021day11"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.loadtxt(filename, dtype=str)
octo_map_orig = []
for line in data:
    line_list = [int(i) for i in [*line]]
    octo_map_orig.append(line_list)
octo_map = copy.deepcopy(octo_map_orig)
octo_map_2 = copy.deepcopy(octo_map_orig)
# ~~~~~~~~~~Part 1~~~~~~~~~~~

def print_map(map_list):
    for ln in map_list:
        new_line = ' '.join([str(x) for x in ln])
        print(new_line)
    print('------------------')

def get_adjacents(coords, o_map):
    adj = []
    y_range = range(0, len(o_map))
    x_range = range(0, len(o_map[0]))
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            (adj_x, adj_y) = (coords[0] + dx, coords[1] + dy)
            if (adj_x in x_range) and (adj_y in y_range) and (dx, dy) != (0, 0):
                adj.append((adj_x, adj_y))
    return adj


def octo_step(o_map):
    # Add 1 to every octopus
    for y in range(0, len(o_map)):
        for x in range(0, len(o_map[0])):
            o_map[y][x] += 1
    # Now, flash them until no more can flash
    flashy_octos = []
    has_flashed = True
    while has_flashed:
        has_flashed = False
        for y in range(0, len(o_map)):
            for x in range(0, len(o_map[0])):
                current_coords = (x, y)
                if o_map[y][x] > 9 and current_coords not in flashy_octos:
                    flashy_octos.append(current_coords)
                    adj_octos = get_adjacents(current_coords, o_map)
                    has_flashed = True
                    for octo in adj_octos:
                        o_map[octo[1]][octo[0]] += 1
    # Now, set any that have flashed to 0
    for octo in flashy_octos:
        o_map[octo[1]][octo[0]] = 0
    n_flashes = len(flashy_octos)
    return o_map, n_flashes, flashy_octos

num_steps = 100

num_flashes = 0
for i in range(0, num_steps):
    octo_map, new_flashes, flash_coords = octo_step(octo_map)
    num_flashes += new_flashes
    #print(flash_coords)

print("Number of Flashes after " + str(num_steps) + " steps: " + str(num_flashes))
#print_map(octo_map)


# ~~~~~~~~~~Part 2~~~~~~~~~~~

num_octopi = int(len(octo_map_2) * len(octo_map_2[0]))

num_flashes_2 = 0
num_steps_2 = 0
while num_flashes_2 < num_octopi:
    octo_map_2, num_flashes_2, flash_coords_2 = octo_step(octo_map_2)
    num_steps_2 += 1

print("Step of First Synchronized Flash: " + str(num_steps_2))

