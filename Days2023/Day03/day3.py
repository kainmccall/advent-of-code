import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day3"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.loadtxt(filename, dtype='str', comments=None)

gears = []
for i in range(len(data)):
    gears.append([])
    for j in range(len(data[i])):
        gears[i].append([])
print(gears)

engine_sum = 0
for i in range(len(data)):
    print("-------- Line " + str(i + 1) + " --------")
    #print(data[i])
    j = 0
    while j < len(data[i]):
        if data[i][j].isnumeric():
            isNum = True
            numStr = data[i][j]
            currentIndex = j
            while isNum:
                currentIndex = currentIndex + 1
                if currentIndex >= len(data[i]):
                    isNum = False
                    break
                if data[i][currentIndex].isnumeric():
                    numStr = numStr + data[i][currentIndex]
                else:
                    isNum = False
            isPartNum = False
            for x in range(i-1, i+2, 1):
                adjLine = ''
                for y in range(j-1, j+len(numStr)+1, 1):
                    if (0 <= x < len(data)) and (0 <= y < len(data[i])):
                        adjLine = adjLine + data[x][y]
                        #print("x: " + str(x) + "   y: " + str(y) + "  val: " + data[x][y])
                        if (data[x][y].isnumeric() == False) and data[x][y] != ".":
                            isPartNum = True
                            if data[x][y] == "*":
                                gears[x][y].append(int(numStr))
                print(adjLine)
            j = j + len(numStr)
            if isPartNum:
                print("Part Number: " + numStr)
                engine_sum = engine_sum + int(numStr)
            else:
                print(numStr + " is NOT a part number")
        else:
            j = j + 1

print("\n")
print("Part 1 Answer: " + str(engine_sum))

# ~~~~~~~~~~Part 2~~~~~~~~~~~

gears_sum = 0
for i in range(len(gears)):
    for j in range(len(gears[i])):
        if len(gears[i][j]) == 2:
            gears_sum = gears_sum + (gears[i][j][0] * gears[i][j][1])

print("Part 2 Answer: " + str(gears_sum))