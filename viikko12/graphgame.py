from functools import lru_cache


class GraphGame:
    def __init__(self, n: int):
        self.n = n
        self.G = {i: [] for i in range(1, n + 1)}

    def add_link(self, a: int, b: int):
        self.G[a].append(b)
        self.winning.cache_clear()

    @lru_cache(None)
    def winning(self, x: int):
        return any(not self.winning(e) for e in self.G[x])


if __name__ == "__main__":
    g = GraphGame(6)
    g.add_link(3, 4)
    g.add_link(1, 4)
    g.add_link(4, 5)
    print(g.winning(3))  # False
    print(g.winning(1))  # False
    g.add_link(3, 1)
    g.add_link(4, 6)
    g.add_link(6, 5)
    print(g.winning(3))  # True
    print(g.winning(1))  # False
    print(g.winning(2))  # False
