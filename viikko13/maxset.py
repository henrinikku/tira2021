class MaxSet:
    def __init__(self, n: int):
        self.parent = {x: x for x in range(1, n + 1)}
        self.size = {x: 1 for x in range(1, n + 1)}
        self.max = 1

    def root(self, x: int):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def merge(self, a: int, b: int):
        a, b = self.root(a), self.root(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.max = max(self.size[a], self.max)

    def get_max(self):
        return self.max


if __name__ == "__main__":
    m = MaxSet(5)
    print(m.get_max())  # 1
    m.merge(1, 2)
    m.merge(3, 4)
    m.merge(3, 5)
    print(m.get_max())  # 3
    m.merge(1, 5)
    print(m.get_max())  # 5
    m = MaxSet(5)
    m.merge(4, 5)
    m.merge(2, 3)
    print(m.get_max())
    print(m.get_max())
    m.merge(4, 5)
    m.merge(3, 4)
    m.merge(2, 5)
    m.merge(4, 5)
    print(m.get_max())  # 4
    m.merge(3, 4)
