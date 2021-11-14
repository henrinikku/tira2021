from collections import Counter
from typing import List


def count(t: List[int]):
    max_sum = sum(t)
    sums = Counter()
    for num in t:
        for current_sum in range(max_sum, -1, -1):
            if current_sum == 0:
                sums[num] += 1
            elif current_sum in sums:
                sums[current_sum + num] += 1
    return len(sums)


if __name__ == "__main__":
    print(count([3, 4, 5]))  # 7
    print(count([1, 1, 2]))  # 4
    print(count([2, 2, 2, 3, 3, 3]))  # 13
    print(count([42, 5, 5, 100, 1, 3, 3, 7]))  # 91
