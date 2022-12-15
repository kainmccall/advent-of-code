import numpy as np
from queue import PriorityQueue
import copy as c

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "2021day15"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter='\n')
risk_map = []
for ln in data:
    risk_map.append([int(i) for i in [*ln]])

# ~~~~~~~~~ Part 1 ~~~~~~~~~~

def get_adjacents(r_map):
    adj = {}
    num_cols = len(r_map[0])
    for y in range(0, len(r_map)):
        for x in range(0, num_cols):
            pos = (x, y)
            adj_list = []
            if pos[0] != len(r_map[0]) - 1:
                test_pos = (pos[0] + 1, pos[1])
                test_num = test_pos[0] + (num_cols * test_pos[1])
                adj_list.append(test_num)
            if pos[1] != len(r_map) - 1:
                test_pos = (pos[0], pos[1] + 1)
                test_num = test_pos[0] + (num_cols * test_pos[1])
                adj_list.append(test_num)
            if pos[0] != 0:
                test_pos = (pos[0] - 1, pos[1])
                test_num = test_pos[0] + (num_cols * test_pos[1])
                adj_list.append(test_num)
            if pos[1] != 0:
                test_pos = (pos[0], pos[1] - 1)
                test_num = test_pos[0] + (num_cols * test_pos[1])
                adj_list.append(test_num)
            adj[x + (num_cols * y)] = adj_list
    return adj

def get_risk_list(r_map):
    num_cols = len(r_map[0])
    num_rows = len(r_map)
    risks = [0 for i in range(0, int(num_rows * num_cols))]
    for y in range(0, len(r_map)):
        for x in range(0, num_cols):
            risks[x + (y * num_cols)] = r_map[y][x]
    return risks


def dijkstra(r_map):
    adjacents_dict = get_adjacents(r_map)
    risks = get_risk_list(r_map)
    queue = PriorityQueue()
    least_risky_paths = {0:0}
    queue.put((0, 0))
    while not queue.empty():
        risk, pt = queue.get()
        for adj in adjacents_dict[pt]:
            new_risk = risk + risks[adj]
            if (adj not in least_risky_paths.keys()) or risks[adj] > new_risk:
                least_risky_paths[adj] = new_risk
                queue.put((new_risk, adj))
    return least_risky_paths


risk_paths = dijkstra(risk_map)
print("Risk of Least Risky Path, original grid (pt. 1): " + str(risk_paths[len(risk_map) * len(risk_map[0]) - 1]))

# ~~~~~~~~~~ Part 2 ~~~~~~~~~~~~~~~~~~~~~

def print_risk_map(r_map):
    for ln in r_map:
        ln_str = [str(x) for x in ln]
        print(''.join(ln_str))


risk_map_2_small = c.deepcopy(risk_map)

risk_map_2 = []
for i in range(0, len(risk_map_2_small)):   # create horizontal map extension
    new_line = []
    old_line = risk_map_2_small[i]
    for n in range(0, 5):
        for j in range(0, len(old_line)):
            char = old_line[j] + n
            if char > 9:
                char = char - 9
            new_line.append(char)
    risk_map_2.append(new_line)
lines = risk_map_2[0:len(risk_map_2)]       # create vertical map extension
for n in range(1, 5):
    for ln in lines:
        new_line = [z + n for z in ln]
        for x in range(0, len(new_line)):
            if new_line[x] > 9:
                new_line[x] = new_line[x] - 9
        risk_map_2.append(new_line)

risk_paths_2 = dijkstra(risk_map_2)
print("Risk of Least Risky Path, larger grid (pt. 2): " + str(risk_paths_2[len(risk_map_2) * len(risk_map_2[0]) - 1]))
