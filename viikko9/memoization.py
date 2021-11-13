import timeit
from functools import lru_cache

@lru_cache(None)
def f_cached(n):
    if n <= 2:
        return n
    return f_cached(n - 1) + f_cached(n - 2) + f_cached(n - 3)


def f_memoized(n):
    mem = [0, 1, 2]
    for i in range(3, n + 1):
        mem.append(mem[i - 1] + mem[i - 2] + mem[i - 3])
    return mem[n]


if __name__ == "__main__":
    assert f_cached(10) == 230
    start = timeit.default_timer()
    result = f_cached(30)
    end = timeit.default_timer()
    assert result == 45152016
    print(f"Cached took {end - start} seconds, result = {result}")

    assert f_memoized(10) == 230
    start = timeit.default_timer()
    result = f_memoized(30)
    end = timeit.default_timer()
    assert result == 45152016
    print(f"Memoized took {end - start} seconds, result = {result}")
