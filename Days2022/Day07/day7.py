import numpy as np
import Folder as f
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

use_test_data = False        # Set to True when testing; set to False for actual problem
filename = "day7"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load either test data or input data
if use_test_data:
    filename = filename + "test.txt"
else:
    filename = filename + ".txt"

data = np.genfromtxt(filename, dtype=str, delimiter='\n', skip_header=1) # skip the first "cd /" command

# ~~~~~~~~~~Part 1~~~~~~~~~~~

root_directory = f.Folder("root")

current_folder = root_directory

directories = [root_directory]

for line in data:
    if line[0] =='$':
        if line.split()[1] == 'cd':
            if line.split()[2] == '..':
                current_folder = current_folder.upper_fold
            elif line.split()[2] == '/':
                current_folder = root_directory
            else:
                sub_folder_names = []
                for folder in current_folder.sub_folds:
                    sub_folder_names.append(folder.name)
                for i in range(0, len(sub_folder_names)):
                    if line[5:] == sub_folder_names[i]:
                        current_folder = current_folder.sub_folds[i]
    elif line[0:3] == 'dir':
        new_folder = f.Folder(line[4:])
        new_folder.upper_fold = current_folder
        current_folder.sub_folds.append(new_folder)
        directories.append(new_folder)
    else:
        file_size = float(line.split()[0])
        current_folder.files.append(file_size)

size_sum = 0
for direct in directories:
    size = direct.get_size()
    if size <= 100000:
        size_sum += size

print("Combined File Size for Smaller Files: " + str(size_sum))



# ~~~~~~~~~~Part 2~~~~~~~~~~~

total_used_space = root_directory.get_size()

total_unused_space = 70000000 - total_used_space

space_needed = 30000000 - total_unused_space

all_dir_sizes = []
for direct in directories:
    all_dir_sizes.append(direct.get_size())
all_dir_sizes.sort()

min_dir_size = 0
for i in range(0, len(all_dir_sizes)):
    if all_dir_sizes[i] >=  space_needed:
        min_dir_size = all_dir_sizes[i]
        break

print("Directory Size to Delete for Update: " + str(min_dir_size))