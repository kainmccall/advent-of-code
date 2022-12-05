import numpy as np

data = np.loadtxt('day5.txt', dtype=str) #load instructions

test_initial_state = ['ZN', 'MCD', 'P']
input_initial_state = ['ZPMHR', 'PCJB', 'SNHGLCD', 'FTMDQSRL', 'FSPQBTZM', 'TFSZBG', 'NRV', 'PGLTDVCM', 'WQNJFML']

boxes_state = input_initial_state.copy()

for line in data:
    for i in range(0, int(line[1])):
        moving_letter = boxes_state[int(line[3]) - 1][-1]
        boxes_state[int(line[3]) - 1] = boxes_state[int(line[3]) - 1][:-1]
        boxes_state[int(line[5]) - 1] = boxes_state[int(line[5]) - 1] + moving_letter

print("Top Boxes, CrateMover 9000:")
for stack in boxes_state:
    print(stack[-1])


#Part 2:
    
boxes_state_9001 = input_initial_state.copy()

for line in data:
    #print(str(int(-1*int(line[1]))))
    moving_letters = boxes_state_9001[int(line[3]) - 1][int(-1*int(line[1])):]
    boxes_state_9001[int(line[3]) - 1] = boxes_state_9001[int(line[3]) - 1][:int(-1*int(line[1]))]
    boxes_state_9001[int(line[5]) - 1] = boxes_state_9001[int(line[5]) - 1] + moving_letters

print("Top Boxes, CrateMover 9001:")
for stack in boxes_state_9001:
    print(stack[-1])