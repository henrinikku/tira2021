import heapq
from typing import List

INF = 2 ** 63


def neighbours(t: List[int], i: int):
    if i - t[i] >= 0:
        yield i - t[i]
    if i + t[i] < len(t):
        yield i + t[i]


def calculate(t: List[int]):
    dist = {i: 0 if i == 0 else INF for i in range(len(t))}
    seen = set()
    heap = [(0, 0)]
    while heap:
        __, node = heapq.heappop(heap)
        if node in seen:
            continue
    
        for neighbour in neighbours(t, node):
            current = dist[neighbour]
            new = dist[node] + t[node]
            if new < current:
                dist[neighbour] = new
                heapq.heappush(heap, (new, neighbour))
    
        seen.add(node)

    out = dist[len(t) - 1]
    return -1 if out == INF else out

if __name__ == "__main__":
    print(calculate([1, 1, 1, 1]))  # 3
    print(calculate([3, 2, 1]))  # -1
    print(calculate([3, 5, 2, 2, 2, 3, 5]))  # 10
    print(calculate([7, 5, 3, 1, 4, 2, 4, 6, 1]))  # 32
