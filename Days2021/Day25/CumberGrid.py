import numpy as np
import SeaCucumber as sc

class CumberGrid:
    def __init__(self, filename):
        data = np.loadtxt(filename, dtype=str)
        maxX = len(data[0])
        maxY = len(data)
        grid = []
        sCucs = []
        eCucs = []
        # create grid
        for i in range(0, maxY):
            grid.append([])
            for j in range(0, maxX):
                grid[i].append(data[i][j])
                if data[i][j] == "v":
                    sCuc = sc.SeaCucumber(j, i, "v")
                    sCucs.append(sCuc)
                elif data[i][j] == ">":
                    eCuc = sc.SeaCucumber(j, i, ">")
                    eCucs.append(eCuc)
        self.grid = grid
        self.sCucs = sCucs
        self.eCucs = eCucs

    def moveCucs(self):
        shape = (len(self.grid), len(self.grid[0]))
        isUpdated = False
        for cuc in self.eCucs:
           cuc.move(shape, self)
        eUpdate = self.updateGrid()
        for cuc in self.sCucs:
            cuc.move(shape, self)
        sUpdate = self.updateGrid()
        if eUpdate or sUpdate:
            isUpdated = True
        return isUpdated

    def updateGrid(self):
        newGrid = []
        for i in range(0, len(self.grid)):
            newGrid.append([])
            for j in range(0, len(self.grid[0])):
                newGrid[i].append(".")
        for cuc in self.eCucs:
            newGrid[cuc.y][cuc.x] = cuc.symbol
        for cuc in self.sCucs:
            newGrid[cuc.y][cuc.x] = cuc.symbol
        isUpdated = self.checkUpdate(newGrid)
        self.grid = newGrid
        return isUpdated

    def checkUpdate(self, newGrid):
        isUpdated = False
        for i in range(0, len(newGrid)):
            for j in range(0, len(newGrid[i])):
                if self.grid[i][j] != newGrid[i][j]:
                    isUpdated = True
                    break
        return isUpdated

    def printGrid(self):
        for ln in self.grid:
            toPrint = ''
            for symb in ln:
                toPrint = toPrint + symb
            print(toPrint)
        print("\n")