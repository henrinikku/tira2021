from typing import  List


def count(t: List[int]):
    if not t:
        return 0

    left = {}
    largest = None
    for i, n in enumerate(t):
        largest = n if largest is None else max(n, largest)
        left[i] = largest

    right = {}
    smallest = None
    for i, n in reversed(list(enumerate(t))):
        smallest = n if smallest is None else min(n, smallest)
        right[i] = smallest

    return sum(left[i - 1] < right[i] for i in range(1, len(t)))


if __name__ == "__main__":
    print(count([1, 2, 3, 4, 5]))  # 4
    print(count([5, 4, 3, 2, 1]))  # 0
    print(count([2, 1, 2, 5, 7, 6, 9]))  # 3
    print(count([1, 2, 3, 1]))  # 0
    print(count([6, 2, 7, 7]))  # 1
