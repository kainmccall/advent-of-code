import numpy as np
import Valve as v
from queue import PriorityQueue
import itertools as i
import functools as f
import collections as c

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day16"
run_part_1 = False

# must be larger than 2447 for pt. 2

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter='\n')

valve_dict = {}
tunnels_dict = {}
rate_dict = {}
for ln in data:
    ln_2 = ln.split(';')
    valve_name = ln_2[0].split(' ')[1]
    valve_rate = int(ln_2[0].split(' ')[4].split('=')[1])
    tunnels_to = ln_2[1].split(' ')[5:]
    tunnels_list = []
    for tunnel in tunnels_to:
        tunnels_list.append(tunnel[0:2])
    valve = v.Valve(valve_name, valve_rate, tunnels_list)
    valve_dict[valve_name] = valve
    tunnels_dict[valve_name] = tunnels_list
    rate_dict[valve_name] = valve_rate

# ~~~~~~~~~~Part 1~~~~~~~~~~~
# def dijkstra(v_dict):
#     tunnels_dict = {}
#     rate_dict = {}
#     for vlv in v_dict.keys():
#         tunnels_dict[vlv] = v_dict[vlv].connections
#         rate_dict[v_dict[vlv].name] = v_dict[vlv].flow_rate
#     queue = PriorityQueue()
#     best_paths = {0:0}
#     queue.put((0, 'AA'))
#     num_steps = 0
#     while not queue.empty():
#         rate, test_vlv = queue.get()
#         for vlv in tunnels_dict[test_vlv]:
#             new_rate = rate + (rate_dict[vlv] * (30 - num_steps))
#             print(new_rate)
#             if ((vlv not in best_paths.keys()) or best_paths[vlv] < new_rate):
#                 best_paths[vlv] = new_rate
#                 queue.put((new_rate, vlv))
#                 num_steps += 2
#             else:
#                 num_steps += 1
#     return best_paths
#
# best_valve_paths = dijkstra(valve_dict)
# print(max(best_valve_paths.values()))

# From start point, find shortest distances to all other non-zero-flow points
# Using those distances, calculate (current # steps - distance) * flow rate for each non-zero-flow point
# Choose the highest value among those; if all values are zero, end it (path chosen)
# Along the way, keep track of the total pressure released

#@f.lru_cache(maxsize = None)
def find_shortest_paths(start_v):
    queue = PriorityQueue()
    shortest_paths = {start_v: 0}
    queue.put((0, start_v))
    while not queue.empty():
        dist, vlv = queue.get()
        for adj_vlv in tunnels_dict[vlv]:
            new_dist = dist + 1
            if (adj_vlv not in shortest_paths.keys()) or shortest_paths[adj_vlv] > new_dist:
                shortest_paths[adj_vlv] = new_dist
                queue.put((new_dist, adj_vlv))
    return shortest_paths

# def next_best_flow_rate(start_v, remain_valves, n_steps, depth, distances): # Doesn't take into account the fact that a lower adj rate now could mean a higher one later
#     print("Depth: " + str(depth))
#     if start_v not in distances:
#         distances[start_v] = find_shortest_paths(start_v)
#     valve_distances = distances[start_v]
#     best_adj_rate = 0
#     best_adj_2nd_rate = 0
#     best_vlv = ''
#     new_num_steps = 0
#     for vlv in remain_valves:
#         if vlv != '' and rate_dict[vlv] != 0:
#             adj_rate = (n_steps - valve_distances[vlv] - 1) * rate_dict[vlv]
#             #print("Valve " + vlv + " has adjusted rate " + str(adj_rate))
#             if depth > 0:
#                 remain_valves.remove(vlv)
#                 secondary_vlv, secondary_rate_part, secondary_num_steps, remain_valves, distances = next_best_flow_rate(vlv, remain_valves, n_steps - valve_distances[vlv] - 1, depth - 1, distances)
#                 secondary_rate = adj_rate + secondary_rate_part
#                 remain_valves.append(vlv)
#                 remain_valves.append(secondary_vlv)
#                 if secondary_rate > best_adj_2nd_rate and secondary_num_steps >= 0:
#                     best_adj_2nd_rate = secondary_rate
#                     best_adj_rate = adj_rate
#                     best_vlv = vlv
#                     new_num_steps = n_steps - valve_distances[vlv] - 1
#             elif adj_rate > best_adj_rate:
#                 best_adj_rate = adj_rate
#                 best_vlv = vlv
#                 new_num_steps = n_steps - valve_distances[vlv] - 1
#     #print("Choose valve " + best_vlv)
#     if len(remain_valves) == 0 or best_vlv not in remain_valves:
#         new_num_steps = 0
#     else:
#         print(best_vlv)
#         print(remain_valves)
#         remain_valves.remove(best_vlv)
#     if best_vlv == '':
#         print("ERROR: returning nothing as best valve")
#     return best_vlv, best_adj_rate, new_num_steps, remain_valves, distances

def next_best_flow_rate(start_v, remain_valves, n_steps, current_rate, distances, possible_pressures):
    if start_v not in distances:
        distances[start_v] = find_shortest_paths(start_v)
    valve_distances = distances[start_v]
    if n_steps > 0:
        for vlv in remain_valves:
            adj_rate = (n_steps - valve_distances[vlv] - 1) * rate_dict[vlv]
            remain_valves.remove(vlv)
            next_best_flow_rate(vlv, remain_valves, n_steps - valve_distances[vlv] - 1, current_rate + adj_rate, distances, possible_pressures)
            remain_valves.append(vlv)
    possible_pressures.append(current_rate)


if run_part_1:
    num_steps = 30
    current_valve = 'AA'
    current_total_flow = 0
    remaining_valves = []
    dist_dicts = {}
    pos_press = []
    for vlv in rate_dict.keys():
        if rate_dict[vlv] != 0:
            remaining_valves.append(vlv)
    next_best_flow_rate(current_valve, remaining_valves, num_steps, 0, {}, pos_press)
    print(max(pos_press))


# ~~~~~~~~~~Part 2~~~~~~~~~~~

#def next_best_flow_rate_2(start_v, elep_v, remain_valves, n_steps, elep_steps, current_rate, distances, possible_pressures, human_str, elep_str):
#    #print("Human at " + start_v + '; elephant at ' + elep_v)
#    #print("Human path: " + human_str + '; elephant path: ' + elep_str + '; current total pressure released by end: ' + str(current_rate))
#    if start_v not in distances:
#        distances[start_v] = find_shortest_paths(start_v)
#    valve_distances = distances[start_v]
#    if elep_v not in distances:
#        distances[elep_v] = find_shortest_paths(elep_v)
#    valve_distances_elep = distances[elep_v]
#    if len(remain_valves) >= 2:
#        if n_steps > 0 and elep_steps > 0:
#            valve_permutations = list(i.permutations(remain_valves, 2))
#        elif n_steps > 0:
#            #print('a')
#            valve_permutations = [(remain_valves[x], elep_v) for x in range(0, len(remain_valves))]
#        elif elep_steps > 0:
#            #print('b')
#            valve_permutations = [(start_v, remain_valves[x]) for x in range(0, len(remain_valves))]
#        else:
#            #print('c')
#            valve_permutations = []
#        for vlv_pair in valve_permutations: # 0 is human, 1 is elephant
#            was_in_remains_0 = False
#            was_in_remains_1 = False
#            if vlv_pair[0] in remain_valves:
#                remain_valves.remove(vlv_pair[0])
#                was_in_remains_0 = True
#            # else:
#            #     print('d')
#            if vlv_pair[1] in remain_valves:
#                remain_valves.remove(vlv_pair[1])
#                was_in_remains_1 = True
#            # else:
#            #     print('e')
#            adj_rate_0 = (n_steps - valve_distances[vlv_pair[0]] - 1) * rate_dict[vlv_pair[0]]
#            adj_rate_1 = (elep_steps - valve_distances_elep[vlv_pair[1]] - 1) * rate_dict[vlv_pair[1]]
#            if adj_rate_0 >= 0 and adj_rate_1 >= 0:
#                human_str = human_str + ', ' + vlv_pair[0]
#                elep_str = elep_str + ', ' + vlv_pair[1]
#                next_best_flow_rate_2(vlv_pair[0], vlv_pair[1], remain_valves, n_steps - valve_distances[vlv_pair[0]] - 1, elep_steps - valve_distances_elep[vlv_pair[1]] - 1, current_rate + adj_rate_0 + adj_rate_1, distances, possible_pressures, human_str, elep_str)
#                human_str = human_str[:-4]
#                elep_str = elep_str[:-4]
#            # elif adj_rate_1 >= 0:
#            #     print("ERROR, STOP, human rate < 0 but elephant rate >= 0")
#            # elif adj_rate_0 >= 0:
#            #     print("ERROR, STOP, elephant rate < 0 but human rate >= 0")
#            if was_in_remains_0:
#                remain_valves.append(vlv_pair[0])
#            if was_in_remains_1:
#                remain_valves.append(vlv_pair[1])
#    elif len(remain_valves) == 1:
#        #print("Triggered!")
#        single_remaining_valve = remain_valves[0]
#        human_dist = valve_distances[single_remaining_valve]
#        elep_dist = valve_distances_elep[single_remaining_valve]
#        # print(human_dist)
#        # print(n_steps)
#        # print(elep_dist)
#        # print(elep_steps)
#        if (human_dist <= elep_dist) and (n_steps > 0):
#            #print("Moving human to " + single_remaining_valve)
#            adj_rate = (n_steps - human_dist - 1) * rate_dict[single_remaining_valve]
#            remain_valves.remove(single_remaining_valve)
#            human_str = human_str + ', ' + single_remaining_valve
#            elep_str = elep_str + ', ' + elep_v
#            if adj_rate >= 0:
#                next_best_flow_rate_2(single_remaining_valve, elep_v, remain_valves, n_steps - human_dist - 1, elep_steps - human_dist - 1, current_rate + adj_rate, distances, possible_pressures, human_str, elep_str)
#            remain_valves.append(single_remaining_valve)
#            human_str = human_str[:-4]
#            elep_str = elep_str[:-4]
#        elif (elep_dist < human_dist) and (elep_steps > 0):
#            #print("Moving elephant to " + single_remaining_valve)
#            adj_rate = (elep_steps - elep_dist - 1) * rate_dict[single_remaining_valve]
#            remain_valves.remove(single_remaining_valve)
#            human_str = human_str + ', ' + start_v
#            elep_str = elep_str + ', ' + single_remaining_valve
#            if adj_rate >= 0:
#                next_best_flow_rate_2(start_v, single_remaining_valve, remain_valves, n_steps - elep_dist - 1, elep_steps - elep_dist - 1, current_rate + adj_rate, distances, possible_pressures, human_str, elep_str)
#            remain_valves.append(single_remaining_valve)
#            human_str = human_str[:-4]
#            elep_str = elep_str[:-4]
#        # else:
#        #     print("Moving neither-- both out of steps!")
#    #possible_pressures.append((current_rate, human_str, elep_str))
#    if current_rate > possible_pressures[0][0]:
#        possible_pressures[0] = (current_rate, human_str, elep_str)
#    #print("Appending " + human_str + ' and ' + elep_str + ' = ' + str(current_rate))
#    #make a thing here to also append a string showing the paths both took-- geting too high of an answer for the example!
#
#
#def myFunc(e):
#    return e[:][0]
#
#num_steps = 26
#elephant_steps = 26
#current_valve = 'AA'
#elep_valve = 'AA'
#current_total_flow = 0
#remaining_valves = []
#dist_dicts = {}
#pos_press = [(0, 'aa', 'aa')]
#for vlv in rate_dict.keys():
#    if rate_dict[vlv] != 0:
#        remaining_valves.append(vlv)
#next_best_flow_rate_2('AA', 'AA', remaining_valves, num_steps, elephant_steps, 0, {}, pos_press, 'AA', 'AA')
##pos_press.sort(reverse=True, key=myFunc)
#print(pos_press)
#print("Best Solution:")
#print(pos_press[0])
##print(max(pos_press[:][0]))
    
#@f.lru_cache(maxsize = None)
#def get_total_pressure_release(steps, path):
#    total_press_released = 0
#    for i in range(0, len(path) - 2, 2):
#        node_0 = path[i:i+2]
#        node_1 = path[i+2:i+4]
##    for i in range(0, len(path) - 1):
##        node_0 = path[i]
##        node_1 = path[i+1]
##        if node_0 not in distances:
##            distances[node_0] = find_shortest_paths(node_0)
##        dist = distances[node_0][node_1]
##        dist = find_shortest_paths(node_0)[node_1]
##        steps_req = dist + 1
##        if steps_req > steps:
###            return total_press_released, distances
##            return total_press_released
##        else:
##            steps = steps - steps_req
##            total_press_released += rate_dict[node_1] * steps
#        steps, press_released = get_pressure_release(steps, node_0, node_1)
#        total_press_released += press_released
##    return total_press_released, distances
#    return total_press_released
#
#@f.lru_cache(maxsize = None)
#def get_pressure_release(steps, p1, p2):
#    dist = find_shortest_paths(p1)[p2]
#    steps_req = dist + 1
#    if steps_req > steps:
#        return steps, 0
#    else:
#        steps = steps - steps_req
#        press_released = rate_dict[p2] * steps
#        return steps, press_released
#
#
#steps_to_start = 26
#best_total_pressure = 0
#best_path = ('', '')
#dists = {}
#start_pos = 'AA'
#pos_ct = 0
#total_ct = 1307674400000
#    
#nonzero_valves = []
#for vlv in rate_dict.keys():
#    if rate_dict[vlv] != 0:
#        nonzero_valves.append(vlv)
#
#perms = []
#for ct in range(7, int((len(nonzero_valves)) / 2) + 1):
#    human_paths = list(i.permutations(nonzero_valves, ct))
#    #print(human_paths)
#    for j in range(0, len(human_paths)):
#        #print(human_paths[j])
##        human_path_list = list(human_paths[j])
##        human_path_list.insert(0, start_pos)
#        human_path_list = ''
#        for h in range(0, len(human_paths[j])):
#            human_path_list = human_path_list + str(human_paths[j][h])
##        print(human_path_list)
#        human_path_list = start_pos + human_path_list
##        human_press, dists = get_total_pressure_release(steps_to_start, list(human_path_list), dists)
#        human_press = get_total_pressure_release(steps_to_start, human_path_list)
#        remaining_valves = []
#        for vlv in nonzero_valves:
#            if vlv not in human_paths[j]:
#                remaining_valves.append(vlv)
#        elep_paths = list(i.permutations(remaining_valves, len(nonzero_valves) - ct))
#        for k in range(0, len(elep_paths)):
#            elep_path_list = ''
#            for n in range(0, len(elep_paths[k])):
#                elep_path_list = elep_path_list + str(elep_paths[k][n])
#            elep_path_list = start_pos + elep_path_list
#            #perms.append((human_path_list, elep_path_list))
##            elep_path_list = list(elep_paths[k])
##            elep_path_list.insert(0, start_pos)
##            elep_press, dists = get_total_pressure_release(steps_to_start, list(elep_path_list), dists)
#            elep_press = get_total_pressure_release(steps_to_start, elep_path_list)
#            tot_pres = human_press + elep_press
#            pos_ct += 1
#            if tot_pres > best_total_pressure:
#                best_total_pressure = tot_pres
#                best_path = (human_path_list, elep_path_list)
#                print("New best!")
#                print(best_path)
#                print(best_total_pressure)
#            if pos_ct % 10000000 == 0:
#                print('Another 10 Million down! Percent complete: ' + str(pos_ct / (total_ct / 100)) + '%')
#print(best_path)
#print(best_total_pressure)               

#print(perms)
#print("Got perms! Now, let's compare...")


#def get_total_pressure_release(steps, path, distances):
#    total_press_released = 0
#    for i in range(0, len(path) - 2, 2):
#        node_0 = path[i:i+2]
#        node_1 = path[i+2:i+4]
#        if node_0 not in distances:
#            distances[node_0] = find_shortest_paths(node_0)
#        dist = distances[node_0][node_1]
#        steps_req = dist + 1
#        if steps_req > steps:
#            return total_press_released, distances
#        else:
#            steps = steps - steps_req
#            total_press_released += rate_dict[node_1] * steps
#    return total_press_released, distances
#
#
#steps_to_start = 26
#best_total_pressure = 0
#best_path = ('', '')
#dists = {}
#for perm in perms:
#    human_press, dists = get_total_pressure_release(steps_to_start, perm[0], dists)
#    elep_press, dists = get_total_pressure_release(steps_to_start, perm[1], dists)
#    tot_pres = human_press + elep_press
#    if tot_pres > best_total_pressure:
#        best_total_pressure = tot_pres
#        best_path = perm
#print(best_path)
#print(best_total_pressure)
    
nonzero_flows = {}
for r in rate_dict.keys():
    if rate_dict[r] != 0:
        nonzero_flows[r] = rate_dict[r]
        
valves = set(rate_dict.keys())
dists = c.defaultdict(lambda: 1000)
for vt in tunnels_dict.keys():
    us = tunnels_dict[vt]
    for u in us:
        dists[u, vt] = 1

for k, n, j in i.product(valves, valves, valves):
    dists[n, j] = min(dists[n, j], dists[n,k] + dists[k,j])
    
@f.lru_cache(maxsize = None)
def srch(t, pos='AA', rem_valves=frozenset(nonzero_flows), e=False):
    return max([nonzero_flows[v] * (t-dists[pos,v]-1) + srch(t-dists[pos,v]-1, v, rem_valves-{v}, e) for v in rem_valves if dists[pos,v]<t] + [srch(26, rem_valves=rem_valves) if e else 0])

print(srch(26, e=True))

