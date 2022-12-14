import numpy as np
import copy as c

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "2021day14"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter='\n')
polymer_string = data[0]
rules_strings = data[1:]

the_rules = {}
for rule in rules_strings:
    new_rule = rule.split(' -> ')
    new_rule[1] = new_rule[0][0] + new_rule[1] + new_rule[0][1]
    the_rules[new_rule[0]] = new_rule[1]

the_rules_2 = {}
pair_counts = {}
for rule in rules_strings:
    new_rule = rule.split(' -> ')
    new_pair_1 = new_rule[0][0] + new_rule[1]
    new_pair_2 = new_rule[1] + new_rule[0][1]
    the_rules_2[new_rule[0]] = [new_pair_1, new_pair_2]
    pair_counts[new_rule[0]] = 0

polymer_1 = []
for i in range(0, len(polymer_string) - 1):
    pair_string = polymer_string[i] + polymer_string[i + 1]
    polymer_1.append(pair_string)

polymer_3 = c.deepcopy(polymer_1)

# ~~~~~~~~~~Part 1~~~~~~~~~~~

def poly_split(poly):
    new_poly = []
    for to_split in poly:
        if len(to_split) == 3:
            pair_1 = to_split[0] + to_split[1]
            pair_2 = to_split[1] + to_split[2]
            new_poly.append(pair_1)
            new_poly.append(pair_2)
        else:
            new_poly.append(to_split)
    return new_poly

def poly_join(poly):
    poly = poly_split(poly)
    poly_string = poly[0]
    for i in range(1, len(poly)):
        poly_string = poly_string + poly[i][1]
    return poly_string

def poly_insert(poly, rules):
    new_poly = []
    for i in range(0, len(poly)):
        pair = poly[i]
        if pair in rules.keys():
            new_poly.append(rules[pair])
        else:
            new_poly.append(pair)
    new_poly = poly_split(new_poly)
    return new_poly


num_steps = 10

for i in range(0, num_steps):
    polymer_1 = poly_insert(polymer_1, the_rules)
polymer_1_string = poly_join(polymer_1)
unique_letters = set(polymer_1_string)
num_appearances = []
for letter in unique_letters:
    num_appearances.append(polymer_1_string.count(letter))

ans = max(num_appearances) - min(num_appearances)
print("Most Common Letter Appearances  minus Least Common Letter Appearances, 10 steps: " + str(ans))

# ~~~~~~~~~~Part 2~~~~~~~~~~~


# def poly_insert_2(poly, rules): # Better than part 1, but still too slow/expensive-- maybe keep track of just the number of pairs instead???
#     new_poly = poly[0]
#     for i in range(1, len(poly)):
#         if poly[i-1:i+1] in rules.keys():
#             new_poly = new_poly + rules[poly[i-1:i+1]][1:3]
#         else:
#             new_poly = new_poly + poly[i]
#     return new_poly
#
#
# num_steps_2 = 40
# polymer_2 = c.deepcopy(polymer_string)
# for i in range(0, num_steps_2):
#     print("Beginning Step " + str(i + 1))
#     polymer_2 = poly_insert_2(polymer_2, the_rules)
# unique_letters_2 = set(polymer_2)
# num_appearances_2 = []
# for letter in unique_letters:
#     num_appearances_2.append(polymer_2.count(letter))
#
# ans_2 = max(num_appearances_2) - min(num_appearances_2)
# print("Most Common Letter Appearances  minus Least Common Letter Appearances, 40 steps: " + str(ans_2))


def poly_insert_3(pairs_ct, rules):
    new_pairs_ct = {}
    for pair in pairs_ct:
        new_pairs_ct[pair] = pairs_ct[pair]
    for pair in pairs_ct:
        pair_occurances = pairs_ct[pair]
        if pair in rules.keys():
            for new_pair in rules[pair]:
                if new_pair in new_pairs_ct.keys():
                    new_pairs_ct[new_pair] += pair_occurances
                else:
                    new_pairs_ct[new_pair] = pair_occurances
            new_pairs_ct[pair] -= pair_occurances
    return new_pairs_ct

num_steps_3 = 40
polymer_3_ct = {}
for pr in polymer_3:
    if pr in polymer_3_ct.keys():
        polymer_3_ct[pr] += 1
    else:
        polymer_3_ct[pr] = 1
for i in range(0, num_steps_3):
    #print("Beginning Step " + str(i + 1))
    polymer_3_ct = poly_insert_3(polymer_3_ct, the_rules_2)

letters_ct = {polymer_string[0]:1, polymer_string[-1]:1}
for pr in polymer_3_ct.keys():
    for ltr in pr:
        if ltr in letters_ct.keys():
            letters_ct[ltr] += polymer_3_ct[pr]
        else:
            letters_ct[ltr] = polymer_3_ct[pr]
for ltr in letters_ct.keys():
    letters_ct[ltr] = int(letters_ct[ltr] / 2)
    #print(ltr + " has count " + str(letters_ct[ltr]))

ans_3 = max(letters_ct.values()) - min(letters_ct.values())
print("Most Common Letter Appearances  minus Least Common Letter Appearances, 40 steps: " + str(ans_3))