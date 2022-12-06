import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day6"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = str(np.loadtxt(filename, dtype=str))

# ~~~~~~~~~~Part 1~~~~~~~~~~~
unique_index = 0
for i in range(3, len(data)):
    substring = data[i-3:i+1]
    unique_chars = set(substring)
    if len(unique_chars) == 4:
        unique_index = i
        break
    
unique_char = unique_index + 1

print("Unique Character: " + str(unique_char))

# ~~~~~~~~~~Part 2~~~~~~~~~~~

unique_index_2 = 0
for i in range(13, len(data)):
    substring = data[i-13:i+1]
    unique_chars = set(substring)
    if len(unique_chars) == 14:
        unique_index_2 = i
        break
    
unique_char_2 = unique_index_2 + 1

print("Unique Character, pt. 2: " + str(unique_char_2))