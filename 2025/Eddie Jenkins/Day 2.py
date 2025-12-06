# pylint: skip-file
# %% [markdown]
# # AoC 2025 - Day 2

# %%
import numpy as np

with open("Data/day2.txt", 'r') as f:
    data = f.read()

ranges = [list(map(int, line.split('-'))) for line in data.split(',')]

# %%
# Part 1
determine_mirrored_string = np.vectorize(lambda x: 0 if len(x) % 2 == 1 else int(x) if x[int(len(x)/2):] == x[:int(len(x)/2)] else 0)
total_sum = 0
for current_range in ranges:
    arr = current_range_expanded = np.arange(current_range[0], current_range[1] + 1).astype(str)
    mirrored = determine_mirrored_string(arr)
    sum_mirrored = mirrored.sum()
    total_sum += sum_mirrored

print(f"Part 1: Total mirrored numbers in ranges: {total_sum}")

# %%
# Part 2
def find_repeated_substrings(num_str):
    max_window_size = len(num_str) // 2
    for window_size in range(max_window_size, 0, -1):
        # Slide the window over the string. All substrings must match
        first_substring = num_str[0:window_size]
        all_match = True
        for start_idx in range(0, len(num_str), window_size):
            substring = num_str[start_idx:start_idx + window_size]
            if substring != first_substring:
                all_match = False
                break
        if all_match:
            return int(num_str)
    return 0

find_repeated_substrings_vec = np.vectorize(find_repeated_substrings)
total_sum = 0
for current_range in ranges:
    arr = current_range_expanded = np.arange(current_range[0], current_range[1] + 1).astype(str)
    repeated = find_repeated_substrings_vec(arr)
    sum_repeated = repeated.sum()
    total_sum += sum_repeated

print(f"Part 2: Total repeated substring numbers in ranges: {total_sum}")

# %%
