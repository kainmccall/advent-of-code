import numpy as np
import itertools as i
import functools as f

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day19"
run_part_1 = False
run_part_2 = True
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter='\n')
blueprints = {}
for ln in data:
    parts = ln.split('.')
    num = int(parts[0].split(':')[0].split(' ')[1])
    s1_ore = parts[0].split(' ')[6]
    s2_ore = parts[1].split(' ')[5]
    s3_ore = parts[2].split(' ')[5]
    s3_clay = parts[2].split(' ')[8]
    s4_ore = parts[3].split(' ')[5]
    s4_obs = parts[3].split(' ')[8]
    bluep = [(int(s1_ore), 0, 0, 0), (int(s2_ore), 0, 0, 0), (int(s3_ore), int(s3_clay), 0, 0), (int(s4_ore), 0, int(s4_obs), 0)]
    blueprints[num] = bluep

# ~~~~~~~~~~Part 1~~~~~~~~~~~

# @f.cache
# def decision_bones(num_decisions):
#     return list(i.product(['A', 'B'], repeat=num_decisions))
#
# def get_decisions_lists(bprint):
#     # num_decisions = 0
#     # for i in range(0, len(bprint) - 1):
#     #     for j in range(0, len(bprint[0])):
#     #         if bprint[i][j] != 0:
#     #             num_decisions += 24 // bprint[i][j]
#     num_decisions = 18
#     print(num_decisions)
#     decision_lists = decision_bones(num_decisions)
#     print('Created decision lists!')
#     return decision_lists
#
#
# def simulate(bprint):      # [], [], number minutes         change to recursive with a for loop over new_robots and recurse from there...?
#     decision_lists = get_decisions_lists(bprint)
#     max_robot_cts = [0, 0, 0, 0]
#     best_geodes = 0
#     for i in range(0, len(bprint)):
#         for j in range(0, len(max_robot_cts)):
#             if bprint[i][j] > max_robot_cts[j]:
#                 max_robot_cts[j] = bprint[i][j]
#     #print(max_robot_cts)
#     print(len(decision_lists))
#     for d in range(0, len(decision_lists)):
#         decision_list = decision_lists[d]
#         materials = [0, 0, 0, 0]
#         robots = [1, 0, 0, 0]
#         decision_count = 0
#         for i in range(0, 24):
#             poss_geodes = materials[3] + (((24 - i) * (24 - i + 1)) / 2) + (robots[3]*(24 - i)) - (24 - i)
#             if poss_geodes < best_geodes:
#                 break
#             materials, robots, decision_count = pass_minute(materials, robots, bprint, decision_count, decision_list, max_robot_cts)
#             #print(decision_count)
#         if materials[3] > best_geodes:
#             print('New best geodes: ' + str(materials[3]))
#             best_geodes = materials[3]
#         if d % 100000 == 0:
#             print('Another 100,000 down! ' + str(100 * (d / len(decision_lists))) + '% done.')
#     return best_geodes
#
# def pass_minute(materials, robots, bprint, decision_count, decision_list, max_robot_cts):
#     # Now, check to see if we should build something!
#     # First, check to see if we are above the threshold for each kind of robot
#     # Then, check to see if we have the materials to build that kind of robot
#     # Finally, check to see if the decision_list says we should build it
#     new_robots = [0, 0, 0, 0]
#     if (materials[0] >= bprint[3][0]) and (materials[1] >= bprint[3][1]) and (materials[2] >= bprint[3][2]) and (materials[3] >= bprint[3][3]):
#         new_robots = [0, 0, 0, 1]
#     else:
#         for i in range(0, len(robots) - 1):
#             should_build = True
#             if robots[i] >= max_robot_cts[i]:
#                 should_build = False
#                 #print('b')
#             elif (materials[0] < bprint[i][0]) or (materials[1] < bprint[i][1]) or (materials[2] < bprint[i][2]) or (materials[3] < bprint[i][3]):
#                 should_build = False
#                 #print('c')
#                 #print(materials)
#                 #print(bprint[i])
#             elif robots[i] == 0 and i != 0:
#                 should_build = True
#             else:
#                 #print(decision_count)
#                 if decision_count < len(decision_list) and decision_list[decision_count] == 'B':
#                     should_build = False
#                     #print('d')
#                 decision_count += 1
#             if should_build:
#                 new_robots[i] += 1
#                 break
#     for i in range(0, len(materials)):
#         materials[i] += robots[i]
#     for i in range(0, len(new_robots)):
#         robots[i] += new_robots[i]
#         for k in range(0, len(materials)):
#             materials[k] -= (bprint[i][k] * new_robots[i])
#     return materials, robots, decision_count


def simulate(time, materials, robots, max_robot_cts, bprint, best_geode, current_string, mins):
    if materials[3] > best_geode[0]:
        print("New best geode count: " + str(materials[3]))
        print(current_string)
        print("Time: " + str(time))
        print("Robots: " + str(robots))
        print("Materials: " + str(materials))
        print('\n')
        best_geode[0] = materials[3]
    poss_geodes = materials[3] + (robots[3] * (mins - time)) + (((mins - time) * (mins - time + 1)) / 2) - (mins - time)
    if time < mins and poss_geodes > best_geode[0]:
        time += 1
        new_materials = [0, 0, 0, 0]
        can_build = [True, True, True, True]
        for i in range(0, len(can_build)):
            build_status = True
            for j in range(0, len(materials)):
                #print('Materials: ' + str(materials[j]) + '; blueprint: ' + str(bprint[i][j]))
                if materials[j] < bprint[i][j]:
                    build_status = False
            can_build[i] = build_status
        for i in range(0, len(robots)):
            new_materials[i] = materials[i] + robots[i]
        #now, check if we can build a geode robot; if so, build it! Otherwise, make the other robots if possible, or do nothing.
        if can_build[3]:
            for i in range(0, len(bprint[3])):
                new_materials[i] -= bprint[3][i]
            new_robots = [robots[0], robots[1], robots[2], robots[3] + 1]
            simulate(time, new_materials, new_robots, max_robot_cts, bprint, best_geode, current_string + 'G', mins)
            for i in range(0, len(bprint[3])):
                new_materials[i] += bprint[3][i]
        # elif can_build[2] and robots[2] == 0:
        #     for i in range(0, len(bprint[2])):
        #         new_materials[i] -= bprint[2][i]
        #     new_robots = [robots[0], robots[1], robots[2] + 1, robots[3]]
        #     simulate(time, new_materials, new_robots, max_robot_cts, bprint, best_geode, current_string + 'B', mins)
        #     for i in range(0, len(bprint[2])):
        #         new_materials[i] += bprint[2][i]
        # elif can_build[1] and robots[1] == 0:
        #     for i in range(0, len(bprint[1])):
        #         new_materials[i] -= bprint[1][i]
        #     new_robots = [robots[0], robots[1] + 1, robots[2], robots[3]]
        #     simulate(time, new_materials, new_robots, max_robot_cts, bprint, best_geode, current_string + 'C', mins)
        #     for i in range(0, len(bprint[1])):
        #         new_materials[i] += bprint[1][i]
        else:
            if (robots[2] < max_robot_cts[2]) and can_build[2] and materials[2] < (mins - time + 1) * max_robot_cts[2]:
                for i in range(0, len(bprint[2])):
                    new_materials[i] -= bprint[2][i]
                new_robots = [robots[0], robots[1], robots[2] + 1, robots[3]]
                simulate(time, new_materials, new_robots, max_robot_cts, bprint, best_geode, current_string + 'B', mins)
                for i in range(0, len(bprint[2])):
                    new_materials[i] += bprint[2][i]
            if (robots[1] < max_robot_cts[1]) and can_build[1] and materials[1] < (mins - time + 1) * max_robot_cts[1]:
                for i in range(0, len(bprint[1])):
                    new_materials[i] -= bprint[1][i]
                new_robots = [robots[0], robots[1] + 1, robots[2], robots[3]]
                simulate(time, new_materials, new_robots, max_robot_cts, bprint, best_geode, current_string + 'C', mins)
                for i in range(0, len(bprint[1])):
                    new_materials[i] += bprint[1][i]
            if (robots[0] < max_robot_cts[0]) and can_build[0] and materials[0] < (mins - time + 1) * max_robot_cts[0]:
                for i in range(0, len(bprint[0])):
                    new_materials[i] -= bprint[0][i]
                new_robots = [robots[0] + 1, robots[1], robots[2], robots[3]]
                simulate(time, new_materials, new_robots, max_robot_cts, bprint, best_geode, current_string + 'R', mins)
                for i in range(0, len(bprint[0])):
                    new_materials[i] += bprint[0][i]
            simulate(time, new_materials, robots, max_robot_cts, bprint, best_geode, current_string + 'W', mins)

# def simulate(time, materials, robots, max_robot_cts, bprint, best_geode):
#     print('Materials: ' + str(materials) + '; Robots: ' + str(robots))
#     if materials[3] > best_geode[0]:
#         print("New best geode count: " + str(materials[3]))
#         print("Time: " + str(time))
#         print("Robots: " + str(robots))
#         print("Materials: " + str(materials))
#         best_geode[0] = materials[3]
#     poss_geodes = materials[3] + (robots[3] * (24 - time)) + (((24 - time) * (24 - time + 1)) / 2) - (24 - time)
#     print(time)
#     if time < 24:
#         new_materials = [0, 0, 0, 0]
#         can_build = [True, True, True, True]
#         for i in range(0, len(can_build)):
#             build_status = True
#             for j in range(0, len(materials)):
#                 #print('Materials: ' + str(materials[j]) + '; blueprint: ' + str(bprint[i][j]))
#                 if materials[j] < bprint[i][j]:
#                     build_status = False
#             can_build[i] = build_status
#         print(can_build)
#         for i in range(0, len(robots)):
#             new_materials[i] = materials[i] + robots[i]
#         for z in range(0, len(can_build)):
#             if can_build[z]:
#                 newrob = [0, 0, 0, 0]
#                 temp_new_materials = [new_materials[0], new_materials[1], new_materials[2], new_materials[3]]
#                 for i in range(0, len(bprint[z])):
#                     temp_new_materials[i] -= bprint[z][i]
#                     if i == z:
#                         newrob[i] += 1
#                 new_robots = [robots[0] + newrob[0], robots[1] + newrob[1], robots[2] + newrob[2], robots[3] + newrob[3]]
#                 simulate(time + 1, temp_new_materials, new_robots, max_robot_cts, bprint, best_geode)
#         simulate(time + 1, new_materials, robots, max_robot_cts, bprint, best_geode)

def run_simulation(bprint, mins, **kwargs):
    time = 0
    materials = [0, 0, 0, 0]
    robots = [1, 0, 0, 0]
    max_robot_cts = [0, 0, 0, 0]
    for i in range(0, len(bprint)):
        for j in range(0, len(max_robot_cts)):
            if bprint[i][j] > max_robot_cts[j]:
                max_robot_cts[j] = bprint[i][j]
    # max_robot_cts = [99, 99, 99, 99]
    if 'current_best' in kwargs:
        best_geode = [kwargs['current_best']]
    else:
        best_geode = [0]
    simulate(time, materials, robots, max_robot_cts, bprint, best_geode, '', mins)
    return best_geode[0]



if run_part_1:
    qualities = 0
    minutes = 24

    for blueprint in blueprints.keys():
        # num_geodes = simulate(blueprints[blueprint])
        num_geodes = run_simulation(blueprints[blueprint], minutes)
        print('Num Geodes from ' + str(blueprint) + ': ' + str(num_geodes))
        qualities += (num_geodes * blueprint)

    print('Total Quality Sum: ' + str(qualities))




# ~~~~~~~~~~Part 2~~~~~~~~~~~

#print(run_simulation(blueprints[1], 32))

if run_part_2:
    minutes = 32
    # geodes_1 = run_simulation(blueprints[1], minutes, current_best=1)           # 41
    geodes_1 = 41
    print('Most Geodes from blueprint 1: ' + str(geodes_1))
    print('\n')
    geodes_2 = run_simulation(blueprints[2], minutes, current_best=11)
    print('Most Geodes from blueprint 2: ' + str(geodes_2))
    print('\n')
    geodes_3 = run_simulation(blueprints[3], minutes, current_best=19)
    print('Most Geodes from blueprint 3: ' + str(geodes_3))
    print('\n')
    print("Product of first 3 blueprints at 32 mins: " + str(geodes_1 * geodes_2 * geodes_3))