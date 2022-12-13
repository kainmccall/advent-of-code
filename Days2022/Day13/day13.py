import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day13"
debug_print = False
run_part_1 = True
run_part_2 = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter='\n\n')

packet_pairs = []
i = 0
while i < len(data):
    pair = [eval(data[i]), eval(data[i + 1])]
    packet_pairs.append(pair)
    i += 2

packets = []
for ln in data:
    packets.append(eval(ln))

# ~~~~~~~~~~Part 1~~~~~~~~~~~


def compare(left, right, is_solved, results):
    if isinstance(left, int) and isinstance(right, int):
        if debug_print:
            print("Comparing ints " + str(left) + ' and ' + str(right))
        if left < right:
            results.append(True)
            if debug_print:
                print("Correct pair!")
        elif left > right:
            if debug_print:
                print("Incorrect pair!")
            results.append(False)
        else:
            if debug_print:
                print("Ints are the same-- moving on.")
            return False
    elif isinstance(left, list) and isinstance(right, list):
        num_comps = 0
        while is_solved is False:
            if debug_print:
                print("Comparing index " + str(num_comps) + " of the following two lists:")
                print(left)
                print(right)
            if num_comps != 0:
                if (len(left[num_comps - 1:]) == 1) and len(right[num_comps - 1:]) != 1:
                    results.append(True)
                    if debug_print:
                        print("Left has shorter list-- correct pair")
                    break
                elif (len(left[num_comps - 1:]) != 1) and len(right[num_comps - 1:]) == 1:
                    results.append(False)
                    if debug_print:
                        print("Right has shorter list-- incorrect pair")
                    break
                elif (len(left[num_comps - 1:]) == 1) and len(right[num_comps - 1:]) == 1:
                    if debug_print:
                        print("Lists are the same-- moving on")
                    return False
            else:
                if len(left) == 0 and len(right) != 0:
                    results.append(True)
                    if debug_print:
                        print("Left list is empty and right is not-- correct pair")
                    break
                elif len(right) == 0 and len(left) != 0:
                    results.append(False)
                    if debug_print:
                        print("Right list is empty and left is not-- incorrect pair")
                    break
                elif len(right) == 0 and len(left) == 0:
                    if debug_print:
                        print("Both lists are empty-- moving on")
                    return False
            if debug_print:
                print("Proceeding with deeper comparison...")
            is_solved = compare(left[num_comps], right[num_comps], is_solved, results)
            num_comps += 1
            if is_solved:
                break
    elif isinstance(left, int):
        is_solved = compare([left], right, is_solved, results)
        return is_solved
    else:
        is_solved = compare(left, [right], is_solved, results)
        return is_solved


if run_part_1:
    true_nums = []
    sum_res = 0
    num_pairs = len(packet_pairs)
    pairs_with_many_results = []
    for i in range(0, len(packet_pairs)):
        res = []
        compare(packet_pairs[i][0], packet_pairs[i][1], False, res)
        if res[-1]:
            true_nums.append(i + 1)
            if debug_print:
                print("Pair " + str(i + 1) + " is correct.")
        else:
            if debug_print:
                print("Pair " + str(i + 1) + " is incorrect.")
        sum_res += len(res)
        if len(res) > 1:
            pairs_with_many_results.append(i + 1)
    if debug_print:
        print("True pair nums: ")
        print(true_nums)
        print("Num pairs: " + str(num_pairs) + '; num results returned by function: ' + str(sum_res))
        print("Pairs which returned many results:")
        print(pairs_with_many_results)

    print("Sum of True Pair Indexes: " + str(sum(true_nums)))

    # Testing for individual pairs:

    # pair_num = 54
    # res_2 = []
    # compare(packet_pairs[pair_num - 1][0], packet_pairs[pair_num - 1][1], False, res_2)
    # print("Result List:")
    # print(res_2)

# ~~~~~~~~~~Part 2~~~~~~~~~~~

if run_part_2:
    divider_1 = [[2]]
    divider_2 = [[6]]
    packets.append(divider_1)
    packets.append(divider_2)
    packet_order = [i + 1 for i in range(0, len(packets))]
    packets_sorted = False

    while not packets_sorted:
        packets_sorted = True
        packet_switch = []
        for i in range(0, len(packets) - 1):
            res_temp = []
            compare(packets[i], packets[i + 1], False, res_temp)
            if not res_temp[0]:
                packets_sorted = False
                packets[i], packets[i + 1] = packets[i + 1], packets[i]
                packet_order[i], packet_order[i + 1] = packet_order[i + 1], packet_order[i]

    decoder = (packets.index(divider_1) + 1) * (packets.index(divider_2) + 1)
    print("Decoder Value: " + str(decoder))
