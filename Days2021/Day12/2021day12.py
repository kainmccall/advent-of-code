import numpy as np
import Cave as c

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "2021day12"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter='\n')
#print(data)

# ~~~~~~~~~~Part 1~~~~~~~~~~~

cave_dict = {}

for ln in data:
    cave_names = ln.split('-')
    cave_1_name = cave_names[0]
    cave_2_name = cave_names[1]
    if cave_1_name in cave_dict.keys():
        cave_1 = cave_dict[cave_1_name]
    else:
        cave_1 = c.Cave(cave_1_name)
        cave_dict[cave_1.name] = cave_1
    if cave_2_name in cave_dict.keys():
        cave_2 = cave_dict[cave_2_name]
    else:
        cave_2 = c.Cave(cave_2_name)
        cave_dict[cave_2.name] = cave_2
    cave_1.connections.append(cave_2)
    cave_2.connections.append(cave_1)

start_cave = cave_dict['start']
# if start_cave.is_big:
#     print("s big")
# else:
#     print("s small")

path_list = []
start_cave.explore('', path_list)
print("Number of paths to end: " + str(len(path_list)))




# ~~~~~~~~~~Part 2~~~~~~~~~~~

small_caves = []

for cv in cave_dict.values():
    if not cv.is_big:
        small_caves.append(cv.name)

#print(small_caves)

path_list_2 = []
start_cave.explore_2('', path_list_2, small_caves)
print("Number of paths to end, pt. 2: " + str(len(path_list_2)))