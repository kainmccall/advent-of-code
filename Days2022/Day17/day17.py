import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day17"
run_part_1 = True
run_part_2 = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

LR_movement = str(np.genfromtxt(filename, dtype=str, delimiter=''))

shape_strings = [['..####.'], ['...#...', '..###..', '...#...'], ['..###..', '....#..', '....#..'], ['..#....', '..#....', '..#....', '..#....'], ['..##...', '..##...']]

shape_points = []
for i in range(0, len(shape_strings)):
    shape_points.append([])
    for j in range(0, len(shape_strings[i])):
        for k in range(0, len(shape_strings[i][j])):
            if shape_strings[i][j][k] == '#':
                shape_points[i].append((k, j))


# ~~~~~~~~~~Part 1~~~~~~~~~~~

def drop_rock(movement_count, r_count, grid):
    rock_count = r_count % len(shape_strings)
    rock_points = shape_points[rock_count].copy()
    for i in range(0, 3):
        grid.append('.......')
    for i in range(0, len(rock_points)):
        new_x = rock_points[i][0]
        new_y = rock_points[i][1] + len(grid)
        rock_points[i] = (new_x, new_y)
    for i in range(0, len(shape_strings[rock_count])):
        grid.append('.......')
    has_fallen = False
    while not has_fallen:
        has_fallen, rock_points, movement_count = move_rock(rock_points, movement_count, grid)
    for pt in rock_points:
        new_ln = grid[pt[1]][0:pt[0]] + '#' + grid[pt[1]][pt[0] + 1:]
        grid[pt[1]] = new_ln
    grid = list(filter(lambda a: a != '.......', grid))
    r_count += 1
    return movement_count, r_count, grid

def move_rock(rock_points, movement_count, grid):
    has_fallen = False
    movement_count = movement_count % len(LR_movement)
    mvmt_str = LR_movement[movement_count]
    if mvmt_str == '<':
        dx = -1
    else:
        dx = 1
    can_move_x = True
    new_rock_points_x = []
    for i in range(0, len(rock_points)):
        if 0 <= rock_points[i][0] + dx < len(grid[0]) and grid[rock_points[i][1]][rock_points[i][0] + dx] != '#':
            new_x = rock_points[i][0] + dx
            new_y = rock_points[i][1]
            new_rock_points_x.append((new_x, new_y))
        else:
            can_move_x = False
    if can_move_x:
        rock_points = new_rock_points_x
    movement_count += 1
    dy = -1
    can_move_y = True
    new_rock_points_y = []
    for i in range(0, len(rock_points)):
        if 0 <= rock_points[i][1] + dy < len(grid) and grid[rock_points[i][1] + dy][rock_points[i][0]] != '#':
            new_x = rock_points[i][0]
            new_y = rock_points[i][1] + dy
            new_rock_points_y.append((new_x, new_y))
        else:
            can_move_y = False
    if can_move_y:
        rock_points = new_rock_points_y
    else:
        has_fallen = True
    return has_fallen, rock_points, movement_count

def print_grid(grid):
    for i in range(-1, -1 * (len(grid) + 1), -1):
        print(grid[i])
if run_part_1:
    grid_1 = []
    grid_height = 0
    shp_ct = 0
    mvt_ct = 0
    while shp_ct < 2022:
        mvt_ct, shp_ct, grid_1 = drop_rock(mvt_ct, shp_ct, grid_1)
    print_grid(grid_1)
    print('Tower Height: ' + str(len(grid_1)))

# ~~~~~~~~~~Part 2~~~~~~~~~~~

def get_col_height(grid):
    col_heights = [0, 0, 0, 0, 0, 0, 0]
    for c in range(0, 7):
        i = len(grid) - 1
        floor_found = False
        while i >= 0 and not floor_found:
            if grid[i][c] == '.':
                col_heights[c] += 1
            else:
                floor_found = True
            i -= 1
    col_h_tup = (col_heights[0], col_heights[1], col_heights[2], col_heights[3], col_heights[4], col_heights[5], col_heights[6])
    return col_h_tup
if run_part_2:
    grid_2 = []
    grid_height = 0
    shp_ct = 0
    mvt_ct = 0
    cycle_found = False
    cyc_dict = {}
    c1_ht = 0
    c2_ht = 0
    r1 = 0
    r2 = 0
    cycle = ()
    while not cycle_found:
        mvt_ct, shp_ct, grid_2 = drop_rock(mvt_ct, shp_ct, grid_2)
        grid_ht = len(grid_2)
        col_ht = get_col_height(grid_2)
        cyc_tup = (mvt_ct % len(LR_movement), shp_ct % len(shape_strings), col_ht)
        if cyc_tup not in cyc_dict.keys():
            cyc_dict[cyc_tup] = (shp_ct, grid_ht, 1)
        else:
            if cyc_dict[cyc_tup][2] > 0:
                cycle_found = True
                print("Cycle found!")
                cycle = cyc_tup
                c1_ht = cyc_dict[cyc_tup][1]
                c2_ht = grid_ht
                r1 = cyc_dict[cyc_tup][0]
                r2 = shp_ct
            else:
                cyc_dict[cyc_tup] = (cyc_dict[cyc_tup][0], cyc_dict[cyc_tup][1], cyc_dict[cyc_tup][2] + 1)


    num_to_drop = 1000000000000
    cyc_ht = c2_ht - c1_ht
    print('Height Added per Cycle: ' + str(cyc_ht))
    cyc_rocks = r2 - r1
    print('Cycle Period: ' + str(cyc_rocks))

    initial_rocks_dropped = cyc_dict[cycle][0]
    print('# of Rocks dropped before cycles start: ' + str(initial_rocks_dropped))
    final_rocks_dropped = (num_to_drop - initial_rocks_dropped) % cyc_rocks
    print('# of Rocks dropped after last full cycle ends: ' + str(final_rocks_dropped))
    num_cycles = int((num_to_drop - initial_rocks_dropped) // cyc_rocks)
    print('# of cycles which would be executed: ' + str(num_cycles))

    grid_3 = []
    shp_ct_3 = 0
    mvt_ct_3 = 0
    print('Starting new grid to drop ' + str(initial_rocks_dropped + final_rocks_dropped) + ' rocks not included in cycles...')
    while shp_ct_3 < (initial_rocks_dropped + final_rocks_dropped):
        mvt_ct_3, shp_ct_3, grid_3 = drop_rock(mvt_ct_3, shp_ct_3, grid_3)
    final_height = ((num_cycles) * cyc_ht) + len(grid_3)
    print('Height from Cycled Rocks: ' + str((num_cycles) * cyc_ht))
    print('Height from non-cycled rocks: ' + str(len(grid_3)))
    print('Total Height: ' + str(final_height))