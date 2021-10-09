from collections import Counter
import timeit
import random
from typing import Callable, List


def count_by_sorting(t: List[int]):
    t = sorted(t)
    return sum(t[i] != t[i + 1] for i in range(0, len(t) - 1)) + 1


def count_using_hashmap(t: List[int]):
    return len(Counter(t).keys())


def test(func: Callable[[List[int]], int], t):
    start = timeit.default_timer()
    result = func(t)
    end = timeit.default_timer()
    print(f"Result = {result}. Took {end - start} seconds.")


if __name__ == "__main__":
    max_int = 10 ** 9
    t = [random.randint(1, max_int) for __ in range(10 ** 6)]
    test(count_by_sorting, t)
    test(count_using_hashmap, t)
