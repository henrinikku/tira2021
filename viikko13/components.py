class Components:
    def __init__(self, n: int):
        self.parent = {x: x for x in range(1, n + 1)}
        self.size = {x: 0 for x in range(1, n + 1)}
        self.components = n

    def root(self, x: int):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def add_road(self, a: int, b: int):
        a, b = self.root(a), self.root(b)
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]

    def count(self):
        return sum(k == v for k, v in self.parent.items())


if __name__ == "__main__":
    c = Components(5)
    print(c.count())  # 5
    c.add_road(1, 2)
    c.add_road(1, 3)
    print(c.count())  # 3
    c.add_road(2, 3)
    print(c.count())  # 3
    c.add_road(4, 5)
    print(c.count())  # 2
