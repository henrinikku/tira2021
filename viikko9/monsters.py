from typing import List

FLOOR = "."
MONSTER = "@"
WALL = "#"
INF = 999


def count(r: List[str]):
    mem = [[0 for x in range(len(r))] for y in range(len(r))]
    for y in range(len(r)):
        for x in range(len(r)):
            if r[y][x] == WALL:
                mem[y][x] = INF
            else:
                if r[y][x] == MONSTER:
                    mem[y][x] += 1

                if y > 0 and x > 0:
                    mem[y][x] += min(mem[y - 1][x], mem[y][x - 1])
                elif y > 0:
                    mem[y][x] += mem[y - 1][x]
                elif x > 0:
                    mem[y][x] += mem[y][x - 1]

    out = mem[-1][-1]
    return -1 if out >= INF else out


if __name__ == "__main__":
    r = [
        "....@",
        "@##.#",
        ".##@#",
        ".@..#",
        "###@.",
    ]
    print(count(r))  # 2
