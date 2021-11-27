from collections import namedtuple

INF = 2 ** 63

Edge = namedtuple("Edge", ["start", "end", "weight"])


class Shortening:
    def __init__(self, n: int):
        self.n = n
        self.edges = []

    def add_edge(self, a: int, b: int, x: int):
        self.edges.append(Edge(a, b, x))

    def check(self, a: int, b: int):
        dist = {a: 0}
        laps = 0
        while True:
            laps += 1
            changed = False
            for edge in self.edges:
                if edge.start not in dist:
                    continue
                current = dist.get(edge.end, INF)
                new = dist[edge.start] + edge.weight
                if new < current:
                    if laps >= self.n and edge.end == b:
                        return True
                    changed = True
                    dist[edge.end] = new

            if not changed or laps >= self.n * 2:
                return False


if __name__ == "__main__":
    s = Shortening(5)
    print(s.check(1, 3))  # False
    s.add_edge(1, 2, 5)
    s.add_edge(2, 3, -2)
    print(s.check(1, 3))  # False
    s.add_edge(2, 4, 1)
    s.add_edge(4, 2, -2)
    print(s.check(1, 3))  # True

    s = Shortening(5)
    s.add_edge(5, 3, 4)
    s.add_edge(1, 4, 0)
    s.add_edge(3, 4, 6)
    s.add_edge(4, 1, -9)
    s.add_edge(3, 5, -1)
    print(s.check(1, 4))  # True
    print(s.check(1, 3))  # False
    print(s.check(2, 4))  # False
    s.add_edge(2, 4, 7)
    s.add_edge(5, 4, 3)
    s.add_edge(3, 4, 9)
    s.add_edge(1, 3, -3)
    s.add_edge(5, 2, 4)
    print(s.check(5, 1))
    s.add_edge(2, 1, -4)
    s.add_edge(5, 4, -7)
    s.add_edge(5, 2, -3)
    print(s.check(5, 4))
    s.add_edge(3, 4, 0)
    print(s.check(4, 5))
