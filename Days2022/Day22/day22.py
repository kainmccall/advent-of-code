import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day22"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

f = open(filename, 'r')
data = f.readlines()

instructions = data[-1]

data = data[:-2]
map_grid = []
max_ln = 0
for ln in data:
    new_ln = ln[:-1]
    map_grid.append(new_ln)
    if len(new_ln) > max_ln:
        max_ln = len(new_ln)

for i in range(0, len(map_grid)):
    for j in range(0, max_ln - len(map_grid[i])):
        map_grid[i] = map_grid[i] + ' '

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

instructions_list = []
temp_inst = ''
for i in range(0, len(instructions)):
    if instructions[i] == 'L' or instructions[i] == 'R':
        instructions_list.append(temp_inst)
        instructions_list.append(instructions[i])
        temp_inst = ''
    else:
        temp_inst = temp_inst + instructions[i]
instructions_list.append(temp_inst)


# ~~~~~~~~~~Part 1~~~~~~~~~~~

def get_row(row):
    first = min([row.index('.'), row.index('#')])
    last = max([len(row) - row[::-1].index('.') - 1, len(row) - row[::-1].index('#') - 1])
    return (first, last)


def walk(grid, pos, facing):
    new_x, new_y = (pos[0] + facing[0], pos[1] + facing[1])
    if facing[1] == 0:      # moving in x direction
        min_x, max_x = get_row(grid[new_y])
        if new_x < min_x:
            new_x = max_x
        elif new_x > max_x:
            new_x = min_x
    else:                   # moving in y direction
        this_column = []
        for y in range(0, len(grid)):
            this_column.append(grid[y][new_x])
        min_y, max_y = get_row(this_column)
        if new_y < min_y:
            new_y = max_y
        elif new_y > max_y:
            new_y = min_y
    #print(new_x, new_y)
    if grid[new_y][new_x] != '#':
        pos = (new_x, new_y)
    return pos

def turn(current_facing_ind, instruction):
    if instruction == 'L':
        new_ind = current_facing_ind - 1
    elif instruction == 'R':
        new_ind = current_facing_ind + 1
    else:
        print('ERROR: ' + str(instruction) + ' is not a turn!!!')
    new_ind = new_ind % len(direction)
    return (new_ind, direction[new_ind])

def make_moves(grid, instruct_list):
    current_heading_ind = 0
    current_heading = direction[current_heading_ind]
    current_pos_y = 0
    current_pos_x, ignore = get_row(grid[0])
    current_pos = (current_pos_x, current_pos_y)
    for i in range(0, len(instruct_list)):
        if instruct_list[i] == 'L' or instruct_list[i] == 'R':
            current_heading_ind, current_heading = turn(current_heading_ind, instruct_list[i])
        else:
            for j in range(0, int(instruct_list[i])):
                current_pos = walk(grid, current_pos, current_heading)
    return (current_pos[0] + 1, current_pos[1] + 1, current_heading_ind)

col, row, head = make_moves(map_grid, instructions_list)
score = (1000 * row) + (4 * col) + head

print("Sum of Score, part 1: " + str(score))

# ~~~~~~~~~~Part 2~~~~~~~~~~~
if use_test_data:
    face_relations = {0:(5, 3, 2, 1), 1:(2, 4, 5, 0), 2:(3, 4, 1, 0), 3:(5, 4, 2, 0), 4:(5, 1, 2, 3), 5:(0, 1, 4, 3)}
    side_length = 4
    face_positions = [(2, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2)]
else:
    face_relations = {0:(1, 2, 4, 5), 1:(3, 2, 0, 5), 2:(1, 3, 4, 0), 3:(1, 5, 4, 2), 4:(3, 5, 0, 2), 5:(3, 1, 0, 4)}
    side_length = 50
    face_positions = [(1, 0), (2, 0), (1, 1), (1, 2), (0, 2), (0, 3)]

def get_global_coordinates(pos, face, facing):
    face_tile = face_positions[face]
    global_pos = (pos[0] + (side_length * face_tile[0]), pos[1] + (side_length * face_tile[1]))
    return global_pos[0], global_pos[1], facing

rotation_matrix = [[2, 1, 0, 3], [3, 2, 1, 0], [0, 3, 2, 1], [1, 0, 3, 2]]
fstring = 'ABCDEF'
hstring = 'RDLU'

def walk_on_cube(pos, face, facing_ind, faces):
    new_x, new_y = (pos[0] + direction[facing_ind][0], pos[1] + direction[facing_ind][1])
    if new_x >= side_length or new_x < 0 or new_y >= side_length or new_y < 0:
        print('new face?!')
        new_face = face_relations[face][facing_ind]
        old_face_heading_ind = face_relations[new_face].index(face)
        rotation_num = rotation_matrix[facing_ind][old_face_heading_ind]
        print('Rotation num: ' + str(rotation_num))
        new_x = new_x % side_length
        new_y = new_y % side_length
        for i in range(0, 4 - rotation_num):
            # x = new_x
            # y = new_y + (side_length - 1)
            # new_y = x % side_length
            # new_x = y % side_length
            new_x, new_y = ((-1 * new_y) + side_length - 1, new_x)
        new_x = new_x % side_length
        new_y = new_y % side_length
        new_facing_ind = (facing_ind - rotation_num) % 4
    else:
        new_face = face
        new_facing_ind = facing_ind
    if faces[new_face][new_y][new_x] != '#':
        return (new_x, new_y), new_face, new_facing_ind
    else:
        return pos, face, facing_ind

def turn_2(current_facing_ind, instruction):
    if instruction == 'L':
        new_ind = current_facing_ind - 1
    elif instruction == 'R':
        new_ind = current_facing_ind + 1
    else:
        print('ERROR: ' + str(instruction) + ' is not a turn!!!')
    new_ind = new_ind % len(direction)
    return new_ind

def make_cube_moves(cube_grid, instruct_list):
    current_heading_ind = 0
    current_face = 0
    current_pos = (0, 0)
    for i in range(0, len(instruct_list)):
        if instruct_list[i] == 'L' or instruct_list[i] == 'R':
            current_heading_ind = turn_2(current_heading_ind, instruct_list[i])
            print('--Turned!--')
            print("Current Face: " + fstring[current_face] + '; current position: ' + str(current_pos) + '; heading: ' + hstring[current_heading_ind])
            print('-----------')
        else:
            for j in range(0, int(instruct_list[i])):
                current_pos, current_face, current_heading_ind = walk_on_cube(current_pos, current_face, current_heading_ind, cube_grid)
                print("Current Face: " + fstring[current_face] + '; current position: ' + str(current_pos) + '; heading: ' + hstring[current_heading_ind])
    global_coords = get_global_coordinates(current_pos, current_face, current_heading_ind)
    return global_coords[0] + 1, global_coords[1] + 1, global_coords[2]




cube_face_grids = []
for i in range(0, len(face_positions)):
    face_grid = []
    for j in range(side_length * face_positions[i][1], side_length * (face_positions[i][1] + 1)):
        face_grid.append(map_grid[j][int(side_length * face_positions[i][0]):int(side_length * (face_positions[i][0] + 1))])
    cube_face_grids.append(face_grid)
print(cube_face_grids[0])

col_2, row_2, head_2 = make_cube_moves(cube_face_grids, instructions_list)
score_2 = (1000 * row_2) + (4 * col_2) + head_2
print('Score for part 2: ' + str(score_2))