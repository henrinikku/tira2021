from functools import lru_cache
from typing import Tuple


Point = Tuple[int, int]


class WallGrid:
    def __init__(self, n: int):
        self.n = n
        self.size = {}
        self.parent = {}

    def remove(self, x: int, y: int):
        point: Point = (x, y)
        if point in self.size:
            return

        self.size[point] = 1
        self.parent[point] = point

        for diff_x, diff_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            adjacent_point: Point = (x + diff_x, y + diff_y)
            if adjacent_point in self.size:
                self.connect(point, adjacent_point)

        self.count.cache_clear()

    @lru_cache(1)
    def count(self):
        return sum(k == v for k, v in self.parent.items())

    def root(self, x: Point):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def connect(self, a: Point, b: Point):
        a, b = self.root(a), self.root(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]


if __name__ == "__main__":
    w = WallGrid(5)
    print(w.count())  # 0
    w.remove(2, 2)
    w.remove(4, 2)
    print(w.count())  # 2
    w.remove(3, 2)
    print(w.count())  # 1
    w.remove(2, 4)
    w.remove(2, 4)
    w.remove(4, 4)
    print(w.count())  # 3
    w.remove(3, 3)
    print(w.count())  # 3
    w.remove(3, 4)
    print(w.count())  # 1
