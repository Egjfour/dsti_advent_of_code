# pylint: skip-file
# %% [markdown]
# # AoC 2025 - Day 7

# %%
import numpy as np

with open("Data/day7.txt", 'r') as f:
    data = f.read().splitlines()

# %%
# Part 1
total_score = 0
x_pos = {data[0].index("S"): "split"}

for row in data[1:]:
    for pos in list(x_pos.keys()):
        if row[pos] == "^":
            x_pos.update({pos - 1: "split", pos + 1: "split"})
            x_pos.pop(pos)
            total_score += 1

print(f"Part 1: Total score after processing all rows: {total_score}")

# %%
# Part 2 - track number of possible unique paths
# For this, we will use a BFS-like approach
from collections import defaultdict

# Initialize a dictionary to track the number of paths at each position
path_counts = defaultdict(int)

# Start with one path at the starting position 'S'
path_counts[data[0].index("S")] = 1

# Process each row of data
for row in data[1:]:
    # Create a new dictionary for the next iteration
    new_path_counts = defaultdict(int)
    
    # For each position that has paths and the count of paths at that position
    for pos, count in path_counts.items():
        # Check if current position has a '^' which causes a split
        if row[pos] == "^":
            # Split: add the path count to both left and right positions
            new_path_counts[pos - 1] += count
            new_path_counts[pos + 1] += count
        else:
            # No split: continue the path count at the same position
            new_path_counts[pos] += count
    
    # Update path_counts for the next row
    path_counts = new_path_counts

# Calculate total unique paths by summing all path counts
total_unique_paths = sum(path_counts.values())
print(f"Part 2: Total unique paths after processing all rows: {total_unique_paths}")

# %%
