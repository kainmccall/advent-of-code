import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day7"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter="\n")

hands_bids_scores = []
hands_bids_scores2 = []
for i in range(len(data)):
    hands_bids_scores.append([data[i].split()[0], int(data[i].split()[1]), 0])
    hands_bids_scores2.append([data[i].split()[0], int(data[i].split()[1]), 0])

# ~~~~~~~~~~Part 1~~~~~~~~~~~
cardVals = {"A":"14", "K":"13", "Q":"12", "J":"11", "T":"10", "9":"09", "8":"08", "7":"07", "6":"06", "5":"05", "4":"04", "3":"03", "2":"02"}
handVals = {"5":"7", "14":"6", "23":"5", "113":"4", "122":"3", "1112":"2", "11111":"1"}

for i in range(len(hands_bids_scores)):
    current_hand = sorted(hands_bids_scores[i][0])
    unique_vals = [1]
    for j in range(len(current_hand) - 1):
        if current_hand[j] == current_hand[j + 1]:
            unique_vals[-1] += 1
        else:
            unique_vals.append(1)
    unique_vals = sorted(unique_vals)
    hand_type_str = ''
    for j in range(len(unique_vals)):
        hand_type_str += str(unique_vals[j])
    hand_score_str = handVals[hand_type_str] + "."
    for j in range(len(hands_bids_scores[i][0])):
        hand_score_str += cardVals[hands_bids_scores[i][0][j]]
    hands_bids_scores[i][2] = float(hand_score_str)

hands_bids_scores.sort(key=lambda x: x[2])

winnings = []
for i in range(len(hands_bids_scores)):
    winnings.append((i + 1) * hands_bids_scores[i][1])

print("Part 1 Sum of All Winnings: " + str(sum(winnings)))


# ~~~~~~~~~~Part 2~~~~~~~~~~~

cardVals2 = {"A":"14", "K":"13", "Q":"12", "J":"00", "T":"10", "9":"09", "8":"08", "7":"07", "6":"06", "5":"05", "4":"04", "3":"03", "2":"02"}

for i in range(len(hands_bids_scores2)):
    current_hand = sorted(hands_bids_scores2[i][0])
    unique_vals = [1]
    unique_cards = current_hand[0]
    for j in range(len(current_hand) - 1):
        if current_hand[j] == current_hand[j + 1]:
            unique_vals[-1] += 1
        else:
            unique_vals.append(1)
            unique_cards += current_hand[j + 1]
    if "J" in unique_cards and (len(unique_cards) > 1):
        num_Js = unique_vals.pop(unique_cards.index("J"))
        unique_vals = sorted(unique_vals)
        unique_vals[-1] += num_Js
    else:
        unique_vals = sorted(unique_vals)
    hand_type_str = ''
    for j in range(len(unique_vals)):
        hand_type_str += str(unique_vals[j])
    hand_score_str = handVals[hand_type_str] + "."
    for j in range(len(hands_bids_scores2[i][0])):
        hand_score_str += cardVals2[hands_bids_scores2[i][0][j]]
    hands_bids_scores2[i][2] = float(hand_score_str)

hands_bids_scores2.sort(key=lambda x: x[2])

winnings2 = []
for i in range(len(hands_bids_scores2)):
    winnings2.append((i + 1) * hands_bids_scores2[i][1])

print("Part 2 Sum of All Winnings: " + str(sum(winnings2)))
