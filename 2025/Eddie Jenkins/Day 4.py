# pylint: skip-file
# %% [markdown]
# # AoC 2025 - Day 4

# %%
import numpy as np
from scipy.signal import convolve2d

with open("Data/day4.txt", 'r') as f:
    data = f.read().splitlines()


# %%
input_matrix = np.array([1 if x == '@' else 0 for line in data for x in line])

# Reshape using the known row count from the input data
input_matrix = input_matrix.reshape((len(data), -1))

# %%
window = np.ones((3, 3), dtype=int)
window[1, 1] = 0  # Exclude the center cell

# Part 1
adjacent_counts = convolve2d(input_matrix, window, mode='same', boundary='fill', fillvalue=0)

# Take the hadamard product to get counts only where there are '@' symbols
result_matrix = adjacent_counts * input_matrix

# %%
num_accessible = (result_matrix < 4 * input_matrix).sum()
print(f"Part 1: Number of accessible '@' positions: {num_accessible}")

# %%
# Part 2 - Same thing iteratively until stable. Count how many are removed
current_matrix = input_matrix.copy()
CONVERGED = False
num_removed = 0
while not CONVERGED:
    adjacent_counts = convolve2d(current_matrix, window, mode='same', boundary='fill', fillvalue=0)

    # Take the hadamard product to get counts only where there are '@' symbols
    result_matrix = adjacent_counts * current_matrix

    to_remove = result_matrix < 4 * current_matrix
    num_removed += (result_matrix < 4 * current_matrix).sum()

    current_matrix[to_remove] = 0
    if to_remove.sum() == 0:
        CONVERGED = True

print(f"Part 2: Number of '@' positions removed until stable: {num_removed}")

# %%
