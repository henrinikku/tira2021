from collections import deque
from typing import List

WALL = "#"
FLOOR = "."
START = "A"
GOAL = "B"


def neighbours(r: int, n: int, m: int, y: int, x: int):
    if y > 0 and r[y - 1][x] in (FLOOR, GOAL):
        yield (y - 1, x)
    if x > 0 and r[y][x - 1] in (FLOOR, GOAL):
        yield (y, x - 1)
    if y < n and r[y + 1][x] in (FLOOR, GOAL):
        yield (y + 1, x)
    if x < m and r[y][x + 1] in (FLOOR, GOAL):
        yield (y, x + 1)


def count(r: List[str]):
    n = len(r)
    m = len(r[0])
    y, x = next((y, x) for y in range(n) for x in range(m) if r[y][x] == START)
    seen = set()
    queue = deque(
        (neighbour_y, neighbour_x, 1)
        for neighbour_y, neighbour_x in neighbours(r, n, m, y, x)
    )
    while queue:
        cur_y, cur_x, length = queue.popleft()
        if (cur_y, cur_x) in seen or r[cur_y][cur_x] == WALL:
            continue
        if r[cur_y][cur_x] == GOAL:
            return length
        seen.add((cur_y, cur_x))
        queue.extend(
            (neighbour_y, neighbour_x, length + 1)
            for neighbour_y, neighbour_x in neighbours(r, n, m, cur_y, cur_x)
        )

    return -1


if __name__ == "__main__":
    r = [
        "########",
        "#.A....#",
        "#.#.##.#",
        "#.##...#",
        "#...B#.#",
        "########",
    ]
    print(count(r))  # 7
