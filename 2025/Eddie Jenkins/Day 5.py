# pylint: skip-file
# %% [markdown]
# # AoC 2025 - Day 5

# %%
import numpy as np

with open("Data/day5.txt", 'r') as f:
    ranges, ingredients = f.read().split("\n\n")
    ranges = ranges.splitlines()
    ingredients = ingredients.splitlines()

    ranges = [(int(range_part.split('-')[0]), int(range_part.split('-')[1])) for
                range_part in ranges]

range_starts = np.array([r[0] for r in ranges])
range_ends = np.array([r[1] for r in ranges])

# Sort the starts and make sure the ends follow
sorted_indices = np.argsort(range_starts)
range_starts = range_starts[sorted_indices]
range_ends = range_ends[sorted_indices]

# Collapse overalpping ranges
collapsed_ranges = []
current_start = range_starts[0]
current_end = range_ends[0]
for start, end in zip(range_starts[1:], range_ends[1:]):
    if start <= current_end:
        current_end = max(current_end, end)
    else:
        collapsed_ranges.append((current_start, current_end))
        current_start = start
        current_end = end
collapsed_ranges.append((current_start, current_end))

# Compress to a flattened array
collapsed_ranges_flat = np.array(collapsed_ranges).flatten()

# %%
# Part 1
def is_ingredient_fresh(ingredient, ranges_array):
    ingredient_val = int(ingredient)

    # We find how many range values are <= ingredient_val
    num_lower = np.where(ranges_array < ingredient_val, 1, 0).sum()

    # If num_lower is odd, ingredient is fresh
    return num_lower % 2 == 1 | (ranges_array == ingredient_val).any()

is_ingredient_fresh_vec = np.vectorize(is_ingredient_fresh, excluded=['ranges_array'])
freshness_results = is_ingredient_fresh_vec(ingredients, ranges_array=collapsed_ranges_flat)
num_fresh = freshness_results.sum()
print(f"Part 1: Number of fresh ingredients: {num_fresh}")

# %%
# Part 2
total_fresh_ingredients = np.array([x[1] - x[0] + 1 for x in collapsed_ranges]).sum()
print(f"Part 2: Total number of fresh ingredients in all ranges: {total_fresh_ingredients}")

# %%
