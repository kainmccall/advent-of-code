import numpy as np

strData = np.loadtxt('2021day5.txt', dtype=str)

allPoints = []
for line in strData:
    pt1 = (int(line[0].split(',')[0]), int(line[0].split(',')[1]))
    pt2 = (int(line[2].split(',')[0]), int(line[2].split(',')[1]))
    allPoints.append([pt1, pt2])

straightLines = []
diagLines = []
maxX = 0
maxY = 0
for ln in allPoints:
    x1, y1 = ln[0]
    x2, y2 = ln[1]
    if x1 == x2 or y1 == y2:
        straightLines.append(ln)
    else:
        diagLines.append(ln)
    if x1 > maxX:
        maxX = x1
    if x2 > maxX:
        maxX = x2
    if y1 > maxY:
        maxY = y1
    if y2 > maxY:
        maxY = y2

grid = np.zeros((maxY + 1, maxX + 1))

for ln in straightLines:
    x1, y1 = ln[0]
    x2, y2 = ln[1]
    if x1 == x2:
        startY = min([y1, y2])
        stopY = max([y1, y2])
        for i in range(startY, stopY + 1):
            grid[i][x1] = grid[i][x1] + 1
    else:
        startX = min([x1, x2])
        stopX = max([x1, x2])
        for i in range(startX, stopX + 1):
            grid[y1][i] = grid[y1][i] + 1

totalStrIntPoints = 0
for i in range(0, maxY + 1):
    for j in range(0, maxX + 1):
        if grid[i][j] > 1:
            totalStrIntPoints = totalStrIntPoints + 1

print("Total Intersecting Points in Straight Lines: " + str(totalStrIntPoints))

# Now, plot the diagonal lines
for ln in diagLines:
    x1a, y1a = ln[0]
    x2a, y2a = ln[1]
    #make sure x2 > x1 (always increment x from x1 to x2)
    if x1a > x2a:
        x1 = x2a
        y1 = y2a
        x2 = x1a
        y2 = y1a
    else:
        x1 = x1a
        y1 = y1a
        x2 = x2a
        y2 = y2a
    x = x1
    y = y1
    if y2 > y1:
        while x <= x2 and y <= y2:
            grid[y][x] = grid[y][x] + 1
            x = x + 1
            y = y + 1
    else:
        while x <= x2 and y >= y2:
            grid[y][x] = grid[y][x] + 1
            x = x + 1
            y = y - 1


totalIntPoints = 0
for y in range(0, maxY + 1):
    for x in range(0, maxX + 1):
        if grid[y][x] > 1:
            totalIntPoints = totalIntPoints + 1

print("Total Intersecting Points: " + str(totalIntPoints))
