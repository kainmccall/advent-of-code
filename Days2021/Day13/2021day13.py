import numpy as np
import math
import copy as c

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "2021day13"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter='\n\n')

folds = []
dot_coordinates = []
max_x = 0
max_y = 0
for ln in data:
    if ln[0] == 'f':
        folds.append(ln.split()[2])
    else:
        coords = ln.split(',')
        dot_coordinates.append((int(coords[0]), int(coords[1])))      # (x, y)
        if int(coords[0]) > max_x:
            max_x = int(coords[0])
        if int(coords[1]) > max_y:
            max_y = int(coords[1])

this_paper = []
for y in range(0, max_y + 1):
    this_paper.append([0 for x in range(0, max_x + 1)])

for dot in dot_coordinates:
    this_paper[dot[1]][dot[0]] += 1

this_paper_2 = c.deepcopy(this_paper)

# ~~~~~~~~~~Part 1~~~~~~~~~~~

def fold_y(line, paper):
    extra_length = float(len(paper[:line]) - len(paper[line + 1:]))
    extra = [[0 for x in range(0, len(paper[0]))] for y in range(0, int(math.fabs(extra_length)))]
    if extra_length < 0: # bottom longer than top; append extra to top of paper
        new_paper = extra
        for ln in paper:
            new_paper.append(ln)
        paper = new_paper
    elif extra_length > 0: # top longer than bottom; append extra to bottom of paper
        new_paper = paper
        for ln in extra:
            new_paper.append(ln)
        paper = new_paper
    folded_paper = [[0 for x in range(0, len(paper[0]))] for y in range(0, int((len(paper) - 1) / 2))]
    # now, fold the paper
    for x in range(0, len(paper[0])):
        for y in range(0, int((len(paper) - 1) / 2)):
            folded_paper[y][x] = paper[y][x] + paper[int(-1 * (y + 1))][x]
    return folded_paper

def fold(instruction, paper):
    instruct = instruction.split('=')
    axis = instruct[0]
    line = int(instruct[1])
    if axis != 'y':
        translated_paper = transpose(paper) # Don't want to write the same folding routine again for x, so turn paper
        folded_paper = fold_y(line, translated_paper)
        paper = transpose(folded_paper) # Turn paper back
    else:
        paper = fold_y(line, paper)
    return paper

def transpose(paper):
    new_paper = [[0 for i in range(0, len(paper))] for j in range(0, len(paper[0]))]
    for y in range(0, len(paper)):
        for x in range(0, len(paper[0])):
            new_paper[x][y] = paper[y][x]
    return new_paper

def get_num_visible_dots(paper):
    num_dots = 0
    for y in range(0, len(paper)):
        for x in range(0, len(paper[0])):
            if paper[y][x] > 0:
                num_dots += 1
    return num_dots

first_instruct = folds[0]
num_vis_dots = get_num_visible_dots(fold(first_instruct, this_paper))
print("Number of Visible Dots after First Fold: " + str(num_vis_dots))



# ~~~~~~~~~~Part 2~~~~~~~~~~~

def print_paper(paper):
    for ln in paper:
        print_str = ''
        for char in ln:
            if char > 0:
                print_str = print_str + '#'
            else:
                print_str = print_str + ' '
        print(print_str)

for fld in folds:
    this_paper_2 = fold(fld, this_paper_2)

print_paper(this_paper_2)
