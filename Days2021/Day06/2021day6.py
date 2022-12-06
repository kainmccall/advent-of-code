import numpy as np
import matplotlib.pyplot as plt

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "2021day6"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.loadtxt(filename, dtype=int, delimiter=',')

lanternfish_orig = list([int(x) for x in data])

# ~~~~~~~~~~Part 1~~~~~~~~~~~

lanternfish = lanternfish_orig.copy()
num_days = 80

def spawn_fish(lfish, n_days):
    for day in range(0, n_days):
        for f in range(0, len(lfish)):
            if lfish[f] == 0:
                lfish[f] = int(6)
                lfish.append(int(8))
            else:
                lfish[f] -= 1
    return lfish

final_fish = spawn_fish(lanternfish, num_days)
num_fish = len(final_fish)


print("# Lanternfish after " + str(num_days) + " days: " + str(num_fish))


# ~~~~~~~~~~Part 2~~~~~~~~~~~

lanternfish_2 = lanternfish_orig.copy()
num_days_2 = 256

def fish_count(in_fish, n_days):
    counts = []
    for i in range(0, 9):
        counts.append(0)
    for fish in in_fish:
        counts[fish] += 1
    for day in range(1, n_days + 1):
        num_zeros = counts[0]
        for i in range(1, len(counts)):
            counts[i-1] = counts[i]
        counts[-1] = num_zeros
        counts[6] += num_zeros
    total_fish = sum(counts)
    return total_fish

num_fish_2 = fish_count(lanternfish_2, num_days_2)
print("# Lanternfish after " + str(num_days_2) + " days: " + str(num_fish_2))

