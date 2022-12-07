import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "2021day9"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.loadtxt(filename, dtype=str)
heat_map = []
for line in data:
    line_list = [int(i) for i in [*line]]
    heat_map.append(line_list)

# ~~~~~~~~~~Part 1~~~~~~~~~~~
lowpoint_sum = 0
for y in range(0, len(heat_map)):
    for x in range(0, len(heat_map[y])):
        adj = []
        if y == 0:
            adj.append(heat_map[y + 1][x])
        elif y == len(heat_map) - 1:
            adj.append(heat_map[y - 1][x])
        else:
            adj.append(heat_map[y + 1][x])
            adj.append(heat_map[y - 1][x])
        if x == 0:
            adj.append(heat_map[y][x + 1])
        elif x == len(heat_map[y]) - 1:
            adj.append(heat_map[y][x - 1])
        else:
            adj.append(heat_map[y][x + 1])
            adj.append(heat_map[y][x - 1])
        is_lowpoint = True
        for pt in adj:
            if heat_map[y][x] >= pt:
                is_lowpoint = False
        if is_lowpoint:
            lowpoint_sum += (heat_map[y][x] + 1)

print("Sum of Low Point Risk Values: " + str(lowpoint_sum))

# ~~~~~~~~~~Part 2~~~~~~~~~~~

def print_map(map_list):
    for ln in map_list:
        new_line = ' '.join([str(x) for x in ln])
        print(new_line)
    print('------------------')

heat_basin = heat_map.copy()

def fill_basin(coords, heat_graph):
    for coord_pair in coords:
        x = coord_pair[0]
        y = coord_pair[1]
        heat_graph[y][x] = 9

def search_adj_coords(coords, heat_graph):
    max_y = len(heat_graph)
    max_x = len(heat_graph[0])
    is_working = True
    while is_working:
        is_working = False
        for coord_pair in coords:
            x = coord_pair[0]
            y = coord_pair[1]
            if x != 0:
                if (heat_graph[y][x - 1] != 9) and [x - 1, y] not in coords:
                    coords.append([x - 1, y])
                    is_working = True
            if x != max_x - 1:
                if (heat_graph[y][x + 1] != 9) and [x + 1, y] not in coords:
                    coords.append([x + 1, y])
                    is_working = True
            if y != 0:
                if (heat_graph[y - 1][x] != 9) and [x, y - 1] not in coords:
                    coords.append([x, y - 1])
                    is_working = True
            if y != max_y - 1:
                if (heat_graph[y + 1][x] != 9) and [x, y + 1] not in coords:
                    coords.append([x, y + 1])
                    is_working = True
    return coords

basin_sizes = []
for y in range(0, len(heat_basin)):
    for x in range(0, len(heat_basin[y])):
        if heat_basin[y][x] != 9:
            coords = [[x, y]]
            coords = search_adj_coords(coords, heat_basin)
            basin_sizes.append(len(coords))
            fill_basin(coords, heat_basin)
            #print_map(heat_basin)


basin_sizes.sort()
#print(basin_sizes)
basin_size_mult = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

print("Multiplied Basin Sizes: " + str(basin_size_mult))