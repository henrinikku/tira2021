import heapq
from collections import namedtuple

Buckets = namedtuple("Buckets", ["a", "b"])

INF = 2 ** 63


def neighbours(a: int, b: int, prev: Buckets):
    if prev.a < a:
        yield Buckets(a, prev.b), a - prev.a
    
    if prev.b < b:
        yield Buckets(prev.a, b), b - prev.b
    
    if prev.a > 0:
        yield Buckets(0, prev.b), prev.a
    
    if prev.b > 0:
        yield Buckets(prev.a, 0), prev.b
    
    if prev.a > 0 and prev.b < b:
        new_b = min(b, prev.b + prev.a)
        taken = new_b - prev.b
        yield Buckets(prev.a - taken, new_b), taken

    if prev.b > 0 and prev.a < a:
        new_a = min(a, prev.a + prev.b)
        taken = new_a - prev.a
        yield Buckets(new_a, prev.b - taken), taken


def count(a: int, b: int, x: int):
    seen = set()
    start = Buckets(0, 0)
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        __, buckets = heapq.heappop(heap)
        if buckets in seen:
            continue

        for neighbour, transferred in neighbours(a, b, buckets):
            current = dist.get(neighbour, INF)
            new = dist[buckets] + transferred
            if new < current:
                dist[neighbour] = new
                heapq.heappush(heap, (new, neighbour))

        seen.add(buckets)

    return min([v for k, v in dist.items() if k.a == x] or [-1])


if __name__ == "__main__":
    print(count(5, 4, 2))  # 22
    print(count(4, 3, 2))  # 16
    print(count(3, 3, 1))  # -1
    print(count(10, 9, 8))  # 46
    print(count(123, 456, 42))  # 10530
