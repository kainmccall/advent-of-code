import numpy as np
import math

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "2021day7"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.loadtxt(filename, dtype=int, delimiter=',')

# ~~~~~~~~~~Part 1~~~~~~~~~~~

num_positions = max(data) + 1
fuel_costs = []

for min_pos in range(0, num_positions):
    fuel_cost = 0
    for pos in data:
        fuel = math.fabs(pos - min_pos)
        fuel_cost += fuel
    fuel_costs.append(fuel_cost)

min_fuel = min(fuel_costs)
min_pos = fuel_costs.index(min_fuel)

print("Minimum Fuel: " + str(min_fuel))


# ~~~~~~~~~~Part 2~~~~~~~~~~~

fuel_costs_2 = []

for min_pos in range(0, num_positions):
    fuel_cost = 0
    for pos in data:
        fuel_num = math.fabs(pos - min_pos)
        fuel = ((fuel_num**2) + fuel_num) / 2
        fuel_cost += fuel
    fuel_costs_2.append(fuel_cost)

min_fuel_2 = min(fuel_costs_2)
min_pos_2 = fuel_costs_2.index(min_fuel_2)

print("Minimum Fuel, pt.2: " + str(min_fuel_2))