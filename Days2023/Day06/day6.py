import numpy as np
import math

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day6"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter="\n")

times = data[0].split(": ")[1].split()
distances = data[1].split(": ")[1].split()

# ~~~~~~~~~~Part 1~~~~~~~~~~~
num_solutions = []
for i in range(len(times)):
    T = float(times[i])
    D = float(distances[i])
    zeros = sorted([(T - ((T**2) - (4 * D))**(0.5)) / 2, (T + ((T**2) - (4 * D))**(0.5)) / 2])  # Quadratic equation
    # print(str(math.ceil(zeros[0])) + ", " + str(math.floor(zeros[1])))
    sols = math.floor(zeros[1]) - math.ceil(zeros[0]) + 1
    if math.floor(zeros[1]) == zeros[1] and math.ceil(zeros[0]) == zeros[0]:
        sols -= 2
    num_solutions.append(sols)

# Multiply together total number of solutions for each race
ans = num_solutions[0]
for i in range(1, len(num_solutions), 1):
    ans = ans * num_solutions[i]
print("Part 1 Solution: " + str(ans))

# ~~~~~~~~~~Part 2~~~~~~~~~~~
# Get the two numbers as strings first, then convert them into floats
time = ''
dist = ''
for i in range(len(times)):
    time += times[i]
    dist += distances[i]
T = float(time)
D = float(dist)

# Pretty much copied the following from part 1
zeros = sorted([(T - ((T**2) - (4 * D))**(0.5)) / 2, (T + ((T**2) - (4 * D))**(0.5)) / 2])
sols = math.floor(zeros[1]) - math.ceil(zeros[0]) + 1
if math.floor(zeros[1]) == zeros[1] and math.ceil(zeros[0]) == zeros[0]:
    sols -= 2
print("Part 2 Solution: " + str(sols))