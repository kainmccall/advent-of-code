import numpy as np

data = np.loadtxt('day3.txt', dtype=str)

numSacks = len(data)

letters = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26, "A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52}
allLetters = letters.keys()

pointVals = []
for i in range(0, numSacks):
    sack = data[i]
    comp1 = sack[0:int(len(sack) / 2)]
    comp2 = sack[int(len(sack) / 2):]
    matchingLetter = ''
    for letter in allLetters:
        if (letter in comp1) & (letter in comp2):
            matchingLetter = letter
    pointVals.append(letters[matchingLetter])

print("Total Points, p1: " + str(np.array(pointVals).sum()))

priVals = []
x = 0
while x < numSacks:
    sack1 = data[x]
    sack2 = data[x + 1]
    sack3 = data[x + 2]
    matchingLetter = ''
    for letter in allLetters:
        if (letter in sack1) & (letter in sack2) & (letter in sack3):
            matchingLetter = letter
    priVals.append(letters[matchingLetter])
    x = x + 3

print("Total Points, p2: " + str(np.array(priVals).sum()))