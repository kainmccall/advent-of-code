import numpy as np
import math

data = np.loadtxt('2021day3.txt', dtype=str)

bitLength = len(data[0])
numRatesCO2 = len(data)
numRatesOx = len(data)

co2Rates = data.copy() #keep least common, equal keep 0
oxRates = data.copy()

#Oxygen (keep most common, equal keep 1)
for x in range(0, bitLength):
    bits = [float(oxRates[y][x]) for y in range(0, numRatesOx)]
    commonDigit = 1
    if (sum(bits)) < float(numRatesOx / 2): #zero is most common
        commonDigit = 0
    oxRates = [z for z in oxRates if float(z[x]) == float(commonDigit)]
    numRatesOx = len(oxRates)

oxRateArray = np.array(list(oxRates[0]), dtype=float)
oxRate = oxRateArray.dot(2**np.arange(oxRateArray.size)[::-1])
print("Oxygen Rate: " + str(oxRate))


#CO2 (keep least common, equal keep 0)
for x in range(0, bitLength):
    bits = [float(co2Rates[y][x]) for y in range(0, numRatesCO2)]
    uncommonDigit = 0
    if numRatesCO2 == 1:
        break
    if (sum(bits)) < float(numRatesCO2 / 2): #one is least common
        uncommonDigit = 1
    co2Rates = [z for z in co2Rates if float(z[x]) == float(uncommonDigit)]
    numRatesCO2 = len(co2Rates)

co2RateArray = np.array(list(co2Rates[0]), dtype=float)
co2Rate = co2RateArray.dot(2**np.arange(co2RateArray.size)[::-1])
print("CO2 Rate: " + str(co2Rate))

lifeRate = oxRate * co2Rate
print("Life Support Rating: " + str(int(lifeRate)))