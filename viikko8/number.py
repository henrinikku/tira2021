import functools


@functools.lru_cache(None)
def _count(n: int, k: int):
    if k == 0 or k > n:
        return 0
    elif k == n:
        return 1
    else:
        return _count(n - 1, k - 1) + _count(n - k, k)


def count(n: int):
    # https://en.wikipedia.org/wiki/Partition_function_(number_theory)
    return sum(_count(n, k) for k in range(n + 1))


if __name__ == "__main__":
    print(count(4))  # 5
    print(count(5))  # 7
    print(count(8))  # 22
    print(count(42))  # 53174
