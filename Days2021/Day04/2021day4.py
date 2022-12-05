import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "2021day4"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

calls = np.loadtxt(filename, max_rows=1, delimiter=',')
cards_temp = np.loadtxt(filename, skiprows=1)
cards = []
num_cards = int(len(cards_temp) / 5)
call_grid = []
for i in range(1, num_cards + 1):
    cards.append([])
    call_grid.append([])
    cards[i - 1].append(cards_temp[int((5 * i) - 5)].tolist())
    cards[i - 1].append(cards_temp[int((5 * i) - 4)].tolist())
    cards[i - 1].append(cards_temp[int((5 * i) - 3)].tolist())
    cards[i - 1].append(cards_temp[int((5 * i) - 2)].tolist())
    cards[i - 1].append(cards_temp[int((5 * i) - 1)].tolist())
    for j in range(0, 5):
        call_grid[i - 1].append([0, 0, 0, 0, 0])

def print_card(card_num):
    for z in range(0, len(cards[card_num])):
        #card_string = str("{:02d}".format(cards[card_num][z][0]))
        #grid_string = str("{:01d}".format(call_grid[card_num][z][0]))
        card_string = str(int(cards[card_num][z][0])).zfill(2)
        grid_string = str(call_grid[card_num][z][0]).zfill(1)
        for y in range(1, len(cards[card_num][z])):
            card_string += (" " + str(int(cards[card_num][z][y])).zfill(2))
            grid_string += (" " + str(call_grid[card_num][z][y]).zfill(1))
        print(card_string + "   |   " + grid_string)

# ~~~~~~~~~~Part 1~~~~~~~~~~~
winning_card = 0
call_count = -1
for call in calls:
    call_count += 1
    for card_num in range(0, num_cards):
        for line_num in range(0, len(cards[card_num])):
            for int_num in range(0, len(cards[card_num][line_num])):
                #print(cards[card_num][line_num])
                #print(call_grid[card_num][line_num])
                if int(call) == int(cards[card_num][line_num][int_num]) and int(call_grid[card_num][line_num][int_num]) == 0:
                    call_grid[card_num][line_num][int_num] += 1
    # Now, check to see if any cards are won!
    for card_num in range(0, num_cards):
        # Check rows for wins first
        rows_win = False
        for line_num in range(0, len(cards[card_num])):
            if (sum(call_grid[card_num][line_num]) >= len(call_grid[card_num][line_num])) or (sum([row[line_num] for row in call_grid[card_num]]) >= len(call_grid[card_num][line_num])):
                winning_card = card_num
                break
        # for col_num in range(0, len(cards[card_num])):
        #     if sum([row[col_num] for row in call_grid[card_num]]) >= len(call_grid[card_num][col_num]):
        #         winning_card = card_num
        #         break
        else:
            continue
        break
    else:
        continue
    break

sum_board = 0
for i in range(0, len(cards[winning_card])):
    for j in range(0, len(cards[winning_card][i])):
        if call_grid[winning_card][i][j] == 0:
            sum_board += cards[winning_card][i][j]

score = sum_board * calls[call_count]

print_card(winning_card)
print("Winning Call: " + str(calls[call_count]))

print("Part 1 Score: " + str(score))

# ~~~~~~~~~~Part 2~~~~~~~~~~~
# See second file!
