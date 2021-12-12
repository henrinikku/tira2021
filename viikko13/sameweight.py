from typing import List, Tuple


class SameWeight:
    def __init__(self, n: int):
        self.n = n
        self.edges = []

    def add_edge(self, a: int, b: int, x: int):
        self.edges.append((x, a, b))

    def check(self):
        return self.kruskal(sorted(self.edges)) == self.kruskal(
            sorted(self.edges, reverse=True)
        )

    def root(self, x: int):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def connect(self, a: int, b: int):
        a, b = self.root(a), self.root(b)
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]

    def kruskal(self, edges: List[Tuple[int, int, int]]):
        self.parent = {x: x for x in range(1, self.n + 1)}
        self.size = {x: 0 for x in range(1, self.n + 1)}

        total_cost = 0
        while edges:
            x, a, b = edges.pop()
            if self.root(a) != self.root(b):
                total_cost += x
                self.connect(a, b)

        if sum(k == v for k, v in self.parent.items()) > 1:
            return -1

        return total_cost


if __name__ == "__main__":
    s = SameWeight(4)
    s.add_edge(1, 2, 2)
    s.add_edge(1, 3, 3)
    print(s.check())  # True
    s.add_edge(1, 4, 3)
    print(s.check())  # True
    s.add_edge(3, 4, 3)
    print(s.check())  # True
    s.add_edge(2, 4, 1)
    print(s.check())  # False
