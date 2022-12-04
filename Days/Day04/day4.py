import numpy as np

data = np.loadtxt('day4.txt', dtype=str)

coords = []

numRedundant = 0
numPartiallyRedundant = 0
for ln in data:
    coordPairs1, coordPairs2 = ln.split(',')
    a1t, b1t = coordPairs1.split('-')
    a2t, b2t = coordPairs2.split('-')
    a1t = int(a1t)
    b1t = int(b1t)
    a2t = int(a2t)
    b2t = int(b2t)
    if a1t > a2t:
        a1 = a2t
        b1 = b2t
        a2 = a1t
        b2 = b1t
    else:
        a1 = a1t
        b1 = b1t
        a2 = a2t
        b2 = b2t
    coords.append([a1, b1, a2, b2])
    if a1 <= a2 and b1 >= b2:
        numRedundant = numRedundant + 1
    elif a2 <= a1 and b2 >= b1:
        numRedundant = numRedundant + 1
    if b1 >= a2 and b1 <= b2:
        numPartiallyRedundant = numPartiallyRedundant + 1
    elif a2 >= a1 and a2 <= b1:
        numPartiallyRedundant = numPartiallyRedundant + 1

print("Number Completely Covered Shifts: " + str(numRedundant))

print("Number Partially Covered Shifts: " + str(numPartiallyRedundant))


