import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day9"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

sets = np.loadtxt(filename, ndmin=2, dtype=int)
# ~~~~~~~~~~Part 1~~~~~~~~~~~

def findDiff(num_set, next_val):
    diffs = []
    for i in range(len(num_set) - 1):
        diff = num_set[i + 1] - num_set[i]
        diffs.append(diff)
    diffs_set = set(diffs)
    # print(diffs_set)
    if (len(diffs_set) != 1) or 0 not in diffs_set:
        next_val = findDiff(diffs, next_val)
    # print(next_val + diffs[-1])
    return next_val + diffs[-1]

next_vals = []
for i in range(len(sets)):
    next_vals.append(findDiff(sets[i], sets[i][-1]))

print("Part 1 (sum of next values in sequences): " + str(sum(next_vals)))

# ~~~~~~~~~~Part 2~~~~~~~~~~~
def findDiff2(num_set, prev_val):
    diffs = []
    for k in range(len(num_set) - 1):
        diff = num_set[k + 1] - num_set[k]
        diffs.append(diff)
    diffs_set = set(diffs)
    # print(diffs)
    if (len(diffs_set) != 1) or 0 not in diffs_set:
        prev_val = findDiff2(diffs, prev_val)
    elif (len(diffs_set) == 1) and 0 in diffs_set:
        # print("Returning " + str(diffs[0]))
        return diffs[0]
    # print(str(prev_val) + " - " + str(diffs[0]) + " = " + str(prev_val - diffs[0]))
    return diffs[0] - prev_val

prev_vals = []
for i in range(len(sets)):
    this_val = findDiff2(sets[i], sets[i][0])
    print("Set " + str(i + 1) + ": " + str(sets[i][0] - this_val))
    print("\n")
    prev_vals.append(sets[i][0] - this_val)

print("Part 2 (sum of previous values in sequences): " + str(sum(prev_vals)))