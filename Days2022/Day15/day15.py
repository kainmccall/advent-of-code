import numpy as np
import math

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

run_part_1 = False           # Part 1 is not super optimized and takes a little while to run, so I've set it to not run by default
run_part_2 = True          # Part 2 takes a little while to run as well-- when numbers start flying in console, you're through the long part

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day15"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter='\n')

positions = []
for ln in data:
    ln_2 = ln.split(':')
    coord_str_sens = ln_2[0].split(',')
    coord_str_beacon = ln_2[1].split(',')
    sens = (int(coord_str_sens[0].split('=')[1]), int(coord_str_sens[1].split('=')[1]))
    beac = (int(coord_str_beacon[0].split('=')[1]), int(coord_str_beacon[1].split('=')[1]))
    positions.append([sens, beac])

# ~~~~~~~~~~Part 1~~~~~~~~~~~
if run_part_1:
    max_x = 0
    max_y = 0
    min_x = 9999999
    min_y = 9999999
    for ln in positions:
        temp_x_max = max([ln[0][0], ln[1][0]])
        temp_y_max = max([ln[0][1], ln[1][1]])
        temp_x_min = min([ln[0][0], ln[1][0]])
        temp_y_min = min([ln[0][1], ln[1][1]])
        if temp_x_max > max_x:
            max_x = temp_x_max
        if temp_y_max > max_y:
            max_y = temp_y_max
        if temp_x_min < min_x:
            min_x = temp_x_min
        if temp_y_min < min_y:
            min_y = temp_y_min

    signal_ranges = {}
    sig_positions = []
    beac_positions = {}

    for p in range(0, len(positions)):
        pair = positions[p]
        sig_pos = pair[0]
        beac_pos = pair[1]
        sig_positions.append(sig_pos)
        if beac_pos[1] not in beac_positions.keys():
            beac_positions[beac_pos[1]] = []
        if beac_pos[0] not in beac_positions[beac_pos[1]]:
            beac_positions[beac_pos[1]].append(beac_pos[0])
        distance = int(math.fabs(sig_pos[0] - beac_pos[0]) + math.fabs(sig_pos[1] - beac_pos[1]))
        sig_x = sig_pos[0]
        sig_y = sig_pos[1]
        for dy in range(int(-1 * distance), distance + 1):
            if (sig_y + dy) not in signal_ranges.keys():
                signal_ranges[sig_y + dy] = []
            dx = distance - math.fabs(dy)
            row_range = (int(sig_x - dx), int(sig_x + dx + 1))
            signal_ranges[sig_y + dy].append(row_range)


    def get_prohibited_spots(row, sig_ranges):
        range_list = sig_ranges[row]
        all_prohibited_spots = []
        for rg in range_list:
            new_range = range(rg[0], rg[1])
            for num in new_range:
                all_prohibited_spots.append(num)
        unique_prohibited_spots = set(all_prohibited_spots)
        existing_beacon_offset = 0
        if row in beac_positions.keys():
            for x_pos in beac_positions[row]:
                if x_pos in unique_prohibited_spots:
                    existing_beacon_offset += 1
        return (len(unique_prohibited_spots) - existing_beacon_offset)


    if use_test_data:
        test_row = 10
    else:
        test_row = 2000000


    num_no_beacon = get_prohibited_spots(test_row, signal_ranges)
    print("# Spots where no beacons can be: " + str(num_no_beacon))

# ~~~~~~~~~~Part 2~~~~~~~~~~~

if run_part_2:
    if use_test_data:
        test_range = 20
    else:
        test_range = 4000000

    signal_ranges = {}
    for p in range(0, len(positions)):
        pair = positions[p]
        sig_pos = pair[0]
        beac_pos = pair[1]
        distance = int(math.fabs(sig_pos[0] - beac_pos[0]) + math.fabs(sig_pos[1] - beac_pos[1]))
        sig_x = sig_pos[0]
        sig_y = sig_pos[1]
        for dy in range(int(-1 * distance), distance + 1):
            if (sig_y + dy) not in signal_ranges.keys():
                signal_ranges[sig_y + dy] = []
            dx = distance - math.fabs(dy)
            row_range = (int(sig_x - dx), int(sig_x + dx))
            signal_ranges[sig_y + dy].append(row_range)
            signal_ranges[sig_y + dy].sort()
            rg = 0
            num_ranges = len(signal_ranges[sig_y + dy])
            while rg < num_ranges - 1:
                old_rg = signal_ranges[sig_y + dy][rg]
                new_rg = signal_ranges[sig_y + dy][rg + 1]
                if new_rg[0] <= old_rg[1]:
                    if new_rg[1] >= old_rg[1]:
                        signal_ranges[sig_y + dy][rg] = (old_rg[0], new_rg[1])
                    signal_ranges[sig_y + dy].pop(rg + 1)
                    num_ranges -= 1
                else:
                    rg += 1

    distress_pos = (0, 0)
    for y in range(0, test_range + 1): #assumes only 1 possible spot where distress beacon could be; may not work when distress beacon is located on an edge of the search area
        print(y)
        ranges = signal_ranges[y]
        zero_range_ind = 0
        lim_range_ind = 0
        for rg in range(0, len(ranges)):
            if ranges[rg][0] <= 0 <= ranges[rg][1]:
                zero_range_ind = rg
            if ranges[rg][0] <= test_range <= ranges[rg][1]:
                lim_range_ind = rg
        ranges[zero_range_ind] = (0, ranges[zero_range_ind][1])
        ranges[lim_range_ind] = (ranges[lim_range_ind][0], test_range)
        limited_ranges = ranges[zero_range_ind:lim_range_ind + 1]
        if len(limited_ranges) >= 2:
            distress_pos = (int((limited_ranges[0][1] + limited_ranges[1][0]) / 2), y)
            break
    print(distress_pos)

    tuning_freq = (4000000 * distress_pos[0]) + distress_pos[1]

    print("Tuning frequency: " + str(tuning_freq))