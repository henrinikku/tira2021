INF = 2 ** 63


class Airports:
    def __init__(self, n: int):
        self.n = n
        self.dist = [[a == b for b in range(n)] for a in range(n)]

    def add_link(self, a: int, b: int):
        a, b = a - 1, b - 1
        self.dist[a][b] = True

    def check(self):
        for k in range(self.n):
            for a in range(self.n):
                for b in range(self.n):
                    self.dist[a][b] = self.dist[a][b] or (self.dist[a][k] and self.dist[k][b])

        return all(all(row) for row in self.dist)


if __name__ == "__main__":
    a = Airports(5)
    a.add_link(1, 2)
    a.add_link(2, 3)
    a.add_link(1, 3)
    a.add_link(4, 5)
    print(a.check())  # False
    a.add_link(3, 5)
    a.add_link(1, 4)
    print(a.check())  # False
    a.add_link(5, 1)
    print(a.check())  # True
