# pylint: skip-file
# %% [markdown]
# # AoC 2025 - Day 8

# %%
import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import euclidean_distances

# %%
with open("Data/day8.txt", 'r') as f:
    data = f.read().splitlines()
nodes = [np.array(list(map(int, x.split(",")))) for x in data]

# %%
# Calculate distances matrix
distances = euclidean_distances(nodes)
upper_triangular_indices = np.triu_indices_from(distances, k=1)
edges = [(i, j, distances[i, j]) for i, j in zip(*upper_triangular_indices)]

# Sort edges ascending by weight
edges.sort(key=lambda x: x[2], reverse=False)

# Connections
NUM_CONNECT = 1000
edges_to_add = edges[:NUM_CONNECT]

# Build graph
G = nx.Graph()
G.add_weighted_edges_from(edges_to_add)


# %%
# Get number of elements in each connected component
connected_components = list(nx.connected_components(G))
component_sizes = [len(component) for component in connected_components]

grand_total = 1
for size in sorted(component_sizes)[-3:]:
    grand_total *= size
print(f"Part 1: Total circuit sizes: {grand_total}")

# %%
# Part 2 - make connections until all nodes are connected
G = nx.Graph()
G.add_nodes_from(range(len(nodes)))
for i, j, weight in edges:
    G.add_edge(i, j, weight=weight)
    if nx.is_connected(G):
        print(f"Part 2: Total connections made: {G.number_of_edges()}")
        final_i = i
        final_j = j
        break
solution = nodes[final_i][0] * nodes[final_j][0]
print(f"Part 2: Solution value: {solution}")

# %%
