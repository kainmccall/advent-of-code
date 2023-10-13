import numpy as np
import Elf as e
from collections import Counter
import copy as c

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day23"
run_part_1 = False
run_part_2 = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, comments=None)

# ~~~~~~~~~~Part 1~~~~~~~~~~~

elf_list = set()
for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        if data[i][j] == '#':
            elf = e.Elf((j, i))
            elf_list.add(elf)

directions = [[(-1, -1), (0, -1), (1, -1)], [(-1, 1), (0, 1), (1, 1)], [(-1, -1), (-1, 0), (-1, 1)], [(1, -1), (1, 0), (1, 1)]]

elf_list_2 = c.deepcopy(elf_list)
directions_2 = c.deepcopy(directions)

def get_elf_pos_list(elves):
    elf_positions = set()
    elf_positions_str = set()
    for elf in elves:
        elf_positions.add(elf.pos)
        elf_positions_str.add(str(elf.pos))
    return elf_positions, elf_positions_str

def round(elves, direction_list):
    moved_elf = False
    moved_count = 0
    proposed_points = {}
    elf_positions, elf_positions_str = get_elf_pos_list(elves)
    for elf in elves:
        elf.propose_move(direction_list, elf_positions_str, proposed_points)
    #proposed_points_count = Counter(proposed_points)
    #print(proposed_points_count)
    for elf in elves:
        #elf.check_proposed_move(proposed_points_count)
        elf.check_proposed_move(proposed_points)
    for elf in elves:
        mvmt = elf.move()
        if mvmt:
            moved_elf = True
            moved_count += 1
    first_direction = direction_list.pop(0)
    direction_list.append(first_direction)
    return moved_elf, moved_count

def get_smallest_rectangle(elves):
    elf_positions, elf_positions_str = get_elf_pos_list(elves)
    min_x = 1000000000
    max_x = -1000000000
    min_y = 1000000000
    max_y = -1000000000
    for pos in elf_positions:
        if pos[0] > max_x:
            max_x = pos[0]
        if pos[0] < min_x:
            min_x = pos[0]
        if pos[1] > max_y:
            max_y = pos[1]
        if pos[1] < min_y:
            min_y = pos[1]
    return min_x, max_x, min_y, max_y

def get_rect_area(elves):
    min_x, max_x, min_y, max_y = get_smallest_rectangle(elves)
    len = max_y - min_y + 1
    wid = max_x - min_x + 1
    return len * wid

def print_elf_grid(elves):
    elf_positions, elf_positions_str = get_elf_pos_list(elves)
    min_x, max_x, min_y, max_y = get_smallest_rectangle(elves)
    for y in range(min_y, max_y + 1):
        print_str = ''
        for x in range(min_x, max_x + 1):
            pos = (x, y)
            if pos in elf_positions:
                print_str = print_str + '#'
            else:
                print_str = print_str + '.'
        print(print_str)
    print('-----')
    print('\n')

if run_part_1:
    num_rounds = 10
    for i in range(0, num_rounds):
        round(elf_list, directions)
    area = get_rect_area(elf_list)
    print_elf_grid(elf_list)
    print('# empty spaces remaining after 10 rounds: ' + str(area - len(elf_list)))

# ~~~~~~~~~~Part 2~~~~~~~~~~~

if run_part_2:
    moved_an_elf = True
    rd = 0
    while moved_an_elf:
        moved_an_elf, num_elves_moved = round(elf_list_2, directions_2)
        rd += 1
        print('# of elves moved in round ' + str(rd) + ': ' + str(num_elves_moved))
    print_elf_grid(elf_list_2)
    print('First round where no elves move: ' + str(rd))
