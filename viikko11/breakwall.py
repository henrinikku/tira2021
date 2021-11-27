import heapq
from typing import List

INF = 2 ** 63


class Labyrinth:
    def __init__(self, r: List[str]):
        self.r = r
        self.n = len(r)
        self.m = len(r[0])

    def neighbours(self, y: int, x: int):
        for diff_y, diff_x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_y, new_x = y + diff_y, x + diff_x
            if not (new_y >= 0 and new_x >= 0 and new_y < self.n and new_x < self.m):
                continue
            elif self.r[new_y][new_x] == "#":
                continue
            elif self.r[new_y][new_x] == "*":
                yield (new_y, new_x, 1)
            else:
                yield (new_y, new_x, 0)

    def find(self, target):
        return next(
            (y, x)
            for y in range(self.n)
            for x in range(self.m)
            if self.r[y][x] == target
        )

    def solve(self):
        seen = set()
        start = self.find("A")
        dist = {start: 0}
        heap = [(0, *start)]
        while heap:
            __, y, x = heapq.heappop(heap)
            if (y, x) in seen:
                continue

            for new_y, new_x, weight in self.neighbours(y, x):
                current_weight = dist.get((new_y, new_x), INF)
                new_weight = dist[(y, x)] + weight
                if new_weight < current_weight:
                    dist[(new_y, new_x)] = new_weight
                    heapq.heappush(heap, (new_weight, new_y, new_x))

            seen.add((y, x))

        return dist.get(self.find("B"), -1)


def count(r: List[str]):
    return Labyrinth(r).solve()


if __name__ == "__main__":
    r = [
        "########",
        "#*A*...#",
        "#.*****#",
        "#.**.**#",
        "#.*****#",
        "#..*.B.#",
        "########",
    ]
    print(count(r))  # 2
