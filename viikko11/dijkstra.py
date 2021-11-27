import heapq
import random
import timeit
from collections import namedtuple
from typing import Dict, List

Edge = namedtuple("Edge", ["end", "weight"])

N = 5000
INF = 2 ** 63


def dijkstra(edges: Dict[int, List[Edge]], start: int):
    dist = {i: 0 if i == start else INF for i in range(1, N + 1)}
    seen = set()
    heap = [(0, start)]
    while heap:
        __, node = heapq.heappop(heap)
        if node in seen:
            continue

        for edge in edges[node]:
            current = dist[edge.end]
            new = dist[node] + edge.weight
            if new < current:
                dist[edge.end] = new
                heapq.heappush(heap, (new, edge.end))

        seen.add(node)

    return dist


if __name__ == "__main__":
    graph = {
        a: [
            Edge(b, random.randint(1, 1000))
            for b in random.sample(range(1, N + 1), k=N)
            if a < b and b - a < 10
        ]
        for a in random.sample(range(1, N + 1), k=N)
    }
    print("Starting...")
    start = timeit.default_timer()
    res = dijkstra(graph, 1)
    end = timeit.default_timer()
    print(f"Took {end - start} secs")
