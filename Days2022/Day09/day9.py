import numpy as np
import math

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day9"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.loadtxt(filename, dtype=str)

# ~~~~~~~~~~Part 1~~~~~~~~~~~
dir_dict = {"R":(1, 0), "L":(-1, 0), "U":(0, -1), "D":(0, 1)}

def get_adjacents(coords):
    adj = []
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            (adj_x, adj_y) = (coords[0] + dx, coords[1] + dy)
            adj.append(str((adj_x, adj_y)))
    return adj

def check_adjacents(coords_tail, coords_head):
    adj_coords = get_adjacents(coords_head)
    t_coords_str = str(coords_tail)
    if t_coords_str in adj_coords:
        return True
    else:
        return False

def add_tail_pos(coords_tail, tail_coords_list):
    if str(coords_tail) not in tail_coords_list:
        tail_coords_list.append(str(coords_tail))
    return tail_coords_list

head_pos = (0, 0)
tail_pos = (0, 0)
tail_pos_list = [str(tail_pos)]
for step in data:
    dx, dy = dir_dict[step[0]]
    num_steps = step[1]
    for i in range(0, int(num_steps)):
        head_pos = (head_pos[0] + dx, head_pos[1] + dy)
        tail_is_adj = check_adjacents(tail_pos, head_pos)
        if not tail_is_adj:
            # move tail
            if head_pos[0] == tail_pos[0]:
                if head_pos[1] > tail_pos[1]:
                    tail_pos = (tail_pos[0], tail_pos[1] + 1)
                else:
                    tail_pos = (tail_pos[0], tail_pos[1] - 1)
            elif head_pos[1] == tail_pos[1]:
                if head_pos[0] > tail_pos[0]:
                    tail_pos = (tail_pos[0] + 1, tail_pos[1])
                else:
                    tail_pos = (tail_pos[0] - 1, tail_pos[1])
            else:
                tail_dx, tail_dy = (int((head_pos[0] - tail_pos[0]) / math.fabs(head_pos[0] - tail_pos[0])), int((head_pos[1] - tail_pos[1]) / math.fabs(head_pos[1] - tail_pos[1])))
                tail_pos = (tail_pos[0] + tail_dx, tail_pos[1] + tail_dy)
            tail_pos_list = add_tail_pos(tail_pos, tail_pos_list)
        #print("Head pos: " + str(head_pos) + "; Tail pos: " + str(tail_pos))


print("Number of Tail Positions, 2-knot rope: " + str(len(tail_pos_list)))
# ~~~~~~~~~~Part 2~~~~~~~~~~~
# Same as part 1, except now generalize and make the "head" the knot in front of the "tail" knot (i. e. add in a for loop
# and give each knot except the last one a turn as the "head" knot; only advance the front knot according to the input though!)
knot_pos = [(0, 0) for i in range(0, 10)]
tail_pos_list_2 = [str((0, 0))]
for step in data:
    dx, dy = dir_dict[step[0]]
    num_steps = step[1]
    for i in range(0, int(num_steps)):
        knot_pos[0] = (knot_pos[0][0] + dx, knot_pos[0][1] + dy)
        for j in range(0, 9):
            head_pos_2 = (knot_pos[j][0], knot_pos[j][1])
            tail_pos_2 = (knot_pos[j + 1][0], knot_pos[j + 1][1])
            tail_is_adj = check_adjacents(tail_pos_2, head_pos_2)
            if not tail_is_adj:
                # move tail
                if head_pos_2[0] == tail_pos_2[0]:
                    if head_pos_2[1] > tail_pos_2[1]:
                        tail_pos_2 = (tail_pos_2[0], tail_pos_2[1] + 1)
                    else:
                        tail_pos_2 = (tail_pos_2[0], tail_pos_2[1] - 1)
                elif head_pos_2[1] == tail_pos_2[1]:
                    if head_pos_2[0] > tail_pos_2[0]:
                        tail_pos_2 = (tail_pos_2[0] + 1, tail_pos_2[1])
                    else:
                        tail_pos_2 = (tail_pos_2[0] - 1, tail_pos_2[1])
                else:
                    tail_dx, tail_dy = (int((head_pos_2[0] - tail_pos_2[0]) / math.fabs(head_pos_2[0] - tail_pos_2[0])), int((head_pos_2[1] - tail_pos_2[1]) / math.fabs(head_pos_2[1] - tail_pos_2[1])))
                    tail_pos_2 = (tail_pos_2[0] + tail_dx, tail_pos_2[1] + tail_dy)
                if j == 8:
                    tail_pos_list_2 = add_tail_pos(tail_pos_2, tail_pos_list_2)
            knot_pos[j] = head_pos_2
            knot_pos[j + 1] = tail_pos_2

        #print("Head pos: " + str(head_pos_2) + "; Tail pos: " + str(tail_pos_2))

#print(tail_pos_list_2)
print("Number of Tail Positions, 10-knot rope: " + str(len(tail_pos_list_2)))