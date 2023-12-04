import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day2"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter="\n")
color_dict = { "red": 0, "green": 1, "blue": 2 }
games = []
for i in range(len(data)):
    game = []
    game_string = data[i].split(": ")[1]
    rounds = game_string.split("; ")
    for j in range(len(rounds)):
        round_score = [0, 0, 0]
        color_strings = rounds[j].split(", ")
        for k in range(len(color_strings)):
            num_color = color_strings[k].split(" ")
            num = num_color[0]
            color = num_color[1]
            round_score[color_dict[color]] = int(num)
        game.append(round_score)
    games.append(game)

# ~~~~~~~~~~Part 1~~~~~~~~~~~

max_cubes = [12, 13, 14]
game_sum = 0
for i in range(len(games)):
    game_num = i + 1
    isPossible = True
    for j in range(len(games[i])):
        if isPossible:
            for k in range(len(games[i][j])):
                if games[i][j][k] > max_cubes[k]:
                    isPossible = False
                    print("Game " + str(game_num) + " is not possible.")
                    break
    if isPossible:
        game_sum = game_sum + game_num
        print("Game " + str(game_num) + " is possible.")

print("\n")
print("Part 1 Answer: " + str(game_sum))

# ~~~~~~~~~~Part 2~~~~~~~~~~~

power_sum = 0
for i in range(len(games)):
    max_colors = [0, 0, 0]
    for j in range(len(games[i])):
        for k in range(len(games[i][j])):
            if games[i][j][k] > max_colors[k]:
                max_colors[k] = games[i][j][k]
    power = max_colors[0] * max_colors[1] * max_colors[2]
    power_sum = power_sum + power

print("\n")
print("Part 2 Answer: " + str(power_sum))