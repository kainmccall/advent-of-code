import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day4"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter="\n")

cards = []
for ln in range(len(data)):
    cards.append([])
    line = data[ln].split(': ')[1]
    winning_nums_str = line.split(' | ')[0].split()
    winning_nums = sorted([int(x) for x in winning_nums_str])
    cards[ln].append(winning_nums)
    my_nums_str = line.split(' | ')[1].split()
    my_nums = sorted([int(x) for x in my_nums_str])
    cards[ln].append(my_nums)

# ~~~~~~~~~~Part 1~~~~~~~~~~~

score = 0
matches_list = []
for cd in range(len(cards)):
    num_matches = -1
    print("Card " + str(cd + 1))
    for num in range(len(cards[cd][1])):
        my_num = cards[cd][1][num]
        winning_ind = 0
        winning_num = cards[cd][0][winning_ind]
        print("Checking for " + str(my_num) + " in winning numbers")
        while my_num >= winning_num and winning_ind < len(cards[cd][0]):
            if my_num == winning_num:
                print("Found " + str(my_num) + " in winning numbers")
                num_matches += 1
            winning_ind += 1
            if winning_ind < len(cards[cd][0]):
                winning_num = cards[cd][0][winning_ind]
    card_score = 0
    if num_matches >= 0:
        card_score = 2**num_matches
    matches_list.append(num_matches + 1)
    score += card_score

print("\n")
print("Part 1 Answer: " + str(score))




# ~~~~~~~~~~Part 2~~~~~~~~~~~

num_cards = [1 for i in range(len(cards))]
for i in range(len(matches_list)):
    num_this_card = num_cards[i]
    for j in range(matches_list[i]):
        if i + j + 1 < len(num_cards):
            num_cards[i + j + 1] += num_this_card

print("\n")
print("Part 2 Answer: " + str(sum(num_cards)))
