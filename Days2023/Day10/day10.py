import numpy as np
import math

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
run_part_1 = False           # Only affects which test data to use!
filename = "day10"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    if run_part_1:
        filename = filename + "test.txt"
    else:
        filename = filename + "testb.txt"
else:
    filename = filename + ".txt"

position_grid = np.genfromtxt(filename, dtype=str, delimiter="\n")

symbol_offset = {"|":[(-1, 0), (1, 0)], "-":[(0, -1), (0, 1)], "L":[(-1, 0), (0, 1)], "J":[(-1, 0), (0, -1)], "7":[(1, 0), (0, -1)], "F":[(1, 0), (0, 1)]}

starting_pos = (0, 0)
for i in range(len(position_grid)):
    if "S" in position_grid[i]:
        starting_pos = (i, position_grid[i].index("S"))

# ~~~~~~~~~~Part 1~~~~~~~~~~~
def fillGrid(start_pos, pos_grid):
    next_pos = []
    fill_grid = [[math.inf for x in range(len(pos_grid[0]))] for y in range(len(pos_grid))]
    fill_grid[start_pos[0]][start_pos[1]] = 0
    for i in range(len(next_pos)):
        fill_grid[next_pos[i][0]][next_pos[i][1]] = 1
    for y in range(start_pos[0] - 1, start_pos[0] + 2, 1):
        if (y >= 0) and (y < len(pos_grid)):
            for x in range(start_pos[1] - 1, start_pos[1] + 2, 1):
                if (x >= 0) and (x < len(pos_grid[y])):
                    if pos_grid[y][x] in symbol_offset.keys():
                        for i in range(len(symbol_offset[pos_grid[y][x]])):
                            test_pos = (y + symbol_offset[pos_grid[y][x]][i][0], x + symbol_offset[pos_grid[y][x]][i][1])
                            if test_pos == start_pos:
                                next_pos.append((y, x))
    isFilled = False
    steps = 1
    while not isFilled:
        steps += 1
        isFilled = True
        temp_next_pos = []
        for i in range(len(next_pos)):
            pos_offsets = symbol_offset[pos_grid[next_pos[i][0]][next_pos[i][1]]]
            for j in range(len(pos_offsets)):
                test_pos = (next_pos[i][0] + pos_offsets[j][0], next_pos[i][1] + pos_offsets[j][1])
                if fill_grid[test_pos[0]][test_pos[1]] > steps:
                    isFilled = False
                    fill_grid[test_pos[0]][test_pos[1]] = steps
                    temp_next_pos.append(test_pos)
        next_pos = temp_next_pos
    return steps - 1, fill_grid

num_steps, f_grid = fillGrid(starting_pos, position_grid)

print("Part 1 Answer: " + str(num_steps) + " steps")

# ~~~~~~~~~~Part 2~~~~~~~~~~~

def printGrid(pos_grid):
    for i in range(len(pos_grid)):
        print(pos_grid[i])


expand_right = {".": ".", "|": ".", "-": "-", "L": "-", "J": ".", "7": ".", "F": "-"}
expand_down = {".": ".", "|": "|", "-": ".", "L": ".", "J": ".", "7": "|", "F": "|"}

def replaceStartPos(start_pos, pos_grid):
    off_pos = []
    for y in range(start_pos[0] - 1, start_pos[0] + 2, 1):
        if (y >= 0) and (y < len(pos_grid)):
            for x in range(start_pos[1] - 1, start_pos[1] + 2, 1):
                if (x >= 0) and (x < len(pos_grid[y])):
                    if pos_grid[y][x] in symbol_offset.keys():
                        for i in range(len(symbol_offset[pos_grid[y][x]])):
                            test_pos = (y + symbol_offset[pos_grid[y][x]][i][0], x + symbol_offset[pos_grid[y][x]][i][1])
                            if test_pos == start_pos:
                                off_pos.append((-1 * symbol_offset[pos_grid[y][x]][i][0], -1 * symbol_offset[pos_grid[y][x]][i][1]))
    off_pos = sorted(off_pos)
    for symbol, offset in symbol_offset.items():
        if sorted(offset) == off_pos:
            pos_grid[start_pos[0]] = pos_grid[start_pos[0]][0:start_pos[1]] + symbol + pos_grid[start_pos[0]][start_pos[1] + 1:]

def expandGrid(pos_grid):
    new_pos_grid = []
    for i in range(len(pos_grid)):
        old_line = pos_grid[i]
        new_line = ''
        for j in range(len(pos_grid[i])):
            new_line += old_line[j] + expand_right[old_line[j]]
        new_pos_grid.append(new_line)
        next_line = ''
        for j in range(len(new_line)):
            next_line += expand_down[new_line[j]]
        new_pos_grid.append(next_line)
    return new_pos_grid

replaceStartPos(starting_pos, position_grid)
expanded_pos_grid = expandGrid(position_grid)
new_starting_pos = (2 * starting_pos[0], 2 * starting_pos[1])
new_steps, new_fill_grid = fillGrid(new_starting_pos, expanded_pos_grid)


def fillFillGrid(fill_grid):
    pos_offset = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    next_pos = []
    for i in range(len(fill_grid[0])):
        if fill_grid[0][i] == math.inf:
            next_pos.append((0, i))
            fill_grid[0][i] = 1
    for i in range(len(fill_grid[len(fill_grid) - 1])):
        if fill_grid[len(fill_grid) - 1][i] == math.inf:
            next_pos.append((len(fill_grid) - 1, i))
            fill_grid[len(fill_grid) - 1][i] = 1
    for i in range(len(fill_grid)):
        if fill_grid[i][0] == math.inf:
            next_pos.append((i, 0))
            fill_grid[i][0] = 1
    for i in range(len(fill_grid)):
        if fill_grid[i][len(fill_grid[0]) - 1] == math.inf:
            next_pos.append((i, len(fill_grid[0]) - 1))
            fill_grid[i][len(fill_grid[0]) - 1] = 1
    isFilled = False
    while not isFilled:
        temp_next_pos = []
        isFilled = True
        for i in range(len(next_pos)):
            for j in range(len(pos_offset)):
                y = next_pos[i][0] + pos_offset[j][0]
                x = next_pos[i][1] + pos_offset[j][1]
                if y >= 0 and y < len(fill_grid) and x >= 0 and x < len(fill_grid[0]):
                    if (y, x) not in temp_next_pos:
                        if fill_grid[y][x] == math.inf:
                            fill_grid[y][x] = 1
                            temp_next_pos.append((y, x))
                            isFilled = False
        next_pos = temp_next_pos
    area_sum = 0
    for i in range(len(fill_grid)):
        for j in range(len(fill_grid[i])):
            if fill_grid[i][j] == math.inf:
                if i % 2 == 0 and j % 2 == 0:
                    area_sum += 1
    return area_sum

print("Area Inside Loop: " + str(fillFillGrid(new_fill_grid)))



