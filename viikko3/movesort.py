from typing import List


def check(t: List[int]):
    half = len(t) // 2
    left = t[:half]
    right = reversed(t[half:])
    return all(i + next(right) == len(t) + 1 for i in left)


if __name__ == "__main__":
    print(check([3, 1, 4, 2]))  # True
    print(check([3, 1, 2, 4]))  # False
    print(check([1, 2]))  # True
    print(check([4, 5, 6, 1, 2, 3]))  # True
    print(check([4, 5, 6, 3, 2, 1]))  # False
    print(check([5, 8, 13, 1, 3, 6, 11, 4, 9, 12, 14, 2, 7, 10]))  # True
    print(check([8, 7, 3, 4, 5, 6, 2, 1]))  # True
    print(
        check([6, 20, 8, 4, 18, 11, 19, 5, 9, 7, 14, 12, 16, 2, 10, 3, 17, 13, 1, 15])
    )  # True
    print(check([5, 7, 4, 3, 8, 2, 6, 1]))  # False
    print(
        check([14, 5, 6, 8, 15, 18, 12, 9, 4, 13, 1, 10, 11, 7, 16, 2, 17, 3])
    )  # False
    print(check([2, 3, 7, 6, 5, 1, 4, 8]))  # False
    print(check([3, 1, 4, 5, 6, 2]))  # False
