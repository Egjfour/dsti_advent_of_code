# pylint: skip-file
# %% [markdown]
# # AoC 2025 - Day 3

# %%
import numpy as np

with open("Data/day3.txt", 'r') as f:
    data = f.read().splitlines()


# %%
def identify_max_joltage(record):
    left_nums = np.array(list(record[:-1]), dtype=int) # #exclude the last element
    start_pos = np.argmax(left_nums)

    # exclude everything to the left of start_pos and the start_pos itself
    right_nums = np.array(list(record[start_pos+1:]), dtype=int)
    end_pos = np.argmax(right_nums) + start_pos + 1

    final_num = int(record[start_pos] + record[end_pos])
    return final_num

identify_max_joltage_vec = np.vectorize(identify_max_joltage)
results = identify_max_joltage_vec(data)
print(f"Part 1: Sum of max joltage values: {results.sum()}")

# %%
# Part 2
def identify_max_joltage_pt2(record):
    # List to hold final joltage values
    final_joltage = []

    # For each index, step backwards and change the index to anything >= current value
    for idx in range(12, 0, -1):
        current_index_value = int(record[-idx])
        keep_idx = idx
        remaining_vals = record[-idx::-1]

        keep_char = record[-idx]
        for str_idx, char in enumerate(remaining_vals):
            char_val = int(char)
            if char_val >= current_index_value:
                current_index_value = char_val
                keep_idx = len(remaining_vals) - str_idx - 1
                keep_char = char
        final_joltage.append(keep_char)

        # Remove all values before and including keep_idx
        record = record[keep_idx + 1:]

    return int(''.join(final_joltage))        

identify_max_joltage_pt2_vec = np.vectorize(identify_max_joltage_pt2)
results_pt2 = identify_max_joltage_pt2_vec(data)
print(f"Part 2: Sum of max joltage values after deletion: {results_pt2.sum()}")

# %%
