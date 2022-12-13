import sys
import numpy as np
import string

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

run_part_2 = False
use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day12"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.loadtxt(filename, dtype=str)
alpha_height_map = []
for line in data:
    line_list = [str(i) for i in [*line]]
    alpha_height_map.append(line_list)

# ~~~~~~~~~~Part 1~~~~~~~~~~~

sys.setrecursionlimit(5000)                     # This is the line that I was missing for 3+ hours, apparently

letters_list = list(string.ascii_lowercase)
values = range(1, 27)
letters_dict = {letters_list[i]: values[i] for i in range(len(values))}
letters_dict['S'] = 1
letters_dict['E'] = 26

start_pos = (0, 0)
end_pos = (0, 0)
for y in range(len(alpha_height_map)):
    for x in range(len(alpha_height_map[y])):
        if alpha_height_map[y][x] == 'S':
            start_pos = (x, y)
        if alpha_height_map[y][x] == 'E':
            end_pos = (x, y)

def find_climb_path(pos, height_map, flood_map):
    if pos[0] != len(height_map[0]) - 1:
        test_pos = (pos[0] + 1, pos[1])
        if run_checks(pos, test_pos, height_map, flood_map):
            flood_map[test_pos[1]][test_pos[0]] = flood_map[pos[1]][pos[0]] + 1
            find_climb_path(test_pos, height_map, flood_map)
    if pos[0] != 0:
        test_pos = (pos[0] - 1, pos[1])
        if run_checks(pos, test_pos, height_map, flood_map):
            flood_map[test_pos[1]][test_pos[0]] = flood_map[pos[1]][pos[0]] + 1
            find_climb_path(test_pos, height_map, flood_map)
    if pos[1] != len(height_map) - 1:
        test_pos = (pos[0], pos[1] + 1)
        if run_checks(pos, test_pos, height_map, flood_map):
            flood_map[test_pos[1]][test_pos[0]] = flood_map[pos[1]][pos[0]] + 1
            find_climb_path(test_pos, height_map, flood_map)
    if pos[1] != 0:
        test_pos = (pos[0], pos[1] - 1)
        if run_checks(pos, test_pos, height_map, flood_map):
            flood_map[test_pos[1]][test_pos[0]] = flood_map[pos[1]][pos[0]] + 1
            find_climb_path(test_pos, height_map, flood_map)

def print_flood_map(flood_map):
    for y in range(0, len(flood_map)):
        print_string = ''
        for x in range(0, len(flood_map[0])):
            if flood_map[y][x] != 99999:
                print_string = print_string + alpha_height_map[y][x]
            else:
                print_string = print_string + ' '
        print(print_string)
    print('-------------------')

def run_checks(pos, test_pos, height_map, flood_map):
    is_valid = True
    if letters_dict[height_map[test_pos[1]][test_pos[0]]] > (letters_dict[height_map[pos[1]][pos[0]]] + 1):
        is_valid = False
    elif flood_map[pos[1]][pos[0]] + 1 >= flood_map[test_pos[1]][test_pos[0]]:
        is_valid = False
    return is_valid



flooded_map = []
for i in range(len(alpha_height_map)):
    flooded_map.append([99999 for x in range(0, len(alpha_height_map[0]))])
flooded_map[start_pos[1]][start_pos[0]] = 0

find_climb_path(start_pos, alpha_height_map, flooded_map)
print_flood_map(flooded_map)
print("Fewest Steps from S to E: " + str(flooded_map[end_pos[1]][end_pos[0]]))


# ~~~~~~~~~~Part 2~~~~~~~~~~~

# WARNING: Part 2 takes a few minutes to run (there are more efficient ways to get the answer for part 2,
# but this is not one of them). Therefore, I have set run_part_2 to 'False' by default; to run part 2, set
# run_part_2 on line 7 to 'True'

if run_part_2:
    smallest_path_lengths = []
    start_pos_list = []
    for y in range(0, len(alpha_height_map)):
        for x in range(0, len(alpha_height_map[y])):
            if alpha_height_map[y][x] == 'a' or alpha_height_map[y][x] == 'S':
                start_pos_list.append((x, y))

    for start_pos_2 in start_pos_list:
        flooded_map_2 = []
        for i in range(len(alpha_height_map)):
            flooded_map_2.append([99999 for x in range(0, len(alpha_height_map[0]))])
        flooded_map_2[start_pos_2[1]][start_pos_2[0]] = 0
        find_climb_path(start_pos_2, alpha_height_map, flooded_map_2)
        smallest_path_lengths.append(flooded_map_2[end_pos[1]][end_pos[0]])

    smallest_path_length = min(smallest_path_lengths)
    print("Smallest Path from any a: " + str(smallest_path_length))