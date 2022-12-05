import CumberGrid as cg

grid = cg.CumberGrid("2021day25.txt")

#print("Initial State:")
#grid.printGrid()

step = 0
isUpdated = True

while isUpdated:
    isUpdated = grid.moveCucs()
    step = step + 1
    #print("After Step " + str(step) + ":")
    #grid.printGrid()


print("Step w/No Movement: " + str(step))



