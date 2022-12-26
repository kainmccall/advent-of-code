import numpy as np
import sys
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day18"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

sys.setrecursionlimit(2000000000)

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=int, delimiter=',')
cube_coords = []

max_x = 0
max_y = 0
max_z = 0

for coord in data:
    cube_coords.append((coord[0], coord[1], coord[2]))
    if coord[0] > max_x:
        max_x = coord[0]
    if coord[1] > max_y:
        max_y = coord[1]
    if coord[2] > max_z:
        max_z = coord[2]

print("Max x: " + str(max_x))
print("Max y: " + str(max_y))
print("Max z: " + str(max_z))

# ~~~~~~~~~~Part 1~~~~~~~~~~~

surface_area = 0

dx_dy_dz = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
for coord in cube_coords:
    x, y, z = coord
    uncovered_sides = 0
    for i in range(0, len(dx_dy_dz)):
        dx, dy, dz = dx_dy_dz[i]
        if (x + dx, y + dy, z + dz) not in cube_coords:
            uncovered_sides += 1
    surface_area += uncovered_sides

print('Total Surface Area: ' + str(surface_area))


# ~~~~~~~~~~Part 2~~~~~~~~~~~

# Ugh, I feel like I knew this was coming somehow...

inner_surface_area = 0

# using min/max coordinates in each dimension, find all bounded non-cube areas and get the surface area of each one. Subtract those surface areas
# from answer above to get the total outer surface area

# Or, just look at the 3d object from each side in a 2d plane, count the number of squares filled in the 2d grid, and add. We just need
# the first square filled visible from that side--- wait; this only works if the shape is totally convex on the outside... hmmm...

def find_pocket(pos, cubes, points, is_outer, this_pocket):
    print("Exploring pocket containing " + str(pos))
    x, y, z = pos
    # if pos not in this_pocket:
    #     this_pocket.append(pos)
    for i in range(0, len(dx_dy_dz)):
        dx, dy, dz = dx_dy_dz[i]
        adj_pos = (x + dx, y + dy, z + dz)
        if adj_pos not in this_pocket:
            if adj_pos not in points:
                print("This pocket is an outer pocket!")
                is_outer = 'outer'
            elif adj_pos not in cubes:
                this_pocket.append(adj_pos)
                print(len(this_pocket))
                is_outer, this_pocket = find_pocket(adj_pos, cubes, points, is_outer, this_pocket)
            else:
                print("Adjacent point is in a cube!")
    return is_outer, this_pocket

def flood_fill(pos, flooded, points, cubes):
    x, y, z = pos
    for i in range(0, len(dx_dy_dz)):
        dx, dy, dz = dx_dy_dz[i]
        adj_pos = (x + dx, y + dy, z + dz)
        if adj_pos in points:
            if adj_pos not in flooded and adj_pos not in cubes:
                flooded.append(adj_pos)
                print(flooded)
                flood_fill(adj_pos, flooded, points, cubes)




all_coords = []
for x in range(1, max_x + 1):
    for y in range(1, max_y + 1):
        for z in range(1, max_z + 1):
            crd = (x, y, z)
            all_coords.append(crd)

outer_coords = []
pocket_coords = []

flood_fill((1, 1, 1), outer_coords, all_coords, cube_coords)


for coord in all_coords:
    if coord not in cube_coords and coord not in pocket_coords and coord not in outer_coords:
        is_outer, pocket = find_pocket(coord, cube_coords, all_coords, '', [coord])
        for crd in pocket:
            if is_outer == '':
                pocket_coords.append(crd)
            else:
                outer_coords.append(crd)



inner_surface_area = 0
for pckt_crd in pocket_coords:
    x, y, z = pckt_crd
    pocket_surface_area = 0
    for i in range(0, len(dx_dy_dz)):
        dx, dy, dz = dx_dy_dz[i]
        if (x + dx, y + dy, z + dz) in cube_coords:
            pocket_surface_area += 1
    inner_surface_area += pocket_surface_area

outer_surface_area = surface_area - inner_surface_area
print("Outer Surface Area: " + str(outer_surface_area))




