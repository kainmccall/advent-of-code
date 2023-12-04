import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False # Set to True when testing; set to False for actual problem
part_2 = True
filename = "day1"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    if part_2:
        filename = filename + "test2.txt"
    else:
        filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.loadtxt(filename, str)

# ~~~~~~~~~~Part 1~~~~~~~~~~~
ans = 0
for i in range(len(data)):
    tensPos = 0
    onesPos = 0
    calibration = 0
    for j in range(len(data[i])):
        if data[i][j].isnumeric():
            tensPos = data[i][j]
            break
    for k in range(-1, -1 * (len(data[i]) + 1), -1):
        if data[i][k].isnumeric():
            onesPos = data[i][k]
            break
    calibration = (int(tensPos) * 10) + int(onesPos)
    # print(calibration)
    ans = ans + calibration


print("Part 1 Answer: " + str(ans))



# ~~~~~~~~~~Part 2~~~~~~~~~~~

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ans2 = 0
for i in range(len(data)):
    #print("Line " + str(i + 1) + ":")
    tensPos2 = 0
    onesPos2 = 0
    calibration2 = 0
    foundTens = False
    foundOnes = False
    #print("Finding 10s place digit...")
    for z in range(len(data[i])):
        #print("Testing " + data[i][z])
        if data[i][z].isnumeric():
            tensPos2 = data[i][z]
            #print("Found matching numeral: " + str(tensPos2))
            foundTens = True
            break
        else:
            for y in range(len(digits)):
                #print("Checking if " + data[i][z:len(digits[y]) + z] + " is a number")
                if data[i][z:len(digits[y]) + z] == digits[y]:
                    tensPos2 = y + 1
                    #print("Found matching number: " + str(tensPos2))
                    foundTens = True
                    break
            if foundTens:
                break
    for x in range(len(data[i]) - 1, -1, -1):
        #print("Testing " + data[i][x])
        if data[i][x].isnumeric():
            onesPos2 = data[i][x]
            #print("Found matching numeral: " + str(onesPos2))
            foundOnes = True
            break
        else:
            for w in range(len(digits)):
                #print("Checking if " + data[i][(x + 1 - len(digits[w])):x + 1] + " is a number")
                if data[i][(x + 1 - len(digits[w])):x + 1] == digits[w]:
                    onesPos2 = w + 1
                    #print("Found matching number: " + str(onesPos2))
                    foundOnes = True
                    break
            if foundOnes:
                break
    calibration2 = (int(tensPos2) * 10) + int(onesPos2)
    print("Line " + str(i + 1) + " Calibration number: " + str(calibration2))
    ans2 = ans2 + calibration2
    print("New sum: " + str(ans2))

print("Part 2 Answer: " + str(ans2))