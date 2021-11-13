import random
from typing import List


def longest_increasing_subarray(t: List[int]):
    longest = [1] * len(t)
    for k in range(len(t)):
        for x in range(k):
            if t[x] < t[k]:
                longest[k] = max(longest[k], longest[x] + 1)
    return max(longest)


if __name__ == "__main__":
    t = list(range(1, 5001))
    random.shuffle(t)
    print(longest_increasing_subarray(t))
