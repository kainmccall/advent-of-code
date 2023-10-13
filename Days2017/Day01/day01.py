import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day1"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str)
#data = str(int(dat))
data = str(data)
print(data)

# ~~~~~~~~~~Part 1~~~~~~~~~~~
sum = 0
for i in range(len(data)):
    print(str(data[i % len(data)]) + ", " + str(data[(i + 1) % len(data)]))
    if int(data[i % len(data)]) == int(data[int(i + 1) % len(data)]):
        sum = sum + int(data[i % len(data)])
print(sum)


# ~~~~~~~~~~Part 2~~~~~~~~~~~
data_len = len(data)
d1 = data[:int(data_len / 2)]
d2 = data[int(data_len / 2):]
sum2 = 0
for i in range(len(d1)):
    if d1[i] == d2[i]:
        sum2 += (int(d1[i]) * 2)

print(sum2)
