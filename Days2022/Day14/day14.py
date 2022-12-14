import numpy as np
import copy as c

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day14"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter='\n')


def draw_rock_line(pt_1, pt_2, cave):
    if pt_1[0] == pt_2[0]:      # vertical line
        x = pt_1[0]
        if pt_1[1] > pt_2[1]:
            start = pt_2[1]
            end = pt_1[1] + 1
        else:
            start = pt_1[1]
            end = pt_2[1] + 1
        for y in range(start, end):
            cave[y][x] = '#'
    else:                       # Horizontal line
        y = pt_1[1]
        if pt_1[0] > pt_2[0]:
            start = pt_2[0]
            end = pt_1[0] + 1
        else:
            start = pt_1[0]
            end = pt_2[0] + 1
        for x in range(start, end):
            cave[y][x] = '#'


max_x = 0
max_y = 0
rock_lines = []
for ln in data:
    rock_points_str = ln.split(' -> ')
    rock_line = []
    for strng in rock_points_str:
        rock_point = strng.split(',')
        rock_point_tup = (int(rock_point[0]), int(rock_point[1]))
        rock_line.append(rock_point_tup)
        if rock_point_tup[0] > max_x:
            max_x = rock_point_tup[0]
        if rock_point_tup[1] > max_y:
            max_y = rock_point_tup[1]
    rock_lines.append(rock_line)

cave_map = []
for i in range(0, max_y + 3):  # Adding 2 extra empty lines to the bottom to allow falling into void
    cave_map.append(['.' for x in range(0, max_x + 1)])

for ln in rock_lines:
    for i in range(0, len(ln) - 1):
        draw_rock_line(ln[i], ln[i + 1], cave_map)

cave_map_2 = c.deepcopy(cave_map)  # For use in part 2
cave_map_2[len(cave_map_2) - 1] = ['#' for z in range(0, len(cave_map_2[0]))]

# ~~~~~~~~~~Part 1~~~~~~~~~~~


def print_cave(cave):
    for ln in cave:
        print(''.join(ln))
    print('---------------')


def drop_sand(sand_drop_x, cave):
    sand_drop = sand_drop_x
    if cave[0][sand_drop] != '.':
        print("WARNING! Sand spawn blocked?!")
        print_cave(cave)
        return
    sand_pos = (sand_drop, 0)
    is_landed = False
    is_void_bound = False
    while (is_landed is False) and (is_void_bound is False):
        is_landed, is_void_bound, sand_pos = move_sand(sand_pos, cave)
    return is_void_bound


def move_sand(sand_pos, cave):
    sand_void = len(cave)
    is_landed = False
    is_void_bound = False
    if sand_pos[1] + 1 == sand_void:    # Sand will fall into the void-- stop now!
        is_void_bound = True
        return is_landed, is_void_bound, sand_pos
    elif cave[sand_pos[1] + 1][sand_pos[0]] == '.':
        sand_pos = (sand_pos[0], sand_pos[1] + 1)
        return is_landed, is_void_bound, sand_pos
    elif sand_pos[0] != 0 and cave[sand_pos[1] + 1][sand_pos[0] - 1] == '.':
        sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)
        return is_landed, is_void_bound, sand_pos
    elif sand_pos[0] != len(cave[0]) - 1 and cave[sand_pos[1] + 1][sand_pos[0] + 1] == '.':
        sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
        return is_landed, is_void_bound, sand_pos
    else:
        cave[sand_pos[1]][sand_pos[0]] = 'o'
        is_landed = True
        return is_landed, is_void_bound, sand_pos


sand_dropped = 0
is_void_bound = False
while is_void_bound is False:
    sand_dropped += 1
    # print("Dropping Sand " + str(sand_dropped))
    is_void_bound = drop_sand(500, cave_map)
    # print_cave(cave_map)

print("Blocks of Sand Dropped, pt. 1: " + str(sand_dropped - 1))


# ~~~~~~~~~~Part 2~~~~~~~~~~~

def check_edges(sand_pos, sand_drop, cave):     # If sand gets too close to left or right edge, moves left or right edge
    if sand_pos[0] == 0:
        # add dots to left, sand_drop and sand pos[0] + 1
        sand_pos[0] = sand_pos[0] + 1
        sand_drop = sand_drop + 1
        for y in range(0, len(cave)):
            if y == len(cave) - 1:
                new_line = ['#']
            else:
                new_line = ['.']
            for x in range(0, len(cave[0])):
                new_line.append(cave[y][x])
            cave[y] = new_line
    elif sand_pos[0] == len(cave[0]) - 1:   # Append dots to the right
        for y in range(0, len(cave) - 1):
            cave[y].append('.')
        cave[len(cave) - 1].append('#')     # Make sure to include the floor!
    return sand_pos, sand_drop, cave


def move_sand_2(sand_pos, cave):
    is_landed = False
    if cave[sand_pos[1] + 1][sand_pos[0]] == '.':
        sand_pos = (sand_pos[0], sand_pos[1] + 1)
        return is_landed, sand_pos
    elif cave[sand_pos[1] + 1][sand_pos[0] - 1] == '.':
        sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)
        return is_landed, sand_pos
    elif cave[sand_pos[1] + 1][sand_pos[0] + 1] == '.':
        sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
        return is_landed, sand_pos
    else:
        cave[sand_pos[1]][sand_pos[0]] = 'o'
        is_landed = True
        return is_landed, sand_pos


def drop_sand_2(sand_drop, cave):
    is_blocked = False
    if cave[0][sand_drop] != '.':
        is_blocked = True
        return is_blocked
    sand_pos = (sand_drop, 0)
    is_landed = False
    while is_landed is False:
        sand_pos, sand_drop, cave = check_edges(sand_pos, sand_drop, cave)
        is_landed, sand_pos = move_sand_2(sand_pos, cave)
    return is_blocked


sand_dropped_2 = 0
is_blocked = False
while is_blocked is False:
    sand_dropped_2 += 1
    # print("Dropping Sand " + str(sand_dropped))
    is_blocked = drop_sand_2(500, cave_map_2)
    # print_cave(cave_map)

print("Blocks of Sand Dropped, pt. 2: " + str(sand_dropped_2 - 1))
