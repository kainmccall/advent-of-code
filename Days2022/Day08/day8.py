import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False       # Set to True when testing; set to False for actual problem
filename = "day8"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.loadtxt(filename, dtype=str)
tree_map = []
for line in data:
    line_list = [int(i) for i in [*line]]
    tree_map.append(line_list)

# ~~~~~~~~~~Part 1~~~~~~~~~~~

visible_trees = []
for y in range(0, len(tree_map)):
    for x in range(0, len(tree_map[0])):
        current_value = tree_map[y][x]
        is_visible1 = True          # ew, but... functional?
        is_visible2 = True
        is_visible3 = True
        is_visible4 = True
        for i in range(0, x):
            if tree_map[y][i] >= current_value:
                is_visible1 = False
                break
        if x != len(tree_map[0]) - 1:
            for i in range(x + 1, len(tree_map[0])):
                if tree_map[y][i] >= current_value:
                    is_visible2 = False
                    break
        for i in range(0, y):
            if tree_map[i][x] >= current_value:
                is_visible3 = False
                break
        if y != len(tree_map) - 1:
            for i in range(y + 1, len(tree_map)):
                if tree_map[i][x] >= current_value:
                    is_visible4 = False
                    break
        is_visible = False
        if is_visible1 or is_visible2 or is_visible3 or is_visible4:
            is_visible = True
        if is_visible:
            visible_trees.append(current_value)

print("Number of Visible Trees: " + str(len(visible_trees)))

# ~~~~~~~~~~Part 2~~~~~~~~~~~

scenic_scores = []
for y in range(0, len(tree_map)):
    for x in range(0, len(tree_map[0])):
        current_value = tree_map[y][x]
        left_score = 0
        x_left = x - 1
        if x != 0:
            while x_left >= 0:
                test_value = tree_map[y][x_left]
                if test_value < current_value:
                    left_score += 1
                    x_left -= 1
                else:
                    left_score += 1
                    break
        right_score = 0
        x_right = x + 1
        if x != len(tree_map[0]) - 1:
            while x_right < len(tree_map[0]):
                test_value = tree_map[y][x_right]
                if test_value < current_value:
                    right_score += 1
                    x_right += 1
                else:
                    right_score += 1
                    break
        up_score = 0
        y_up = y - 1
        if y != 0:
            while y_up >= 0:
                test_value = tree_map[y_up][x]
                if test_value < current_value:
                    up_score += 1
                    y_up -= 1
                else:
                    up_score += 1
                    break
        down_score = 0
        y_down = y + 1
        if y != len(tree_map[0]) - 1:
            while y_down < len(tree_map[0]):
                test_value = tree_map[y_down][x]
                if test_value < current_value:
                    down_score += 1
                    y_down += 1
                else:
                    down_score += 1
                    break
        scenic_score = up_score * down_score * left_score * right_score
        scenic_scores.append(scenic_score)

print("Max Scenic Score: " + str(max(scenic_scores)))