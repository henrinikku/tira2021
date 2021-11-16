from collections import deque
from typing import Dict, List

AdjacencyMatrix = Dict[int, List[int]]

N = 1000


def count_components(graph: AdjacencyMatrix):
    components = 0
    visited = set()
    for node, neighbours in graph.items():
        if node in visited:
            continue

        queue = deque(neighbours)
        while queue:
            neighbour = queue.popleft()
            if neighbour in visited:
                continue

            visited.add(neighbour)
            queue.extend(graph[neighbour])

        components += 1

    return components


if __name__ == "__main__":
    graph: AdjacencyMatrix = {
        i: [j for j in range(2, N + 1) if i != j and (i % j == 0 or j % i == 0)]
        for i in range(2, N + 1)
    }
    components = count_components(graph)
    print(components)
