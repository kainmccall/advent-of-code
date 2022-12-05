import numpy as np

data = np.loadtxt('2021day3.txt', dtype=str)

bitLength = len(data[0])
numRates = len(data)

commonDigits = []
uncommonDigits = []
for x in range(0, bitLength):
    digitCounter = [0, 0]
    for y in range(0, numRates):
        digit = int(data[y][x])
        digitCounter[digit] = digitCounter[digit] + 1
    if digitCounter[0] > digitCounter[1]:
        commonDigits.append(0)
        uncommonDigits.append(1)
    else:
        commonDigits.append(1)
        uncommonDigits.append(0)

#Convert commonDigits & uncommonDigits to numpy arrays
commonArray = np.array(commonDigits)
uncommonArray = np.array(uncommonDigits)

gammaRate = commonArray.dot(2**np.arange(commonArray.size)[::-1])
epsilonRate = uncommonArray.dot(2**np.arange(uncommonArray.size)[::-1])

powerRate = gammaRate * epsilonRate
print("Power Rate: " + str(powerRate))



