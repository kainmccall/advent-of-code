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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_x(cycle_num, input_dx):
    x = 1 + sum(input_dx[0:cycle_num - 1])
    return x

dx = []

for line in data:
    dx.append(0)
    if line[0] == 'addx':
        dx.append(int(line[1]))

x = 1
CRT = []
for i in range(0, len(dx)):
    if int(i % 40) <= x + 1 and int(i % 40) >= x - 1:
        CRT.append('#')
    else:
        CRT.append('.')
    x += dx[i]

def print_CRT(crt):
    print(''.join(crt[0:40]))
    print(''.join(crt[40:80]))
    print(''.join(crt[80:120]))
    print(''.join(crt[120:160]))
    print(''.join(crt[160:200]))
    print(''.join(crt[200:240]))

print_CRT(CRT)

