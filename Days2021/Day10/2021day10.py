# Ignore incomplete lines
# First illegal character point values:
#   ) = 3 pts
#   ] = 57 pts
#   } = 1197 pts
#   > = 25137 pts


import numpy as np

data = np.loadtxt('2021day10.txt', dtype=str)

pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

illegalCharScores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

incompleteCharScores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

#openers = ["(", "[", "{", "<"]
#closers = [")", "]", "}", ">"]

openers = pairs.keys()
closers = pairs.values()

numLines = data.shape[0]

totalPoints = 0
incompleteLines = []
for x in range(0, numLines):
    # Determine whether line is incomplete or corrupted
    line = data[x]
    numChars = len(line)
    illegalChar = ''
    isComplete = True
    y = 0
    while y < numChars - 1:
        opener = line[y]
        nextChar = line[y + 1]
        if opener not in openers:
            isComplete = False
            incompleteLines.append(line)
            break #incomplete line
        if nextChar in closers:
            # remove the pair and go back one
            # also check if pair is legal and if not, if it's the first illegal pair, record the illegal character
            if pairs[opener] != nextChar:
                if illegalChar == '':
                    illegalChar = nextChar
            line = line[0 : y : ] + line[y + 2 : : ]
            numChars = len(line)
            #print(line)
            if y != 0:
                #y = y - 1
                y = 0
        else:
            y = y + 1
        if numChars < 2:
            isComplete = False
            incompleteLines.append(line)
            break
    if isComplete & (illegalChar != ''):
        totalPoints = totalPoints + illegalCharScores[illegalChar]
    elif not isComplete or illegalChar == '':
        incompleteLines.append(line)
print("Total Score: " + str(totalPoints))
print("Incomplete lines:")
print(incompleteLines)

completionLines = []

for incompleteLine in incompleteLines:
    completionLine = ''
    for x in range(0, len(incompleteLine)):
        completionLine = pairs[incompleteLine[x]] + completionLine
    completionLines.append(completionLine)

incompletePointsScores = []
for z in range(0, len(completionLines)):
    incompletePoints = 0
    cLine = completionLines[z]
    print(cLine)
    for i in range(0, len(cLine)):
        incompletePoints = (5 * incompletePoints) + incompleteCharScores[cLine[i]]
    incompletePointsScores.append(incompletePoints)

print("Incomplete Points Scores:")
print(incompletePointsScores)

midScore = np.median(np.array(incompletePointsScores))
print("Mid Score: " + str(midScore))



