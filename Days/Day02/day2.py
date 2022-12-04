# A = rock
# B = paper
# C = scissors
#
# X = your rock, 1 pts
# Y = your paper, 2 pts
# Z = your scissors, 3 pts
#
# loss = 0 pts, tie = 3 pts, win = 6 pts

import numpy as np

data = np.loadtxt('day2.txt', ndmin=2, dtype=str)

mat = [[3, 0, 6], [6, 3, 0], [0, 6, 3]]

numMatches, numCompetitors = data.shape

totalPoints = 0
for x in range(0, numMatches):
    matchPoints = 0
    yourNum = 0
    compNum = 0
    if data[x][0] == 'A':
        compNum = 0; #rock
    elif data[x][0] == 'B':
        compNum = 1; #paper
    else:
        compNum = 2; #scissors
    if data[x][1] == 'X':
        yourNum = 0; #rock
    elif data[x][1] == 'Y':
        yourNum = 1; #paper
    else:
        yourNum = 2; #scissors
    matchPoints = 1 + yourNum + mat[yourNum][compNum]
#    print(matchPoints)
    totalPoints = totalPoints + matchPoints

print("Total Points: " + str(totalPoints))