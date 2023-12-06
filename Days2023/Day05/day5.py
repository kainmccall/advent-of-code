import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False   # Set to True when testing; set to False for actual problem
filename = "day5"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter="\n\n")

seeds1 = [int(x) for x in data[0].split(": ")[1].split()]

header_indexes = []
maps = []
for i in range(7):
    maps.append([])

for i in range(1, len(data)):
    if data[i][-1] == ":":
        header_indexes.append(i)
header_indexes.append(len(data))

for i in range(len(header_indexes) - 1):
    ind = header_indexes[i] + 1
    while ind < header_indexes[i + 1]:
        map_line = [int(x) for x in data[ind].split()]
        maps[i].append(map_line)
        ind += 1

# ~~~~~~~~~~Part 1~~~~~~~~~~~

def getLocation(seed, maps_list):
    current_val = seed
    for j in range(len(maps_list)):
        notConverted = True
        for k in range(len(maps_list[j])):
            if notConverted and (maps_list[j][k][1] <= current_val < maps_list[j][k][1] + maps_list[j][k][2]):
                diff = maps_list[j][k][0] - maps_list[j][k][1]
                current_val = current_val + diff
                notConverted = False
                break
    return current_val


def getLocations(seeds_list, maps_list):
    locations = []
    for i in range(len(seeds_list)):
        locations.append(getLocation(seeds_list[i], maps_list))
    return locations

locs1 = getLocations(seeds1, maps)
print("Part 1 (minimum location): " + str(min(locs1)))


# ~~~~~~~~~~Part 2~~~~~~~~~~~
# Convert seeds to seed ranges
seed_ranges_2 = []
for i in range(0, len(seeds1) - 1, 2):
    seed_range = [seeds1[i], seeds1[i] + seeds1[i+1] - 1]
    seed_ranges_2.append(seed_range)

def splitConvert(to_convert, map):
    converts = []
    allConverted = False
    while not allConverted:
        sd = to_convert.pop(0)
        isConvertedOrSplit = False
        for i in range(len(map)):
            map_range = [map[i][1], map[i][1] + map[i][2] - 1]
            if map_range[0] <= sd[0] and map_range[1] >= sd[1]: # if current seed range fits completely within a map range, convert it
                # CONVERT, then add to converts
                diff = map[i][0] - map[i][1]
                converts.append([sd[0] + diff, sd[1] + diff])
                isConvertedOrSplit = True
            elif sd[0] < map_range[0] and map_range[0] <= sd[1]:    # if curent seed range intersects with a map range, split it and retry
                # print("(" + str(sd[0]) + ", " + str(sd[1]) + ") -> (" + str(sd[0]) + ", " + str(map_range[0] - 1) + "), (" + str(map_range[0]) + ", " + str(sd[1]) + ")")
                to_convert.append([sd[0], map_range[0] - 1])
                to_convert.append([map_range[0], sd[1]])
                isConvertedOrSplit = True
                break
            elif sd[0] <= map_range[1] and map_range[1] < sd[1]:    # if curent seed range intersects with a map range, split it and retry
                # print("(" + str(sd[0]) + ", " + str(sd[1]) + ") -> (" + str(sd[0]) + ", " + str(map_range[1]) + "), (" + str(map_range[1] + 1) + ", " + str(sd[1]) + ")")
                to_convert.append([sd[0], map_range[1]])
                to_convert.append([map_range[1] + 1, sd[1]])
                isConvertedOrSplit = True
                break
        if not isConvertedOrSplit:  # If current seed range doesn't intersect with any map ranges, keep it as-is and consider it converted
            converts.append([sd[0], sd[1]])
        if len(to_convert) <= 0:    # Stop once all seed ranges have been converted
            allConverted = True
    return converts

# print("Initial Seed Ranges:")
# print(seed_ranges_2)
curr_ranges = seed_ranges_2
for i in range(len(maps)):  # do conversions for each map (seeds to soil, soil to fertilizer, etc.)
    # print("Map Conversion " + str(i+1))
    curr_ranges = splitConvert(curr_ranges, maps[i])
    # print(curr_ranges)

mins = [x[0] for x in curr_ranges] # get minimum value of each range and print the minimum of these minima
print("Part 2 Min Location: " + str(min(mins)))
