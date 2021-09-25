from typing import List


def find(t: List[int], x: int):
    t.sort(reverse=True)
    left = 0
    right = len(t) - 1
    result = 0
    while left < right:
        if t[left] + t[right] <= x:
            result += right - left
            right -= 1
            continue

        left += 1

    return result


if __name__ == "__main__":
    print(find([1, 2, 3], 4))  # 2
    print(find([5, 2, 4, 7], 10))  # 4
    print(find([1, 1, 1, 1], 2))  # 6
    print(find([1, 1, 1, 1], 1))  # 0
    print(find([8, 8, 1, 2, 5, 1, 9, 3], 9))  # 14
    print(find([2, 3, 3, 3, 2, 4, 3, 1, 1], 5))  # 24
    print(find([2, 1, 4, 6, 2, 2, 5, 6], 7))  # 16
    print(find([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))  # 16
