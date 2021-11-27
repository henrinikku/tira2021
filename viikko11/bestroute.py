import heapq
from collections import namedtuple

Edge = namedtuple("Edge", ["end", "weight"])
INF = 2 ** 63


class BestRoute:
    def __init__(self, n: int):
        self.n = n
        self.edges = {i: [] for i in range(1, n + 1)}

    def add_road(self, a: int, b: int, x: int):
        self.edges[a].append(Edge(b, x))
        self.edges[b].append(Edge(a, x))

    def find_route(self, a: int, b: int):
        dist = {i: 0 if i == a else INF for i in range(1, self.n + 1)}
        seen = set()
        heap = [(0, a)]
        while heap:
            __, node = heapq.heappop(heap)
            if node in seen:
                continue

            for edge in self.edges[node]:
                current = dist[edge.end]
                new = dist[node] + edge.weight
                if new < current:
                    dist[edge.end] = new
                    heapq.heappush(heap, (new, edge.end))

            seen.add(node)

        return dist[b] if b in seen else -1


if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1, 2, 2)
    print(b.find_route(1, 3))  # -1
    b.add_road(1, 3, 5)
    print(b.find_route(1, 3))  # 5
    b.add_road(2, 3, 1)
    print(b.find_route(1, 3))  # 3
