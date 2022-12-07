import numpy as np
import itertools
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "2021day8"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

#data = np.loadtxt(filename, dtype=str, ndmin=1)

f = open(filename, 'r')
data = []
for ln in f.readlines():
    data.append(ln.replace('\n', ''))
f.close()

# ~~~~~~~~~~Part 1~~~~~~~~~~~
# How many 1s (2 seg), 4s (4 seg), 7s (3 seg), and 8s (7 seg) are there in the output?

known_value_lengths = [2, 4, 3, 7]

count = 0
for line in data:
    output_vals = line.split('|')[1].split()
    for val in output_vals:
        if len(val) in known_value_lengths:
            count += 1

print("# of 1's, 4's, 7's, and 8's in output values: " + str(count))

# ~~~~~~~~~~Part 2~~~~~~~~~~~

number_dict = {'abcefg':0, 'cf':1, 'acdeg':2, 'acdfg':3, 'bcdf':4, 'abdfg':5, 'abdefg':6, 'acf':7, 'abcdefg':8, 'abcdfg':9}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

all_tuple_combos = itertools.permutations(letters, 7)

all_combos = []
for combo in all_tuple_combos:
    all_combos.append(list(combo))

def decode_string(input_string, decoder):
    decoded = []
    for i in range(len(input_string)):
        decoded.append(decoder[letters.index(input_string[i])])
    decoded.sort()
    decoded_string = ''.join(decoded)
    return decoded_string

output_sum = 0
for line in data:
    input_vals = line.split('|')[0].split()
    output_vals = line.split('|')[1].split()
    valid_decoder = []
    for combo in all_combos:
        is_valid_decoder = True
        input_counter = 0
        while is_valid_decoder:
            input_decoded = decode_string(input_vals[input_counter], combo)
            if input_decoded not in number_dict.keys():
                is_valid_decoder = False
            elif input_counter == len(input_vals) - 1:
                valid_decoder = combo
                break
            input_counter += 1
        if is_valid_decoder:
            output_list = []
            for val in output_vals:
                output_list.append(str(number_dict[decode_string(val, valid_decoder)]))
            output_num = float(''.join(output_list))
            output_sum += output_num
            break

print("Sum of decoded outputs: " + str(output_sum))