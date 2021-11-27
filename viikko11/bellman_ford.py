import random
import timeit
from collections import namedtuple
from typing import List

Edge = namedtuple("Edge", ["start", "end", "weight"])

N = 5000
INF = 2 ** 63


def bellman_ford(edges: List[Edge]):
    dist = {i: 1 if i == 1 else INF for i in range(1, N + 1)}
    changed = True
    while changed:
        changed = False
        for edge in edges:
            current = dist[edge.end]
            new = dist[edge.start] + edge.weight
            if new < current:
                changed = True
                dist[edge.end] = new
    return dist


if __name__ == "__main__":
    edges = [
        Edge(a, b, random.randint(1, 1000))
        for a in range(1, N + 1)
        for b in range(1, N + 1)
        if a < b and b - a < 10
    ]
    random.shuffle(edges)
    start = timeit.default_timer()
    res = bellman_ford(edges)
    end = timeit.default_timer()
    print(f"Took {end - start} secs")
