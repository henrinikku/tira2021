from typing import List


def find(a: List[int], b: List[int]):
    a.sort()
    b.sort()
    return sum(abs(a[i] - b[i]) for i in range(len(a)))


if __name__ == "__main__":
    print(find([1, 2, 3], [2, 5, 2]))  # 3
    print(find([2], [7]))  # 5
    print(find([1, 1, 1, 1], [3, 4, 3, 4]))  # 10
    print(find([5, 2, 9, 1, 2, 4], [8, 8, 2, 3, 9, 4]))  # 11
