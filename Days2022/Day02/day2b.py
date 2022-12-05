# Column 1 = their move (A = rock (1 pts), B = paper (2 pts), C = scissors (3 pts))
# Column 2 = outcome of game (X = you lose (0 pts), Y = tie (3 pts), Z = you win (6 pts))
# Match Points = movePoints + outcomePoints

import numpy as np

data = np.loadtxt('day2.txt', ndmin=2, dtype=str)
numMatches, numCompetitors = data.shape

#   A B C       A B C
# X S R P     X 3 1 2
# Y R P S --> Y 1 2 3
# Z P S R     Z 2 3 1

mat = [[3, 1, 2], [1, 2, 3], [2, 3, 1]]

totalPoints = 0
for x in range(0, numMatches):
    matchPoints = 0
    movePoints = 0
    outcomePoints = 0
    outInd = 0
    theirMove = data[x][0]
    theirInd = 0
    outcome = data[x][1]
    #Get outcomePoints:
    if outcome == 'Z':
        outcomePoints = 6
        outInd = 2
    elif outcome == 'Y':
        outcomePoints = 3
        outInd = 1
    #Get theirInd:
    if theirMove == 'C':
        theirInd = 2
    elif theirMove == 'B':
        theirInd = 1
    movePoints = mat[outInd][theirInd]
    matchPoints = float(outcomePoints + movePoints)
#    print(data[x][0] + ", " + data[x][1] + ": " + str(outcomePoints) + " outcome pts + " + str(movePoints) + " move pts = " + str(matchPoints))
    totalPoints = totalPoints + matchPoints
print("Total Points: " + str(totalPoints))