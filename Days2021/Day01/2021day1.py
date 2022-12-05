import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "2021day1"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.loadtxt(filename)

# ~~~~~~~~~~Part 1~~~~~~~~~~~

increased_count = 0
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        increased_count += 1

print("Number of increases: " + str(increased_count))

# ~~~~~~~~~~Part 2~~~~~~~~~~~

# Since in each window, 2 measurements will always be equal, we only need to worry about the 2 unequal measurements
increased_window_count = 0
for i in range(3, len(data)):
    if data[i] > data[i-3]:
        increased_window_count += 1

print("Number of window increases: " + str(increased_window_count))