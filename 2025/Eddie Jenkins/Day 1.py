#pylint: skip-file
# %% [markdown]
# # AoC Day 1

# %%
import numpy as np

# %%
def read_input(file_path):
    with open(file_path, 'r') as f:
        data = f.read().splitlines()

    data = [int(i.replace("L", "-").replace("R", "")) for i in data]

    return data

steps = read_input("Data/day1.txt")

# %% [markdown]
# ## Part 1

# %%
def move_idx(arr_max, idx, current_step):
    if current_step > 0:
        new_idx = (idx + current_step) % (arr_max + 1)
    else:
        new_idx = (idx - abs(current_step)) % (arr_max + 1)

    return new_idx

# %%
START_IDX = 50
CURRENT_IDX = START_IDX
VISITED = [CURRENT_IDX]

for step in steps:
    CURRENT_IDX = move_idx(99, CURRENT_IDX, step)
    VISITED.append(CURRENT_IDX)


# %%
print(f"Part 1: Visited position '0' {np.where(np.array(VISITED) == 0, 1, 0).sum()} times")

# %% [markdown]
# # Part 2

# %%
def move_idx_pt2(arr_max, idx, current_step):
    """
    Move index around circular array and count wrap arounds
    """
    wrap_around = 0
    if current_step > 0:
        new_idx = (idx + current_step) % (arr_max + 1)
        if idx + current_step > arr_max:
            num_times = (idx + current_step) // (arr_max + 1)
            wrap_around += num_times
    else:
        new_idx = (idx - abs(current_step)) % (arr_max + 1)
        if idx - abs(current_step) < 0:
            num_times = (idx - abs(current_step)) // (arr_max + 1)
            wrap_around += num_times * -1  # Make positive and add to count
        if new_idx == 0:
            wrap_around += 1  # Special case when landing exactly on 0 from the left
        if idx == 0:
            wrap_around -= 1  # Special case when starting on 0 and moving left
    return new_idx, wrap_around

# %%
START_IDX = 50
CURRENT_IDX = START_IDX
VISITED = [CURRENT_IDX]
WRAP_AROUND = []
NUM_TIMES_PASSED_0 = 0

for step in steps:
    CURRENT_IDX, ct_wrap_around = move_idx_pt2(99, CURRENT_IDX, step)
    VISITED.append(CURRENT_IDX)
    WRAP_AROUND.append(ct_wrap_around)
    NUM_TIMES_PASSED_0 += ct_wrap_around

print(f"Part 2: Passed position '0' {NUM_TIMES_PASSED_0} times")

# %%
