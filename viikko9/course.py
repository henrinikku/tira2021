from functools import reduce
from operator import mul

TASKS_PER_WEEK = 8


def binom(n: int, k: int):
    mem = [[0 for __ in range(k + 1)] for __ in range(n + 1)]
    mem[0][0] = 1
    for i in range(1, n + 1):
        mem[i][0] = 1
        for j in range(1, k + 1):
            mem[i][j] = mem[i - 1][j - 1] + mem[i - 1][j]
    return mem[n][k]


tasks_ways_map = {k: binom(TASKS_PER_WEEK, k) for k in range(5, TASKS_PER_WEEK + 1)}


def count(x: int):
    return sum(
        reduce(mul, (w1, w2, w3, w4, w5, w6, w7))
        for t1, w1 in tasks_ways_map.items()
        for t2, w2 in tasks_ways_map.items()
        for t3, w3 in tasks_ways_map.items()
        for t4, w4 in tasks_ways_map.items()
        for t5, w5 in tasks_ways_map.items()
        for t6, w6 in tasks_ways_map.items()
        for t7, w7 in tasks_ways_map.items()
        if (
            all(i >= 5 for i in (t1, t2, t3, t4, t5, t6, t7))
            and sum((t1, t2, t3, t4, t5, t6, t7)) == x
        )
    )


if __name__ == "__main__":
    print(count(35))  # 1727094849536
    print(count(42))  # 2375030784000
    print(count(55))  # 56
    print(count(56))  # 1
    print(count(80))  # 0
