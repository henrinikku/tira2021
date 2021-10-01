import timeit
from typing import List


def add(n: int):
    l = []
    for i in range(n):
        l.append(i)
    return l


def pop(l: List[int]):
    for _ in range(len(l)):
        l.pop(0)


if __name__ == "__main__":
    n = 10 ** 5
    print(f"N = {n}")

    start_time = timeit.default_timer()
    l = add(n)
    end_time = timeit.default_timer()
    print(f"Adding took {end_time - start_time} seconds")

    start_time = timeit.default_timer()
    pop(l)
    end_time = timeit.default_timer()
    print(f"Removing took {end_time - start_time} seconds")
