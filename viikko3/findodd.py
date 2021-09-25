from collections import Counter
from typing import List


def find(t: List[int]):
    counts = Counter()
    for i in t:
        counts[i] += 1
    
    return min(counts, key=counts.get)

if __name__ == "__main__":
    print(find([2, 2, 4, 3, 4]))  # 3
    print(find([1, 2, 3, 4, 1, 2, 3]))  # 4
    print(find([1]))  # 1
    print(find([1, 4, 2, 3, 2, 3, 4]))  # 1
    print(find([4, 1, 3, 2, 3, 2, 1]))  # 4
