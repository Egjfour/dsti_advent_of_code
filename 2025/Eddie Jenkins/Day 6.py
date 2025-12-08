# pylint: skip-file
# %% [markdown]
# Day 6 - AoC 2025

# %%
import numpy as np

with open("Data/day6.txt", 'r') as f:
    data = f.read().splitlines()

# %%
# First, we will find the separator columns
# Create a boolean array - True is any space character
space_bool_array = np.array([[char == ' ' for char in line] for line in data])

# Get the column sums
col_sums = space_bool_array.sum(axis=0)

# Separator columns are those where all rows are spaces
separator_cols = np.where(col_sums == space_bool_array.shape[0])[0]

# %%
# Now, we can split into the columns
parsed_data = []
start_idx = 0
for sep_idx in separator_cols:
    column_data = [line[start_idx:sep_idx].strip() for line in data]
    parsed_data.append(column_data)
    start_idx = sep_idx + 1

# Append the last column after the final separator
column_data = [line[start_idx:].strip() for line in data]
parsed_data.append(column_data)

# %%
# Part 1
def process_column(col_vals):
    operator = col_vals[-1]
    numbers = [int(x) for x in col_vals[:-1] if x.isdigit()]

    if operator == '+':
        return sum(numbers)
    elif operator == '*':
        result = 1
        for num in numbers:
            result *= num
        return result
    
results = [process_column(col) for col in parsed_data]
print(f"Part 1: Results total: {sum(results)}")

# %%
# Part 2

# Need to re-parse data without stripping spaces so we can deal w/ column alignment
parsed_data = []
start_idx = 0
for sep_idx in separator_cols:
    column_data = [line[start_idx:sep_idx] for line in data]
    parsed_data.append(column_data)
    start_idx = sep_idx + 1
# Append the last column after the final separator
column_data = [line[start_idx:] for line in data]
parsed_data.append(column_data)

# %%
def process_column_pt2(col_vals):
    operator = col_vals[-1].strip()
    numbers = col_vals[:-1]
    
    # Let's first split into individual characters
    num_rows = len(numbers)
    char_lists = [list(num_str) for num_str in numbers]

    # Convert to matrix and transpose
    char_matrix = np.array(char_lists).T
    transposed_chars = [''.join(row).strip() for row in char_matrix]

    if operator == '+':
        total = 0
        for num_str in transposed_chars:
            if num_str.isdigit():
                total += int(num_str)
        return total
    elif operator == '*':
        result = 1
        for num_str in transposed_chars:
            if num_str.isdigit():
                result *= int(num_str)
        return result
results_pt2 = [process_column_pt2(col) for col in parsed_data]
print(f"Part 2: Results total: {sum(results_pt2)}")

# %%
