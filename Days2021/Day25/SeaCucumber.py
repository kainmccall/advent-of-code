class SeaCucumber:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
        if self.symbol == "v":
            self.isSouth = True
        else:
            self.isSouth = False


    def move(self, shape, grid):
        maxY, maxX = shape
        if self.canMove(shape, grid):
            if self.isSouth:
                self.y = (self.y + 1) % maxY
            else:
                self.x = (self.x + 1) % maxX

    def canMove(self, shape, grid):
        maxY, maxX = shape
        canMove = False
        #print("Current Cumber Coords: (" + str(self.x) + ", " + str(self.y) + ")")
        if self.isSouth:
            #print("Target Cumber Coords: (" + str(self.x) + ", " + str((self.y + 1) % maxY) + ")")
            if grid.grid[(self.y + 1) % maxY][self.x] == '.':
                canMove = True
        else:
            #print("Target Cumber Coords: (" + str((self.x + 1) % maxX) + ", " + str(self.y))
            if grid.grid[self.y][(self.x + 1) % maxX] == '.':
                canMove = True
        return canMove