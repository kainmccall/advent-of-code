import numpy as np
import math

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day10"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data_temp = np.genfromtxt(filename, dtype=str, delimiter='\n')
data = []
for ln in data_temp:
    if ln == 'noop':
        data.append(['noop', '0'])
    else:
        data.append(ln.split())

# ~~~~~~~~~~Part 1~~~~~~~~~~~

def get_signal_strength(cycle_num, input_dx):
    x = 1 + sum(input_dx[0:cycle_num - 1])
    sig_strength = float(x * cycle_num)
    print("During cycle " + str(cycle_num) + ", X = " + str(x) + "; signal strength = " + str(sig_strength))
    return sig_strength

num_cycles = [20, 60, 100, 140, 180, 220]

dx = []

for line in data:
    dx.append(0)
    if line[0] == 'addx':
        dx.append(int(line[1]))


sum_signal = 0
for num in num_cycles:
    sum_signal += get_signal_strength(num, dx)

print("Signal Strength Sum: " + str(sum_signal))


