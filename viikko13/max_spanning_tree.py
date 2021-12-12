import more_itertools

n = 1000
max_spanning_tree_weight = sum(
    min(edge) for edge in more_itertools.pairwise(range(1, n + 1))
)
print(max_spanning_tree_weight)
