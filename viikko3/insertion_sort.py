import logging
import random
import timeit
from typing import List

logger = logging.getLogger(__name__)

N = 100000


def insertion_sort(l: List[int]):
    result = l.copy()
    for i in range(1, len(result)):
        j = i - 1
        while 0 <= j and result[j + 1] < result[j]:
            result[j], result[j + 1] = result[j + 1], result[j]
            j -= 1

    return result


def is_sorted(l: List[int]):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    l = list(range(1, N + 1))
    random.shuffle(l)

    start_time = timeit.default_timer()
    sorted_list = insertion_sort(l)
    end_time = timeit.default_timer()

    if not is_sorted(sorted_list):
        raise RuntimeError("List was not sorted properly")

    logger.info("List of %s items sorted in %s seconds", N, end_time - start_time)
