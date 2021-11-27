INF = 2 ** 63


class AllRoutes:
    def __init__(self, n: int):
        self.n = n
        self.dist = [[0 if a == b else INF for b in range(n)] for a in range(n)]

    def add_road(self, a: int, b: int, x: int):
        a, b = a - 1, b - 1
        if x < self.dist[a][b]:
            self.dist[a][b] = x
            self.dist[b][a] = x

    def get_table(self):
        for k in range(self.n):
            for a in range(self.n):
                for b in range(self.n):
                    self.dist[a][b] = min(
                        self.dist[a][b], self.dist[a][k] + self.dist[k][b]
                    )

        return [[-1 if b == INF else b for b in row] for row in self.dist]


if __name__ == "__main__":
    a = AllRoutes(4)
    a.add_road(1, 2, 2)
    a.add_road(1, 3, 5)
    a.add_road(2, 3, 1)
    print(a.get_table())
    # [[0,2,3,-1],[2,0,1,-1],[3,1,0,-1],[-1,-1,-1,0]]
