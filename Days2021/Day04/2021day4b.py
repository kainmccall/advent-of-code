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

def print_card(card_number):
    for z in range(0, len(cards[card_number])):
        card_string = str(int(cards[card_number][z][0])).zfill(2)
        grid_string = str(call_grid[card_number][z][0]).zfill(1)
        for y in range(1, len(cards[card_number][z])):
            card_string += (" " + str(int(cards[card_number][z][y])).zfill(2))
            grid_string += (" " + str(call_grid[card_number][z][y]).zfill(1))
        print(card_string + "   |   " + grid_string)


# ~~~~~~~~~~Part 2~~~~~~~~~~~
winning_cards = []
call_count = -1
while (len(winning_cards) < num_cards) and call_count + 1 < len(calls):
    call_count += 1
    for card_num in range(0, num_cards):
        for line_num in range(0, len(cards[card_num])):
            for int_num in range(0, len(cards[card_num][line_num])):
                if (int(calls[call_count]) == int(cards[card_num][line_num][int_num]) and int(call_grid[card_num][line_num][int_num]) == 0) and (str(card_num) not in winning_cards):
                    call_grid[card_num][line_num][int_num] += 1
    print(calls[call_count])
    for x in range(len(cards)):
        print_card(x)
        print("--------------------------------")
    # Now, check to see if any cards are won!
    for card_num in range(0, num_cards):
        for line_num in range(0, len(cards[card_num])):
            if ((sum(call_grid[card_num][line_num]) >= len(call_grid[card_num][line_num])) or (sum([row[line_num] for row in call_grid[card_num]]) >= len(call_grid[card_num][line_num]))) and (str(card_num) not in winning_cards):
                winning_cards.append(str(card_num))
                print(str(len(winning_cards)) + " of " + str(num_cards) + " cards won")
                break


sum_board = 0
for i in range(0, len(cards[int(winning_cards[-1])])):
    for j in range(0, len(cards[int(winning_cards[-1])][i])):
        if call_grid[int(winning_cards[-1])][i][j] == 0:
            sum_board += cards[int(winning_cards[-1])][i][j]

score = sum_board * calls[call_count]

print("Last Winning Board:")
print_card(int(winning_cards[-1]))
print("Winning Call: " + str(calls[call_count]))
print("Part 2 Score: " + str(score))