import heapq
import itertools
import random
import timeit
from functools import partial
from typing import Callable, List

N = 10 ** 6

get_number = partial(random.randint, b=(N ** 9))


def alg1(nums: List[int]):
    return sum(itertools.islice(sorted(nums), len(nums) // 10))


def alg2(nums: List[int]):
    n = len(nums)
    heapq.heapify(nums)
    return sum(heapq.heappop(nums) for __ in range(n // 10))


def measure(alg: Callable, *args, **kwargs):
    start = timeit.default_timer()
    result = alg(*args, **kwargs)
    end = timeit.default_timer()
    print(f"{alg.__name__} took {end - start} seconds.", f"Result = {result}")


if __name__ == "__main__":
    nums = list(map(get_number, range(N)))
    measure(alg1, nums.copy())
    measure(alg2, nums.copy())
