import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "2021day2"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.loadtxt(filename, dtype=str)

# ~~~~~~~~~~Part 1~~~~~~~~~~~

directions = {"forward":(1, 0), "down":(0, 1), "up":(0, -1)}

x = 0
y = 0
for instruct in data:
    dx_mult, dy_mult = directions[instruct[0]]
    dx = int(instruct[1]) * dx_mult
    dy = int(instruct[1]) * dy_mult
    x += dx
    y += dy

print("Final Position: (" + str(x) + ", " + str(y) + ")")
print("Part 1 Answer: " + str(x * y))

# ~~~~~~~~~~Part 2~~~~~~~~~~~

x2 = 0
y2 = 0
a2 = 0
dirs_aim = {"down":(0, 0, 1), "up":(0, 0, -1), "forward":(1, 1, 0)}

for instruct in data:
    dx_mult, dy_mult, da_mult = dirs_aim[instruct[0]]
    dx = int(instruct[1]) * dx_mult
    dy = int(instruct[1]) * dy_mult * a2
    da = int(instruct[1]) * da_mult
    x2 += dx
    y2 += dy
    a2 += da
#    print("(" + str(x2) + ", " + str(y2) + ", " + str(a2) + ")")

print("Final Position, part 2: (" + str(x2) + ", " + str(y2) + ", " + str(a2) + ")")
print("Part 2 Answer: " + str(x2 * y2))