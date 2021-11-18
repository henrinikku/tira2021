from collections import deque
from typing import List

WALL = "#"
FLOOR = "."


def neighbours(r: int, n: int, m: int, y: int, x: int):
    if y > 0 and r[y - 1][x] == FLOOR:
        yield (y - 1, x)
    if x > 0 and r[y][x - 1] == FLOOR:
        yield (y, x - 1)
    if y < n and r[y + 1][x] == FLOOR:
        yield (y + 1, x)
    if x < m and r[y][x + 1] == FLOOR:
        yield (y, x + 1)


def count(r: List[str]):
    n = len(r)
    m = len(r[0])
    seen = set()
    out = 0
    for y in range(n):
        for x in range(m):
            if r[y][x] == WALL or (y, x) in seen:
                continue
            out += 1
            queue = deque(neighbours(r, n, m, y, x))
            while queue:
                cur_y, cur_x = queue.pop()
                if (cur_y, cur_x) in seen:
                    continue
                seen.add((cur_y, cur_x))
                queue.extend(neighbours(r, n, m, cur_y, cur_x))
    return out


if __name__ == "__main__":
    r = [
        "########",
        "#..#...#",
        "####.#.#",
        "#..#.#.#",
        "########",
    ]
    print(count(r))  # 3
