import logging
import random
import timeit
from typing import List

logger = logging.getLogger(__name__)

N = 100000


class MergeSort(object):
    def sort(self, l: List[int]):
        self.arr = l.copy()
        self.helper = [0] * len(l)
        self._sort(0, len(l) - 1)
        return self.arr

    def _sort(self, a: int, b: int):
        if a == b:
            return

        k = int((a + b) / 2)
        self._sort(a, k)
        self._sort(k + 1, b)
        self._merge(a, k, k + 1, b)

    def _merge(self, a1: int, b1: int, a2: int, b2: int):
        start, end = a1, b2
        for i in range(start, end + 1):
            if b2 < a2 or (a1 <= b1 and self.arr[a1] <= self.arr[a2]):
                self.helper[i] = self.arr[a1]
                a1 += 1
            else:
                self.helper[i] = self.arr[a2]
                a2 += 1

        for i in range(start, end + 1):
            self.arr[i] = self.helper[i]


def is_sorted(l: List[int]):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    l = list(range(1, N + 1))
    random.shuffle(l)

    start_time = timeit.default_timer()
    sorted_list = MergeSort().sort(l)
    end_time = timeit.default_timer()

    if not is_sorted(sorted_list):
        raise RuntimeError("List was not sorted properly")

    logger.info("List of %s items sorted in %s seconds", N, end_time - start_time)
